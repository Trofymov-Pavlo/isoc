<template>
  <section class="account-page">
    <div v-if="loading && !user" class="loading">Chargement...</div>
    <div v-else-if="error && !user" class="error">{{ error }}</div>

    <div v-else-if="user" class="grid">
      <aside class="sidebar">
        <div class="account-card">
          <p class="eyebrow">Votre compte</p>
          <span class="status" :class="statusClass">{{ statusLabel }}</span>
          <p class="name">{{ displayName }}</p>
          <p class="muted">ID client : {{ user.id || '—' }}</p>
          <button class="copy-btn" type="button" @click="copyId">Copier l’ID client</button>
        </div>

        <nav class="nav">
          <button class="nav-item" type="button" @click="scrollTo('infos')">Vos informations</button>
          <button class="nav-item" type="button" @click="scrollTo('saved')">Médias enregistrés</button>
          <button class="nav-item" type="button" @click="scrollTo('contact')">Nous contacter</button>
        </nav>

        <button class="logout-btn" type="button" @click="handleLogout">Se déconnecter</button>
      </aside>

      <main class="main">
        <section id="infos" class="info-card">
          <h3>Vos informations</h3>

          <div class="info-rows">
            <div class="info-row">
              <div>
                <p class="label">Civilité</p>
                <p class="value">{{ user.first_name ? user.first_name + ' ' + (user.last_name || '') : displayName }}</p>
              </div>
              <button class="info-action" type="button" @click="toggleEdit">Modifier vos coordonnées</button>
            </div>

            <div class="info-row">
              <div>
                <p class="label">Adresse e-mail</p>
                <p class="value">{{ user.email }}</p>
              </div>
            </div>

            <div class="info-row">
              <div>
                <p class="label">Mot de passe</p>
                <p class="value">••••••••</p>
              </div>
              <button class="info-action" type="button" @click="togglePassword">Changer</button>
            </div>
          </div>

          <div v-if="editMode" class="editor">
            <div class="form-grid">
              <div class="field">
                <span class="label">Nom d'utilisateur</span>
                <input v-model="editData.username" type="text" />
              </div>
              <div class="field">
                <span class="label">Email</span>
                <input v-model="editData.email" type="email" />
              </div>
              <div class="field">
                <span class="label">Prénom</span>
                <input v-model="editData.firstName" type="text" />
              </div>
              <div class="field">
                <span class="label">Nom</span>
                <input v-model="editData.lastName" type="text" />
              </div>
              <div class="actions-row">
                <button class="btn-secondary" type="button" @click="resetEdit">Annuler</button>
                <button class="btn-primary" type="button" @click="handleUpdateProfile" :disabled="loading">Sauvegarder</button>
              </div>
              <p v-if="editError" class="error">{{ editError }}</p>
            </div>
          </div>

          <div v-if="passwordMode" class="editor">
            <div class="form-grid">
              <div class="field">
                <span class="label">Ancien mot de passe</span>
                <input v-model="passwordData.oldPassword" type="password" />
              </div>
              <div class="field">
                <span class="label">Nouveau mot de passe</span>
                <input v-model="passwordData.newPassword" type="password" />
              </div>
              <div class="field">
                <span class="label">Confirmez</span>
                <input v-model="passwordData.confirmPassword" type="password" />
              </div>
              <div class="actions-row">
                <button class="btn-secondary" type="button" @click="cancelPasswordChange">Annuler</button>
                <button class="btn-primary" type="button" @click="handleChangePassword" :disabled="loading">Mettre à jour</button>
              </div>
              <p v-if="passwordError" class="error">{{ passwordError }}</p>
              <p v-if="passwordSuccess" class="success">{{ passwordSuccess }}</p>
            </div>
          </div>
        </section>

        <section id="saved" class="info-card">
          <div class="card-header-row">
            <h3>Vos médias enregistrés</h3>
            <NuxtLink class="btn-secondary link-btn" to="/liked">Voir tout</NuxtLink>
          </div>

          <div v-if="loadingArticles" class="muted">Chargement de vos médias enregistrés…</div>
          <div v-else-if="!likedTop3.length" class="muted">Vous n'avez pas encore enregistré de média.</div>
          <ul v-else class="liked-list">
            <li v-for="item in likedTop3" :key="item.link" class="liked-item">
              <div class="liked-meta">
                <p class="liked-title">{{ item.title }}</p>
                <p class="liked-source">{{ item.source || 'Source inconnue' }}</p>
              </div>
              <NuxtLink class="btn-primary link-btn" :to="item.link" target="_blank">Ouvrir</NuxtLink>
            </li>
          </ul>
        </section>

        <section id="contact" class="info-card">
          <h3>Nous contacter</h3>
          <p class="muted">Besoin d'aide ou d'une information ? Écrivez-nous directement.</p>
          <NuxtLink class="btn-primary link-btn" to="/contact">Aller à la page contact</NuxtLink>
        </section>
      </main>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import { useRouter } from '#app';
import { useAuthAPI } from '~/composables/useAuthAPI';
import { useAuthState } from '~/composables/useAuthState';
import { useSavedMedia } from '~/composables/useSavedMedia';

const router = useRouter();
const { user, loading, error, me, updateProfile, changePassword, logout } = useAuthAPI();
const { setAuth } = useAuthState();
const { getTopSaved, loading: loadingArticles } = useSavedMedia();

const editMode = ref(false);
const passwordMode = ref(false);
const editError = ref('');
const passwordError = ref('');
const passwordSuccess = ref('');

const editData = ref({ username: '', email: '', firstName: '', lastName: '' });
const passwordData = ref({ oldPassword: '', newPassword: '', confirmPassword: '' });

const displayName = computed(() => user.value?.first_name || user.value?.username || '');

const likedTop3 = ref<any[]>([]);

const isSubscribed = computed(() => {
  const u = (user.value as any) || {};
  const directFlag =
    u.is_subscribed ??
    u.subscribed ??
    u.subscription_active ??
    u.is_premium ??
    u.isPremium ??
    u.isSubscriber ??
    u.has_subscription ??
    u.abonne ??
    u.abonnee;

  if (typeof directFlag === 'boolean') return directFlag;

  const subscription = u.subscription;
  if (subscription && typeof subscription === 'object') {
    if (typeof subscription.active === 'boolean') return subscription.active;
    if (typeof subscription.status === 'string') {
      return ['active', 'paid', 'trial', 'subscribed'].includes(subscription.status.toLowerCase());
    }
  }

  return false;
});

const statusLabel = computed(() => (isSubscribed.value ? 'ABONNÉ' : 'NON ABONNÉ'));
const statusClass = computed(() => (isSubscribed.value ? 'is-subscribed' : 'is-not-subscribed'));

const copyId = async () => {
  try {
    await navigator.clipboard.writeText(String(user.value?.id || ''));
  } catch {
    // no-op
  }
};

const scrollTo = (id: string) => {
  const element = document.getElementById(id);
  element?.scrollIntoView({ behavior: 'smooth', block: 'start' });
};

const hydrateEditForm = () => {
  if (!user.value) return;
  editData.value = {
    username: user.value.username || '',
    email: user.value.email || '',
    firstName: user.value.first_name || '',
    lastName: user.value.last_name || '',
  };
};

const loadUser = async () => {
  if (!user.value) {
    await me();
  }
  hydrateEditForm();
};

onMounted(async () => {
  await loadUser();
  const top3 = await getTopSaved(3);
  likedTop3.value = top3;
});

const toggleEdit = () => {
  if (editMode.value) hydrateEditForm();
  editError.value = '';
  editMode.value = !editMode.value;
};

const resetEdit = () => {
  hydrateEditForm();
  editError.value = '';
  editMode.value = false;
};

const togglePassword = () => {
  passwordError.value = '';
  passwordSuccess.value = '';
  passwordMode.value = !passwordMode.value;
};

const cancelPasswordChange = () => {
  passwordMode.value = false;
  passwordError.value = '';
  passwordSuccess.value = '';
  passwordData.value = { oldPassword: '', newPassword: '', confirmPassword: '' };
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
    }, 1800);
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

</script>

<style scoped lang="scss">
.account-page {
  padding: 28px 0 48px;
  background: transparent;
}

.grid {
  display: grid;
  grid-template-columns: minmax(260px, 320px) minmax(0, 1fr);
  gap: 24px;
  align-items: start;
}

.muted { color: var(--text-secondary); margin: 2px 0; }

button,
.link-btn {
  font: inherit;
}

button:focus-visible,
.link-btn:focus-visible {
  outline: 2px solid var(--brand-accent);
  outline-offset: 2px;
}

/* Sidebar */
.sidebar { display: flex; flex-direction: column; gap: 16px; }
.account-card { background: var(--bg-primary); border: 1px solid var(--border-color); border-radius: 12px; padding: 18px; }
.eyebrow { letter-spacing: 0.12em; text-transform: uppercase; font-size: 12px; font-weight: 700; color: var(--text-tertiary); margin: 0 0 10px 0; }
.status { display: inline-flex; align-items: center; gap: 8px; background: var(--bg-primary); border: 1px solid var(--border-color); border-radius: 999px; padding: 6px 10px; font-size: 11px; font-weight: 900; letter-spacing: 0.08em; }
.status.is-not-subscribed { background: rgba(177, 90, 0, 0.10); border-color: rgba(177, 90, 0, 0.35); color: #b15a00; }
.status.is-subscribed { background: rgba(29, 131, 72, 0.10); border-color: rgba(29, 131, 72, 0.35); color: #1d8348; }
.name { margin: 12px 0 6px 0; font-size: 20px; font-weight: 800; color: var(--text-primary); }
.copy-btn { margin-top: 14px; border: 1px solid var(--border-color); background: var(--bg-primary); padding: 10px 12px; border-radius: 999px; font-weight: 800; cursor: pointer; }
.copy-btn:hover { background: var(--bg-secondary); }

.nav { background: var(--bg-primary); border: 1px solid var(--border-color); border-radius: 12px; padding: 6px; display: grid; }
.nav-item { text-align: left; border: none; background: transparent; padding: 14px 12px; border-radius: 10px; cursor: pointer; color: var(--text-primary); font-weight: 700; }
.nav-item:hover { background: var(--bg-secondary); }
.nav-link { text-align: left; padding: 14px 12px; border-radius: 10px; color: var(--text-primary); font-weight: 800; text-decoration: none; }
.nav-link:hover { background: var(--bg-secondary); text-decoration: none; }
.logout-btn { border: 1px solid rgba(192, 57, 43, 0.35); background: rgba(192, 57, 43, 0.06); padding: 12px; border-radius: 10px; font-weight: 900; cursor: pointer; color: #c0392b; }
.logout-btn:hover { background: rgba(192, 57, 43, 0.10); }

/* Main */
.main { display: grid; gap: 18px; }
.info-card { background: var(--bg-primary); border: 1px solid var(--border-color); border-radius: 12px; padding: 18px; }
h3 { margin: 0 0 14px 0; font-size: 30px; color: var(--text-primary); }

.card-header-row { display: flex; justify-content: space-between; align-items: center; gap: 12px; }

.btn-primary { border: none; padding: 10px 14px; border-radius: 10px; font-weight: 800; cursor: pointer; background: var(--brand-primary); color: #fff; width: fit-content; text-decoration: none; display: inline-flex; align-items: center; justify-content: center; }
.btn-primary:hover { filter: brightness(1.05); }
.btn-secondary { border: 1px solid var(--border-color); padding: 10px 18px; border-radius: 10px; font-weight: 800; cursor: pointer; background: var(--bg-secondary); color: var(--text-primary); width: fit-content; text-decoration: none; display: inline-flex; align-items: center; justify-content: center; }
.btn-secondary:hover { filter: brightness(0.98); }
.btn-primary:disabled,
.btn-secondary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.blue-alert { display: grid; grid-template-columns: auto 1fr; gap: 12px; align-items: start; background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 10px; padding: 18px; margin: 12px 0 18px 0; }
.alert-icon { width: 22px; height: 22px; border-radius: 50%; border: 2px solid var(--brand-accent); color: var(--brand-accent); display: flex; align-items: center; justify-content: center; font-weight: 900; margin-top: 2px; }
.alert-title { margin: 0; font-weight: 900; color: var(--text-primary); }
.alert-text .muted { margin-top: 6px; }
.blue-alert .btn-primary { margin-top: 14px; }

.info-rows { border-top: 1px solid var(--border-color); margin-top: 6px; }
.info-row { display: flex; justify-content: space-between; align-items: center; padding: 16px 0; border-top: 1px solid var(--border-color); gap: 16px; }
.info-row:first-child { border-top: none; }
.label { margin: 0; font-size: 12px; font-weight: 900; letter-spacing: 0.08em; text-transform: uppercase; color: var(--text-tertiary); }
.value { margin: 6px 0 0 0; font-size: 15px; color: var(--text-primary); }
.info-action { border: none; background: transparent; color: var(--brand-accent); font-weight: 900; cursor: pointer; padding: 8px 10px; border-radius: 10px; }
.info-action:hover { background: var(--bg-secondary); }

.editor { margin-top: 16px; border-top: 1px solid var(--border-color); padding-top: 16px; }
.form-grid { display: grid; gap: 12px; }
.field { display: grid; gap: 6px; }
.field input { width: 100%; padding: 12px; border-radius: 10px; border: 1px solid var(--border-color); background: var(--bg-primary); }
.field input:focus-visible { outline: 2px solid var(--brand-accent); outline-offset: 2px; }
.actions-row { display: flex; justify-content: flex-end; gap: 10px; margin-top: 10px; }

.liked-list { list-style: none; padding: 0; margin: 0; display: grid; gap: 12px; }
.liked-item { display: flex; justify-content: space-between; gap: 12px; padding: 12px; border: 1px solid var(--border-color); border-radius: 12px; background: var(--bg-secondary); align-items: center; flex-wrap: wrap; }
.liked-meta { display: grid; gap: 4px; min-width: 0; }
.liked-title { margin: 0; font-weight: 800; color: var(--text-primary); }
.liked-source { margin: 0; color: var(--text-secondary); font-size: 13px; }


.loading { text-align: center; color: var(--text-secondary); }
.error { color: #c0392b; }
.success { color: #1d8348; }

@media (max-width: 1100px) {
  .grid { grid-template-columns: 1fr; }
  h3 { font-size: 28px; }
}

@media (max-width: 640px) {
  .account-page { padding: 18px 0 36px; }
  .hero-card, .info-card, .account-card { padding: 16px; }
  .info-row { flex-direction: column; align-items: flex-start; }
  .actions-row { justify-content: stretch; }
  .actions-row .btn-primary,
  .actions-row .btn-secondary { width: 100%; }
}
</style>

