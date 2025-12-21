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

      <!-- Date range filter -->
      <div class="filter-group">
        <h4 class="filter-title">Période</h4>
        <select v-model="filters.dateRange" @change="applyFilters" class="sort-select">
          <option value="all">Toutes les dates</option>
          <option value="today">Aujourd'hui</option>
          <option value="week">Cette semaine</option>
          <option value="month">Ce mois-ci</option>
          <option value="3months">3 derniers mois</option>
          <option value="6months">6 derniers mois</option>
          <option value="year">Cette année</option>
        </select>
      </div>

      <!-- Sources filter (Articles) -->
      <div v-if="filters.types.includes('articles') && availableSources.length > 0" class="filter-group">
        <button class="filter-title expandable" @click="showSourcesFilter = !showSourcesFilter">
          <span>Sources ({{ filters.sources.length }})</span>
          <span class="expand-icon">{{ showSourcesFilter ? '▼' : '▶' }}</span>
        </button>
        <div v-show="showSourcesFilter" class="filter-options scrollable">
          <label v-for="source in availableSources" :key="source" class="checkbox-label">
            <input
              v-model="filters.sources"
              type="checkbox"
              :value="source"
              @change="applyFilters"
            />
            <span class="checkbox-text">{{ source }}</span>
          </label>
        </div>
      </div>

      <!-- Channels filter (Videos) -->
      <div v-if="filters.types.includes('videos') && availableChannels.length > 0" class="filter-group">
        <button class="filter-title expandable" @click="showChannelsFilter = !showChannelsFilter">
          <span>Chaînes ({{ filters.channels.length }})</span>
          <span class="expand-icon">{{ showChannelsFilter ? '▼' : '▶' }}</span>
        </button>
        <div v-show="showChannelsFilter" class="filter-options scrollable">
          <label v-for="channel in availableChannels" :key="channel" class="checkbox-label">
            <input
              v-model="filters.channels"
              type="checkbox"
              :value="channel"
              @change="applyFilters"
            />
            <span class="checkbox-text">{{ channel }}</span>
          </label>
        </div>
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
          <a 
            v-for="item in paginatedItems" 
            :key="item.link" 
            :href="item.link" 
            target="_blank" 
            class="item-card"
          >
            <div class="item-image-container">
              <img 
                v-if="item.image" 
                :src="item.image" 
                :alt="item.title"
                class="item-image"
                loading="lazy"
                @error="handleImageError"
              />
              <div v-else class="item-image-placeholder">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                  <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                  <circle cx="8.5" cy="8.5" r="1.5"></circle>
                  <polyline points="21 15 16 10 5 21"></polyline>
                </svg>
              </div>
              <span v-if="item.type === 'article'" class="media-badge article-badge">Article</span>
              <span v-else class="media-badge video-badge">Vidéo</span>
              <button 
                class="like-btn" 
                @click.prevent.stop="toggleLike(item.link)"
                :title="isSavedItem(item.link) ? 'Retirer des favoris' : 'Ajouter aux favoris'"
              >
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
                <span class="meta-item date">{{ formatDate(item.published) }}</span>
              </div>
            </div>
          </a>
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
  dateRange: 'all',
  sources: [] as string[],
  channels: [] as string[],
});

const showSourcesFilter = ref(false);
const showChannelsFilter = ref(false);

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
      published: a.published,
      publishedTime: a.publishedTime,
      link: a.link,
      image: a.image,
    })));
  }

  // Add videos
  if (filters.value.types.includes('videos')) {
    combined.push(...videos.value.map(v => ({
      type: 'video',
      title: v.title,
      summary: v.summary,
      source: v.channel,
      published: v.published,
      publishedTime: v.publishedTime,
      link: v.link,
      image: v.thumbnail,
    })));
  }

  return combined;
});

// Filtering and sorting
const filteredItems = computed(() => {
  let result = [...allItems.value];

  // Date range filter
  if (filters.value.dateRange !== 'all') {
    const now = Date.now();
    const ranges: Record<string, number> = {
      today: 24 * 60 * 60 * 1000,
      week: 7 * 24 * 60 * 60 * 1000,
      month: 30 * 24 * 60 * 60 * 1000,
      '3months': 90 * 24 * 60 * 60 * 1000,
      '6months': 180 * 24 * 60 * 60 * 1000,
      year: 365 * 24 * 60 * 60 * 1000,
    };
    const cutoff = now - (ranges[filters.value.dateRange] || 0);
    result = result.filter(item => (item.publishedTime || 0) >= cutoff);
  }

  // Sources filter (Articles)
  if (filters.value.sources.length > 0) {
    result = result.filter(item => 
      item.type === 'video' || filters.value.sources.includes(item.source)
    );
  }

  // Channels filter (Videos)
  if (filters.value.channels.length > 0) {
    result = result.filter(item => 
      item.type === 'article' || filters.value.channels.includes(item.source)
    );
  }

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
      sorted.sort((a, b) => (a.publishedTime || 0) - (b.publishedTime || 0));
      break;
    case 'title-asc':
      sorted.sort((a, b) => a.title.localeCompare(b.title));
      break;
    case 'title-desc':
      sorted.sort((a, b) => b.title.localeCompare(a.title));
      break;
    case 'date-desc':
    default:
      sorted.sort((a, b) => (b.publishedTime || 0) - (a.publishedTime || 0));
  }

  return sorted;
});

// Available sources and channels
const availableSources = computed(() => {
  const sources = new Set<string>();
  articles.value.forEach(a => {
    if (a.source) sources.add(a.source);
  });
  return Array.from(sources).sort();
});

const availableChannels = computed(() => {
  const channels = new Set<string>();
  videos.value.forEach(v => {
    if (v.channel) channels.add(v.channel);
  });
  return Array.from(channels).sort();
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
  searchQuery.value || 
  filters.value.types.length < 2 || 
  filters.value.dateRange !== 'all' ||
  filters.value.sources.length > 0 ||
  filters.value.channels.length > 0
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
  filters.value.dateRange = 'all';
  filters.value.sources = [];
  filters.value.channels = [];
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

function handleImageError(event: Event) {
  const img = event.target as HTMLImageElement;
  img.style.display = 'none';
}

function formatDate(dateStr: string | undefined): string {
  if (!dateStr) return '';
  try {
    const date = new Date(dateStr);
    if (isNaN(date.getTime())) return '';
    return new Intl.DateTimeFormat('fr-FR', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
    }).format(date);
  } catch {
    return '';
  }
}

// Load data on mount
onMounted(() => {
  loadData();
  
  // Check for URL query parameter
  const urlParams = new URLSearchParams(window.location.search);
  const qParam = urlParams.get('q');
  if (qParam) {
    searchQuery.value = qParam;
  }
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
  width: 100%;
  background: none;
  border: none;
  text-align: left;
  cursor: default;
  padding: 0;
}

.filter-title.expandable {
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 0;
  transition: color 0.2s ease;
}

.filter-title.expandable:hover {
  color: #7b5ce0;
}

.expand-icon {
  font-size: 10px;
  color: #6c757d;
}

.filter-options {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.filter-options.scrollable {
  max-height: 200px;
  overflow-y: auto;
  padding-right: 4px;
}

.filter-options.scrollable::-webkit-scrollbar {
  width: 6px;
}

.filter-options.scrollable::-webkit-scrollbar-track {
  background: #f1f3f5;
  border-radius: 3px;
}

.filter-options.scrollable::-webkit-scrollbar-thumb {
  background: #ced4da;
  border-radius: 3px;
}

.filter-options.scrollable::-webkit-scrollbar-thumb:hover {
  background: #adb5bd;
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
  text-decoration: none;
  color: inherit;
  cursor: pointer;
}

.item-card:hover {
  border-color: #7b5ce0;
  box-shadow: 0 8px 24px rgba(123, 92, 224, 0.15);
  transform: translateY(-2px);
}

/* Image container */
.item-image-container {
  position: relative;
  width: 100%;
  height: 200px;
  background: #f8f9fa;
  overflow: hidden;
}

.item-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.item-card:hover .item-image {
  transform: scale(1.05);
}

.item-image-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #ced4da;
}

.item-image-placeholder svg {
  width: 60px;
  height: 60px;
}

.media-badge {
  position: absolute;
  top: 12px;
  left: 12px;
  font-size: 11px;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 6px;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  backdrop-filter: blur(8px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.article-badge {
  background: rgba(231, 245, 255, 0.95);
  color: #0066cc;
}

.video-badge {
  background: rgba(255, 243, 191, 0.95);
  color: #997404;
}

.like-btn {
  position: absolute;
  top: 12px;
  right: 12px;
  background: rgba(255, 255, 255, 0.95);
  border: none;
  cursor: pointer;
  padding: 8px;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  color: #dee2e6;
  transition: all 0.2s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(8px);
}

.like-btn:hover {
  background: white;
  color: #dc3545;
  transform: scale(1.1);
}

.like-btn svg {
  width: 20px;
  height: 20px;
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
  font-size: 15px;
  font-weight: 600;
  color: #212529;
  line-height: 1.4;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.item-summary {
  margin: 0;
  font-size: 13px;
  color: #6c757d;
  line-height: 1.5;
  flex: 1;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
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
