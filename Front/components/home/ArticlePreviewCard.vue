<template>
  <v-card class="article-preview-card" :to="`/articles/${article.slug}`" elevation="2">
    <v-card-item>
      <div class="article-header">
        <h3 class="article-title">{{ article.title }}</h3>
      </div>

      <div class="article-metadata">
        <span class="metadata-item">
          <v-icon small>mdi-calendar</v-icon>
          {{ formatDate(article.date) }}
        </span>
        <span class="metadata-item">
          <v-icon small>mdi-account</v-icon>
          {{ article.author }}
        </span>
      </div>
    </v-card-item>

    <v-card-text class="article-excerpt-container">
      <div class="article-excerpt">
        {{ article.excerpt }}
      </div>
      <div class="excerpt-fade"></div>
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="primary"
        variant="text"
        append-icon="mdi-arrow-right"
        size="small"
      >
        Lire la suite
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup lang="ts">
import type { FeaturedArticle } from '~/composables/useFeaturedArticles'

defineProps<{
  article: FeaturedArticle
}>()

const formatDate = (date: string) => {
  return new Intl.DateTimeFormat('fr-FR', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  }).format(new Date(date))
}
</script>

<style scoped>
.article-preview-card {
  cursor: pointer;
  transition: all 0.3s ease;
  height: 100%;
  display: flex;
  flex-direction: column;
  text-decoration: none;
}

.article-preview-card:hover {
  elevation: 8;
  transform: translateY(-4px);
}

.article-header {
  margin-bottom: 12px;
}

.article-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--v-primary);
  line-height: 1.4;
  margin: 0;
}

.article-metadata {
  display: flex;
  gap: 16px;
  margin-bottom: 16px;
  font-size: 0.875rem;
  color: rgba(0, 0, 0, 0.6);
}

.metadata-item {
  display: flex;
  align-items: center;
  gap: 4px;
}

.article-excerpt-container {
  flex: 1;
  position: relative;
  overflow: hidden;
}

.article-excerpt {
  line-height: 1.6;
  color: rgba(0, 0, 0, 0.7);
  max-height: 100px;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
}

.excerpt-fade {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 30px;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    rgba(255, 255, 255, 0.4) 50%,
    rgba(255, 255, 255, 0.8) 100%
  );
  pointer-events: none;
}

:deep(.v-card__text) {
  padding-top: 16px;
}

:deep(.v-card__actions) {
  margin-top: auto;
}
</style>
