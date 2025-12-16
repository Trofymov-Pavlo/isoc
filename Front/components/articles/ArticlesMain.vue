<template>
  <main class="articles-page">
    <PageHero
      title="Tous les Articles"
      subtitle="Consultez l'intégralité de nos articles sur le conflit Ukraine-Russie"
      badge="Archive complète"
    />

    <div class="articles-content">
      <div class="search-bar-container">
        <div class="search-wrapper">
          <input
            v-model="localQuery"
            class="search-input"
            placeholder="Rechercher un article..."
            @keyup.enter="filterArticles"
          />
          <svg v-if="!localQuery" class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <path d="m21 21-4.35-4.35"></path>
          </svg>
          <button v-else @click="localQuery = ''; filterArticles()" class="clear-btn">×</button>
        </div>
        <span class="article-count">{{ filteredArticles.length }} article(s)</span>
      </div>

      <div v-if="loading" class="loading-state">
        <p>Chargement des articles...</p>
      </div>

      <div v-else-if="error" class="error-state">
        <p>⚠️ {{ error }}</p>
        <button @click="load" class="retry-btn">Réessayer</button>
      </div>

      <div v-else-if="filteredArticles.length === 0" class="empty-state">
        <p>Aucun article trouvé</p>
        <button @click="resetSearch" class="retry-btn">Réinitialiser la recherche</button>
      </div>

      <section v-else class="articles-container">
        <FeaturedLive v-if="filteredArticles[0]" :article="filteredArticles[0]" />
        <LiveArticlesGrid v-if="filteredArticles.length > 1" :articles="filteredArticles.slice(1)" />
      </section>
    </div>
  </main>
</template>

<script setup lang="ts">
import { computed, onMounted, onUnmounted, ref } from 'vue';
import { useArticles } from '@/composables/useArticles';
import PageHero from '~/components/shared/PageHero.vue';
import FeaturedLive from '~/components/in-live/FeaturedLive.vue';
import LiveArticlesGrid from '~/components/in-live/LiveArticlesGrid.vue';

const { all, loading, error, load } = useArticles({
  apiBase: 'http://127.0.0.1:5000',
  query: '', // Pas de filtre supplémentaire, le backend filtre déjà avec keywords.py
  hours: 0, // Tous les articles, sans limite de temps
  meta: 1,
});

const localQuery = ref('');

const filteredArticles = computed(() => {
  const query = localQuery.value.trim().toLowerCase();
  if (!query) return all.value;
  return all.value.filter(a =>
    a.title.toLowerCase().includes(query) ||
    (a.summary ?? '').toLowerCase().includes(query) ||
    (a.source ?? '').toLowerCase().includes(query)
  );
});

const filterArticles = () => {
  // Reactive computed property handles filtering
};

const resetSearch = () => {
  localQuery.value = '';
};

let refreshInterval: number | null = null;

onMounted(() => {
  load();
  // Auto-refresh toutes les 5 minutes pour recharger archive.json
  refreshInterval = window.setInterval(load, 5 * 60 * 1000);
});

onUnmounted(() => {
  if (refreshInterval) clearInterval(refreshInterval);
});
</script>

<style scoped>
.articles-page {
  min-height: 100vh;
  background: #ffffff;
  padding-bottom: 60px;
}

.articles-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 calc(2vw);
}

.search-bar-container {
  padding: 32px 0 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  border-bottom: 1px solid #f0f0f0;
  margin-bottom: 32px;
}

.search-wrapper {
  position: relative;
  flex: 1;
  max-width: 400px;
}

.search-input {
  width: 100%;
  padding: 10px 38px 10px 16px;
  border-radius: 8px;
  border: 1px solid #ddd;
  background: #f8f8f8;
  color: #333;
  font-size: 14px;
  transition: all 0.2s ease;
}

.search-input::placeholder {
  color: #999;
}

.search-input:focus {
  outline: none;
  border-color: #2f0538;
  background: #fff;
  box-shadow: 0 2px 8px rgba(47, 5, 56, 0.1);
}

.search-icon {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: #999;
  pointer-events: none;
}

.clear-btn {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: #666;
  font-size: 24px;
  cursor: pointer;
  padding: 0;
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.2s ease;
}

.clear-btn:hover {
  color: #333;
}

.article-count {
  font-size: 13px;
  color: #666;
  font-weight: 500;
}

.loading-state,
.error-state,
.empty-state {
  text-align: center;
  padding: 60px 20px;
  color: #666;
}

.retry-btn {
  margin-top: 16px;
  padding: 10px 24px;
  background: #2f0538;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.2s ease;
}

.retry-btn:hover {
  background: #3a0f4f;
  transform: translateY(-2px);
}

.articles-container {
  max-width: 1200px;
  margin: 0 auto;
}

@media (max-width: 680px) {
  .search-bar-container {
    flex-direction: column;
    align-items: stretch;
  }
  
  .search-wrapper {
    max-width: 100%;
  }
  
  .article-count {
    text-align: center;
  }
}
</style>
