<template>
  <section class="featured-articles-section my-16">
    <v-container>
      <!-- Section Title -->
      <div class="section-header mb-12">
        <h2 class="section-title">Articles en vedette</h2>
        <p class="section-subtitle">
          Explorez nos analyses approfondies sur les enjeux clés du conflit
        </p>
      </div>

      <!-- Articles Grid -->
      <v-row :gutter="24">
        <v-col
          v-for="article in articles"
          :key="article.id"
          cols="12"
          md="6"
          lg="4"
        >
          <ArticlePreviewCard :article="article" />
        </v-col>
      </v-row>

      <!-- View All Button -->
      <div class="text-center mt-12">
        <v-btn
          to="/articles/technologies-militaires"
          color="primary"
          size="large"
          variant="outlined"
        >
          Découvrir tous les articles
        </v-btn>
      </div>
    </v-container>
  </section>
</template>

<script setup lang="ts">
import { useFeaturedArticles } from '~/composables/useFeaturedArticles'
import ArticlePreviewCard from './ArticlePreviewCard.vue'

const { articles } = useFeaturedArticles()
</script>

<style scoped>
.featured-articles-section {
  padding: 60px 0;
}

.section-header {
  text-align: center;
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

@media (max-width: 960px) {
  .section-title {
    font-size: 2rem;
  }

  .featured-articles-section {
    padding: 40px 0;
  }
}

@media (max-width: 600px) {
  .section-title {
    font-size: 1.5rem;
  }

  .section-subtitle {
    font-size: 1rem;
  }
}
</style>
