<template>
  <main class="live-feed">
    <PageHero
      title="En Direct"
      subtitle="Suivez en temps réel les derniers développements du conflit Ukraine-Russie"
      badge="Live 24/7"
      :show-live-dot="true"
    />

    <div class="live-content">
      <div class="search-bar-container">
        <div class="counter-spacer"></div>
        <div class="search-wrapper">
          <input
            v-model="localQuery"
            class="search-input"
            placeholder="Rechercher..."
            @keyup.enter="reload"
          />
          <svg v-if="!localQuery" class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <path d="m21 21-4.35-4.35"></path>
          </svg>
          <button v-else @click="localQuery = ''; reload()" class="clear-btn">×</button>
        </div>
        <div class="update-section">
          <span class="update-time">Mis à jour à {{ updateTime }}</span>
        </div>
      </div>

      <LiveAlert v-if="error" :message="error" />
      <LiveLoading v-else-if="loading" />
      <LiveEmptyState v-else-if="filtered.length === 0" @reset="resetSearch" />

      <section v-else class="articles-container">
        <FeaturedLive v-if="filtered[0]" :article="filtered[0]" />
        <LiveArticlesGrid v-if="filtered.length > 1" :articles="filtered.slice(1)" />
      </section>
    </div>
  </main>
</template>

<script setup lang="ts">
import { computed, onMounted, onUnmounted, ref } from 'vue';
import { useArchiveFeed } from '@/composables/useArchiveFeed';
import PageHero from '~/components/shared/PageHero.vue';
import FeaturedLive from '~/components/in-live/FeaturedLive.vue';
import LiveAlert from '~/components/in-live/LiveAlert.vue';
import LiveArticlesGrid from '~/components/in-live/LiveArticlesGrid.vue';
import LiveEmptyState from '~/components/in-live/LiveEmptyState.vue';
import LiveLoading from '~/components/in-live/LiveLoading.vue';

const { items, loading, error, load } = useArchiveFeed();

const localQuery = ref('');
let refreshInterval: number | null = null;

const updateTime = computed(() => {
  const now = new Date();
  return now.toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' });
});

const filtered = computed(() => {
  const now = Date.now();
  const twentyFourHoursAgo = now - (24 * 60 * 60 * 1000);
  
  console.log(`⏰ Filtre 24h: now=${now}, cutoff=${twentyFourHoursAgo}`);
  console.log(`📦 Items total avant filtre: ${items.value.length}`);
  
  // Filtrer par date (dernières 24h)
  let result = items.value.filter(item => {
    const publishedTime = item.publishedTime || 0;
    const isRecent = publishedTime >= twentyFourHoursAgo;
    if (!isRecent && item.type === 'video') {
      console.log(`⏭️ Vidéo filtrée (trop ancienne):`, item.title.substring(0, 40), publishedTime, '<', twentyFourHoursAgo);
    }
    return isRecent;
  });
  
  const articlesCount = result.filter(r => r.type === 'article').length;
  const videosCount = result.filter(r => r.type === 'video').length;
  
  console.log(`🔍 En direct: ${result.length} items <24h (${articlesCount} articles, ${videosCount} vidéos)`);
  
  // Filtrer par recherche si une query existe
  const query = localQuery.value.trim().toLowerCase();
  if (query) {
    result = result.filter(item =>
      item.title.toLowerCase().includes(query) ||
      (item.summary ?? '').toLowerCase().includes(query) ||
      (item.source ?? '').toLowerCase().includes(query)
    );
  }
  
  return result;
});

const reload = () => {
  load();
};

const resetSearch = () => {
  localQuery.value = '';
  reload();
};

onMounted(() => {
  load();
  refreshInterval = window.setInterval(load, 5 * 60 * 1000);
});

onUnmounted(() => {
  if (refreshInterval) clearInterval(refreshInterval);
});
</script>

<style scoped>
.live-feed {
  min-height: 100vh;
  background: #ffffff;
  padding-bottom: 60px;
}

.live-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 calc(2vw);
}

.search-bar-container {
  padding: 32px 0 24px;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 24px;
  border-bottom: 1px solid #f0f0f0;
  margin-bottom: 32px;
}

.counter-spacer {
  min-width: 100px;
  order: -1;
}

.search-wrapper {
  position: relative;
  width: 100%;
  max-width: 400px;
  order: 0;
}

.update-section {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  min-width: 100px;
  order: 1;
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

.update-time {
  font-size: 13px;
  color: #666;
  font-weight: 500;
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
  
  .update-time {
    text-align: center;
  }
}
</style>

