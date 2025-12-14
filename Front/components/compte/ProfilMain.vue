<template>
  <section class="profile-page">
    <div class="profile-card">
      <div class="profile-header">
        <p class="eyebrow">Espace membre</p>
        <h1>Mon compte</h1>
        <p class="sub">Gérez vos informations et vos préférences.</p>
      </div>

      <div v-if="loading && !user" class="loading">Chargement...</div>
      <div v-else-if="error && !user" class="error">{{ error }}</div>
      <div v-else-if="user" class="profile-content">
        <!-- Edit Profile Section -->
        <div class="info-section" v-if="!editMode && !passwordMode">
          <div class="section-header">
            <h2>Informations personnelles</h2>
            <button @click="editMode = true" class="btn-edit">Modifier</button>
          </div>
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

        <!-- Edit Profile Form -->
        <div class="info-section" v-if="editMode">
          <div class="section-header">
            <h2>Modifier le profil</h2>
            <button @click="cancelEdit" class="btn-cancel">Annuler</button>
          </div>
          <form @submit.prevent="handleUpdateProfile" class="edit-form">
            <label class="field">
              <span class="label">Nom d'utilisateur</span>
              <input v-model="editData.username" type="text" required />
            </label>
            <label class="field">
              <span class="label">Email</span>
              <input v-model="editData.email" type="email" required />
            </label>
            <label class="field">
              <span class="label">Prénom</span>
              <input v-model="editData.firstName" type="text" />
            </label>
            <label class="field">
              <span class="label">Nom</span>
              <input v-model="editData.lastName" type="text" />
            </label>
            <p v-if="editError" class="error">{{ editError }}</p>
            <button type="submit" class="btn-save" :disabled="loading">
              {{ loading ? 'Enregistrement...' : 'Enregistrer' }}
            </button>
          </form>
        </div>

        <!-- Change Password Form -->
        <div class="info-section" v-if="passwordMode">
          <div class="section-header">
            <h2>Changer le mot de passe</h2>
            <button @click="cancelPasswordChange" class="btn-cancel">Annuler</button>
          </div>
          <form @submit.prevent="handleChangePassword" class="edit-form">
            <label class="field">
              <span class="label">Mot de passe actuel</span>
              <div class="password-field">
                <input v-model="passwordData.oldPassword" :type="showOldPassword ? 'text' : 'password'" required />
                <PasswordToggle :is-shown="showOldPassword" @toggle="showOldPassword = !showOldPassword" />
              </div>
            </label>
            <label class="field">
              <span class="label">Nouveau mot de passe</span>
              <div class="password-field">
                <input v-model="passwordData.newPassword" :type="showNewPassword ? 'text' : 'password'" required />
                <PasswordToggle :is-shown="showNewPassword" @toggle="showNewPassword = !showNewPassword" />
              </div>
            </label>
            <label class="field">
              <span class="label">Confirmer le nouveau mot de passe</span>
              <div class="password-field">
                <input v-model="passwordData.confirmPassword" :type="showConfirmPassword ? 'text' : 'password'" required />
                <PasswordToggle :is-shown="showConfirmPassword" @toggle="showConfirmPassword = !showConfirmPassword" />
              </div>
            </label>
            <p v-if="passwordError" class="error">{{ passwordError }}</p>
            <p v-if="passwordSuccess" class="success">{{ passwordSuccess }}</p>
            <button type="submit" class="btn-save" :disabled="loading">
              {{ loading ? 'Modification...' : 'Changer le mot de passe' }}
            </button>
          </form>
        </div>

        <!-- Actions -->
        <div class="actions" v-if="!editMode && !passwordMode">
          <button @click="passwordMode = true" class="btn-password">Changer le mot de passe</button>
          <button @click="handleLogout" class="btn-logout">Se déconnecter</button>
        </div>

        <!-- Preferences & activity -->
        <div class="info-section" v-if="!editMode && !passwordMode">
          <div class="section-header">
            <h2>Préférences & notifications</h2>
          </div>
          <div class="pref-grid">
            <div class="pref-card">
              <div class="card-header">Newsletter</div>
              <p class="card-text">Gérez votre abonnement aux emails Axiome.</p>
              <div class="pill" :class="newsletterEnabled ? 'pill-on' : 'pill-off'">
                {{ newsletterEnabled ? 'Abonnement actif' : 'Abonnement désactivé' }}
              </div>
              <button class="card-btn" @click="toggleNewsletter">{{ newsletterEnabled ? 'Résilier la newsletter' : "Se réabonner" }}</button>
              <p v-if="newsletterMessage" class="note success-lite">{{ newsletterMessage }}</p>
            </div>

            <div class="pref-card">
              <div class="card-header">Sécurité</div>
              <ul class="card-list">
                <li>Authentification par mot de passe (JWT).</li>
                <li>Pensez à mettre à jour votre mot de passe régulièrement.</li>
                <li>Les sessions inactives expirent automatiquement.</li>
              </ul>
              <button class="card-link" @click="passwordMode = true">Mettre à jour le mot de passe</button>
            </div>

            <div class="pref-card">
              <div class="card-header">Sessions & activité</div>
              <ul class="card-list">
                <li>Connexion active sur ce navigateur.</li>
                <li>Déconnexion possible sur tous les appareils via « Se déconnecter ».</li>
                <li>Les jetons d’accès expirent après 1h, refresh 7j.</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Saved articles -->
        <div class="info-section" v-if="!editMode && !passwordMode">
          <div class="section-header">
            <h2>Derniers articles enregistrés</h2>
            <NuxtLink class="link" to="/liked">Voir tous</NuxtLink>
          </div>
          <ul v-if="savedArticles.length" class="saved-list">
            <li v-for="item in savedArticles" :key="item.title" class="saved-item">
              <div class="saved-meta">
                <p class="saved-title">{{ item.title }}</p>
                <p class="saved-info">{{ item.category }} • {{ item.date }}</p>
              </div>
              <div class="saved-actions">
                <NuxtLink :to="item.link" class="chip">Ouvrir</NuxtLink>
                <button class="chip ghost" @click="removeSaved(item.title)">Retirer</button>
              </div>
            </li>
          </ul>
          <p v-else class="muted">Vous n'avez pas encore enregistré d'article.</p>
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
const { me, logout, updateProfile, changePassword, loading } = useAuthAPI();

const user = ref<any>(null);
const error = ref('');
const editMode = ref(false);
const passwordMode = ref(false);
const editError = ref('');
const passwordError = ref('');
const passwordSuccess = ref('');

const editData = ref({
  username: '',
  email: '',
  firstName: '',
  lastName: ''
});

const passwordData = ref({
  oldPassword: '',
  newPassword: '',
  confirmPassword: ''
});

const showOldPassword = ref(false);
const showNewPassword = ref(false);
const showConfirmPassword = ref(false);

const newsletterEnabled = ref(true);
const newsletterMessage = ref('');
const savedArticles = ref([
  { title: 'Analyse : Situation sur le front Est', date: '13 déc 2025', category: 'Analyse', link: '/article-en-vedette' },
  { title: 'Podcast : Voix du terrain', date: '12 déc 2025', category: 'Podcast', link: '/podcast' },
  { title: 'Dossier vidéo : décryptage', date: '10 déc 2025', category: 'Vidéo', link: '/video' },
]);

onMounted(async () => {
  if (!isAuthenticated.value) {
    await router.push('/connexion');
    return;
  }

  try {
    const userData = await me();
    if (userData) {
      user.value = userData;
      editData.value = {
        username: userData.username || '',
        email: userData.email || '',
        firstName: userData.first_name || '',
        lastName: userData.last_name || ''
      };
    }
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Erreur lors du chargement du profil';
  }
});

const cancelEdit = () => {
  editMode.value = false;
  editError.value = '';
  if (user.value) {
    editData.value = {
      username: user.value.username || '',
      email: user.value.email || '',
      firstName: user.value.first_name || '',
      lastName: user.value.last_name || ''
    };
  }
};

const cancelPasswordChange = () => {
  passwordMode.value = false;
  passwordError.value = '';
  passwordSuccess.value = '';
  passwordData.value = {
    oldPassword: '',
    newPassword: '',
    confirmPassword: ''
  };
};

const handleUpdateProfile = async () => {
  editError.value = '';
  try {
    const updated = await updateProfile(
      editData.value.username,
      editData.value.email,
      editData.value.firstName,
      editData.value.lastName
    );
    user.value = updated;
    editMode.value = false;
  } catch (err) {
    editError.value = err instanceof Error ? err.message : 'Erreur lors de la mise à jour du profil';
  }
};

const handleChangePassword = async () => {
  passwordError.value = '';
  passwordSuccess.value = '';

  if (passwordData.value.newPassword !== passwordData.value.confirmPassword) {
    passwordError.value = 'Les mots de passe ne correspondent pas.';
    return;
  }

  if (passwordData.value.newPassword.length < 8) {
    passwordError.value = 'Le mot de passe doit contenir au moins 8 caractères.';
    return;
  }

  try {
    await changePassword(passwordData.value.oldPassword, passwordData.value.newPassword);
    passwordSuccess.value = 'Mot de passe changé avec succès !';
    setTimeout(() => {
      cancelPasswordChange();
    }, 2000);
  } catch (err) {
    passwordError.value = err instanceof Error ? err.message : 'Erreur lors du changement de mot de passe';
  }
};

const handleLogout = async () => {
  try {
    await logout();
    setAuth(false);
    await router.push('/');
  } catch (err) {
    console.error('Erreur lors de la déconnexion', err);
  }
};

const toggleNewsletter = () => {
  newsletterEnabled.value = !newsletterEnabled.value;
  newsletterMessage.value = newsletterEnabled.value
    ? 'Newsletter réactivée. Vous recevrez les prochaines publications.'
    : 'Newsletter désactivée. Vous ne recevrez plus les emails.';
  setTimeout(() => { newsletterMessage.value = ''; }, 2500);
};

const removeSaved = (title: string) => {
  savedArticles.value = savedArticles.value.filter((item) => item.title !== title);
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

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.btn-edit,
.btn-cancel {
  padding: 8px 16px;
  background: #fff;
  border: 1px solid #7b5ce0;
  color: #7b5ce0;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 13px;
}

.btn-edit:hover,
.btn-cancel:hover {
  background: #7b5ce0;
  color: #fff;
}

.btn-password {
  padding: 10px 20px;
  background: #fff;
  border: 1px solid #6b5ca5;
  color: #6b5ca5;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-password:hover {
  background: #6b5ca5;
  color: #fff;
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

.btn-save {
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
  margin-top: 8px;
}

.btn-save:hover {
  transform: translateY(-1px);
  box-shadow: 0 10px 20px rgba(47, 5, 56, 0.16);
}

.btn-save:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.edit-form {
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

.success {
  background: #efe;
  border-left: 3px solid #3c3;
  padding: 12px;
  color: #3c3;
  border-radius: 4px;
  font-size: 13px;
}

.pref-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 16px;
}

.pref-card {
  background: #f7f7fb;
  border-radius: 10px;
  padding: 14px;
  display: grid;
  gap: 8px;
  border: 1px solid #e8e4f0;
}

.card-header {
  font-weight: 700;
  color: #241431;
}

.card-text {
  margin: 0;
  color: #4a4a55;
  font-size: 14px;
}

.pill {
  display: inline-flex;
  align-items: center;
  padding: 6px 10px;
  border-radius: 999px;
  font-weight: 700;
  font-size: 12px;
  width: fit-content;
}

.pill-on {
  background: #e8f8ef;
  color: #1b8a4d;
  border: 1px solid #b8e6c9;
}

.pill-off {
  background: #fff4f4;
  color: #c0392b;
  border: 1px solid #f3c7c1;
}

.card-btn,
.card-link {
  border: none;
  background: linear-gradient(135deg, #2f0538 0%, #3a0f4f 100%);
  color: #fff;
  padding: 10px 12px;
  border-radius: 10px;
  font-weight: 700;
  cursor: pointer;
  text-decoration: none;
  text-align: center;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card-link {
  background: #fff;
  color: #6b5ca5;
  border: 1px solid #dcd9e6;
}

.card-btn:hover,
.card-link:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 14px rgba(47, 5, 56, 0.12);
}

.card-list {
  margin: 0;
  padding-left: 16px;
  display: grid;
  gap: 6px;
  color: #4a4a55;
  font-size: 14px;
}

.note {
  margin: 0;
  font-size: 13px;
}

.success-lite {
  color: #1b8a4d;
}

.saved-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  gap: 10px;
}

.saved-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  padding: 12px;
  border-radius: 10px;
  background: #f7f7fb;
  border: 1px solid #e8e4f0;
}

.saved-meta {
  display: grid;
  gap: 4px;
}

.saved-title {
  margin: 0;
  font-weight: 700;
  color: #241431;
}

.saved-info {
  margin: 0;
  color: #6b5ca5;
  font-size: 13px;
}

.saved-actions {
  display: flex;
  gap: 8px;
}

.chip {
  padding: 8px 12px;
  border-radius: 999px;
  background: #2f0538;
  color: #fff;
  border: none;
  font-weight: 700;
  text-decoration: none;
  cursor: pointer;
}

.chip.ghost {
  background: #fff;
  color: #6b5ca5;
  border: 1px solid #dcd9e6;
}

.muted {
  color: #6e6585;
  font-size: 14px;
  margin: 0;
}
</style>
