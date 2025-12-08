<template>
  <section class="live-updates">
    <div class="section-container">
      <h2 class="section-title">Mises à jour en direct</h2>
      <div class="live-ticker">
        <div class="ticker-item" v-for="i in 3" :key="i">
          <span class="ticker-time">{{ getCurrentTime }}</span>
          <p class="ticker-text">Mise à jour en direct du conflit...</p>
        </div>
      </div>
      <a href="/inLivePage" class="view-all-link">Voir tous les mises à jour →</a>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed } from 'vue';

const getCurrentTime = computed(() => {
  const now = new Date();
  return now.toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' });
});
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

.live-ticker {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-bottom: 24px;
}

.ticker-item {
  background: #fff;
  padding: 16px;
  border-radius: 8px;
  border-left: 3px solid #ff6b6b;
  display: flex;
  gap: 16px;
  align-items: flex-start;
}

.ticker-time {
  font-size: 12px;
  font-weight: 700;
  color: #ff6b6b;
  white-space: nowrap;
}

.ticker-text {
  margin: 0;
  font-size: 14px;
  color: #555;
  flex: 1;
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
