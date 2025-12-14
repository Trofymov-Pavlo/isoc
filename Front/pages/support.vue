<template>
  <section class="donation-page">
    <div class="hero">
      <p class="eyebrow">Soutenir Axiome</p>
      <h1>Financez un journalisme indépendant et rigoureux</h1>
      <p class="lede">
        Chaque contribution renforce notre capacité à enquêter, vérifier et publier sans compromis.
        Choisissez un montant, un mode de paiement (carte ou PayPal) et obtenez une référence claire.
      </p>
      <div class="hero-pills">
        <span class="pill">Transparence totale</span>
        <span class="pill">Paiement sécurisé (à connecter PSP)</span>
        <span class="pill">Reçu par email</span>
      </div>
    </div>

    <div class="layout">
      <div class="card donate-card">
        <div class="card-header">
          <div>
            <p class="eyebrow">Don unique</p>
            <h2>Choisissez votre soutien</h2>
          </div>
          <div class="badge">Carte ou PayPal</div>
        </div>

        <div class="amount-grid">
          <button
            v-for="value in presetAmounts"
            :key="value"
            type="button"
            :class="['amount-btn', resolvedAmount === value && !form.customAmount ? 'is-active' : '']"
            @click="selectAmount(value)"
          >
            {{ value }} €
          </button>
          <div class="amount-custom">
            <label for="don-custom">Autre montant</label>
            <div class="input-wrap">
              <span>€</span>
              <input
                id="don-custom"
                type="number"
                min="1"
                step="1"
                placeholder="Ex : 75"
                v-model="form.customAmount"
              />
            </div>
          </div>
        </div>

        <div class="method-switch">
          <label :class="['method-pill', form.method === 'card' ? 'is-active' : '']">
            <input type="radio" value="card" v-model="form.method" />
            <span>Carte bancaire</span>
          </label>
          <label :class="['method-pill', form.method === 'paypal' ? 'is-active' : '']">
            <input type="radio" value="paypal" v-model="form.method" />
            <span>PayPal</span>
          </label>
        </div>

        <div class="form-grid">
          <div class="field">
            <label for="don-name">Nom / Organisation</label>
            <input id="don-name" v-model="form.name" type="text" placeholder="Ex : Jeanne Martin" />
          </div>
          <div class="field">
            <label for="don-email">Email pour le reçu</label>
            <input id="don-email" v-model="form.email" type="email" placeholder="vous@exemple.fr" />
          </div>
          <div class="field full">
            <label for="don-message">Message (optionnel)</label>
            <textarea id="don-message" v-model="form.message" rows="3" placeholder="Un mot pour la rédaction..."></textarea>
          </div>
        </div>

        <div v-if="form.method === 'card'" class="card-form">
          <div class="field full">
            <label for="don-card">Numéro de carte</label>
            <input id="don-card" v-model="form.cardNumber" inputmode="numeric" placeholder="4242 4242 4242 4242" />
          </div>
          <div class="field">
            <label for="don-exp">Expiration</label>
            <input id="don-exp" v-model="form.cardExpiry" placeholder="MM/AA" />
          </div>
          <div class="field">
            <label for="don-cvc">CVC</label>
            <input id="don-cvc" v-model="form.cardCvc" inputmode="numeric" placeholder="123" />
          </div>
          <p class="note">Saisie illustrative : la capture réelle passe par un PSP (Stripe, Mollie…) que nous pourrons connecter.</p>
        </div>
        <div v-else class="paypal-hint">
          <p class="paypal-title">Paiement PayPal</p>
          <p class="note">Après validation, vous serez redirigé vers PayPal pour confirmer. La référence ci-dessous permettra d'associer le règlement.</p>
        </div>

        <div class="cta-row">
          <div>
            <p class="amount">{{ resolvedAmount }} €</p>
            <p class="note">Montant TTC, reçu PDF envoyé par email.</p>
          </div>
          <button class="submit" type="button" :disabled="loading" @click="submitDonation">
            <span v-if="!loading">Valider et obtenir la référence</span>
            <span v-else>Envoi en cours…</span>
          </button>
        </div>

        <div v-if="status === 'success'" class="feedback success">
          Merci ! Référence : <strong>{{ reference }}</strong>. Suivez les instructions de paiement ci-dessus.
        </div>
        <div v-if="status === 'error'" class="feedback error">
          {{ feedback || 'Une erreur est survenue. Merci de réessayer.' }}
        </div>
      </div>

      <div class="sidebar">
        <div class="card info-card">
          <p class="eyebrow">Transparence</p>
          <h3>Vos dons financent</h3>
          <ul>
            <li>Enquêtes terrain et vérification des sources.</li>
            <li>Production vidéo et podcast sans publicité intrusive.</li>
            <li>Hébergement et sécurité des données.</li>
          </ul>
          <div class="pill secondary">Reporting trimestriel</div>
        </div>

        <div class="card guarantees">
          <p class="eyebrow">Garanties</p>
          <div class="guarantee-grid">
            <div>
              <h4>Protection des données</h4>
              <p>Emails et montants stockés en France, accès restreint.</p>
            </div>
            <div>
              <h4>Traçabilité</h4>
              <p>Références uniques pour chaque don, vérifiables par notre équipe.</p>
            </div>
            <div>
              <h4>Flexibilité</h4>
              <p>Carte ou PayPal, montant libre dès 5 €.</p>
            </div>
          </div>
        </div>

        <div class="card contact-card">
          <h4>Une question ?</h4>
          <p>Contact direct : <a href="mailto:soutien@axiome.media">soutien@axiome.media</a></p>
          <p>Téléphone rédaction : +33 1 84 88 88 00</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed, reactive, ref } from 'vue';

const runtimeConfig = useRuntimeConfig();
const donationsBase = runtimeConfig.public.donationsBase || 'http://localhost:8000/api/donations';
const presetAmounts = [10, 20, 35, 50, 100];

type PaymentMethod = 'card' | 'paypal';

const form = reactive({
  amount: 20,
  customAmount: '',
  method: 'card' as PaymentMethod,
  name: '',
  email: '',
  message: '',
  cardNumber: '',
  cardExpiry: '',
  cardCvc: '',
});

const loading = ref(false);
const status = ref<'idle' | 'success' | 'error'>('idle');
const feedback = ref('');
const reference = ref('');

const resolvedAmount = computed(() => {
  const custom = parseFloat(form.customAmount);
  if (!Number.isNaN(custom) && custom > 0) return Number(custom.toFixed(2));
  return Number(form.amount);
});

const selectAmount = (value: number) => {
  form.amount = value;
  form.customAmount = '';
};

const submitDonation = async () => {
  status.value = 'idle';
  feedback.value = '';
  reference.value = '';

  const amount = resolvedAmount.value;
  if (!amount || amount <= 0) {
    status.value = 'error';
    feedback.value = 'Merci de saisir un montant valide.';
    return;
  }

  loading.value = true;
  try {
    const payload = {
      donor_name: form.name,
      donor_email: form.email,
      amount,
      currency: 'EUR',
      method: form.method,
      message: form.message,
    };

    const data = await $fetch(donationsBase + '/', {
      method: 'POST',
      body: payload,
    });

    reference.value = (data as { reference?: string }).reference || '';
    status.value = 'success';
    feedback.value = 'Référence générée. Finalisez le paiement via le prestataire choisi.';
  } catch (err) {
    console.error(err);
    status.value = 'error';
    feedback.value = 'Impossible de créer le don pour le moment.';
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
.donation-page { display: grid; gap: 24px; padding: 32px 0 48px; }
.hero { background: radial-gradient(circle at 10% 10%, rgba(123, 92, 224, 0.15), transparent 35%),
  radial-gradient(circle at 90% 20%, rgba(255, 107, 107, 0.18), transparent 30%), #0f0b1b; color: #f4f1ff; padding: 32px; border-radius: 16px; box-shadow: 0 16px 40px rgba(0, 0, 0, 0.25); display: grid; gap: 12px; }
.eyebrow { text-transform: uppercase; letter-spacing: 0.2rem; font-size: 12px; color: #c5b3ff; margin: 0; }
.lede { margin: 0; max-width: 820px; color: #e9e5ff; line-height: 1.6; }
.hero h1 { margin: 0; font-size: 32px; letter-spacing: -0.02em; }
.hero-pills { display: flex; gap: 10px; flex-wrap: wrap; }
.pill { padding: 8px 12px; border-radius: 999px; background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); color: #f4f1ff; font-weight: 700; font-size: 13px; }
.pill.secondary { background: #f5f3ff; color: #2f0538; border-color: #e2dcff; }
.layout { display: grid; grid-template-columns: 2fr 1fr; gap: 16px; }
.card { background: #fff; border-radius: 14px; padding: 20px; box-shadow: 0 12px 32px rgba(15, 11, 27, 0.12); border: 1px solid #f0ecff; }
.donate-card { display: grid; gap: 16px; }
.card-header { display: flex; align-items: center; justify-content: space-between; }
.card-header h2 { margin: 4px 0 0; }
.badge { background: linear-gradient(135deg, #2f0538, #7b5ce0); color: #fff; border-radius: 10px; padding: 8px 12px; font-weight: 700; font-size: 13px; }
.amount-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 10px; }
.amount-btn { padding: 14px 12px; border-radius: 12px; border: 1px solid #e4ddff; background: #fbfaff; font-weight: 700; cursor: pointer; transition: all 0.18s ease; }
.amount-btn.is-active { border-color: #7b5ce0; background: linear-gradient(135deg, rgba(123, 92, 224, 0.12), rgba(123, 92, 224, 0.04)); box-shadow: 0 10px 20px rgba(123, 92, 224, 0.15); }
.amount-custom { border: 1px dashed #d9d2ff; border-radius: 12px; padding: 10px; display: grid; gap: 6px; background: #fcfbff; }
.input-wrap { display: flex; align-items: center; gap: 6px; background: #fff; border: 1px solid #e4ddff; border-radius: 10px; padding: 8px 10px; }
.method-switch { display: flex; gap: 10px; flex-wrap: wrap; }
.method-pill { display: inline-flex; align-items: center; gap: 8px; border: 1px solid #e4ddff; padding: 10px 14px; border-radius: 12px; cursor: pointer; background: #fbfaff; font-weight: 700; }
.method-pill.is-active { border-color: #7b5ce0; background: linear-gradient(135deg, rgba(123, 92, 224, 0.14), rgba(123, 92, 224, 0.06)); }
.method-pill input { display: none; }
.form-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; }
.field { display: grid; gap: 6px; }
.field.full { grid-column: 1 / -1; }
label { font-weight: 700; color: #2f0538; }
input, textarea { border: 1px solid #e4ddff; border-radius: 10px; padding: 10px 12px; font-size: 14px; width: 100%; background: #fff; }
textarea { resize: vertical; }
.card-form { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; }
.note { margin: 0; color: #6f6689; font-size: 13px; }
.paypal-hint { border: 1px dashed #d9d2ff; border-radius: 12px; padding: 12px; background: #fbfaff; }
.paypal-title { margin: 0 0 4px; font-weight: 700; }
.cta-row { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; }
.amount { margin: 0; font-size: 28px; font-weight: 800; color: #2f0538; }
.submit { border: none; background: linear-gradient(135deg, #2f0538, #7b5ce0); color: #fff; padding: 12px 16px; border-radius: 12px; font-weight: 800; cursor: pointer; min-width: 240px; box-shadow: 0 12px 24px rgba(123, 92, 224, 0.18); transition: transform 0.2s ease, box-shadow 0.2s ease; }
.submit:disabled { opacity: 0.6; cursor: not-allowed; transform: none; box-shadow: none; }
.submit:not(:disabled):hover { transform: translateY(-1px); box-shadow: 0 16px 28px rgba(123, 92, 224, 0.22); }
.feedback { padding: 12px; border-radius: 10px; font-weight: 700; }
.feedback.success { background: #e8f8ef; color: #136b3c; border: 1px solid #b7e6c8; }
.feedback.error { background: #fff4f4; color: #b23a2b; border: 1px solid #f3c7c1; }
.sidebar { display: grid; gap: 12px; }
.info-card ul { padding-left: 18px; color: #4b3c67; display: grid; gap: 6px; }
.guarantees h4, .contact-card h4, .info-card h3 { margin: 4px 0; }
.guarantee-grid { display: grid; gap: 10px; }
.contact-card a { color: #2f0538; font-weight: 700; text-decoration: none; }
@media (max-width: 1024px) { .layout { grid-template-columns: 1fr; } }
@media (max-width: 640px) { .hero { padding: 20px; } .submit { width: 100%; } }
</style>
