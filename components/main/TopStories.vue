<template>
  <section class="top-stories">
    <div class="section-container">
      <h2 class="section-title">À la une</h2>
      <div class="stories-grid">
        <article class="story-card" v-for="i in 2" :key="i">
          <div class="story-image"></div>
          <div class="story-content">
            <span class="story-category">Actualité</span>
            <h3 class="story-title">Titre de l'article principal</h3>
            <p class="story-excerpt">Extrait de l'article avec les points clés...</p>
            <div class="story-meta">
              <span class="story-time">Il y a 4h</span>
              <span class="story-read">5 min de lecture</span>
            </div>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
</script>

<style scoped>
.top-stories {
  padding: 0 20px 48px 20px;
  background: #ffffff;
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

.stories-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 32px;
}

.story-card {
  display: flex;
  flex-direction: column;
  gap: 16px;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.story-card:hover {
  transform: translateY(-4px);
}

.story-image {
  width: 100%;
  aspect-ratio: 16/9;
  background: linear-gradient(135deg, #f5f5f5, #e8e8e8);
  border-radius: 10px;
}

.story-content {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.story-category {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  color: #ff6b6b;
  letter-spacing: 0.5px;
}

.story-title {
  margin: 0;
  font-size: 18px;
  font-weight: 700;
  color: #1a1a1a;
  line-height: 1.4;
}

.story-excerpt {
  margin: 0;
  font-size: 14px;
  color: #555;
  line-height: 1.5;
}

.story-meta {
  display: flex;
  gap: 16px;
  font-size: 12px;
  color: #999;
}

@media (max-width: 1100px) {
  .stories-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 680px) {
  .section-title {
    font-size: 22px;
  }

  .stories-grid {
    gap: 16px;
  }
}

@media (max-width: 480px) {
  .section-title {
    font-size: 18px;
    padding-top: 24px;
  }
}
</style>
