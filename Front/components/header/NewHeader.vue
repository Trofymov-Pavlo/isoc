<template>
  <header class="header">
    <!-- Tagline with pulse indicator -->
    <div class="tagline-bar">
      <span class="pulse-indicator"></span>
      <span class="tagline">Média indépendant | Conflit Ukraine-Russie</span>
    </div>

    <!-- Main navigation bar -->
    <nav class="header-nav">
      <div class="container">
        <div class="nav-content">
          <!-- Logo on the left -->
          <div class="logo-block" @click="goIndex">
            <img :src="logo" alt="ISOC AXIOM" class="logo-img" />
          </div>

          <!-- Navigation links in center -->
          <div class="nav-links">
            <NuxtLink to="/" exact-active-class="active">Accueil</NuxtLink>
            <NuxtLink to="/en-direct" exact-active-class="active">
              <span class="live-dot"></span>En Direct
            </NuxtLink>
            <NuxtLink to="/explorer" exact-active-class="active">Explorer</NuxtLink>
            <NuxtLink to="/liked" exact-active-class="active">Mes Favoris</NuxtLink>
            <NuxtLink to="/a-propos" exact-active-class="active">À Propos</NuxtLink>
            <NuxtLink to="/contact" exact-active-class="active">Contact</NuxtLink>
          </div>

          <!-- Right side: Search, RSS, Account -->
          <div class="nav-right">
            <!-- Search -->
            <div class="search-box">
              <button class="search-toggle" @click="toggleSearch" title="Rechercher">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                  <circle cx="11" cy="11" r="8"></circle>
                  <path d="m21 21-4.35-4.35"></path>
                </svg>
              </button>
              <Transition name="search-panel">
                <div v-if="isSearchOpen" class="search-dropdown">
                  <input
                    ref="searchInput"
                    v-model="searchTerm"
                    type="text"
                    placeholder="Rechercher articles, vidéos..."
                    class="search-input"
                    @keydown.esc="closeSearch"
                    @keyup.enter="performSearch"
                  />
                </div>
              </Transition>
            </div>

            <!-- RSS Link -->
            <a href="/rss.xml" class="icon-link" title="Flux RSS">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <path d="M4 11a9 9 0 0 1 9 9M4 4a16 16 0 0 1 16 16"></path>
                <circle cx="5" cy="19" r="1"></circle>
              </svg>
            </a>

            <!-- Account Link -->
            <NuxtLink :to="accountLink" class="account-btn">
              {{ accountLabel }}
            </NuxtLink>
          </div>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup lang="ts">
import { ref, computed, nextTick } from 'vue';
import logoIsoc from '@/assets/logoIsoc.png';
import { useAuthState } from '~/composables/useAuthState';

const logo = logoIsoc;
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
  navigateTo('/');
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
    navigateTo(`/explorer?q=${encodeURIComponent(searchTerm.value)}`);
    closeSearch();
  }
}
</script>

<style scoped>
* {
  box-sizing: border-box;
}

.header {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: #ffffff;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

/* Tagline bar */
.tagline-bar {
  background: #f1f3f5;
  border-bottom: 1px solid #e5e7eb;
  padding: 10px 40px;
  font-size: 12px;
  display: flex;
  align-items: center;
  gap: 10px;
  color: #343a40;
}

.pulse-indicator {
  width: 7px;
  height: 7px;
  background: #dc3545;
  border-radius: 50%;
  flex-shrink: 0;
  animation: pulse-animation 2s ease-in-out infinite;
}

@keyframes pulse-animation {
  0%, 100% {
    opacity: 1;
    box-shadow: 0 0 0 3px rgba(220, 53, 69, 0.2);
  }
  50% {
    opacity: 0.7;
    box-shadow: 0 0 0 8px rgba(220, 53, 69, 0.1);
  }
}

.tagline {
  color: #2d2f33;
  font-weight: 600;
  letter-spacing: 0.3px;
  font-size: 12px;
}

.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 40px;
}

/* Main navigation */
.header-nav {
  padding: 12px 0;
  border-bottom: 1px solid #e6e8ec;
  background: #ffffff;
}

.nav-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 40px;
  display: flex;
  align-items: center;
  gap: 30px;
  justify-content: flex-start;
}

/* Logo block (left) */
.logo-block {
  flex-shrink: 0;
  cursor: pointer;
  display: flex;
  align-items: center;
  transition: opacity 0.2s ease;
}

.logo-block:hover {
  opacity: 0.8;
}

.logo-img {
  height: 40px;
  width: auto;
}

/* Navigation links (center) */
.nav-links {
  display: flex;
  gap: 30px;
  flex: 1;
}

.nav-links a {
  position: relative;
  color: #3b4048;
  text-decoration: none;
  font-size: 13px;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: color 0.2s ease;
  white-space: nowrap;
}

.nav-links a:hover {
  color: #212529;
}

.nav-links a.active {
  color: #7b5ce0;
}

.nav-links a.active::after {
  content: '';
  position: absolute;
  bottom: -12px;
  left: 0;
  right: 0;
  height: 3px;
  background: #7b5ce0;
  border-radius: 2px 2px 0 0;
}

.live-dot {
  width: 6px;
  height: 6px;
  background: #dc3545;
  border-radius: 50%;
  display: inline-block;
  animation: pulse-animation 2s ease-in-out infinite;
  flex-shrink: 0;
}

/* Right section: Search, RSS, Account */
.nav-right {
  display: flex;
  align-items: center;
  gap: 16px;
  flex-shrink: 0;
}

/* Search box */
.search-box {
  position: relative;
}

.search-toggle {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  background: none;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  color: #6c757d;
  cursor: pointer;
  transition: all 0.2s ease;
  padding: 0;
}

.search-toggle:hover {
  border-color: #7b5ce0;
  color: #7b5ce0;
  background: #f8f9ff;
}

.search-toggle svg {
  width: 18px;
  height: 18px;
}

.search-dropdown {
  position: absolute;
  top: 100%;
  right: 0;
  margin-top: 8px;
  background: white;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
  padding: 12px;
  min-width: 340px;
}

.search-input {
  width: 100%;
  padding: 10px 14px;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  font-size: 13px;
  background: #ffffff;
  color: #212529;
  outline: none;
  transition: all 0.2s ease;
}

.search-input:focus {
  border-color: #7b5ce0;
  box-shadow: 0 0 0 3px rgba(123, 92, 224, 0.1);
}

.search-input::placeholder {
  color: #adb5bd;
}

/* Icon link (RSS) */
.icon-link {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  color: #5c606a;
  text-decoration: none;
  transition: all 0.2s ease;
  cursor: pointer;
  flex-shrink: 0;
}

.icon-link:hover {
  color: #111827;
}

.icon-link svg {
  width: 100%;
  height: 100%;
}

/* Account button */
.account-btn {
  padding: 8px 16px;
  background: #ffffff;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  color: #374151;
  text-decoration: none;
  font-size: 13px;
  font-weight: 600;
  transition: all 0.25s ease;
  cursor: pointer;
  white-space: nowrap;
  flex-shrink: 0;
}

.account-btn:hover {
  background: #f8fafc;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

/* Transitions */
.search-panel-enter-active,
.search-panel-leave-active {
  transition: all 0.2s ease;
}

.search-panel-enter-from,
.search-panel-leave-to {
  opacity: 0;
  transform: translateY(-8px);
}

/* Responsive */
@media (max-width: 1024px) {
  .tagline-bar,
  .nav-content {
    padding: 0 24px;
  }

  .nav-content {
    gap: 20px;
  }

  .nav-links {
    gap: 20px;
  }

  .nav-links a {
    font-size: 12px;
    gap: 4px;
  }

  .search-dropdown {
    min-width: 280px;
  }
}

@media (max-width: 768px) {
  .tagline-bar,
  .nav-content {
    padding: 0 16px;
  }

  .tagline {
    font-size: 11px;
  }

  .logo-img {
    height: 36px;
  }

  .nav-links {
    gap: 16px;
  }

  .nav-links a {
    font-size: 11px;
  }

  .nav-right {
    gap: 12px;
  }

  .search-dropdown {
    min-width: 260px;
    right: -12px;
  }
}

@media (max-width: 480px) {
  .tagline-bar {
    padding: 8px 12px;
    font-size: 11px;
    gap: 8px;
  }

  .header-nav {
    padding: 10px 0;
  }

  .tagline-bar,
  .nav-content {
    padding: 0 12px;
  }

  .tagline {
    display: none;
  }

  .logo-img {
    height: 32px;
  }

  .nav-links {
    gap: 12px;
    flex: 1;
  }

  .nav-links a {
    font-size: 10px;
  }

  .nav-right {
    gap: 8px;
  }

  .search-dropdown {
    position: fixed;
    left: 16px;
    right: 16px;
    width: auto;
    min-width: unset;
  }
}
</style>
