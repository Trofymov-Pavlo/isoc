<template>
  <section class="top-stories">
    <div class="section-container">
      <h2 class="section-title">À la une</h2>
      <div v-if="aLaUne.length" class="stories-grid">
        <article class="story-card" v-for="article in aLaUne" :key="article.link">
          <div class="story-image" v-if="article.image">
            <img :src="article.image" :alt="article.title" loading="lazy" />
          </div>
          <div class="story-content">
            <span class="story-category">Actualité</span>
            <h3 class="story-title">{{ article.title }}</h3>
            <p class="story-excerpt">{{ article.summary || 'Résumé non disponible pour le moment.' }}</p>
            <div class="story-meta">
              <span class="story-time">{{ article.published || 'Date inconnue' }}</span>
              <a :href="article.link" target="_blank" class="story-read">Lire l'article</a>
            </div>
          </div>
        </article>
      </div>
      <p v-else class="stories-empty">Aucun article disponible pour le moment.</p>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { useArticles } from '~/composables/useArticles';

const { all, load } = useArticles({ query: 'inLive', hours: 48 });
onMounted(() => { load(); });

const now = Date.now();
const deuxHeuresMs = 2 * 60 * 60 * 1000;
const aLaUne = computed(() => {
  const withSummary = all.value.filter(a => a.summary);

  // 1) Priorité : >=2h et publishedTime présent
  const aged = withSummary
    .filter(a => a.publishedTime && now - a.publishedTime > deuxHeuresMs)
    .sort((a, b) => (b.publishedTime || 0) - (a.publishedTime || 0));
  if (aged.length >= 2) return aged.slice(0, 2);

  // 2) Fallback : avec résumé, triés par publishedTime quand présent
  return withSummary
    .sort((a, b) => (b.publishedTime || 0) - (a.publishedTime || 0))
    .slice(0, 2);
});
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
  gap: 24px;
}

.story-card {
  background: #fff;
  border-radius: 10px;
  overflow: hidden;
  transition: all 0.3s ease;
  cursor: pointer;
  display: block;
}

.story-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.story-image {
  width: 100%;
  aspect-ratio: 16/9;
  background: linear-gradient(135deg, #f5f5f5, #e8e8e8);
}

.story-content {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.story-category {
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  color: #ff6b6b;
  letter-spacing: 0.5px;
}

.story-title {
  margin: 0;
  font-size: 16px;
  font-weight: 700;
  color: #1a1a1a;
  line-height: 1.4;
}

.story-excerpt {
  margin: 0;
  font-size: 13px;
  color: #555;
  line-height: 1.5;
}

.story-meta {
  display: flex;
  gap: 12px;
  font-size: 13px;
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
