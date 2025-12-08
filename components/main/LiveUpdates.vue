<template>
  <section class="live-updates">
    <div class="section-container">
      <h2 class="section-title">Mise à jour en direct</h2>
      <ul class="live-list">
        <li class="live-item" v-for="article in liveUpdates" :key="article.link">
          <span class="live-dot"></span>
          {{ article.title }}
        </li>
      </ul>
      <a href="/inLivePage" class="view-all-link">Voir tous les mises à jour →</a>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { useArticles } from '~/composables/useArticles';

const { all, load } = useArticles({ query: 'inLive', hours: 48 });
onMounted(() => { load(); });

const liveUpdates = computed(() =>
  all.value
    .sort((a, b) => {
      const dateA = a.published ? new Date(a.published).getTime() : 0;
      const dateB = b.published ? new Date(b.published).getTime() : 0;
      return dateB - dateA;
    })
    .slice(0, 3)
);
</script>

<style scoped>
.live-updates {
  background: #f5f5f5;
  padding: 48px 20px;
  margin-bottom: 48px;
}

.section-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.section-title {
  margin: 0;
  font-size: 28px;
  font-weight: 700;
  color: #2f0538;
  margin-bottom: 32px;
  padding-top: 48px;
}

.live-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-bottom: 24px;
}

.live-item {
  background: #fff;
  padding: 16px;
  border-radius: 8px;
  border-left: 3px solid #ff6b6b;
  display: flex;
  gap: 16px;
  align-items: flex-start;
}

.live-dot {
  width: 8px;
  height: 8px;
  background: #ff6b6b;
  border-radius: 50%;
  flex-shrink: 0;
}

.view-all-link {
  color: #7b5ce0;
  text-decoration: none;
  font-weight: 600;
}

.view-all-link:hover {
  text-decoration: underline;
}

@media (max-width: 680px) {
  .section-title {
    font-size: 22px;
  }
}

@media (max-width: 480px) {
  .section-title {
    font-size: 18px;
    padding-top: 24px;
  }
}
</style>
