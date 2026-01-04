<template>
  <v-container class="article-page">
    <v-row>
      <v-col cols="12" lg="8" offset-lg="2">
        <!-- Header -->
        <div class="article-header mb-8">
          <v-btn
            variant="text"
            prepend-icon="mdi-arrow-left"
            @click="$router.back()"
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

          <v-divider class="my-6"></v-divider>
        </div>

        <!-- Content -->
        <div v-if="article?.content && article.content !== 'À remplir'" class="article-content">
          <div v-html="formattedContent"></div>
        </div>

        <!-- Placeholder for articles not yet written -->
        <v-alert
          v-else
          type="info"
          variant="tonal"
          class="mt-8"
        >
          <template #title>Article en cours de rédaction</template>
          Cet article sera bientôt disponible. Revenez pour plus de détails !
        </v-alert>

        <!-- Navigation -->
        <div class="article-navigation mt-12">
          <v-divider class="mb-8"></v-divider>
          <div class="d-flex justify-space-between">
            <v-btn
              v-if="previousArticle"
              variant="tonal"
              prepend-icon="mdi-arrow-left"
              :to="`/articles/${previousArticle.slug}`"
            >
              {{ previousArticle.title }}
            </v-btn>
            <div></div>
            <v-btn
              v-if="nextArticle"
              variant="tonal"
              append-icon="mdi-arrow-right"
              :to="`/articles/${nextArticle.slug}`"
            >
              {{ nextArticle.title }}
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

const route = useRoute()
const { articles, getArticle } = useFeaturedArticles()

const article = computed(() => getArticle(route.params.slug as string))

const formattedContent = computed(() => {
  if (!article.value?.content) return ''
  const content = article.value.content
  
  // Simple markdown-like formatting
  return content
    .replace(/^### (.+)$/gm, '<h3>$1</h3>')
    .replace(/^## (.+)$/gm, '<h2>$1</h2>')
    .replace(/^# (.+)$/gm, '<h1>$1</h1>')
    .replace(/\n- (.+)/g, '\n<li>$1</li>')
    .replace(/(<li>.+<\/li>)/s, '<ul>$1</ul>')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\n\n/g, '</p><p>')
    .replace(/^/g, '<p>')
    .replace(/$/g, '</p>')
})

const currentIndex = computed(() => {
  return articles.findIndex(a => a.slug === route.params.slug)
})

const previousArticle = computed(() => {
  const index = currentIndex.value
  return index > 0 ? articles[index - 1] : null
})

const nextArticle = computed(() => {
  const index = currentIndex.value
  return index < articles.length - 1 ? articles[index + 1] : null
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
  padding: 40px 20px;
}

.article-header {
  text-align: left;
}

.article-title {
  font-size: 2.5rem;
  font-weight: 700;
  line-height: 1.2;
  color: var(--v-primary);
  margin-bottom: 24px;
}

.article-meta {
  display: flex;
  gap: 24px;
  flex-wrap: wrap;
  font-size: 1rem;
  color: rgba(0, 0, 0, 0.6);
}

.meta-item {
  display: flex;
  align-items: center;
}

.article-content {
  font-size: 1.1rem;
  line-height: 1.8;
  color: rgba(0, 0, 0, 0.8);
}

.article-content :deep(h2) {
  font-size: 1.75rem;
  font-weight: 600;
  margin: 32px 0 16px 0;
  color: var(--v-primary);
}

.article-content :deep(h3) {
  font-size: 1.35rem;
  font-weight: 600;
  margin: 24px 0 12px 0;
  color: rgba(0, 0, 0, 0.8);
}

.article-content :deep(p) {
  margin-bottom: 16px;
}

.article-content :deep(ul),
.article-content :deep(ol) {
  margin-left: 24px;
  margin-bottom: 16px;
}

.article-content :deep(li) {
  margin-bottom: 8px;
}

.article-content :deep(blockquote) {
  border-left: 4px solid var(--v-primary);
  padding-left: 16px;
  margin: 16px 0;
  color: rgba(0, 0, 0, 0.6);
}

.article-content :deep(code) {
  background-color: rgba(0, 0, 0, 0.05);
  padding: 2px 6px;
  border-radius: 4px;
  font-family: 'Courier New', monospace;
}

.article-navigation {
  min-height: 60px;
}

@media (max-width: 600px) {
  .article-title {
    font-size: 2rem;
  }

  .article-meta {
    flex-direction: column;
    gap: 12px;
  }

  .article-navigation .d-flex {
    flex-direction: column;
    gap: 12px;
  }

  .article-navigation :deep(.v-btn) {
    width: 100%;
  }
}
</style>
