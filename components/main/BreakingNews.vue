<template>
  <section class="breaking-news">
    <div class="section-container">
      <div class="breaking-item">
        <span class="breaking-badge">DIRECT</span>
        <p class="breaking-text">Actualités en temps réel</p>
        <a href="/inLivePage" class="breaking-link">Voir le live →</a>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
</script>

<style scoped>
.breaking-news {
  background: #fff5f5;
  border-bottom: 1px solid #f0f0f0;
  padding: 24px 20px;
  margin-bottom: 48px;
}

.section-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.breaking-item {
  display: flex;
  align-items: center;
  gap: 16px;
  max-width: 1200px;
  margin: 0 auto;
}

.breaking-badge {
  background: #ff6b6b;
  color: #fff;
  padding: 6px 12px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.5px;
  flex-shrink: 0;
}

.breaking-text {
  margin: 0;
  font-size: 14px;
  color: #2f0538;
  font-weight: 600;
  flex: 1;
}

.breaking-link {
  color: #7b5ce0;
  text-decoration: none;
  font-weight: 600;
  white-space: nowrap;
}

.breaking-link:hover {
  text-decoration: underline;
}

@media (max-width: 680px) {
  .breaking-item {
    flex-direction: column;
    text-align: center;
  }
}
</style>
