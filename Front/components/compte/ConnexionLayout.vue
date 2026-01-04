<template>
  <div class="login-root">
    <div class="login-container">
      <div class="login-hero">
        <div class="hero-content">
          <h1 class="hero-title">AXIOME</h1>
          <p class="hero-subtitle">Votre accès aux informations vérifiées</p>
        </div>
      </div>

      <div class="login-form-wrapper">
        <div class="form-card">
          <div class="form-header">
            <h2>Connexion</h2>
            <p>Accédez à vos suivis et contenus personnalisés.</p>
          </div>

          <form class="login-form" @submit.prevent="handleSubmit">
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
              />
            </div>

            <div class="form-group">
              <label for="password" class="form-label">Mot de passe</label>
              <div class="password-wrapper">
                <input
                  v-model="password"
                  id="password"
                  :type="showPassword ? 'text' : 'password'"
                  name="password"
                  class="form-input"
                  placeholder="••••••••"
                  required
                  autocomplete="current-password"
                />
                <PasswordToggle :is-shown="showPassword" @toggle="showPassword = !showPassword" />
              </div>
            </div>

            <div class="form-options">
              <label class="checkbox">
                <input v-model="remember" type="checkbox" name="remember" />
                <span>Se souvenir de moi</span>
              </label>
            </div>

            <button type="submit" class="submit-button" :disabled="loading">
              {{ loading ? 'Connexion en cours...' : 'Se connecter' }}
            </button>

            <p v-if="error" class="error-message">{{ error }}</p>
          </form>

          <div class="form-footer">
            <p class="signup-link">
              Pas encore de compte ?
              <NuxtLink to="/signup" class="link" exact>Créer un compte</NuxtLink>
            </p>
            <p class="security-note">🔒 Connexion sécurisée. Vos données restent privées.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from '#imports';
import { useAuthState } from '~/composables/useAuthState';
import { useAuthAPI } from '~/composables/useAuthAPI';
import PasswordToggle from '~/components/compte/PasswordToggle.vue';

const email = ref('');
const password = ref('');
const remember = ref(false);
const showPassword = ref(false);
const error = ref('');
const router = useRouter();
const { setAuth } = useAuthState();
const { login, loading } = useAuthAPI();

const handleSubmit = async () => {
  error.value = '';
  
  if (!email.value || !password.value) {
    error.value = 'Email et mot de passe requis.';
    return;
  }

  try {
    const response = await login(email.value, password.value, remember.value);
    if (response?.access) {
      setAuth(true, remember.value);
      await router.push('/mon-compte');
      return;
    }
    error.value = 'Identifiants incorrects.';
  } catch (err: any) {
    error.value = err.message || 'Erreur lors de la connexion.';
  }
};
</script>

<style scoped>
.login-root {
  min-height: 100vh;
  display: flex;
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
}

.login-container {
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 100vh;
}

.login-hero {
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
  font-size: 24px;
  font-weight: 400;
  margin: 0;
  color: rgba(255, 255, 255, 0.9);
  line-height: 1.4;
}

.login-form-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px;
  background: #fff;
}

.form-card {
  width: 100%;
  max-width: 400px;
}

.form-header {
  margin-bottom: 32px;
  text-align: center;
}

.form-header h2 {
  font-size: 32px;
  font-weight: 800;
  color: #2f0538;
  margin: 0 0 8px;
}

.form-header p {
  font-size: 14px;
  color: #666;
  margin: 0;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 24px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-label {
  font-size: 13px;
  font-weight: 600;
  color: #2f0538;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.form-input {
  padding: 12px 16px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background: #f8f8f8;
  font-size: 14px;
  transition: all 0.2s ease;
  font-family: inherit;
}

.form-input::placeholder {
  color: #999;
}

.form-input:focus {
  outline: none;
  border-color: #2f0538;
  background: #fff;
  box-shadow: 0 2px 8px rgba(47, 5, 56, 0.1);
}

.password-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.password-wrapper .form-input {
  padding-right: 44px;
}

.form-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 13px;
}

.checkbox {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  color: #666;
  font-weight: 500;
}

.checkbox input {
  width: 16px;
  height: 16px;
  cursor: pointer;
}

.forgot-link {
  color: #2f0538;
  text-decoration: none;
  font-weight: 600;
  transition: color 0.2s ease;
}

.forgot-link:hover {
  color: #ff6b6b;
}

.submit-button {
  width: 100%;
  padding: 14px;
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  color: #fff;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s ease;
}

.submit-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(47, 5, 56, 0.3);
}

.submit-button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.error-message {
  color: #e74c3c;
  font-size: 13px;
  margin: 0;
  text-align: center;
}

.form-footer {
  text-align: center;
}

.signup-link {
  font-size: 13px;
  color: #666;
  margin: 0 0 12px;
}

.link {
  color: #2f0538;
  text-decoration: none;
  font-weight: 700;
  transition: color 0.2s ease;
}

.link:hover {
  color: #ff6b6b;
}

.security-note {
  font-size: 12px;
  color: #999;
  margin: 0;
}

@media (max-width: 968px) {
  .login-container {
    grid-template-columns: 1fr;
  }

  .login-hero {
    display: none;
  }

  .login-form-wrapper {
    min-height: 100vh;
  }
}

@media (max-width: 480px) {
  .login-form-wrapper {
    padding: 24px;
  }

  .form-card {
    max-width: 100%;
  }

  .form-header h2 {
    font-size: 24px;
  }
}
</style>
