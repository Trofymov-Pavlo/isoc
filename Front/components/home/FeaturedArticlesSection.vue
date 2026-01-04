<template>
  <section class="featured-articles-section">
    <v-container>
      <!-- Section Title -->
      <div class="section-header">
        <h2 class="section-title">Nos analyses</h2>
        <p class="section-subtitle">
          Dans quelle mesure les nouvelles technologies transforment-elles la conduite de la guerre en Ukraine ?
        </p>
      </div>

      <!-- Articles Grid -->
      <div class="articles-grid">
        <article
          v-for="article in articles"
          :key="article.id"
          class="article-card"
          @click="$router.push(`/articles/${article.slug}`)"
        >
          <div class="article-header">
            <h3 class="article-title">{{ article.title }}</h3>
            <div class="article-meta">
              <span class="meta-author">{{ article.author }}</span>
              <span class="meta-separator">•</span>
              <span class="meta-date">{{ formatDate(article.date) }}</span>
            </div>
          </div>

          <div class="article-preview">
            <p class="article-text">{{ getPreviewText(article.content) }}</p>
            <div class="text-fade"></div>
          </div>

          <div class="article-action">
            <span class="read-more">Lire la suite</span>
            <v-icon size="small" class="arrow-icon">mdi-arrow-right</v-icon>
          </div>
        </article>
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

const getPreviewText = (content: string) => {
  // Get the first paragraph(s), skip headers and empty lines
  const paragraphs = content.split('\n\n').filter(para => {
    const trimmed = para.trim()
    return trimmed && 
           !trimmed.match(/^[A-Z\s]+$/) && // Skip all-caps headers
           !trimmed.startsWith('##') &&
           !trimmed.startsWith('#') &&
           !trimmed.startsWith('À COMPLÉTER') &&
           trimmed.length > 100 // Only substantial paragraphs
  })
  
  // Take first 2 paragraphs or ~400 characters
  let preview = paragraphs.slice(0, 2).join(' ')
  
  if (preview.length > 400) {
    const cutPoint = preview.lastIndexOf('.', 400)
    if (cutPoint > 300) {
      preview = preview.substring(0, cutPoint + 1)
    } else {
      preview = preview.substring(0, 400) + '...'
    }
  }
  
  return preview
}
</script>

<style scoped>
.featured-articles-section {
  padding: 60px 0 80px 0;
  background: #ffffff;
}

.section-header {
  text-align: center;
  margin-bottom: 60px;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

.section-title {
  font-size: 2.75rem;
  font-weight: 800;
  color: #111827;
  margin-bottom: 16px;
  letter-spacing: -0.02em;
}

.section-subtitle {
  font-size: 1.15rem;
  line-height: 1.7;
  color: #4b5563;
  font-weight: 400;
}

.articles-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 32px;
  max-width: 900px;
  margin: 0 auto;
}

.article-card {
  background: #ffffff;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 32px;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.article-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, #7b5ce0 0%, #a78bfa 100%);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.3s ease;
}

.article-card:hover::before {
  transform: scaleX(1);
}

.article-card:hover {
  border-color: #c4b5fd;
  box-shadow: 0 20px 40px rgba(123, 92, 224, 0.08);
  transform: translateY(-2px);
}

.article-header {
  margin-bottom: 20px;
}

.article-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #111827;
  margin: 0 0 12px 0;
  line-height: 1.3;
  letter-spacing: -0.01em;
}

.article-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.875rem;
  color: #6b7280;
}

.meta-author {
  font-weight: 600;
  color: #7b5ce0;
}

.meta-separator {
  color: #d1d5db;
}

.article-preview {
  position: relative;
  margin-bottom: 20px;
  max-height: 120px;
  overflow: hidden;
}

.article-text {
  font-size: 1rem;
  line-height: 1.75;
  color: #4b5563;
  margin: 0;
}

.text-fade {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 40px;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    rgba(255, 255, 255, 0.5) 40%,
    rgba(255, 255, 255, 0.95) 80%,
    rgba(255, 255, 255, 1) 100%
  );
  pointer-events: none;
}

.article-action {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #7b5ce0;
  font-weight: 600;
  font-size: 0.95rem;
  transition: gap 0.3s ease;
}

.article-card:hover .article-action {
  gap: 10px;
}

.read-more {
  transition: color 0.2s ease;
}

.arrow-icon {
  transition: transform 0.3s ease;
}

.article-card:hover .arrow-icon {
  transform: translateX(4px);
}

@media (max-width: 768px) {
  .featured-articles-section {
    padding: 40px 0 60px 0;
  }

  .section-title {
    font-size: 2rem;
  }

  .section-subtitle {
    font-size: 1rem;
  }

  .section-header {
    margin-bottom: 40px;
  }

  .article-card {
    padding: 24px;
  }

  .article-title {
    font-size: 1.25rem;
  }

  .articles-grid {
    gap: 24px;
  }
}

@media (max-width: 600px) {
  .section-title {
    font-size: 1.75rem;
  }

  .article-card {
    padding: 20px;
  }

  .article-preview {
    max-height: 100px;
  }

  .article-text {
    font-size: 0.95rem;
  }
}
</style>
