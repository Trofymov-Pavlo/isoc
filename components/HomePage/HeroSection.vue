<template>
  <section class="hero">
    <div class="section-container">
      <div class="hero-badge">
        <span class="badge-dot"></span>
        En continu
      </div>
      <h1 class="hero-title">Média indépendant dédié au conflit Ukraine-Russie</h1>
      <p class="hero-subtitle">Suivez en direct les derniers développements, analyses et reportages</p>
    </div>
  </section>
</template>

<script setup lang="ts">
</script>

<style scoped>
.hero {
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  padding: 80px 20px;
  text-align: center;
  color: #fff;
  margin-bottom: 0;
}

.section-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 107, 107, 0.2);
  border: 1px solid rgba(255, 107, 107, 0.5);
  color: #ff9999;
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  margin-bottom: 24px;
}

.badge-dot {
  width: 8px;
  height: 8px;
  background: #ff6b6b;
  border-radius: 50%;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.3; }
}

.hero-title {
  font-size: 48px;
  font-weight: 700;
  line-height: 1.2;
  margin: 0 0 16px 0;
  color: #fff;
}

.hero-subtitle {
  font-size: 18px;
  color: rgba(255, 255, 255, 0.9);
  margin: 0;
  font-weight: 400;
}

@media (max-width: 1100px) {
  .hero-title {
    font-size: 36px;
  }
}

@media (max-width: 680px) {
  .hero {
    padding: 50px 16px;
  }

  .hero-title {
    font-size: 28px;
  }

  .hero-subtitle {
    font-size: 16px;
  }
}

@media (max-width: 480px) {
  .hero-title {
    font-size: 22px;
  }
}
</style>
