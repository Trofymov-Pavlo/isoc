<template>
  <section class="breaking-news">
    <div class="section-container">
      <div class="breaking-item">
        <span class="breaking-badge">DIRECT</span>
        <p class="breaking-text">Actualités en temps réel</p>
          <a href="/en-direct" class="breaking-link">Voir le live →</a>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
</script>

<style scoped>
.breaking-news {
  background: linear-gradient(90deg, #fff5f5 0%, #fff 100%);
  border-bottom: 2px solid #ffe0e0;
  border-top: 2px solid #ffe0e0;
  padding: 16px 20px;
  margin-bottom: 24px;
  box-shadow: 0 2px 8px rgba(255, 107, 107, 0.08);
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
  font-weight: 700;
  white-space: nowrap;
  padding: 8px 16px;
  background: rgba(123, 92, 224, 0.1);
  border-radius: 6px;
  transition: all 0.3s ease;
}

.breaking-link:hover {
  background: rgba(123, 92, 224, 0.2);
  transform: translateX(4px);
}

@media (max-width: 680px) {
  .breaking-item {
    flex-direction: column;
    text-align: center;
  }
}
</style>
