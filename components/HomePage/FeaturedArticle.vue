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
  padding: 24px 20px;
  margin-bottom: 24px;
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
  transition: all 0.28s ease;
  cursor: pointer;
  background: #fff;
  padding: 32px;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.05);
}

.featured-article:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 32px rgba(47, 5, 56, 0.12);
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
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: #fff;
  background: linear-gradient(135deg, #2f0538, #4b2faa);
  text-decoration: none;
  font-weight: 700;
  width: fit-content;
  padding: 12px 24px;
  border-radius: 8px;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(47, 5, 56, 0.2);
}

.read-more:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(47, 5, 56, 0.3);
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
