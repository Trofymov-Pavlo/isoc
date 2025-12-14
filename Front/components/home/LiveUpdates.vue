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
        <a href="/en-direct" class="view-all-link">En Direct →</a>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useArticles } from '~/composables/useArticles';

const { all, load } = useArticles({ query: 'ukraine', hours: 48 });
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
  background: #ffffff;
  padding: 24px 20px;
  margin-bottom: 24px;
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
  padding-top: 24px;
}

.section-title::before {
  content: "";
  display: inline-block;
  vertical-align: middle;
  width: 6px;
  height: 28px;
  background: linear-gradient(180deg, #ff6b6b, #ff8c8c);
  margin-right: 12px;
  border-radius: 3px;
  animation: livePulse 2s ease-in-out infinite;
}

@keyframes livePulse {
  0%, 100% { opacity: 1; transform: scaleY(1); }
  50% { opacity: 0.7; transform: scaleY(0.95); }
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
  margin-top: 4px;
  box-shadow: 0 0 0 0 rgba(255, 107, 107, 0.7);
  animation: liveDotPulse 2s infinite;
}

@keyframes liveDotPulse {
  0% {
    box-shadow: 0 0 0 0 rgba(255, 107, 107, 0.7);
  }
  50% {
    box-shadow: 0 0 0 6px rgba(255, 107, 107, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(255, 107, 107, 0);
  }
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
