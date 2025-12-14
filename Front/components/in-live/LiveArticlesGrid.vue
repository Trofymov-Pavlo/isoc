<template>
  <div class="articles-grid" v-if="articles.length">
    <article
      v-for="(article, i) in articles"
      :key="(article.link || article.title) + (i + 1)"
      class="article-card"
    >
      <a
        v-if="article.image"
        :href="article.link"
        target="_blank"
        rel="noopener"
        class="article-image"
      >
        <img :src="article.image" :alt="article.title" loading="lazy" />
        <div class="image-overlay"></div>
      </a>
      <div v-else class="article-image placeholder">
        <span class="placeholder-icon">📰</span>
      </div>

      <div class="article-content">
        <p v-if="article.source" class="article-source">{{ article.source }}</p>
        <h2 class="article-title">
          <a :href="article.link" target="_blank" rel="noopener">{{ article.title }}</a>
        </h2>
        <p v-if="article.summary" class="article-summary">
          {{ truncate(article.summary, 120) }}
        </p>
        <div class="article-footer">
          <time v-if="article.published" class="article-time">
            {{ formatTime(article.published) }}
          </time>
          <a :href="article.link" target="_blank" rel="noopener" class="read-link">
            Lire →
          </a>
        </div>
      </div>
    </article>
  </div>
</template>

<script setup lang="ts">
interface Article {
  title: string;
  link: string;
  summary?: string;
  image?: string;
  source?: string;
  published?: string;
}

const props = defineProps<{ articles: Article[] }>();

const truncate = (text: string, max: number): string => {
  if (!text) return '';
  if (text.length <= max) return text;
  return text.substring(0, max).trim() + '...';
};

const formatTime = (dateString?: string): string => {
  if (!dateString) return '';

  try {
    if (/jan|fév|mar|avr|mai|jui|aoû|sep|oct|nov|déc/i.test(dateString)) {
      return dateString;
    }

    const date = new Date(dateString);
    if (isNaN(date.getTime())) return dateString;

    const now = new Date();
    const diffMs = now.getTime() - date.getTime();
    const diffMins = Math.floor(diffMs / 60000);
    const diffHours = Math.floor(diffMs / 3600000);
    const diffDays = Math.floor(diffMs / 86400000);

    if (diffMins < 1) return "À l'instant";
    if (diffMins < 60) return `Il y a ${diffMins}m`;
    if (diffHours < 24) return `Il y a ${diffHours}h`;
    if (diffDays < 7) return `Il y a ${diffDays}j`;

    return date.toLocaleDateString('fr-FR', { day: 'numeric', month: 'short' });
  } catch {
    return dateString;
  }
};
</script>

<style scoped>
.articles-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.article-card {
  background: #ffffff;
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid #e5e5e5;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
}

.article-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  border-color: #d0d0d0;
}

.article-image {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 9;
  overflow: hidden;
  background: #f5f5f5;
  display: block;
}

.article-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.article-card:hover .article-image img {
  transform: scale(1.05);
}

.image-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.1), transparent);
  pointer-events: none;
}

.article-image.placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #f5f5f5 0%, #fafafa 100%);
}

.placeholder-icon {
  font-size: 48px;
  opacity: 0.3;
}

.article-content {
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  flex: 1;
}

.article-source {
  margin: 0;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: #ff6b6b;
}

.article-title {
  margin: 0;
  font-size: 16px;
  font-weight: 700;
  line-height: 1.4;
  color: #1a1a1a;
}

.article-title a {
  color: inherit;
  text-decoration: none;
  transition: color 0.22s ease;
}

.article-title a:hover {
  color: #7b5ce0;
}

.article-summary {
  margin: 0;
  font-size: 14px;
  line-height: 1.5;
  color: #555;
  flex: 1;
}

.article-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 8px;
  padding-top: 12px;
  border-top: 1px solid #f0f0f0;
}

.article-time {
  font-size: 12px;
  color: #999;
  font-weight: 500;
}

.read-link {
  font-size: 13px;
  font-weight: 600;
  color: #7b5ce0;
  text-decoration: none;
  transition: all 0.22s ease;
  padding: 4px 8px;
  border-radius: 4px;
}

.read-link:hover {
  background: rgba(123, 92, 224, 0.1);
  color: #6a4dc7;
}

@media (max-width: 1100px) {
  .articles-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
  }
}

@media (max-width: 680px) {
  .articles-grid {
    grid-template-columns: 1fr;
    gap: 16px;
  }
}
</style>
