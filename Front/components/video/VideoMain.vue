<template>
  <main class="live-feed">
    <PageHero
      title="Vidéos"
      subtitle="Suivez en temps réel les derniers développements du conflit Ukraine-Russie"
      badge="Vidéos"
      badge-icon="▶"
    />

    <div class="video-content">
      <div class="search-bar-container">
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

      <!-- Channel filter tabs -->
      <div v-if="channels.length > 0" class="channel-tabs">
        <button
          :class="['tab-btn', { active: selectedChannel === '' }]"
          @click="selectedChannel = ''"
        >
          Tous les canaux
        </button>
        <button
          v-for="channel in channels"
          :key="channel"
          :class="['tab-btn', { active: selectedChannel === channel }]"
          @click="selectedChannel = channel"
        >
          {{ channel }}
        </button>
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
      <section v-else class="articles-container">
        <FeaturedVideo v-if="filteredVideos[0]" :video="filteredVideos[0]" />
        <VideosGrid v-if="filteredVideos.length > 1" :videos="filteredVideos.slice(1)" />
      </section>
    </div>
  </main>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import PageHero from '~/components/shared/PageHero.vue';
import EmptyState from '~/components/video/EmptyState.vue';
import FeaturedVideo from '~/components/video/FeaturedVideo.vue';
import VideosGrid from '~/components/video/VideosGrid.vue';
import { useVideos } from '~/composables/useVideos';

const localQuery = ref('');
const selectedChannel = ref('');

const {
  videos,
  loading,
  error,
  fetchVideos,
  getChannels,
  filterByChannel,
  filterByQuery,
} = useVideos();

const channels = computed(() => getChannels);

const filteredVideos = computed(() => {
  let result = videos.value;

  if (selectedChannel.value) {
    result = filterByChannel(selectedChannel.value);
  }

  if (localQuery.value) {
    result = filterByQuery(localQuery.value);
  }

  return result;
});

const filterVideos = () => {
  // Reactive computed property handles filtering
};

const resetSearch = () => {
  localQuery.value = '';
  selectedChannel.value = '';
};

const loadVideos = async () => {
  await fetchVideos({ hours: 0, limit: 1000 }); // Toutes les vidéos
};

onMounted(() => {
  loadVideos();
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
  justify-content: center;
  border-bottom: 1px solid #f0f0f0;
  margin-bottom: 32px;
}

.search-wrapper {
  position: relative;
  width: 100%;
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
