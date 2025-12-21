<template>
  <div class="explorer-page">
    <!-- Sidebar filters -->
    <aside class="sidebar">
      <div class="sidebar-header">
        <h3>Filtres</h3>
        <button v-if="hasActiveFilters" @click="resetFilters" class="reset-btn" title="Réinitialiser">
          ✕
        </button>
      </div>

      <!-- Media type filter -->
      <div class="filter-group">
        <h4 class="filter-title">Type de média</h4>
        <div class="filter-options">
          <label class="checkbox-label">
            <input
              v-model="filters.types"
              type="checkbox"
              value="articles"
              @change="applyFilters"
            />
            <span class="checkbox-text">Articles</span>
            <span class="count">({{ articleCount }})</span>
          </label>
          <label class="checkbox-label">
            <input
              v-model="filters.types"
              type="checkbox"
              value="videos"
              @change="applyFilters"
            />
            <span class="checkbox-text">Vidéos</span>
            <span class="count">({{ videoCount }})</span>
          </label>
        </div>
      </div>

      <!-- Sorting -->
      <div class="filter-group">
        <h4 class="filter-title">Trier par</h4>
        <select v-model="sortBy" @change="applyFilters" class="sort-select">
          <option value="date-desc">Plus récent</option>
          <option value="date-asc">Plus ancien</option>
          <option value="title-asc">Titre (A-Z)</option>
          <option value="title-desc">Titre (Z-A)</option>
        </select>
      </div>

      <!-- Items per page -->
      <div class="filter-group">
        <h4 class="filter-title">Par page</h4>
        <select v-model.number="itemsPerPage" @change="applyFilters" class="sort-select">
          <option :value="12">12 items</option>
          <option :value="24">24 items</option>
          <option :value="48">48 items</option>
        </select>
      </div>
    </aside>

    <!-- Main content -->
    <main class="explorer-content">
      <!-- Search bar -->
      <div class="search-section">
        <div class="search-wrapper">
          <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <circle cx="11" cy="11" r="8"></circle>
            <path d="m21 21-4.35-4.35"></path>
          </svg>
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Rechercher dans tous les médias..."
            class="search-input"
            @keyup.enter="applyFilters"
          />
          <button v-if="searchQuery" @click="clearSearch" class="clear-btn">✕</button>
        </div>
      </div>

      <!-- Results info -->
      <div class="results-info">
        <p v-if="filteredItems.length > 0">
          <strong>{{ filteredItems.length }}</strong> résultats
          <span v-if="searchQuery"> pour "{{ searchQuery }}"</span>
        </p>
        <p v-else>Aucun résultat trouvé</p>
      </div>

      <!-- Loading state -->
      <div v-if="isLoading" class="loading-state">
        <div class="spinner"></div>
        <p>Chargement des médias...</p>
      </div>

      <!-- Error state -->
      <div v-else-if="error" class="error-state">
        <p>⚠️ {{ error }}</p>
        <button @click="loadData" class="retry-btn">Réessayer</button>
      </div>

      <!-- Empty state -->
      <div v-else-if="filteredItems.length === 0" class="empty-state">
        <p>Aucun média ne correspond à vos critères</p>
        <button v-if="hasActiveFilters" @click="resetFilters" class="retry-btn">
          Réinitialiser les filtres
        </button>
      </div>

      <!-- Grid of items -->
      <template v-else>
        <div class="items-grid">
          <article v-for="item in paginatedItems" :key="item.link" class="item-card">
            <div class="item-header">
              <span v-if="item.type === 'article'" class="media-badge article-badge">Article</span>
              <span v-else class="media-badge video-badge">Vidéo</span>
              <button class="like-btn" @click="toggleLike(item.link)">
                <svg :class="{ liked: isSavedItem(item.link) }" viewBox="0 0 24 24" fill="currentColor" stroke="none">
                  <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
                </svg>
              </button>
            </div>
            <div class="item-content">
              <h3 class="item-title">{{ item.title }}</h3>
              <p v-if="item.summary" class="item-summary">{{ truncateSummary(item.summary) }}</p>
              <div class="item-meta">
                <span v-if="item.source" class="meta-item source">{{ item.source }}</span>
                <span class="meta-item date">{{ formatDate(item.date) }}</span>
              </div>
            </div>
            <a :href="item.link" target="_blank" class="item-link">
              Lire la suite →
            </a>
          </article>
        </div>

        <!-- Pagination -->
        <div class="pagination">
          <button
            :disabled="currentPage === 1"
            @click="prevPage"
            class="pagination-btn"
          >
            ← Précédent
          </button>

          <div class="pagination-info">
            Page <strong>{{ currentPage }}</strong> sur <strong>{{ totalPages }}</strong>
          </div>

          <button
            :disabled="currentPage === totalPages"
            @click="nextPage"
            class="pagination-btn"
          >
            Suivant →
          </button>
        </div>
      </template>
    </main>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import { useArticles } from '@/composables/useArticles';
import { useVideos } from '@/composables/useVideos';
import { useSavedMedia } from '@/composables/useSavedMedia';

// Data fetching
const { all: articles, loading: articlesLoading, error: articlesError, load: loadArticles } = useArticles({
  apiBase: 'http://127.0.0.1:5000',
  query: '',
  hours: 0,
  meta: 1,
});

const { all: videos, loading: videosLoading, error: videosError, load: loadVideos } = useVideos({
  apiBase: 'http://127.0.0.1:5000',
  query: '',
  meta: 1,
});

const { isSaved, toggleSave: saveMedia } = useSavedMedia();

// UI State
const searchQuery = ref('');
const sortBy = ref('date-desc');
const itemsPerPage = ref(24);
const currentPage = ref(1);

const filters = ref({
  types: ['articles', 'videos'],
});

// Combined data
const allItems = computed(() => {
  const combined: any[] = [];
  
  // Add articles
  if (filters.value.types.includes('articles')) {
    combined.push(...articles.value.map(a => ({
      type: 'article',
      title: a.title,
      summary: a.summary,
      source: a.source,
      date: a.date,
      link: a.link,
    })));
  }

  // Add videos
  if (filters.value.types.includes('videos')) {
    combined.push(...videos.value.map(v => ({
      type: 'video',
      title: v.title,
      summary: v.description,
      source: v.channel,
      date: v.date,
      link: v.link,
    })));
  }

  return combined;
});

// Filtering and sorting
const filteredItems = computed(() => {
  let result = [...allItems.value];

  // Search filter
  if (searchQuery.value.trim()) {
    const q = searchQuery.value.trim().toLowerCase();
    result = result.filter(item =>
      item.title.toLowerCase().includes(q) ||
      (item.summary ?? '').toLowerCase().includes(q) ||
      (item.source ?? '').toLowerCase().includes(q)
    );
  }

  // Sort
  const sorted = [...result];
  switch (sortBy.value) {
    case 'date-asc':
      sorted.sort((a, b) => new Date(a.date).getTime() - new Date(b.date).getTime());
      break;
    case 'title-asc':
      sorted.sort((a, b) => a.title.localeCompare(b.title));
      break;
    case 'title-desc':
      sorted.sort((a, b) => b.title.localeCompare(a.title));
      break;
    case 'date-desc':
    default:
      sorted.sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
  }

  return sorted;
});

// Pagination
const totalPages = computed(() => Math.ceil(filteredItems.value.length / itemsPerPage.value));

const paginatedItems = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value;
  const end = start + itemsPerPage.value;
  return filteredItems.value.slice(start, end);
});

// Counts
const articleCount = computed(() => articles.value.length);
const videoCount = computed(() => videos.value.length);

// Loading/Error state
const isLoading = computed(() => articlesLoading.value || videosLoading.value);
const error = computed(() => articlesError.value || videosError.value || null);

// Filter helpers
const hasActiveFilters = computed(() => 
  searchQuery.value || filters.value.types.length < 2
);

// Methods
function loadData() {
  loadArticles();
  loadVideos();
}

function applyFilters() {
  currentPage.value = 1;
}

function clearSearch() {
  searchQuery.value = '';
  applyFilters();
}

function resetFilters() {
  searchQuery.value = '';
  filters.value.types = ['articles', 'videos'];
  sortBy.value = 'date-desc';
  itemsPerPage.value = 24;
  currentPage.value = 1;
}

function nextPage() {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}

function prevPage() {
  if (currentPage.value > 1) {
    currentPage.value--;
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}

function isSavedItem(link: string): boolean {
  return isSaved(link, 'liked');
}

async function toggleLike(link: string) {
  // Find the item to get its metadata
  const item = allItems.value.find(i => i.link === link);
  if (!item) return;

  await saveMedia({
    link,
    title: item.title,
    source: item.source || '',
    media_type: item.type === 'article' ? 'article' : 'video',
    category: 'liked',
  });
}

function truncateSummary(text: string, maxLength: number = 150): string {
  if (!text) return '';
  if (text.length <= maxLength) return text;
  return text.slice(0, maxLength).trim() + '...';
}

function formatDate(dateStr: string): string {
  try {
    const date = new Date(dateStr);
    return new Intl.DateTimeFormat('fr-FR', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
    }).format(date);
  } catch {
    return dateStr;
  }
}

// Load data on mount
onMounted(() => {
  loadData();
});
</script>

<style scoped>
* {
  box-sizing: border-box;
}

.explorer-page {
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: 40px;
  max-width: 1400px;
  margin: 0 auto;
  padding: 40px;
  min-height: calc(100vh - 200px);
}

/* Sidebar */
.sidebar {
  position: sticky;
  top: 140px;
  height: fit-content;
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  padding: 20px;
}

.sidebar-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding-bottom: 12px;
  border-bottom: 2px solid #e9ecef;
}

.sidebar-header h3 {
  margin: 0;
  font-size: 16px;
  font-weight: 600;
  color: #212529;
}

.reset-btn {
  background: none;
  border: none;
  color: #6c757d;
  cursor: pointer;
  font-size: 20px;
  padding: 0;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.2s ease;
}

.reset-btn:hover {
  color: #dc3545;
}

/* Filter groups */
.filter-group {
  margin-bottom: 24px;
}

.filter-title {
  margin: 0 0 12px 0;
  font-size: 13px;
  font-weight: 600;
  color: #212529;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.filter-options {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  font-size: 13px;
  color: #495057;
  transition: color 0.2s ease;
}

.checkbox-label:hover {
  color: #212529;
}

.checkbox-label input[type="checkbox"] {
  cursor: pointer;
  width: 16px;
  height: 16px;
  accent-color: #7b5ce0;
}

.checkbox-text {
  flex: 1;
}

.count {
  color: #adb5bd;
  font-size: 12px;
  font-weight: 500;
}

.sort-select {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  font-size: 13px;
  color: #212529;
  background: white;
  cursor: pointer;
  transition: border-color 0.2s ease;
}

.sort-select:hover,
.sort-select:focus {
  border-color: #7b5ce0;
  outline: none;
}

/* Main content */
.explorer-content {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.search-section {
  display: flex;
  gap: 12px;
}

.search-wrapper {
  flex: 1;
  position: relative;
  display: flex;
  align-items: center;
}

.search-icon {
  position: absolute;
  left: 14px;
  width: 18px;
  height: 18px;
  color: #adb5bd;
  pointer-events: none;
}

.search-input {
  width: 100%;
  padding: 12px 14px 12px 44px;
  border: 1.5px solid #dee2e6;
  border-radius: 8px;
  font-size: 14px;
  color: #212529;
  background: white;
  transition: all 0.2s ease;
}

.search-input:focus {
  outline: none;
  border-color: #7b5ce0;
  box-shadow: 0 0 0 3px rgba(123, 92, 224, 0.1);
}

.search-input::placeholder {
  color: #adb5bd;
}

.clear-btn {
  position: absolute;
  right: 12px;
  background: none;
  border: none;
  color: #adb5bd;
  cursor: pointer;
  font-size: 18px;
  padding: 0;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.2s ease;
}

.clear-btn:hover {
  color: #495057;
}

/* Results info */
.results-info {
  padding: 12px 0;
  color: #6c757d;
  font-size: 13px;
  border-bottom: 1px solid #e9ecef;
}

.results-info p {
  margin: 0;
}

.results-info strong {
  color: #212529;
  font-weight: 600;
}

/* States */
.loading-state,
.error-state,
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 40px;
  text-align: center;
  color: #6c757d;
}

.loading-state {
  gap: 20px;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 3px solid #e9ecef;
  border-top-color: #7b5ce0;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error-state p,
.empty-state p {
  margin: 0 0 20px 0;
  font-size: 16px;
  color: #495057;
}

.retry-btn {
  padding: 10px 24px;
  background: #7b5ce0;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.retry-btn:hover {
  background: #6a4dc7;
  transform: translateY(-1px);
}

/* Items grid */
.items-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 24px;
  margin: 24px 0;
}

.item-card {
  display: flex;
  flex-direction: column;
  background: white;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  overflow: hidden;
  transition: all 0.2s ease;
}

.item-card:hover {
  border-color: #7b5ce0;
  box-shadow: 0 4px 12px rgba(123, 92, 224, 0.1);
}

.item-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  background: #f8f9fa;
  border-bottom: 1px solid #e9ecef;
}

.media-badge {
  font-size: 11px;
  font-weight: 600;
  padding: 4px 8px;
  border-radius: 4px;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.article-badge {
  background: #e7f5ff;
  color: #0066cc;
}

.video-badge {
  background: #fff3bf;
  color: #997404;
}

.like-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
  width: 20px;
  height: 20px;
  color: #dee2e6;
  transition: all 0.2s ease;
}

.like-btn:hover {
  color: #dc3545;
  transform: scale(1.1);
}

.like-btn svg {
  width: 100%;
  height: 100%;
}

.like-btn svg.liked {
  color: #dc3545;
}

.item-content {
  padding: 16px;
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.item-title {
  margin: 0;
  font-size: 14px;
  font-weight: 600;
  color: #212529;
  line-height: 1.4;
}

.item-summary {
  margin: 0;
  font-size: 13px;
  color: #6c757d;
  line-height: 1.5;
  flex: 1;
}

.item-meta {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  padding-top: 8px;
  border-top: 1px solid #e9ecef;
}

.meta-item {
  font-size: 12px;
  color: #adb5bd;
}

.meta-item.source {
  color: #7b5ce0;
  font-weight: 500;
}

.item-link {
  display: inline-block;
  padding: 12px 16px;
  background: #f8f9fa;
  color: #7b5ce0;
  text-decoration: none;
  font-size: 13px;
  font-weight: 500;
  border-top: 1px solid #e9ecef;
  transition: all 0.2s ease;
}

.item-link:hover {
  background: #e7f5ff;
}

/* Pagination */
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  padding: 40px 0;
  border-top: 1px solid #e9ecef;
}

.pagination-btn {
  padding: 10px 20px;
  background: white;
  border: 1.5px solid #dee2e6;
  border-radius: 6px;
  color: #212529;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.pagination-btn:hover:not(:disabled) {
  border-color: #7b5ce0;
  color: #7b5ce0;
  background: #f8f9ff;
}

.pagination-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.pagination-info {
  font-size: 13px;
  color: #6c757d;
  white-space: nowrap;
}

.pagination-info strong {
  color: #212529;
  font-weight: 600;
}

/* Responsive */
@media (max-width: 1024px) {
  .explorer-page {
    grid-template-columns: 240px 1fr;
    gap: 30px;
    padding: 30px 24px;
  }

  .sidebar {
    top: 130px;
  }

  .items-grid {
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  }
}

@media (max-width: 768px) {
  .explorer-page {
    grid-template-columns: 1fr;
    gap: 24px;
    padding: 24px 16px;
  }

  .sidebar {
    position: relative;
    top: 0;
    sticky: none;
  }

  .items-grid {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 16px;
  }

  .pagination {
    flex-wrap: wrap;
    gap: 12px;
  }
}

@media (max-width: 480px) {
  .explorer-page {
    grid-template-columns: 1fr;
    gap: 16px;
    padding: 16px 12px;
  }

  .sidebar {
    padding: 16px;
  }

  .items-grid {
    grid-template-columns: 1fr;
  }

  .pagination {
    flex-direction: column;
  }

  .pagination-btn {
    width: 100%;
  }
}
</style>
