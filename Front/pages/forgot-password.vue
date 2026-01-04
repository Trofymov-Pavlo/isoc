<template>
  <div class="forgot-password-root">
    <div class="forgot-password-container">
      <div class="form-hero">
        <div class="hero-content">
          <h1 class="hero-title">AXIOME</h1>
          <p class="hero-subtitle">Récupérez l'accès à votre compte</p>
        </div>
      </div>

      <div class="form-wrapper">
        <div class="form-card">
          <div class="form-header">
            <h2>{{ currentStep === 'email' ? 'Réinitialiser votre mot de passe' : 'Créer un nouveau mot de passe' }}</h2>
            <p v-if="currentStep === 'email'" class="subtitle">Entrez votre email pour recevoir un lien de réinitialisation.</p>
            <p v-else class="subtitle">Entrez votre code de réinitialisation et choisissez un nouveau mot de passe.</p>
          </div>

          <!-- Step 1: Email -->
          <form v-if="currentStep === 'email'" class="forgot-form" @submit.prevent="handleEmailSubmit">
            <div class="form-group">
              <label for="email" class="form-label">Email</label>
              <input
                v-model="email"
                id="email"
                type="email"
                name="email"
                class="form-input"
                placeholder="vous@example.com"
                required
                autocomplete="email"
                :disabled="loadingEmail"
              />
            </div>

            <button type="submit" class="submit-button" :disabled="loadingEmail">
              {{ loadingEmail ? 'Envoi en cours...' : 'Envoyer le code' }}
            </button>

            <p v-if="errorEmail" class="error-message">{{ errorEmail }}</p>
            <p v-if="successEmail" class="success-message">{{ successEmail }}</p>
          </form>

          <!-- Step 2: Reset -->
          <form v-else-if="currentStep === 'reset'" class="forgot-form" @submit.prevent="handleResetSubmit">
            <div class="form-group">
              <label for="token" class="form-label">Code de réinitialisation</label>
              <input
                v-model="token"
                id="token"
                type="text"
                name="token"
                class="form-input"
                placeholder="Copiez-collez le code reçu par email"
                required
                :disabled="loadingReset"
              />
            </div>

            <div class="form-group">
              <label for="new_password" class="form-label">Nouveau mot de passe</label>
              <div class="password-wrapper">
                <input
                  v-model="newPassword"
                  id="new_password"
                  :type="showNewPassword ? 'text' : 'password'"
                  name="new_password"
                  class="form-input"
                  placeholder="••••••••"
                  required
                  autocomplete="new-password"
                  :disabled="loadingReset"
                />
                <PasswordToggle :is-shown="showNewPassword" @toggle="showNewPassword = !showNewPassword" />
              </div>
              <p class="password-hint">Minimum 8 caractères, avec lettres, chiffres et caractères spéciaux.</p>
            </div>

            <div class="form-group">
              <label for="new_password_confirm" class="form-label">Confirmer le mot de passe</label>
              <div class="password-wrapper">
                <input
                  v-model="newPasswordConfirm"
                  id="new_password_confirm"
                  :type="showConfirmPassword ? 'text' : 'password'"
                  name="new_password_confirm"
                  class="form-input"
                  placeholder="••••••••"
                  required
                  autocomplete="new-password"
                  :disabled="loadingReset"
                />
                <PasswordToggle :is-shown="showConfirmPassword" @toggle="showConfirmPassword = !showConfirmPassword" />
              </div>
            </div>

            <button type="submit" class="submit-button" :disabled="loadingReset">
              {{ loadingReset ? 'Réinitialisation en cours...' : 'Réinitialiser le mot de passe' }}
            </button>

            <p v-if="errorReset" class="error-message">{{ errorReset }}</p>
            <p v-if="successReset" class="success-message">{{ successReset }}</p>
          </form>

          <!-- Step 3: Success -->
          <div v-else-if="currentStep === 'success'" class="success-box">
            <div class="success-icon">✓</div>
            <h3>Mot de passe réinitialisé !</h3>
            <p>Votre mot de passe a été changé avec succès. Vous pouvez maintenant vous connecter.</p>
            <NuxtLink to="/connexion" class="submit-button">Retour à la connexion</NuxtLink>
          </div>

          <div class="form-footer">
            <p class="back-link">
              <NuxtLink to="/connexion" class="link">← Retour à la connexion</NuxtLink>
            </p>
            <p class="security-note">🔒 Vos données restent sécurisées et chiffrées.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from '#imports';
import PasswordToggle from '~/components/compte/PasswordToggle.vue';
import { useAuthAPI } from '~/composables/useAuthAPI';

// Disable default layout (no header, footer, subheader)
definePageMeta({
  layout: false,
});

const router = useRouter();
const { passwordReset, passwordResetConfirm, loading: loadingAPI } = useAuthAPI();

// Form states
const currentStep = ref<'email' | 'reset' | 'success'>('email');
const email = ref('');
const token = ref('');
const newPassword = ref('');
const newPasswordConfirm = ref('');
const showNewPassword = ref(false);
const showConfirmPassword = ref(false);

// Loading states
const loadingEmail = ref(false);
const loadingReset = ref(false);

// Error/Success messages
const errorEmail = ref('');
const successEmail = ref('');
const errorReset = ref('');
const successReset = ref('');

const handleEmailSubmit = async () => {
  errorEmail.value = '';
  successEmail.value = '';

  if (!email.value) {
    errorEmail.value = 'Email requis.';
    return;
  }

  loadingEmail.value = true;
  try {
    await passwordReset(email.value);
    successEmail.value = 'Un code de réinitialisation a été envoyé à votre email.';
    setTimeout(() => {
      currentStep.value = 'reset';
      successEmail.value = '';
    }, 2000);
  } catch (err: any) {
    errorEmail.value = err.message || 'Erreur lors de l\'envoi du code.';
  } finally {
    loadingEmail.value = false;
  }
};

const handleResetSubmit = async () => {
  errorReset.value = '';
  successReset.value = '';

  // Validation
  if (!token.value || !newPassword.value || !newPasswordConfirm.value) {
    errorReset.value = 'Tous les champs sont requis.';
    return;
  }

  if (newPassword.value !== newPasswordConfirm.value) {
    errorReset.value = 'Les mots de passe ne correspondent pas.';
    return;
  }

  if (newPassword.value.length < 8) {
    errorReset.value = 'Le mot de passe doit contenir au moins 8 caractères.';
    return;
  }

  loadingReset.value = true;
  try {
    await passwordResetConfirm(token.value, newPassword.value);
    successReset.value = 'Mot de passe réinitialisé avec succès !';
    setTimeout(() => {
      currentStep.value = 'success';
      successReset.value = '';
    }, 2000);
  } catch (err: any) {
    errorReset.value = err.message || 'Erreur lors de la réinitialisation.';
  } finally {
    loadingReset.value = false;
  }
};
</script>

<style scoped>
.forgot-password-root {
  min-height: 100vh;
  display: flex;
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
}

.forgot-password-container {
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 100vh;
}

.form-hero {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px;
  color: #fff;
}

.hero-content {
  text-align: center;
  max-width: 400px;
}

.hero-title {
  font-size: 64px;
  font-weight: 900;
  letter-spacing: 4px;
  margin: 0 0 24px;
  background: linear-gradient(90deg, #ffffff, #d8c3ff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-subtitle {
  font-size: 18px;
  color: rgba(255, 255, 255, 0.9);
  margin: 0;
  line-height: 1.5;
}

.form-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px;
  background: #ffffff;
}

.form-card {
  width: 100%;
  max-width: 420px;
}

.form-header {
  margin-bottom: 32px;
  text-align: center;
}

.form-header h2 {
  font-size: 28px;
  font-weight: 800;
  color: #111827;
  margin: 0 0 8px 0;
}

.subtitle {
  color: #6b7280;
  font-size: 14px;
  margin: 0;
}

.forgot-form {
  display: grid;
  gap: 20px;
  margin-bottom: 24px;
}

.form-group {
  display: grid;
  gap: 8px;
}

.form-label {
  font-size: 14px;
  font-weight: 600;
  color: #111827;
}

.form-input {
  padding: 12px 16px;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  font-size: 14px;
  transition: all 0.2s ease;
  font-family: inherit;
}

.form-input:focus {
  outline: none;
  border-color: #7b5ce0;
  box-shadow: 0 0 0 3px rgba(123, 92, 224, 0.1);
}

.form-input:disabled {
  background: #f3f4f6;
  cursor: not-allowed;
}

.password-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.password-wrapper .form-input {
  width: 100%;
  padding-right: 44px;
}

.password-hint {
  font-size: 12px;
  color: #9ca3af;
  margin: 4px 0 0 0;
}

.submit-button {
  padding: 12px 24px;
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  text-decoration: none;
  display: inline-block;
  text-align: center;
  width: 100%;
}

.submit-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 12px 24px rgba(75, 47, 170, 0.3);
}

.submit-button:active:not(:disabled) {
  transform: translateY(0);
}

.submit-button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.error-message {
  padding: 12px;
  background: #fee2e2;
  color: #991b1b;
  border-radius: 6px;
  font-size: 14px;
  margin: 0;
  border-left: 3px solid #dc2626;
}

.success-message {
  padding: 12px;
  background: #dcfce7;
  color: #166534;
  border-radius: 6px;
  font-size: 14px;
  margin: 0;
  border-left: 3px solid #22c55e;
}

.success-box {
  text-align: center;
  padding: 40px 24px;
}

.success-icon {
  font-size: 64px;
  margin-bottom: 16px;
  color: #22c55e;
}

.success-box h3 {
  font-size: 24px;
  color: #111827;
  margin: 0 0 12px 0;
}

.success-box p {
  color: #6b7280;
  margin: 0 0 24px 0;
}

.form-footer {
  text-align: center;
  padding-top: 24px;
  border-top: 1px solid #e5e7eb;
}

.back-link {
  margin: 0 0 12px 0;
}

.link {
  color: #7b5ce0;
  text-decoration: none;
  font-weight: 600;
  transition: color 0.2s ease;
}

.link:hover {
  color: #4b2faa;
}

.security-note {
  color: #9ca3af;
  font-size: 12px;
  margin: 0;
}

/* Responsive */
@media (max-width: 1024px) {
  .forgot-password-container {
    grid-template-columns: 1fr;
  }

  .form-hero {
    display: none;
  }

  .hero-title {
    font-size: 48px;
  }

  .form-card {
    max-width: 100%;
  }
}

@media (max-width: 640px) {
  .form-wrapper {
    padding: 20px 16px;
  }

  .form-header h2 {
    font-size: 24px;
  }

  .hero-title {
    font-size: 40px;
  }

  .form-input {
    font-size: 16px;
  }
}
</style>
