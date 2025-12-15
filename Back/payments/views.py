from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from decimal import Decimal

from paypalcheckoutsdk.orders import OrdersCreateRequest, OrdersCaptureRequest
from .paypal_client import get_paypal_client
from donations.models import Donation


def _validate_amount(value):
    try:
        amount = Decimal(str(value))
        if amount <= 0:
            raise ValueError
        return amount
    except Exception:
        return None


@csrf_exempt
def paypal_create_order(request):
    if request.method != "POST":
        return HttpResponseBadRequest("POST only")

    amount = _validate_amount(request.POST.get("amount"))
    currency = request.POST.get("currency", "EUR").upper()
    if not amount:
        return HttpResponseBadRequest("Invalid amount")

    donation = Donation.objects.create(
        amount=amount,
        currency=currency,
        method="paypal",
        status="initiated",
        donor_name=request.POST.get("donor_name", ""),
        donor_email=request.POST.get("donor_email", ""),
        message=request.POST.get("message", ""),
        user=request.user if getattr(request, "user", None) and request.user.is_authenticated else None,
    )

    request_order = OrdersCreateRequest()
    request_order.prefer("return=representation")
    request_order.request_body({
        "intent": "CAPTURE",
        "purchase_units": [{
            "reference_id": donation.reference,
            "amount": {"currency_code": donation.currency, "value": str(donation.amount)},
            "description": f"Donation {donation.reference}",
        }],
        "application_context": {
            "brand_name": "Axiome",
            "landing_page": "NO_PREFERENCE",
            "user_action": "PAY_NOW",
        },
    })
    client = get_paypal_client()
    resp = client.execute(request_order)
    order_id = resp.result.id

    return JsonResponse({"orderID": order_id, "reference": donation.reference})


@csrf_exempt
def paypal_capture_order(request):
    if request.method != "POST":
        return HttpResponseBadRequest("POST only")

    order_id = request.POST.get("orderID")
    if not order_id:
        return HttpResponseBadRequest("Missing orderID")

    client = get_paypal_client()
    cap_req = OrdersCaptureRequest(order_id)
    cap_req.request_body({})
    resp = client.execute(cap_req)

    try:
        pu = resp.result.purchase_units[0]
        reference = pu.reference_id
        donation = Donation.objects.get(reference=reference)
    except Exception:
        return HttpResponse(status=400)

    status = getattr(resp.result, "status", "")
    if status == "COMPLETED":
        donation.status = "authorized"
    else:
        donation.status = "failed"
    donation.save(update_fields=["status"])

    return JsonResponse({"status": donation.status, "reference": donation.reference})
