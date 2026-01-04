<template>
  <section class="featured-articles-section">
    <v-container>
      <!-- Section Title -->
      <div class="section-header mb-12">
        <h2 class="section-title">Articles en vedette</h2>
        <p class="section-subtitle">
          Explorez nos analyses approfondies sur les enjeux clés du conflit
        </p>
      </div>

      <!-- Articles Stack (Full Width) -->
      <div class="articles-stack">
        <div
          v-for="(article, index) in articles"
          :key="article.id"
          class="article-item"
          :class="`article-${index + 1}`"
          @click="$router.push(`/articles/${article.slug}`)"
        >
          <div class="article-content-container">
            <div class="article-index">{{ String(index + 1).padStart(2, '0') }}</div>
            <div class="article-info">
              <h3 class="article-title">{{ article.title }}</h3>
              <p class="article-excerpt">{{ article.excerpt }}</p>
              
              <div class="article-footer">
                <div class="article-meta">
                  <span class="meta-date">
                    <v-icon small>mdi-calendar</v-icon>
                    {{ formatDate(article.date) }}
                  </span>
                  <span class="meta-author">
                    <v-icon small>mdi-account</v-icon>
                    {{ article.author }}
                  </span>
                </div>
                <v-btn
                  color="white"
                  variant="text"
                  append-icon="mdi-arrow-right"
                  size="small"
                >
                  Lire la suite
                </v-btn>
              </div>
            </div>
          </div>
        </div>
      </div>
    </v-container>
  </section>
</template>

<script setup lang="ts">
import { useFeaturedArticles } from '~/composables/useFeaturedArticles'

const { articles } = useFeaturedArticles()

const formatDate = (date: string) => {
  return new Intl.DateTimeFormat('fr-FR', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  }).format(new Date(date))
}
</script>

<style scoped>
.featured-articles-section {
  padding: 80px 0;
  background: #f8fafc;
}

.section-header {
  text-align: center;
  margin-bottom: 60px;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--v-primary);
  margin-bottom: 12px;
}

.section-subtitle {
  font-size: 1.1rem;
  color: rgba(0, 0, 0, 0.6);
  max-width: 600px;
  margin: 0 auto;
}

.articles-stack {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.article-item {
  cursor: pointer;
  border-radius: 16px;
  padding: 32px;
  transition: all 0.3s ease;
  background: white;
  border: 2px solid transparent;
  display: flex;
  align-items: center;
  gap: 24px;
  min-height: 200px;
}

.article-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.1);
}

/* Color coding for each article */
.article-1 {
  background: linear-gradient(135deg, #fef3c7 0%, #fef08a 100%);
  border-color: #fbbf24;
}

.article-1:hover {
  border-color: #f59e0b;
  background: linear-gradient(135deg, #fef08a 0%, #fde047 100%);
}

.article-2 {
  background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
  border-color: #60a5fa;
}

.article-2:hover {
  border-color: #3b82f6;
  background: linear-gradient(135deg, #bfdbfe 0%, #93c5fd 100%);
}

.article-3 {
  background: linear-gradient(135deg, #ddd6fe 0%, #c4b5fd 100%);
  border-color: #a78bfa;
}

.article-3:hover {
  border-color: #8b5cf6;
  background: linear-gradient(135deg, #c4b5fd 0%, #a78bfa 100%);
}

.article-content-container {
  display: flex;
  gap: 24px;
  width: 100%;
  align-items: flex-start;
}

.article-index {
  font-size: 3rem;
  font-weight: 900;
  color: rgba(0, 0, 0, 0.15);
  min-width: 80px;
  text-align: center;
  line-height: 1;
}

.article-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.article-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: rgba(0, 0, 0, 0.9);
  margin: 0;
  line-height: 1.4;
}

.article-excerpt {
  font-size: 1rem;
  color: rgba(0, 0, 0, 0.7);
  margin: 0;
  line-height: 1.6;
}

.article-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: auto;
  padding-top: 12px;
}

.article-meta {
  display: flex;
  gap: 16px;
  font-size: 0.875rem;
  color: rgba(0, 0, 0, 0.6);
}

.meta-date,
.meta-author {
  display: flex;
  align-items: center;
  gap: 4px;
}

:deep(.v-btn) {
  text-transform: none;
}

@media (max-width: 768px) {
  .featured-articles-section {
    padding: 40px 0;
  }

  .section-title {
    font-size: 2rem;
  }

  .article-item {
    flex-direction: column;
    text-align: center;
    padding: 24px;
    min-height: auto;
  }

  .article-content-container {
    flex-direction: column;
    align-items: center;
  }

  .article-index {
    font-size: 2rem;
  }

  .article-footer {
    flex-direction: column;
    gap: 12px;
  }

  .article-meta {
    justify-content: center;
  }
}

@media (max-width: 600px) {
  .article-item {
    padding: 16px;
  }

  .article-title {
    font-size: 1.25rem;
  }

  .article-excerpt {
    font-size: 0.95rem;
  }

  .section-title {
    font-size: 1.5rem;
  }

  .section-subtitle {
    font-size: 1rem;
  }
}
</style>
