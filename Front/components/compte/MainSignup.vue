<template>
  <section class="auth-page">
    <div class="auth-card">
      <div class="auth-header">
        <p class="eyebrow">Espace membre</p>
        <h1>Créer un compte</h1>
        <p class="sub">Rejoignez la communauté et suivez vos analyses préférées.</p>
      </div>

      <form class="auth-form" @submit.prevent="handleSubmit">
        <label class="field">
          <span class="label">Nom d'utilisateur</span>
          <input v-model="username" type="text" name="username" placeholder="john_doe" required autocomplete="username" />
        </label>

        <label class="field">
          <span class="label">Email</span>
          <input v-model="email" type="email" name="email" placeholder="vous@example.com" required autocomplete="email" />
        </label>

        <label class="field">
          <span class="label">Prénom</span>
          <input v-model="firstName" type="text" name="firstname" placeholder="Jean" />
        </label>

        <label class="field">
          <span class="label">Nom</span>
          <input v-model="lastName" type="text" name="lastname" placeholder="Dupont" />
        </label>

        <label class="field">
          <span class="label">Mot de passe</span>
          <div class="password-field">
            <input v-model="password" :type="showPassword ? 'text' : 'password'" name="password" placeholder="••••••••" required autocomplete="new-password" />
            <button type="button" class="toggle-password" @click="showPassword = !showPassword" :aria-label="showPassword ? 'Cacher le mot de passe' : 'Afficher le mot de passe'">
              <svg v-if="!showPassword" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
                <circle cx="12" cy="12" r="3"/>
              </svg>
              <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M17.94 17.94A10.07 10.07 0 0112 20c-7 0-11-8-11-8a18.45 18.45 0 015.06-5.94M9.9 4.24A9.12 9.12 0 0112 4c7 0 11 8 11 8a18.5 18.5 0 01-2.16 3.19m-6.72-1.07a3 3 0 11-4.24-4.24"/>
                <line x1="1" y1="1" x2="23" y2="23"/>
              </svg>
            </button>
          </div>
        </label>

        <label class="field">
          <span class="label">Confirmation</span>
          <div class="password-field">
            <input v-model="passwordConfirm" :type="showPasswordConfirm ? 'text' : 'password'" name="confirm" placeholder="••••••••" required autocomplete="new-password" />
            <button type="button" class="toggle-password" @click="showPasswordConfirm = !showPasswordConfirm" :aria-label="showPasswordConfirm ? 'Cacher le mot de passe' : 'Afficher le mot de passe'">
              <svg v-if="!showPasswordConfirm" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
                <circle cx="12" cy="12" r="3"/>
              </svg>
              <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M17.94 17.94A10.07 10.07 0 0112 20c-7 0-11-8-11-8a18.45 18.45 0 015.06-5.94M9.9 4.24A9.12 9.12 0 0112 4c7 0 11 8 11 8a18.5 18.5 0 01-2.16 3.19m-6.72-1.07a3 3 0 11-4.24-4.24"/>
                <line x1="1" y1="1" x2="23" y2="23"/>
              </svg>
            </button>
          </div>
        </label>

        <label class="checkbox">
          <input v-model="newsletter" type="checkbox" name="newsletter" />
          <span>Recevoir les mises à jour Axiome</span>
        </label>

        <button type="submit" class="primary" :disabled="loading">{{ loading ? 'Création en cours...' : 'Créer mon compte' }}</button>
        <p v-if="error" class="error">{{ error }}</p>
      </form>

      <div class="meta">
        <p>Déjà membre ? <NuxtLink class="link" to="/connexion">Se connecter</NuxtLink></p>
        <p class="small">Nous stockons vos informations en toute sécurité.</p>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from '#imports';
import { useAuthState } from '~/composables/useAuthState';
import { useAuthAPI } from '~/composables/useAuthAPI';

const email = ref('');
const username = ref('');
const firstName = ref('');
const lastName = ref('');
const password = ref('');
const passwordConfirm = ref('');
const showPassword = ref(false);
const showPasswordConfirm = ref(false);
const newsletter = ref(false);
const error = ref('');
const router = useRouter();
const { setAuth } = useAuthState();
const { signup, loading } = useAuthAPI();

const handleSubmit = async () => {
  error.value = '';

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
.auth-page {
  min-height: 70vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 48px 16px;
  background: #f7f7fb;
}

.auth-card {
  width: min(520px, 100%);
  background: #ffffff;
  border-radius: 16px;
  padding: 36px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.06);
  display: grid;
  gap: 20px;
}

.auth-header {
  display: grid;
  gap: 6px;
}

.eyebrow {
  margin: 0;
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #6b5ca5;
  font-weight: 700;
}

h1 {
  margin: 0;
  font-size: 28px;
  color: #241431;
}

.sub {
  margin: 0;
  color: #4a4a55;
  font-size: 14px;
}

.auth-form {
  display: grid;
  gap: 16px;
}

.field {
  display: grid;
  gap: 6px;
}

.label {
  font-size: 13px;
  font-weight: 600;
  color: #241431;
}

input[type="text"],
input[type="email"],
input[type="password"] {
  width: 100%;
  padding: 12px 14px;
  border-radius: 10px;
  border: 1px solid #dcd9e6;
  background: #faf9fd;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

input:focus {
  outline: none;
  border-color: #7b5ce0;
  box-shadow: 0 0 0 3px rgba(123, 92, 224, 0.15);
}

.password-field {
  position: relative;
  display: flex;
  align-items: center;
}

.password-field input {
  flex: 1;
  padding-right: 45px;
}

.toggle-password {
  position: absolute;
  right: 12px;
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #6b5ca5;
  transition: color 0.2s ease;
}

.toggle-password:hover {
  color: #7b5ce0;
}

.checkbox {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  color: #3c314f;
}

.checkbox input {
  width: 16px;
  height: 16px;
}

.primary {
  width: 100%;
  border: none;
  border-radius: 12px;
  padding: 14px;
  font-size: 15px;
  font-weight: 700;
  background: linear-gradient(135deg, #2f0538 0%, #3a0f4f 100%);
  color: #ffffff;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 10px 20px rgba(47, 5, 56, 0.16);
}

.primary:active {
  transform: translateY(0);
}

.meta {
  display: grid;
  gap: 4px;
  font-size: 13px;
  color: #4a4a55;
}

.link {
  color: #7b5ce0;
  text-decoration: none;
  font-weight: 600;
}

.small {
  margin: 0;
  color: #6e6585;
  font-size: 12px;
}

@media (max-width: 640px) {
  .auth-card {
    padding: 28px;
  }
}
</style>
