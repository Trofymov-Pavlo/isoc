<template>
  <section class="auth-page">
    <div class="auth-card">
      <div class="auth-header">
        <p class="eyebrow">Espace membre</p>
        <h1>Connexion</h1>
        <p class="sub">Accédez à vos suivis et contenus personnalisés.</p>
      </div>

      <form class="auth-form" @submit.prevent="handleSubmit">
        <label class="field">
          <span class="label">Email</span>
          <input v-model="email" type="email" name="email" placeholder="vous@example.com" required autocomplete="email" />
        </label>

        <label class="field">
          <span class="label">Mot de passe</span>
          <input v-model="password" type="password" name="password" placeholder="••••••••" required autocomplete="current-password" />
        </label>

        <div class="row">
          <label class="checkbox">
            <input v-model="remember" type="checkbox" name="remember" />
            <span>Se souvenir de moi</span>
          </label>
          <NuxtLink class="link" to="/support">Mot de passe oublié ?</NuxtLink>
        </div>

        <button type="submit" class="primary" :disabled="loading">{{ loading ? 'Connexion en cours...' : 'Se connecter' }}</button>
        <p v-if="error" class="error">{{ error }}</p>
      </form>

      <div class="meta">
        <p>Pas encore de compte ? <NuxtLink class="link" to="/signup">Créer un compte</NuxtLink></p>
        <p class="small">Connexion sécurisée. Vos données restent privées.</p>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from '#imports';
import { useAuthState } from '~/composables/useAuthState';

const email = ref('');
const password = ref('');
const remember = ref(false);
const loading = ref(false);
const error = ref('');
const router = useRouter();
const { setAuth } = useAuthState();

const handleSubmit = async () => {
  error.value = '';
  loading.value = true;
  await new Promise((resolve) => setTimeout(resolve, 400));

  if (!email.value || !password.value) {
    error.value = 'Email et mot de passe requis.';
    loading.value = false;
    return;
  }

  // TODO: remplacer par un appel API sécurisé côté backend (Django/Flask)
  setAuth(true, remember.value);
  loading.value = false;
  await router.push('/');
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

.row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
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

.error {
  margin: 8px 0 0;
  color: #c0392b;
  font-size: 13px;
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
