<template>
  <main class="live-feed">
    <LiveHeader
      v-model:query="localQuery"
      :update-time="updateTime"
      @search="reload"
    />

    <LiveAlert v-if="error" :message="error" />
    <LiveLoading v-else-if="loading" />
    <LiveEmptyState v-else-if="filtered.length === 0" @reset="resetSearch" />

    <section v-else class="articles-container">
      <FeaturedLive v-if="filtered[0]" :article="filtered[0]" />
      <LiveArticlesGrid v-if="filtered.length > 1" :articles="filtered.slice(1)" />
    </section>
  </main>
</template>

<script setup lang="ts">
import { computed, onMounted, onUnmounted, ref } from 'vue';
import { useArticles } from '@/composables/useArticles';
import FeaturedLive from '~/components/in-live/FeaturedLive.vue';
import LiveAlert from '~/components/in-live/LiveAlert.vue';
import LiveArticlesGrid from '~/components/in-live/LiveArticlesGrid.vue';
import LiveEmptyState from '~/components/in-live/LiveEmptyState.vue';
import LiveHeader from '~/components/in-live/LiveHeader.vue';
import LiveLoading from '~/components/in-live/LiveLoading.vue';

const { all, loading, error, load } = useArticles({
  apiBase: 'http://127.0.0.1:5000',
  query: 'ukraine',
  hours: 48,
  meta: 1,
});

const localQuery = ref('');
let refreshInterval: number | null = null;

const updateTime = computed(() => {
  const now = new Date();
  return now.toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' });
});

const filtered = computed(() => {
  const query = localQuery.value.trim().toLowerCase();
  if (!query) return all.value;
  return all.value.filter(a =>
    a.title.toLowerCase().includes(query) ||
    (a.summary ?? '').toLowerCase().includes(query) ||
    (a.source ?? '').toLowerCase().includes(query)
  );
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

.articles-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}
@media (max-width: 680px) {
  .articles-container {
    padding: 0 16px;
  }
}
</style>

