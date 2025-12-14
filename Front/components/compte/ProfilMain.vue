<template>
  <section class="profile-page">
    <div class="profile-card">
      <div class="profile-header">
        <p class="eyebrow">Espace membre</p>
        <h1>Mon compte</h1>
        <p class="sub">Gérez vos informations et vos préférences.</p>
      </div>

      <div v-if="loading" class="loading">Chargement...</div>
      <div v-else-if="error" class="error">{{ error }}</div>
      <div v-else-if="user" class="profile-content">
        <div class="info-section">
          <h2>Informations personnelles</h2>
          <div class="info-grid">
            <div class="info-item">
              <span class="label">Nom d'utilisateur</span>
              <span class="value">{{ user.username }}</span>
            </div>
            <div class="info-item">
              <span class="label">Email</span>
              <span class="value">{{ user.email }}</span>
            </div>
            <div class="info-item" v-if="user.first_name">
              <span class="label">Prénom</span>
              <span class="value">{{ user.first_name }}</span>
            </div>
            <div class="info-item" v-if="user.last_name">
              <span class="label">Nom</span>
              <span class="value">{{ user.last_name }}</span>
            </div>
          </div>
        </div>

        <div class="actions">
          <button @click="handleLogout" class="btn-logout">Se déconnecter</button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRouter } from '#imports';
import { useAuthState } from '~/composables/useAuthState';
import { useAuthAPI } from '~/composables/useAuthAPI';

const router = useRouter();
const { isAuthenticated, setAuth } = useAuthState();
const { me, logout } = useAuthAPI();

const user = ref<any>(null);
const loading = ref(true);
const error = ref('');

onMounted(async () => {
  if (!isAuthenticated.value) {
    await router.push('/connexion');
    return;
  }

  try {
    const userData = await me();
    user.value = userData;
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Erreur lors du chargement du profil';
  } finally {
    loading.value = false;
  }
});

const handleLogout = async () => {
  try {
    await logout();
    setAuth(false);
    await router.push('/');
  } catch (err) {
    console.error('Erreur lors de la déconnexion', err);
  }
};
</script>

<style scoped lang="scss">
.profile-page {
  min-height: 70vh;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: 48px 16px;
  background: #f7f7fb;
}

.profile-card {
  width: min(720px, 100%);
  background: #ffffff;
  border-radius: 16px;
  padding: 36px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.06);
  display: grid;
  gap: 32px;
}

.profile-header {
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

h2 {
  margin: 0 0 16px 0;
  font-size: 18px;
  color: #241431;
}

.sub {
  margin: 0;
  color: #4a4a55;
  font-size: 14px;
}

.loading {
  text-align: center;
  padding: 24px;
  color: #6b5ca5;
}

.error {
  background: #fee;
  border-left: 3px solid #c33;
  padding: 12px;
  color: #c33;
  border-radius: 4px;
}

.profile-content {
  display: grid;
  gap: 24px;
}

.info-section {
  display: grid;
  gap: 12px;
}

.info-grid {
  display: grid;
  gap: 16px;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
}

.info-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 12px;
  background: #f7f7fb;
  border-radius: 8px;
}

.info-item .label {
  font-size: 12px;
  color: #6b5ca5;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.info-item .value {
  font-size: 15px;
  color: #241431;
  font-weight: 500;
}

.actions {
  display: flex;
  gap: 12px;
  padding-top: 16px;
  border-top: 1px solid #e8e4f0;
}

.btn-logout {
  padding: 10px 20px;
  background: #fff;
  border: 1px solid #c33;
  color: #c33;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-logout:hover {
  background: #c33;
  color: #fff;
}
</style>
