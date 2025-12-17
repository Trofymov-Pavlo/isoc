<template>
  <main class="articles-page">
    <PageHero
      title="Articles"
      subtitle="Tous les articles sur le conflit Ukraine-Russie"
      badge="Archive article"
    />

    <div class="articles-content">
      <div class="search-bar-container">
        <div class="search-row">
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
        </div>
        <div class="sort-section">
          <label for="sort-articles" class="sort-label">Trier par :</label>
          <select id="sort-articles" v-model="sortBy" class="sort-select">
            <option value="date-desc">Plus récent</option>
            <option value="date-asc">Plus ancien</option>
            <option value="title-asc">Titre (A-Z)</option>
            <option value="title-desc">Titre (Z-A)</option>
            <option value="source-asc">Source (A-Z)</option>
          </select>
        </div>
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

      <template v-else>
        <section class="articles-container">
          <FeaturedLive v-if="paginatedArticles[0]" :article="paginatedArticles[0]" />
          <LiveArticlesGrid v-if="paginatedArticles.length > 1" :articles="paginatedArticles.slice(1)" />
        </section>

        <Pagination
          :current-page="currentPage"
          :total-pages="totalPages"
          :items-per-page="itemsPerPage"
          :visible-pages="visiblePages"
          @update:items-per-page="setItemsPerPage"
          @next="nextPage"
          @prev="prevPage"
          @go-to="goToPage"
        />
      </template>
    </div>
  </main>
</template>

<script setup lang="ts">
import { computed, onMounted, onUnmounted, ref } from 'vue';
import { useArticles } from '@/composables/useArticles';
import { usePagination } from '@/composables/usePagination';
import { compareAlphabetic } from '@/utils/sortUtils';
import PageHero from '~/components/shared/PageHero.vue';
import FeaturedLive from '~/components/in-live/FeaturedLive.vue';
import LiveArticlesGrid from '~/components/in-live/LiveArticlesGrid.vue';
import Pagination from '~/components/shared/Pagination.vue';

const { all, loading, error, load } = useArticles({
  apiBase: 'http://127.0.0.1:5000',
  query: '', // Pas de filtre supplémentaire, le backend filtre déjà avec keywords.py
  hours: 0, // Tous les articles, sans limite de temps
  meta: 1,
});

const localQuery = ref('');
const sortBy = ref('date-desc');

const filteredArticles = computed(() => {
  const query = localQuery.value.trim().toLowerCase();
  let result = all.value;
  
  // Filter
  if (query) {
    result = result.filter(a =>
      a.title.toLowerCase().includes(query) ||
      (a.summary ?? '').toLowerCase().includes(query) ||
      (a.source ?? '').toLowerCase().includes(query)
    );
  }
  
  // Sort
  const sorted = [...result];
  switch (sortBy.value) {
    case 'date-desc':
      sorted.sort((a, b) => (b.publishedTime || 0) - (a.publishedTime || 0));
      break;
    case 'date-asc':
      sorted.sort((a, b) => (a.publishedTime || 0) - (b.publishedTime || 0));
      break;
    case 'title-asc':
      sorted.sort((a, b) => compareAlphabetic(a.title, b.title));
      break;
    case 'title-desc':
      sorted.sort((a, b) => compareAlphabetic(b.title, a.title));
      break;
    case 'source-asc':
      sorted.sort((a, b) => compareAlphabetic(a.source || '', b.source || ''));
      break;
  }
  
  return sorted;
});

const {
  currentPage,
  itemsPerPage,
  totalPages,
  paginatedItems: paginatedArticles,
  setItemsPerPage,
  nextPage,
  prevPage,
  goToPage,
  visiblePages,
} = usePagination(filteredArticles);

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
  flex-direction: column;
  align-items: center;
  gap: 16px;
  border-bottom: 1px solid #f0f0f0;
  margin-bottom: 32px;
  width: 100%;
}

.search-row {
  display: flex;
  justify-content: center;
  width: 100%;
}

.counter-section {
  display: none;
}

.sort-section {
  display: flex;
  align-items: center;
  gap: 8px;
  justify-content: center;
}

.search-wrapper {
  position: relative;
  width: 100%;
  max-width: 400px;
}

.sort-label {
  font-size: 12px;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  white-space: nowrap;
}

.sort-select {
  padding: 8px 12px;
  border: 1px solid #ddd;
  background: #f8f8f8;
  color: #666;
  border-radius: 6px;
  cursor: pointer;
  font-size: 13px;
  font-weight: 500;
  transition: all 0.2s ease;
  min-width: 140px;
}

.sort-select:hover {
  background: #fff;
  border-color: #2f0538;
}

.sort-select:focus {
  outline: none;
  border-color: #2f0538;
  background: #fff;
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
