<template>
  <header class="header">
    <nav class="header-nav">
      <div class="container">
        <div class="nav-content">
          <div class="nav-left">
            <div class="logo-block" @click="goIndex">
              <img :src="logo" alt="ISOC AXIOM" class="logo-img" />
            </div>
          </div>

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

          <div class="nav-right">
            <div class="search-box">
              <button class="search-toggle" @click="toggleSearch" title="Rechercher">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <path d="m21 21-4.35-4.35"></path>
                </svg>
              </button>
              <Transition name="search-panel">
                <div v-if="searchOpen" class="search-dropdown">
                  <input
                    ref="searchInputRef"
                    v-model="searchQuery"
                    type="text"
                    placeholder="Rechercher..."
                    class="search-input"
                    @keyup.enter="performSearch"
                  />
                </div>
              </Transition>
            </div>

            <a href="/rss.xml" class="icon-link" title="Flux RSS">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M4 11a9 9 0 0 1 9 9"></path>
                <path d="M4 4a16 16 0 0 1 16 16"></path>
                <circle cx="5" cy="19" r="1"></circle>
              </svg>
            </a>

            <NuxtLink v-if="isAuthenticated" to="/mon-compte" class="account-btn">
              Mon Compte
            </NuxtLink>
            <NuxtLink v-else to="/connexion" class="account-btn">
              Connexion
            </NuxtLink>
          </div>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup lang="ts">
import { ref, nextTick } from 'vue'
import { useAuthState } from '~/composables/useAuthState'
import logoIsoc from '@/assets/logoIsoc.png'

const logo = logoIsoc
const { isAuthenticated } = useAuthState()

const searchOpen = ref(false)
const searchQuery = ref('')
const searchInputRef = ref<HTMLInputElement | null>(null)

function toggleSearch() {
  searchOpen.value = !searchOpen.value
  if (searchOpen.value) {
    nextTick(() => searchInputRef.value?.focus())
  }
}

function performSearch() {
  if (searchQuery.value.trim()) {
    navigateTo('/explorer?q=' + encodeURIComponent(searchQuery.value.trim()))
    searchOpen.value = false
    searchQuery.value = ''
  }
}

function goIndex() {
  navigateTo('/')
}
</script>

<style scoped>
* { box-sizing: border-box; }

.header {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: #ffffff;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
}

.header-nav {
  padding: 14px 0;
  border-bottom: 1px solid #e9ecf1;
  background: #ffffff;
}

.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 32px;
}

.nav-content {
  display: grid;
  grid-template-columns: 200px 1fr 200px;
  align-items: center;
  gap: 24px;
}

.nav-left {
  display: flex;
  align-items: center;
  justify-content: flex-start;
}

.logo-block {
  display: flex;
  align-items: center;
  cursor: pointer;
  transition: opacity 0.2s ease;
}

.logo-block:hover { opacity: 0.85; }

.logo-img {
  height: 40px;
  width: auto;
  transform: scale(2);
  transform-origin: left center;
}

.nav-links {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
  flex: 1;
}

.nav-links a {
  position: relative;
  color: #374151;
  text-decoration: none;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.2px;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 0;
  transition: color 0.2s ease;
}

.nav-links a:hover { color: #111827; }

.nav-links a.active {
  color: #6d5dd3;
}

.nav-links a.active::after {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 3px;
  background: linear-gradient(90deg, #6d5dd3 0%, #8c7cff 100%);
  border-radius: 999px;
}

.live-dot {
  width: 7px;
  height: 7px;
  background: #ff6b6b;
  border-radius: 50%;
  display: inline-block;
  box-shadow: 0 0 0 6px rgba(255, 107, 107, 0.16);
  animation: pulse 1.8s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; box-shadow: 0 0 0 6px rgba(255, 107, 107, 0.16); }
  50% { opacity: 0.6; box-shadow: 0 0 0 12px rgba(255, 107, 107, 0.08); }
}

.nav-right {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 12px;
}

.search-box { position: relative; }

.search-toggle {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  background: #ffffff;
  border: 1px solid #d9dce3;
  border-radius: 10px;
  color: #5b6170;
  cursor: pointer;
  transition: all 0.2s ease;
}

.search-toggle:hover {
  border-color: #6d5dd3;
  color: #6d5dd3;
  box-shadow: 0 4px 14px rgba(109, 93, 211, 0.16);
}

.search-toggle svg { width: 17px; height: 17px; }

.search-dropdown {
  position: absolute;
  top: calc(100% + 8px);
  right: 0;
  background: #ffffff;
  border: 1px solid #e4e7ed;
  border-radius: 12px;
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.12);
  padding: 10px;
  min-width: 300px;
  z-index: 100;
}

.search-input {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #d9dce3;
  border-radius: 10px;
  font-size: 13px;
  color: #111827;
  background: #ffffff;
  transition: all 0.2s ease;
}

.search-input:focus {
  outline: none;
  border-color: #6d5dd3;
  box-shadow: 0 0 0 3px rgba(109, 93, 211, 0.12);
}

.icon-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 26px;
  height: 26px;
  color: #5b6170;
  text-decoration: none;
  transition: all 0.2s ease;
}

.icon-link:hover { color: #111827; }

.icon-link svg { width: 100%; height: 100%; }

.account-btn {
  padding: 9px 16px;
  background: linear-gradient(120deg, #6d5dd3, #8c7cff);
  border: 1px solid #6d5dd3;
  border-radius: 10px;
  color: #ffffff;
  font-size: 13px;
  font-weight: 700;
  text-decoration: none;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.account-btn:hover {
  box-shadow: 0 8px 24px rgba(109, 93, 211, 0.28);
  transform: translateY(-1px);
}

.search-panel-enter-active,
.search-panel-leave-active { transition: all 0.2s ease; }
.search-panel-enter-from,
.search-panel-leave-to { opacity: 0; transform: translateY(-6px); }

@media (max-width: 1100px) {
  .container { padding: 0 24px; }
  .nav-links { gap: 16px; }
}

@media (max-width: 900px) {
  .nav-content { flex-wrap: wrap; justify-content: center; }
  .nav-left { order: 1; }
  .nav-right { order: 3; }
  .nav-links { order: 2; width: 100%; justify-content: center; }
}

@media (max-width: 640px) {
  .container { padding: 0 16px; }
  .logo-img { height: 34px; }
  .tagline { display: none; }
  .tagline-pill { padding: 6px 10px; }
  .nav-links { gap: 12px; flex-wrap: wrap; }
  .nav-links a { font-size: 12px; }
  .search-dropdown { min-width: 260px; }
}

@media (max-width: 480px) {
  .nav-right { gap: 10px; }
  .account-btn { padding: 8px 12px; font-size: 12px; }
  .search-dropdown {
    position: fixed;
    left: 16px;
    right: 16px;
    width: auto;
    min-width: unset;
  }
}
</style>
