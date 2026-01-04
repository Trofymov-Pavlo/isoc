"""
Authentication and User Management Views.

This module contains all API endpoints for:
- User registration (signup)
- Authentication (login/logout)
- Password management (reset, change)
- Profile management (view, update)
"""
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

from .serializers import (
    UserSerializer, SignUpSerializer, LoginSerializer,
    PasswordResetSerializer, PasswordResetConfirmSerializer,
    UpdateProfileSerializer, ChangePasswordSerializer
)
from .throttles import SignupRateThrottle, LoginRateThrottle, PasswordResetRateThrottle

User = get_user_model()


@api_view(['GET'])
def home(request):
    """Redirect to Django admin panel"""
    return redirect('/admin/')


class AccountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'], permission_classes=[AllowAny], throttle_classes=[SignupRateThrottle])
    def signup(self, request):
        """Sign up a new user"""
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserSerializer(user).data,
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny], throttle_classes=[LoginRateThrottle])
    def login(self, request):
        """Login a user"""
        logger.info(f"Login attempt - Request data: {request.data}")
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            remember_me = serializer.validated_data.get('remember_me', False)

            logger.info(f"Validated email: {email}, remember_me: {remember_me}")

            # Case-insensitive email search
            try:
                user = User.objects.get(email__iexact=email)
                logger.info(f"User found: {user.email}, username: {user.username}, is_active: {user.is_active}")
            except User.DoesNotExist:
                logger.warning(f"No user found with email: {email}")
                return Response({
                    'error': 'Invalid credentials',
                    'detail': f'No user found with email: {email}'
                }, status=status.HTTP_401_UNAUTHORIZED)

            # Verify password
            if not user.check_password(password):
                logger.warning(f"Invalid password for user: {email}")
                return Response({
                    'error': 'Invalid credentials',
                    'detail': 'Password is incorrect'
                }, status=status.HTTP_401_UNAUTHORIZED)

            logger.info(f"Password verified for user: {email}")

            # Check if user is active
            if not user.is_active:
                logger.warning(f"Account disabled for user: {email}")
                return Response({
                    'error': 'Account disabled',
                    'detail': 'This account has been deactivated'
                }, status=status.HTTP_403_FORBIDDEN)

            user.remember_me = remember_me
            user.save()

            refresh = RefreshToken.for_user(user)
            logger.info(f"Login successful for user: {email}")
            return Response({
                'user': UserSerializer(user).data,
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'remember_me': remember_me,
            }, status=status.HTTP_200_OK)

        logger.error(f"Login validation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def logout(self, request):
        """Logout a user"""
        try:
            refresh_token = request.data.get('refresh')
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
            return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny], throttle_classes=[PasswordResetRateThrottle])
    def password_reset(self, request):
        """Request password reset"""
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            try:
                user = User.objects.get(email=email)
                reset_token = get_random_string(64)
                user.password_reset_token = reset_token
                user.save()
                
                # Send email with reset token
                subject = 'Réinitialisation de votre mot de passe AXIOME'
                reset_link = f'http://localhost:3000/forgot-password'
                message = f"""
Bonjour {user.first_name or user.username},

Vous avez demandé une réinitialisation de mot de passe pour votre compte AXIOME.

Voici votre code de réinitialisation:
{reset_token}

Allez sur {reset_link} et entrez ce code pour réinitialiser votre mot de passe.

Ce code expirera dans 24 heures.

Si vous n'avez pas demandé cette réinitialisation, ignorez cet email.

Cordialement,
L'équipe AXIOME
                """
                
                try:
                    send_mail(
                        subject,
                        message,
                        settings.DEFAULT_FROM_EMAIL,
                        [user.email],
                        fail_silently=False,
                    )
                    logger.info(f"Password reset email sent to {user.email}")
                except Exception as e:
                    logger.error(f"Failed to send password reset email: {str(e)}")
                    
            except User.DoesNotExist:
                # Don't reveal if email exists
                logger.info(f"Password reset requested for non-existent email: {email}")
                pass
            
            return Response({
                'message': 'Check your email for password reset link'
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def password_reset_confirm(self, request):
        """Confirm password reset"""
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data.get('token')
            new_password = serializer.validated_data.get('new_password')

            try:
                user = User.objects.get(password_reset_token=token)
            except User.DoesNotExist:
                return Response({'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.password_reset_token = None
            user.save()

            return Response({'message': 'Password reset successfully'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        """Get current user info"""
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    @action(detail=False, methods=['put', 'patch'], permission_classes=[IsAuthenticated])
    def update_profile(self, request):
        """Update user profile"""
        serializer = UpdateProfileSerializer(
            request.user,
            data=request.data,
            context={'request': request},
            partial=request.method == 'PATCH'
        )
        if serializer.is_valid():
            serializer.save()
            return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def change_password(self, request):
        """Change user password"""
        serializer = ChangePasswordSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
