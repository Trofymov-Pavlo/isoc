<template>
  <v-container class="article-page">
    <v-row>
      <v-col cols="12" lg="8" offset-lg="2">
        <!-- Header -->
        <div class="article-header mb-4">
          <v-btn
            variant="text"
            prepend-icon="mdi-arrow-left"
            @click="$router.push('/')"
            class="mb-4"
          >
            Retour
          </v-btn>

          <h1 class="article-title mb-4">{{ article?.title }}</h1>

          <div class="article-meta">
            <div class="meta-item">
              <v-icon small class="me-2">mdi-account</v-icon>
              <strong>{{ article?.author }}</strong>
            </div>
            <div class="meta-item">
              <v-icon small class="me-2">mdi-calendar</v-icon>
              {{ formatDate(article?.date || '') }}
            </div>
          </div>

          <v-divider class="my-4"></v-divider>
        </div>

        <!-- Content -->
        <div v-if="article?.content" class="article-content">
          <div v-html="formattedContent"></div>
        </div>

        <!-- Navigation -->
        <div class="article-navigation mt-8">
          <v-divider class="mb-4"></v-divider>
          <div class="d-flex justify-space-between gap-4">
            <v-btn
              v-if="previousSlug"
              variant="tonal"
              prepend-icon="mdi-arrow-left"
              :to="`/${previousSlug}`"
            >
              Article précédent
            </v-btn>
            <v-btn
              variant="tonal"
              prepend-icon="mdi-home"
              @click="$router.push('/')"
            >
              Retour à l'accueil
            </v-btn>
            <v-btn
              v-if="nextSlug"
              variant="tonal"
              append-icon="mdi-arrow-right"
              :to="`/${nextSlug}`"
            >
              Article suivant
            </v-btn>
          </div>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useFeaturedArticles } from '~/composables/useFeaturedArticles'

const { articles, getArticle } = useFeaturedArticles()

const slug = 'technologies-militaires'
const article = computed(() => getArticle(slug))

const currentIndex = computed(() => articles.findIndex(a => a.slug === slug))

const previousSlug = computed((): string | null => {
  const index = currentIndex.value
  if (index <= 0) return null
  const previous = articles[index - 1]
  return previous ? previous.slug : null
})

const nextSlug = computed((): string | null => {
  const index = currentIndex.value
  if (index < 0 || index >= articles.length - 1) return null
  const next = articles[index + 1]
  return next ? next.slug : null
})

const formattedContent = computed(() => {
  if (!article.value?.content) return ''
  const content = article.value.content
  
  let formatted = content
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;')
  
  formatted = formatted
    .replace(/^([A-ZÀ-ÖØ-Ý0-9][A-ZÀ-ÖØ-Ý0-9\s'’"():,.\-–—…!?]+)$/gm, '<h2 style="margin-top: 24px; margin-bottom: 16px; font-weight: 700;">$1</h2>')
    .replace(/^• (.+)$/gm, '<li style="margin-left: 20px;">$1</li>')
    .replace(/^- (.+)$/gm, '<li style="margin-left: 20px;">$1</li>')
    .replace(/(<li[^>]*>.+<\/li>)/s, '<ul style="list-style: none; padding: 0; margin-bottom: 16px;">$1</ul>')
    .replace(/\n\n+/g, '</p><p style="margin: 16px 0; line-height: 1.8;">')
    .replace(/^(?!<)/gm, '<p style="margin: 16px 0; line-height: 1.8;">')
  
  return formatted + '</p>'
})

const formatDate = (date: string) => {
  if (!date) return ''
  return new Intl.DateTimeFormat('fr-FR', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  }).format(new Date(date))
}
</script>

<style scoped>
.article-page {
  padding: 20px 16px;
}

.article-header {
  text-align: left;
}

.article-title {
  font-size: 2.25rem;
  font-weight: 700;
  line-height: 1.2;
  color: #8b5cf6;
  margin-bottom: 16px;
}

.article-meta {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  font-size: 0.95rem;
  color: rgba(0, 0, 0, 0.6);
}

.meta-item {
  display: flex;
  align-items: center;
}

.article-content {
  font-size: 1.05rem;
  line-height: 1.7;
  color: rgba(0, 0, 0, 0.8);
}

.article-content :deep(h2) {
  font-size: 1.5rem;
  font-weight: 700;
  margin: 24px 0 12px 0;
  color: #8b5cf6;
  padding-left: 12px;
  border-left: 4px solid #a78bfa;
}

.article-content :deep(h3) {
  font-size: 1.25rem;
  font-weight: 600;
  margin: 16px 0 8px 0;
  color: #7c3aed;
}

.article-content :deep(p) {
  margin-bottom: 12px;
}

.article-content :deep(ul),
.article-content :deep(ol) {
  margin-left: 20px;
  margin-bottom: 12px;
}

.article-content :deep(li) {
  margin-bottom: 6px;
}

.article-navigation {
  min-height: 50px;
  margin-top: 32px;
}

@media (max-width: 600px) {
  .article-page {
    padding: 16px 12px;
  }

  .article-title {
    font-size: 1.75rem;
  }

  .article-meta {
    flex-direction: column;
    gap: 8px;
  }

  .article-navigation .d-flex {
    flex-direction: column;
    gap: 8px;
  }

  .article-navigation :deep(.v-btn) {
    width: 100%;
  }
}
</style>
