<template>
  <section class="signup-page">
    <div class="signup-container">
      <div class="signup-header">
        <div class="icon-badge">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path>
            <circle cx="9" cy="7" r="4"></circle>
            <line x1="19" y1="8" x2="19" y2="14"></line>
            <line x1="22" y1="11" x2="16" y2="11"></line>
          </svg>
        </div>
        <h1>Rejoignez Axiome</h1>
        <p class="sub">Créez votre compte pour accéder à l'analyse géopolitique indépendante</p>
      </div>

      <form class="signup-form" @submit.prevent="handleSubmit">
        <div class="form-row">
          <label class="field">
            <span class="label">Email *</span>
            <input v-model="email" type="email" name="email" placeholder="votre@email.com" required autocomplete="email" />
          </label>

          <label class="field">
            <span class="label">Nom d'utilisateur *</span>
            <input v-model="username" type="text" name="username" placeholder="johndoe" required autocomplete="username" />
          </label>
        </div>

        <div class="form-row">
          <label class="field">
            <span class="label">Prénom</span>
            <input v-model="firstName" type="text" name="firstname" placeholder="Jean" />
          </label>

          <label class="field">
            <span class="label">Nom</span>
            <input v-model="lastName" type="text" name="lastname" placeholder="Dupont" />
          </label>
        </div>

        <label class="field">
          <span class="label">Mot de passe *</span>
          <div class="password-field">
            <input v-model="password" :type="showPassword ? 'text' : 'password'" name="password" placeholder="Min. 8 caractères" required autocomplete="new-password" />
            <PasswordToggle :is-shown="showPassword" @toggle="showPassword = !showPassword" />
          </div>
          <span class="hint">Au moins 8 caractères</span>
        </label>

        <label class="field">
          <span class="label">Confirmer le mot de passe *</span>
          <div class="password-field">
            <input v-model="passwordConfirm" :type="showPasswordConfirm ? 'text' : 'password'" name="confirm" placeholder="Retapez votre mot de passe" required autocomplete="new-password" />
            <PasswordToggle :is-shown="showPasswordConfirm" @toggle="showPasswordConfirm = !showPasswordConfirm" />
          </div>
        </label>

        <p v-if="error" class="error-message">{{ error }}</p>

        <button type="submit" class="btn-signup" :disabled="loading">
          <span v-if="!loading">Créer mon compte</span>
          <span v-else>
            <svg class="spinner" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            Création en cours...
          </span>
        </button>
      </form>

      <div class="signup-footer">
        <p class="login-link">Vous avez déjà un compte ? <NuxtLink to="/connexion">Connectez-vous</NuxtLink></p>
        <p class="terms">En créant un compte, vous acceptez nos <a href="/conditions">conditions d'utilisation</a>.</p>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from '#imports';
import { useAuthState } from '~/composables/useAuthState';
import { useAuthAPI } from '~/composables/useAuthAPI';
import { useRateLimit } from '~/composables/useRateLimit';

const email = ref('');
const username = ref('');
const firstName = ref('');
const lastName = ref('');
const password = ref('');
const passwordConfirm = ref('');
const showPassword = ref(false);
const showPasswordConfirm = ref(false);
const error = ref('');
const router = useRouter();
const { setAuth } = useAuthState();
const { signup, loading } = useAuthAPI();
const { checkLimit, isLockedOut, lockoutRemainingSeconds, getAttemptsRemaining } = useRateLimit({
  maxAttempts: 3,
  windowMs: 3600000, // 1 heure
  lockoutMs: 1800000, // 30 minutes de blocage
});

const handleSubmit = async () => {
  error.value = '';

  // Vérifier le rate limit
  if (!checkLimit()) {
    if (isLockedOut.value) {
      error.value = `Trop de tentatives. Veuillez attendre ${lockoutRemainingSeconds.value}s`;
    } else {
      error.value = `Limite atteinte. Tentatives restantes: ${getAttemptsRemaining()}`;
    }
    return;
  }

  if (!email.value || !username.value || !password.value || !passwordConfirm.value) {
    error.value = 'Tous les champs requis doivent être remplis.';
    return;
  }

  if (password.value !== passwordConfirm.value) {
    error.value = 'Les mots de passe ne correspondent pas.';
    return;
  }

  if (password.value.length < 8) {
    error.value = 'Le mot de passe doit contenir au moins 8 caractères.';
    return;
  }

  try {
    await signup(email.value, username.value, password.value, firstName.value, lastName.value);
    setAuth(true, false);
    await router.push('/mon-compte');
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Erreur lors de la création du compte';
  }
};
</script>

<style scoped lang="scss">
.signup-page {
  min-height: 75vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 60px 20px;
  background: linear-gradient(135deg, #f8f7fc 0%, #eceaf5 100%);
}

.signup-container {
  width: min(600px, 100%);
  background: #ffffff;
  border-radius: 20px;
  padding: 48px 40px;
  box-shadow: 0 20px 60px rgba(47, 5, 56, 0.12);
}

.signup-header {
  text-align: center;
  margin-bottom: 32px;
}

.icon-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: linear-gradient(135deg, #7b5ce0 0%, #9c7ef5 100%);
  color: #ffffff;
  margin-bottom: 16px;
}

h1 {
  margin: 0 0 8px 0;
  font-size: 32px;
  font-weight: 800;
  color: #1a0b25;
  letter-spacing: -0.5px;
}

.sub {
  margin: 0;
  color: #5a4a6e;
  font-size: 15px;
  line-height: 1.5;
}

.signup-form {
  display: grid;
  gap: 20px;
  margin-bottom: 28px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.field {
  display: grid;
  gap: 8px;
}

.label {
  font-size: 13px;
  font-weight: 700;
  color: #2a1a3a;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.hint {
  font-size: 12px;
  color: #7a6a8a;
  margin-top: -4px;
}

input[type="text"],
input[type="email"],
input[type="password"] {
  width: 100%;
  padding: 13px 16px;
  border-radius: 12px;
  border: 2px solid #e5e0f0;
  background: #fafbff;
  font-size: 15px;
  color: #1a0b25;
  transition: all 0.3s ease;

  &::placeholder {
    color: #a89bb8;
  }

  &:focus {
    outline: none;
    border-color: #7b5ce0;
    background: #ffffff;
    box-shadow: 0 0 0 4px rgba(123, 92, 224, 0.1);
  }
}

.password-field {
  position: relative;
  display: flex;
  align-items: center;
}

.password-field input {
  flex: 1;
  padding-right: 50px;
}

.options {
  margin: 8px 0;
}

.checkbox-styled {
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  user-select: none;

  input[type="checkbox"] {
    position: absolute;
    opacity: 0;
    cursor: pointer;

    &:checked + .checkmark {
      background: linear-gradient(135deg, #7b5ce0 0%, #9c7ef5 100%);
      border-color: #7b5ce0;

      &::after {
        display: block;
      }
    }
  }

  .checkmark {
    position: relative;
    width: 20px;
    height: 20px;
    border: 2px solid #d0c5e0;
    border-radius: 6px;
    background: #fafbff;
    transition: all 0.2s ease;
    flex-shrink: 0;

    &::after {
      content: '';
      position: absolute;
      display: none;
      left: 6px;
      top: 2px;
      width: 5px;
      height: 10px;
      border: solid white;
      border-width: 0 2px 2px 0;
      transform: rotate(45deg);
    }
  }

  .text {
    font-size: 14px;
    color: #3a2a4a;
  }
}

.error-message {
  margin: 0;
  padding: 12px 16px;
  background: #fff0f0;
  border-left: 4px solid #e74c3c;
  border-radius: 8px;
  color: #c0392b;
  font-size: 14px;
  font-weight: 500;
}

.btn-signup {
  width: 100%;
  border: none;
  border-radius: 14px;
  padding: 16px;
  font-size: 16px;
  font-weight: 700;
  background: linear-gradient(135deg, #7b5ce0 0%, #9c7ef5 100%);
  color: #ffffff;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  box-shadow: 0 8px 24px rgba(123, 92, 224, 0.3);

  &:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: 0 12px 32px rgba(123, 92, 224, 0.4);
  }

  &:active:not(:disabled) {
    transform: translateY(0);
  }

  &:disabled {
    opacity: 0.7;
    cursor: not-allowed;
  }

  .spinner {
    width: 20px;
    height: 20px;
    animation: spin 1s linear infinite;
  }
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.signup-footer {
  text-align: center;
  border-top: 1px solid #e5e0f0;
  padding-top: 24px;
}

.login-link {
  margin: 0 0 12px 0;
  font-size: 14px;
  color: #5a4a6e;

  a {
    color: #7b5ce0;
    text-decoration: none;
    font-weight: 700;
    transition: color 0.2s ease;

    &:hover {
      color: #9c7ef5;
      text-decoration: underline;
    }
  }
}

.terms {
  margin: 0;
  font-size: 12px;
  color: #8a7a9a;
  line-height: 1.6;

  a {
    color: #7a6a8a;
    text-decoration: underline;

    &:hover {
      color: #7b5ce0;
    }
  }
}

@media (max-width: 640px) {
  .signup-container {
    padding: 36px 28px;
  }

  .form-row {
    grid-template-columns: 1fr;
  }

  h1 {
    font-size: 26px;
  }
}
</style>
