<template>
  <section class="live-updates">
    <div class="section-container">
      <h2 class="section-title">En Direct</h2>
      <ul class="live-list">
        <li class="live-item" v-for="article in liveUpdates" :key="article.link">
          <span class="live-dot"></span>
          <div class="live-content">
            <h3 class="live-title">{{ article.title }}</h3>
            <span class="live-time">{{ getRelativeTime(article.publishedTime) }}</span>
          </div>
        </li>
      </ul>
      <a href="/inLivePage" class="view-all-link">En Direct →</a>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useArticles } from '~/composables/useArticles';

const { all, load } = useArticles({ query: 'inLive', hours: 48 });
const now = ref(Date.now());
let interval: ReturnType<typeof setInterval> | null = null;

onMounted(() => { 
  load();
  // Rafraîchir le timestamp toutes les 30 secondes
  interval = setInterval(() => {
    now.value = Date.now();
  }, 30000);
});

onUnmounted(() => {
  if (interval) clearInterval(interval);
});

function getRelativeTime(publishedTime?: number): string {
  if (!publishedTime) return 'À l\'instant';
  
  try {
    const diffMs = now.value - publishedTime;
    const diffMins = Math.floor(diffMs / 60000);
    
    if (diffMins < 1) return 'À l\'instant';
    if (diffMins < 60) return `il y a ${diffMins} min`;
    
    const diffHours = Math.floor(diffMins / 60);
    if (diffHours < 24) return `il y a ${diffHours}h`;
    
    const diffDays = Math.floor(diffHours / 24);
    return `il y a ${diffDays}j`;
  } catch {
    return 'À l\'instant';
  }
}

const liveUpdates = computed(() =>
  all.value
    .sort((a, b) => {
      const dateA = a.publishedTime || 0;
      const dateB = b.publishedTime || 0;
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
  padding: 16px 20px;
  border-radius: 8px;
  border-left: 4px solid #ff6b6b;
  display: flex;
  gap: 16px;
  align-items: flex-start;
  transition: all 0.3s ease;
}

.live-item:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transform: translateX(4px);
}

.live-dot {
  width: 10px;
  height: 10px;
  background: #ff6b6b;
  border-radius: 50%;
  flex-shrink: 0;
  margin-top: 2px;
  animation: pulse 2s infinite;
}

.live-content {
  display: flex;
  flex-direction: column;
  gap: 6px;
  flex: 1;
}

.live-title {
  margin: 0;
  font-size: 15px;
  font-weight: 600;
  color: #1a1a1a;
  line-height: 1.4;
}

.live-time {
  font-size: 12px;
  color: #999;
  font-weight: 500;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.6; }
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
