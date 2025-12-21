<template>
  <main class="live-feed">
    <div class="video-content">
      <div class="search-bar-container">
        <div class="search-row">
          <div class="search-wrapper">
            <input
              v-model="localQuery"
              class="search-input"
              placeholder="Rechercher une vidéo..."
              @keyup.enter="filterVideos"
            />
            <svg v-if="!localQuery" class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="8"></circle>
              <path d="m21 21-4.35-4.35"></path>
            </svg>
            <button v-else @click="localQuery = ''; filterVideos()" class="clear-btn">×</button>
          </div>
        </div>
        <div class="sort-section">
          <label for="sort-videos" class="sort-label">Trier par :</label>
          <select id="sort-videos" v-model="sortBy" class="sort-select">
            <option value="date-desc">Plus récent</option>
            <option value="date-asc">Plus ancien</option>
            <option value="title-asc">Titre (A-Z)</option>
            <option value="title-desc">Titre (Z-A)</option>
            <option value="channel-asc">Chaîne (A-Z)</option>
          </select>
        </div>
      </div>

      

      <!-- Loading state -->
      <div v-if="loading" class="loading-state">
        <p>Chargement des vidéos...</p>
      </div>

      <!-- Error state -->
      <div v-else-if="error" class="error-state">
        <p>⚠️ Erreur lors du chargement des vidéos</p>
        <button @click="loadVideos" class="retry-btn">Réessayer</button>
      </div>

      <!-- Empty state -->
      <EmptyState v-else-if="filteredVideos.length === 0" @reset="resetSearch" />

      <!-- Videos content -->
      <template v-else>
        <section class="articles-container">
          <FeaturedVideo v-if="paginatedVideos[0]" :video="paginatedVideos[0]" />
          <VideosGrid v-if="paginatedVideos.length > 1" :videos="paginatedVideos.slice(1)" />
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
import { ref, computed, onMounted, onUnmounted } from 'vue';
import EmptyState from '~/components/video/EmptyState.vue';
import FeaturedVideo from '~/components/video/FeaturedVideo.vue';
import VideosGrid from '~/components/video/VideosGrid.vue';
import Pagination from '~/components/shared/Pagination.vue';
import { useVideos } from '~/composables/useVideos';
import { usePagination } from '~/composables/usePagination';
import { compareAlphabetic } from '~/utils/sortUtils';

const localQuery = ref('');
const selectedChannel = ref('');
const sortBy = ref('date-desc');

const {
  videos,
  loading,
  error,
  fetchVideos,
  getChannels,
  filterByChannel,
  filterByQuery,
} = useVideos();

// Channel tabs removed per request

const filteredVideos = computed(() => {
  let result = videos.value;

  // Channel filter disabled

  if (localQuery.value) {
    result = filterByQuery(localQuery.value);
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
    case 'channel-asc':
      sorted.sort((a, b) => compareAlphabetic(a.channel || '', b.channel || ''));
      break;
  }

  return sorted;
});

const {
  currentPage,
  itemsPerPage,
  totalPages,
  paginatedItems: paginatedVideos,
  setItemsPerPage,
  nextPage,
  prevPage,
  goToPage,
  visiblePages,
} = usePagination(filteredVideos);

const loadVideos = () => {
  fetchVideos();
};

const filterVideos = () => {
  // Reactive computed property handles filtering
};

const resetSearch = () => {
  localQuery.value = '';
};

let refreshInterval: number | null = null;

onMounted(() => {
  loadVideos();
  // Refresh videos every 2 minutes
  refreshInterval = window.setInterval(() => {
    loadVideos();
  }, 2 * 60 * 1000);
});

onUnmounted(() => {
  if (refreshInterval) {
    clearInterval(refreshInterval);
  }
});
</script>

<style scoped>
.live-feed {
  min-height: 100vh;
  background: #ffffff;
  padding-bottom: 60px;
}

.video-content {
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

.counter-label {
  font-size: 12px;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 4px;
}

.counter-value {
  font-size: 24px;
  font-weight: 700;
  color: #2f0538;
}

.counter-spacer {
  min-width: 120px;
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

.search-wrapper {
  position: relative;
  width: 100%;
  max-width: 350px;
  order: 0;
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

.channel-tabs {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  padding: 16px 0;
  border-bottom: 1px solid #f0f0f0;
  margin-bottom: 32px;
}

.tab-btn {
  padding: 8px 16px;
  border: 1px solid #ddd;
  background: #f8f8f8;
  color: #666;
  border-radius: 6px;
  cursor: pointer;
  font-size: 13px;
  font-weight: 500;
  transition: all 0.2s ease;
}

.tab-btn:hover {
  background: #fff;
  border-color: #2f0538;
  color: #2f0538;
}

.tab-btn.active {
  background: #2f0538;
  color: white;
  border-color: #2f0538;
}

.loading-state,
.error-state {
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
  .search-wrapper {
    max-width: 100%;
  }
}
</style>
