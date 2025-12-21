<template>
  <div class="new-header">
    <!-- Top bar with tagline and account -->
    <div class="header-top">
      <div class="top-left">
        <span class="pulse-dot"></span>
        <span class="tagline">Média indépendant — Conflit Ukraine / Russie</span>
      </div>
      <div class="top-right">
        <a href="/rss.xml" class="icon-link" title="Flux RSS">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M4 11a9 9 0 0 1 9 9M4 4a16 16 0 0 1 16 16"></path>
            <circle cx="5" cy="19" r="1"></circle>
          </svg>
        </a>
        <NuxtLink :to="accountLink" class="account-link" :title="accountLabel">
          <svg v-if="!isAuthenticated" class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
            <circle cx="12" cy="7" r="4"></circle>
          </svg>
          <span v-else>{{ accountLabel }}</span>
        </NuxtLink>
      </div>
    </div>

    <!-- Main navigation bar -->
    <div class="header-main">
      <div class="logo-block" @click="goIndex">
        <img :src="logo" alt="ISOC AXIOM" class="logo" />
      </div>

      <nav class="main-nav">
        <NuxtLink to="/" class="nav-item" exact-active-class="active">
          Accueil
        </NuxtLink>
        <NuxtLink to="/en-direct" class="nav-item" exact-active-class="active">
          <span class="live-badge">●</span>
          En Direct
        </NuxtLink>
        <NuxtLink to="/articles" class="nav-item" exact-active-class="active">
          Articles
        </NuxtLink>
        <NuxtLink to="/video" class="nav-item" exact-active-class="active">
          Vidéos
        </NuxtLink>
        <NuxtLink to="/liked" class="nav-item" exact-active-class="active">
          ❤️ Aimés
        </NuxtLink>
        <NuxtLink to="/a-propos" class="nav-item" exact-active-class="active">
          À Propos
        </NuxtLink>
        <NuxtLink to="/contact" class="nav-item" exact-active-class="active">
          Contact
        </NuxtLink>
      </nav>

      <div class="header-right">
        <div class="search-container" :class="{ open: isSearchOpen }">
          <button
            class="search-btn"
            title="Rechercher"
            @click="toggleSearch"
            :aria-pressed="isSearchOpen"
          >
            <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="11" cy="11" r="8"></circle>
              <path d="m21 21-4.35-4.35"></path>
            </svg>
          </button>
          <div v-if="isSearchOpen" class="search-panel">
            <input
              ref="searchInput"
              v-model="searchTerm"
              type="search"
              placeholder="Rechercher..."
              class="search-input"
              @keydown.esc="closeSearch"
              @keyup.enter="performSearch"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, nextTick } from 'vue';
import { useRouter } from 'vue-router';
import logoIsoc from '@/assets/logoIsoc.png';
import { useAuthState } from '~/composables/useAuthState';

const logo = logoIsoc;
const router = useRouter();
const { isAuthenticated } = useAuthState();
const isSearchOpen = ref(false);
const searchTerm = ref('');
const searchInput = ref<HTMLInputElement | null>(null);

const accountLabel = computed(() => 
  isAuthenticated.value ? 'Mon compte' : 'Connexion'
);

const accountLink = computed(() =>
  isAuthenticated.value ? '/mon-compte' : '/connexion'
);

function goIndex() {
  router.push('/');
}

function toggleSearch() {
  isSearchOpen.value = !isSearchOpen.value;
  if (isSearchOpen.value) {
    nextTick(() => searchInput.value?.focus());
  }
}

function closeSearch() {
  isSearchOpen.value = false;
}

function performSearch() {
  if (searchTerm.value.trim()) {
    router.push(`/articles?q=${encodeURIComponent(searchTerm.value)}`);
    closeSearch();
  }
}
</script>

<style scoped>
.new-header {
  background: #ffffff;
  border-bottom: 1px solid #f0f0f0;
  display: flex;
  flex-direction: column;
  position: sticky;
  top: 0;
  z-index: 999;
}

/* Top bar */
.header-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 12px;
  font-size: 11px;
  border-bottom: 1px solid #f0f0f0;
  background: #fafafa;
}

.top-left {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.pulse-dot {
  width: 8px;
  height: 8px;
  background: #ff6b6b;
  border-radius: 50%;
  box-shadow: 0 0 0 6px rgba(255, 107, 107, 0.18);
  animation: pulse 2s infinite;
  flex-shrink: 0;
}

@keyframes pulse {
  0%, 100% { 
    opacity: 1; 
    box-shadow: 0 0 0 6px rgba(255, 107, 107, 0.18);
  }
  50% { 
    opacity: 0.65; 
    box-shadow: 0 0 0 10px rgba(255, 107, 107, 0.08);
  }
}

.tagline {
  color: #2f0538;
  font-weight: 600;
  letter-spacing: 0.15px;
}

.top-right {
  display: flex;
  align-items: center;
  gap: 12px;
}

.icon-link {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  color: #555;
  text-decoration: none;
  cursor: pointer;
  transition: color 0.2s ease;
}

.icon-link:hover {
  color: #2f0538;
}

.account-link {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #2f0538;
  text-decoration: none;
  font-weight: 500;
  font-size: 12px;
  transition: opacity 0.2s ease;
}

.account-link:hover {
  opacity: 0.7;
}

/* Main header */
.header-main {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 12px;
  gap: 20px;
}

.logo-block {
  display: flex;
  align-items: center;
  cursor: pointer;
  flex-shrink: 0;
}

.logo {
  height: 40px;
  width: auto;
}

.main-nav {
  display: flex;
  align-items: center;
  gap: 1px;
  flex: 1;
  justify-content: center;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 12px;
  color: #555;
  text-decoration: none;
  font-size: 13px;
  font-weight: 500;
  transition: all 0.2s ease;
  border-bottom: 2px solid transparent;
  position: relative;
  white-space: nowrap;
}

.nav-item:hover {
  color: #2f0538;
  background: rgba(47, 5, 56, 0.05);
}

.nav-item.active {
  color: #2f0538;
  border-bottom-color: #7b5ce0;
  background: rgba(123, 92, 224, 0.08);
}

.live-badge {
  color: #ff6b6b;
  font-size: 10px;
  animation: blink 1.5s infinite;
}

@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

/* Right side controls */
.header-right {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-shrink: 0;
}

.search-container {
  position: relative;
}

.search-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  background: none;
  border: none;
  color: #555;
  cursor: pointer;
  transition: color 0.2s ease;
  padding: 0;
}

.search-btn:hover {
  color: #2f0538;
}

.search-panel {
  position: absolute;
  top: 100%;
  right: 0;
  margin-top: 8px;
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  padding: 8px;
  min-width: 280px;
  animation: slideDown 0.2s ease;
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.search-input {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 13px;
  outline: none;
  transition: border-color 0.2s ease;
}

.search-input:focus {
  border-color: #7b5ce0;
  background: rgba(123, 92, 224, 0.05);
}

.icon {
  width: 16px;
  height: 16px;
}

/* Mobile responsiveness */
@media (max-width: 768px) {
  .header-top {
    padding: 6px 8px;
    font-size: 10px;
  }

  .header-main {
    padding: 8px;
    gap: 12px;
  }

  .logo {
    height: 32px;
  }

  .main-nav {
    display: none;
  }

  .nav-item {
    padding: 6px 8px;
    font-size: 12px;
  }

  .search-panel {
    min-width: 200px;
  }
}

@media (max-width: 480px) {
  .tagline {
    display: none;
  }

  .top-right {
    gap: 8px;
  }

  .logo {
    height: 28px;
  }

  .header-main {
    padding: 6px;
  }
}
</style>
