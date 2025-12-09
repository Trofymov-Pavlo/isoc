<template>
  <section class="featured-main">
    <div class="section-container">
      <article class="featured-article">
        <div class="featured-image">
          <!-- Featured image will go here -->
        </div>
        <div class="featured-content">
          <span class="featured-category">Gros plan</span>
          <h2 class="featured-title">Article principal en vedette</h2>
          <p class="featured-desc">Résumé de l'article principal avec contexte et analyse détaillée sur le conflit...</p>
          <div class="featured-meta">
            <span class="featured-author">Par ISOC Media</span>
            <span class="featured-date">Il y a 2h</span>
          </div>
          <a href="#" class="read-more">Lire l'article complet →</a>
        </div>
      </article>
    </div>
  </section>
</template>

<script setup lang="ts">
</script>

<style scoped>
.featured-main {
  padding: 48px 20px;
  margin-bottom: 48px;
}

.section-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.featured-article {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  align-items: center;
}

.featured-image {
  width: 100%;
  aspect-ratio: 16/9;
  background: linear-gradient(135deg, #f5f5f5, #e8e8e8);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #999;
  font-size: 14px;
}

.featured-content {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.featured-category {
  display: inline-block;
  background: #7b5ce0;
  color: #fff;
  padding: 6px 12px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  width: fit-content;
}

.featured-title {
  margin: 0;
  font-size: 36px;
  font-weight: 700;
  line-height: 1.3;
  color: #1a1a1a;
}

.featured-desc {
  margin: 0;
  font-size: 16px;
  line-height: 1.6;
  color: #555;
}

.featured-meta {
  display: flex;
  align-items: center;
  gap: 24px;
  font-size: 13px;
  color: #999;
}

.featured-author {
  font-weight: 600;
  color: #2f0538;
}

.read-more {
  color: #7b5ce0;
  text-decoration: none;
  font-weight: 600;
  width: fit-content;
}

.read-more:hover {
  text-decoration: underline;
}

@media (max-width: 1100px) {
  .featured-article {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 680px) {
  .featured-article {
    grid-template-columns: 1fr;
  }

  .featured-content {
    order: 2;
  }

  .featured-image {
    order: 1;
  }

  .featured-title {
    font-size: 24px;
  }
}

@media (max-width: 480px) {
  .featured-title {
    font-size: 20px;
  }
}
</style>
