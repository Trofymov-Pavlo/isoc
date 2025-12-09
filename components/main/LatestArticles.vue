<template>
  <section class="latest-articles">
    <div class="section-container">
      <h2 class="section-title">Dernières actualités</h2>
      <div class="articles-grid">
        <article class="article-card" v-for="i in 6" :key="i">
          <div class="article-image"></div>
          <div class="article-content">
            <span class="article-category">Reportage</span>
            <h3 class="article-title">Titre de l'article</h3>
            <p class="article-excerpt">Extrait de l'article...</p>
            <div class="article-footer">
              <span class="article-date">Il y a 6h</span>
              <span class="read-time">3 min</span>
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
.latest-articles {
  padding: 48px 20px;
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

.articles-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.article-card {
  background: #ffffff;
  border: 1px solid #e5e5e5;
  border-radius: 10px;
  overflow: hidden;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
}

.article-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
  border-color: #d0d0d0;
}

.article-image {
  width: 100%;
  aspect-ratio: 16/9;
  background: linear-gradient(135deg, #f5f5f5, #e8e8e8);
}

.article-content {
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  flex: 1;
}

.article-category {
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  color: #7b5ce0;
  letter-spacing: 0.5px;
}

.article-title {
  margin: 0;
  font-size: 16px;
  font-weight: 700;
  color: #1a1a1a;
  line-height: 1.4;
}

.article-excerpt {
  margin: 0;
  font-size: 13px;
  color: #666;
  line-height: 1.5;
  flex: 1;
}

.article-footer {
  display: flex;
  justify-content: space-between;
  font-size: 11px;
  color: #999;
  margin-top: auto;
  padding-top: 12px;
  border-top: 1px solid #f0f0f0;
}

@media (max-width: 1100px) {
  .articles-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 680px) {
  .section-title {
    font-size: 22px;
  }

  .articles-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .section-title {
    font-size: 18px;
    padding-top: 24px;
  }
}
</style>
