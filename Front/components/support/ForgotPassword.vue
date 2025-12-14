<template>
  <section class="auth-page">
    <div class="auth-card">
      <div class="auth-header">
        <p class="eyebrow">Aide</p>
        <h1>Réinitialiser mon mot de passe</h1>
        <p class="sub">Entrez votre email pour recevoir les instructions.</p>
      </div>

      <form v-if="!resetSent" class="auth-form" @submit.prevent="handlePasswordReset">
        <label class="field">
          <span class="label">Email</span>
          <input v-model="email" type="email" name="email" placeholder="vous@example.com" required autocomplete="email" />
        </label>

        <button type="submit" class="primary" :disabled="loading">{{ loading ? 'Envoi en cours...' : 'Envoyer le lien' }}</button>
        <p v-if="error" class="error">{{ error }}</p>
      </form>

      <div v-else class="success-message">
        <p>✓ Lien de réinitialisation envoyé à <strong>{{ email }}</strong></p>
        <p>Vérifiez votre email et cliquez sur le lien pour définir un nouveau mot de passe.</p>
        <button class="primary" @click="resetSent = false">Retour</button>
      </div>

      <div class="meta">
        <p><NuxtLink class="link" to="/connexion">Retour à la connexion</NuxtLink></p>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useAuthAPI } from '~/composables/useAuthAPI';

const email = ref('');
const error = ref('');
const resetSent = ref(false);
const { passwordReset, loading } = useAuthAPI();

const handlePasswordReset = async () => {
  error.value = '';

  if (!email.value) {
    error.value = 'Email requis.';
    return;
  }

  try {
    await passwordReset(email.value);
    resetSent.value = true;
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Erreur lors de la réinitialisation';
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

.primary:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 10px 20px rgba(47, 5, 56, 0.16);
}

.primary:active:not(:disabled) {
  transform: translateY(0);
}

.primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.error {
  margin: 8px 0 0;
  color: #c0392b;
  font-size: 13px;
}

.success-message {
  display: grid;
  gap: 16px;
  padding: 20px;
  background: #edf5e3;
  border-radius: 12px;
  color: #2d5016;
}

.success-message p {
  margin: 0;
  font-size: 14px;
}

.success-message strong {
  font-weight: 700;
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

@media (max-width: 640px) {
  .auth-card {
    padding: 28px;
  }
}
</style>
