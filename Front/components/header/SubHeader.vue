<template>
  <div class="sub-header">
    <div class="container">
      <nav class="nav">
        <NuxtLink to="/" class="nav-link" exact-active-class="is-active">Accueil</NuxtLink>
        <NuxtLink to="/en-direct" class="nav-link" exact-active-class="is-active">
          <span class="live-badge">●</span>
          En Direct
        </NuxtLink>
        <NuxtLink to="/video" class="nav-link" exact-active-class="is-active">
          Vidéos
        </NuxtLink>
        <NuxtLink to="/articles" class="nav-link" exact-active-class="is-active">Articles</NuxtLink>
        <div class="nav-divider"></div>
        <NuxtLink to="/article-en-vedette" class="nav-link" exact-active-class="is-active">Article en Vedette</NuxtLink>
        <NuxtLink to="/podcast" class="nav-link" exact-active-class="is-active">Podcast</NuxtLink>
      </nav>
      <div class="nav-right">
        <div class="search-container" :class="{ open: isSearchOpen }" ref="searchWrapper">
          <button
            class="icon-btn search-btn"
            title="Rechercher"
            @click="toggleSearch"
            :aria-pressed="isSearchOpen"
            :aria-expanded="isSearchOpen"
            aria-controls="subheader-search-panel"
          >
            <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="8"></circle>
              <path d="m21 21-4.35-4.35"></path>
            </svg>
          </button>

          <div
            v-if="isSearchOpen"
            id="subheader-search-panel"
            class="search-panel"
          >
            <div class="search-input-row">
              <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="11" cy="11" r="8"></circle>
                <path d="m21 21-4.35-4.35"></path>
              </svg>
              <input
                ref="searchInput"
                v-model="searchTerm"
                type="search"
                placeholder="Rechercher article ou vidéo..."
                class="search-input"
                @keydown.esc="closeSearch"
              />
              <button class="clear-btn" v-if="searchTerm" @click="clearSearch" aria-label="Effacer la recherche">✕</button>
            </div>
            <div class="search-results">
              <div v-if="loading" class="search-info">Chargement...</div>
              <div v-else-if="searchTerm.trim().length < 2" class="search-info">Saisissez au moins 2 lettres</div>
              <div v-else-if="results.length === 0" class="search-info">Aucun résultat</div>
              <ul v-else class="results-list">
                <li v-for="(item, index) in results" :key="index" class="result-item">
                  <a :href="item.link" target="_blank" rel="noopener" class="result-link">
                    <span class="result-type">{{ item.type === 'video' ? '▶ Vidéo' : '📄 Article' }}</span>
                    <span class="result-title">{{ item.title }}</span>
                    <span class="result-meta" v-if="item.type === 'video'">{{ (item as any)['channel'] || 'Chaîne inconnue' }}</span>
                    <span class="result-meta" v-else>{{ (item as any)['source'] || 'Source inconnue' }}</span>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <NuxtLink to="/liked" class="icon-btn heart-btn" title="Articles likés">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
          </svg>
        </NuxtLink>
        <button 
          class="icon-btn theme-btn" 
          :title="isDark ? 'Mode clair' : 'Mode sombre'"
          @click="toggleTheme"
          :aria-pressed="isDark"
        >
          <!-- Sun icon (show when in dark mode) -->
          <svg v-if="isDark" class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="5"></circle>
            <line x1="12" y1="1" x2="12" y2="3"></line>
            <line x1="12" y1="21" x2="12" y2="23"></line>
            <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
            <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
            <line x1="1" y1="12" x2="3" y2="12"></line>
            <line x1="21" y1="12" x2="23" y2="12"></line>
            <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
            <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
          </svg>
          <!-- Moon icon (show when in light mode) -->
          <svg v-else class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { nextTick, onBeforeUnmount, ref, computed } from 'vue';
import { useArticles } from '~/composables/useArticles';
import { useVideos } from '~/composables/useVideos';
import { useTheme } from '~/composables/useTheme';

const { isDark, toggleTheme } = useTheme();

const isSearchOpen = ref(false);
const searchTerm = ref('');
const searchInput = ref<HTMLInputElement | null>(null);
const searchWrapper = ref<HTMLElement | null>(null);

// Load articles
const { all: articles, loading: loadingArticles, load: loadArticles } = useArticles({
  hours: 0,
  apiBase: 'http://127.0.0.1:5000',
});

// Load videos
const { videos, loading: loadingVideos, fetchVideos } = useVideos();

const loading = computed(() => loadingArticles.value || loadingVideos.value);

const results = computed(() => {
  const term = searchTerm.value.trim().toLowerCase();
  if (term.length < 2) return [];

  // Search in articles
  const articleResults = articles.value
    .filter(a =>
      a.title.toLowerCase().includes(term) ||
      (a.summary ?? '').toLowerCase().includes(term) ||
      (a.source ?? '').toLowerCase().includes(term)
    )
    .slice(0, 4)
    .map(a => ({ ...a, type: 'article' as const }));

  // Search in videos
  const videoResults = videos.value
    .filter(v =>
      v.title.toLowerCase().includes(term) ||
      (v.summary ?? '').toLowerCase().includes(term) ||
      (v.channel ?? '').toLowerCase().includes(term)
    )
    .slice(0, 4)
    .map(v => ({ ...v, type: 'video' as const }));

  return [...articleResults, ...videoResults] as Array<any>;
});

function toggleSearch() {
  isSearchOpen.value = !isSearchOpen.value;
  if (isSearchOpen.value) {
    nextTick(() => searchInput.value?.focus());
    if (articles.value.length === 0) void loadArticles();
    if (videos.value.length === 0) void fetchVideos({ hours: 0, limit: 1000 });
  } else {
    clearSearch();
  }
}

function clearSearch() {
  searchTerm.value = '';
}

function closeSearch() {
  isSearchOpen.value = false;
  clearSearch();
}

function handleOutside(event: MouseEvent) {
  if (!isSearchOpen.value) return;
  const target = event.target as Node | null;
  if (target && searchWrapper.value && !searchWrapper.value.contains(target)) {
    closeSearch();
  }
}

if (typeof window !== 'undefined') {
  window.addEventListener('click', handleOutside, { capture: true });
}

onBeforeUnmount(() => {
  if (typeof window !== 'undefined') {
    window.removeEventListener('click', handleOutside, { capture: true });
  }
});
</script>

<style scoped>
.sub-header {
  background: linear-gradient(90deg, #2f0538 0%, #3a0f4f 100%);
  color: #f0f0f3;
  border-bottom: 1px solid rgba(123, 92, 224, 0.25);
  padding: 0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 calc(2vw);
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 56px;
}

.nav {
  display: flex;
  gap: 0;
  align-items: center;
  padding: 0;
  flex: 1;
  height: 100%;
}

.nav-link {
  color: #e8e4f0;
  text-decoration: none;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.3px;
  position: relative;
  transition: all 0.22s ease;
  padding: 0 16px;
  display: flex;
  align-items: center;
  gap: 6px;
  height: 100%;
  border-right: 1px solid rgba(123, 92, 224, 0.15);
}

.nav-link:last-of-type {
  border-right: none;
}

.nav-link:hover {
  color: #c5b3ff;
  background: rgba(123, 92, 224, 0.08);
}

.nav-link:hover::after {
  width: calc(100% - 32px);
}

.nav-link.is-active {
  color: #c5b3ff;
}

.nav-link.is-active::after {
  width: calc(100% - 32px);
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 16px;
  right: 16px;
  width: 0;
  height: 3px;
  background: linear-gradient(90deg, #7b5ce0, #c5b3ff);
  transition: width 0.22s ease;
  margin: 0 auto;
}

.live-badge {
  font-size: 12px;
  color: #ff6b6b;
  animation: pulse-red 1.4s ease-in-out infinite;
  margin-right: 6px;
}

@keyframes pulse-red {
  0%, 100% {
    opacity: 1;
    transform: scale(1);
  }
  50% {
    opacity: 0.35;
    transform: scale(0.9);
  }
}

.nav-right {
  display: flex;
  gap: 8px;
  align-items: center;
  margin-left: auto;
  padding-left: 16px;
  height: 100%;
}

.icon-btn {
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  transition: all 0.22s ease;
  color: #e8e4f0;
}

.icon-btn:hover {
  background: rgba(123, 92, 224, 0.15);
  color: #c5b3ff;
  transform: translateY(-2px);
}

.icon-btn:active {
  transform: translateY(0);
  background: rgba(123, 92, 224, 0.25);
}

.icon {
  width: 20px;
  height: 20px;
  stroke: currentColor;
}

.search-container {
  position: relative;
  display: flex;
  align-items: center;
}

.search-panel {
  position: absolute;
  top: calc(100% + 10px);
  right: 0;
  width: min(420px, 90vw);
  background: #241431;
  border: 1px solid rgba(197, 179, 255, 0.2);
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
  padding: 12px;
  z-index: 10;
}

.search-input-row {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 10px;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(197, 179, 255, 0.18);
}

.search-input {
  flex: 1;
  background: transparent;
  border: none;
  color: #f0f0f3;
  font-size: 14px;
  outline: none;
}

.search-input::placeholder {
  color: #999;
}

.clear-btn {
  background: none;
  border: none;
  color: #c5b3ff;
  cursor: pointer;
  font-size: 14px;
  padding: 4px;
}

.search-results {
  margin-top: 10px;
  max-height: 340px;
  overflow-y: auto;
}

.search-info {
  color: #c5b3ff;
  font-size: 13px;
  padding: 6px 2px;
}

.results-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.result-item {
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(197, 179, 255, 0.12);
  border-radius: 10px;
  padding: 10px 12px;
  transition: border-color 0.18s ease, transform 0.18s ease;
}

.result-item:hover {
  border-color: rgba(197, 179, 255, 0.4);
  transform: translateY(-1px);
}

.result-link {
  color: #f0f0f3;
  text-decoration: none;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.result-type {
  font-size: 11px;
  color: #7b5ce0;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-weight: 600;
}

.result-title {
  font-size: 14px;
  font-weight: 600;
}

.result-meta {
  font-size: 12px;
  color: #b3a6d9;
}

.heart-btn {
  color: #ff9fb3;
}

@media (max-width: 1024px) {
  .nav-link {
    font-size: 12px;
    padding: 0 12px;
  }
  
  .nav-divider {
    display: none;
  }

  .icon {
    width: 18px;
    height: 18px;
  }
}

@media (max-width: 768px) {
  .nav-link {
    font-size: 11px;
    padding: 0 8px;
    border-right: none;
  }

  .nav-divider {
    display: none;
  }

  .nav-right {
    gap: 6px;
    padding-left: 8px;
  }

  .icon-btn {
    padding: 6px;
  }

  .icon {
    width: 18px;
    height: 18px;
  }
}

@media (max-width: 480px) {
  .container {
    padding: 0 calc(1vw);
  }

  .nav-link {
    font-size: 10px;
    padding: 0 6px;
  }

  .nav-link::after {
    display: none;
  }

  .icon-btn {
    padding: 4px;
  }

  .icon {
    width: 16px;
    height: 16px;
  }
}
</style>
