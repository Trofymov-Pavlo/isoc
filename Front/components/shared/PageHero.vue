<template>
  <section class="page-hero">
    <div class="hero-container">
      <div class="hero-content">
        <div v-if="badge" class="hero-badge">
          <span v-if="badgeIcon" class="badge-icon">{{ badgeIcon }}</span>
          <span v-else-if="showLiveDot" class="badge-dot"></span>
          {{ badge }}
        </div>
        <h1 class="hero-title">{{ title }}</h1>
        <p v-if="subtitle" class="hero-subtitle">{{ subtitle }}</p>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
defineProps<{
  title: string;
  subtitle?: string;
  badge?: string;
  badgeIcon?: string;
  showLiveDot?: boolean;
}>();
</script>

<style scoped>
.page-hero {
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  padding: 40px 0;
  color: #fff;
  margin-bottom: 0;
}

.hero-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 calc(2vw);
}

.hero-content {
  max-width: 900px;
  margin: 0 auto;
  text-align: center;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 107, 107, 0.2);
  border: 1px solid rgba(255, 107, 107, 0.5);
  color: #ff9999;
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 11px;
  font-weight: 600;
  margin-bottom: 16px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.badge-dot {
  width: 6px;
  height: 6px;
  background: #ff6b6b;
  border-radius: 50%;
  animation: pulse 2s infinite;
}

.badge-icon {
  font-size: 14px;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.3; }
}

.hero-title {
  font-size: 36px;
  font-weight: 700;
  line-height: 1.2;
  margin: 0 0 12px 0;
  color: #fff;
}

.hero-subtitle {
  font-size: 16px;
  color: rgba(255, 255, 255, 0.85);
  margin: 0;
  font-weight: 400;
  line-height: 1.5;
}

@media (max-width: 1100px) {
  .hero-title {
    font-size: 30px;
  }
}

@media (max-width: 680px) {
  .page-hero {
    padding: 32px 0;
  }

  .hero-title {
    font-size: 24px;
  }

  .hero-subtitle {
    font-size: 14px;
  }
}

@media (max-width: 480px) {
  .hero-title {
    font-size: 20px;
  }
}
</style>
