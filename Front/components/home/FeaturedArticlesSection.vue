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

      <!-- Articles List -->
      <div class="articles-list">
        <article
          v-for="(article, index) in articles"
          :key="article.id"
          class="article-entry"
          @click="$router.push(`/${article.slug}`)"
        >
          <div class="article-number">{{ String(index + 1).padStart(2, '0') }}</div>
          
          <div class="article-body">
            <div class="article-meta">
              <span class="meta-author">{{ article.author }}</span>
              <span class="meta-separator">—</span>
              <span class="meta-date">{{ formatDate(article.date) }}</span>
            </div>

            <h3 class="article-title">{{ article.title }}</h3>

            <div class="article-preview">
              <p class="preview-text">{{ getPreviewText(article.content) }}</p>
              <div class="preview-fade"></div>
            </div>

            <div class="article-link">
              <span>Lire l'article</span>
              <v-icon size="small">mdi-arrow-right</v-icon>
            </div>
          </div>

          <div v-if="index < articles.length - 1" class="article-divider"></div>
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
           !trimmed.match(/^[A-Z\s:]+$/) && // Skip all-caps headers (with colons)
           !trimmed.startsWith('##') &&
           !trimmed.startsWith('#') &&
           !trimmed.startsWith('À COMPLÉTER') &&
           !trimmed.startsWith('•') && // Skip bullet points
           trimmed.length > 50 // Lower threshold for substantial paragraphs
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
  padding: 16px 0 24px 0;
  background: #ffffff;
}

.section-header {
  text-align: center;
  margin-bottom: 20px;
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

.articles-list {
  max-width: 900px;
  margin: 0 auto;
}

.article-entry {
  display: grid;
  grid-template-columns: 60px 1fr;
  gap: 20px;
  padding: 16px 0;
  cursor: pointer;
  position: relative;
  transition: all 0.3s ease;
}

.article-entry:first-child {
  padding-top: 0;
}

.article-entry:hover .article-title {
  color: #7b5ce0;
}

.article-entry:hover .article-link {
  color: #7b5ce0;
  gap: 8px;
}

.article-entry:hover .article-link v-icon {
  transform: translateX(4px);
}

.article-number {
  font-size: 1.5rem;
  font-weight: 700;
  color: #e5e7eb;
  line-height: 1;
  padding-top: 4px;
}

.article-body {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.article-meta {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.875rem;
}

.meta-author {
  font-weight: 600;
  color: #111827;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-size: 0.8rem;
}

.meta-separator {
  color: #d1d5db;
}

.meta-date {
  color: #6b7280;
}

.article-title {
  font-size: 1.75rem;
  font-weight: 700;
  color: #111827;
  margin: 0;
  line-height: 1.3;
  letter-spacing: -0.01em;
  transition: color 0.3s ease;
}

.article-preview {
  position: relative;
  margin-top: 0;
  max-height: 110px;
  overflow: hidden;
}

.preview-text {
  font-size: 1rem;
  line-height: 1.75;
  color: #4b5563;
  margin: 0;
}

.preview-fade {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 50px;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    rgba(255, 255, 255, 0.3) 30%,
    rgba(255, 255, 255, 0.8) 70%,
    rgba(255, 255, 255, 1) 100%
  );
  pointer-events: none;
}

.article-link {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #111827;
  font-weight: 600;
  font-size: 0.9rem;
  margin-top: 0;
  transition: all 0.3s ease;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.article-link v-icon {
  transition: transform 0.3s ease;
}

.article-divider {
  grid-column: 1 / -1;
  height: 1px;
  background: #e5e7eb;
  margin-top: 16px;
}

@media (max-width: 768px) {
  .featured-articles-section {
    padding: 12px 0 20px 0;
  }

  .section-title {
    font-size: 2rem;
  }

  .section-subtitle {
    font-size: 1rem;
  }

  .section-header {
    margin-bottom: 16px;
  }

  .article-entry {
    grid-template-columns: 50px 1fr;
    gap: 16px;
    padding: 14px 0;
  }

  .article-number {
    font-size: 1.25rem;
  }

  .article-title {
    font-size: 1.4rem;
  }

  .article-divider {
    margin-top: 14px;
  }
}

@media (max-width: 600px) {
  .section-title {
    font-size: 1.75rem;
  }

  .article-entry {
    grid-template-columns: 1fr;
    gap: 16px;
  }

  .article-number {
    display: none;
  }

  .article-title {
    font-size: 1.3rem;
  }

  .preview-text {
    font-size: 0.95rem;
  }

  .article-preview {
    max-height: 90px;
  }
}
</style>
    font-size: 0.95rem;
