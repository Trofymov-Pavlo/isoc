<template>
  <div class="articles-index">
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-btn
            prepend-icon="mdi-arrow-left"
            variant="text"
            @click="$router.push('/')"
            class="mb-6"
          >
            Retour à l'accueil
          </v-btn>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="12">
          <h1 class="page-title">Articles en vedette</h1>
          <p class="page-subtitle">
            Approfondissez votre compréhension des enjeux clés du conflit à travers nos analyses
          </p>
        </v-col>
      </v-row>

      <v-row class="mt-8" :gutter="24">
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
    </v-container>
  </div>
</template>

<script setup lang="ts">
import ArticlePreviewCard from '~/components/home/ArticlePreviewCard.vue'

const articles = [
  {
    id: 1,
    title: 'Les technologies militaires utilisées dans le conflit',
    author: 'Hiba ABDESSADAK',
    date: '2025-12-05',
    excerpt: 'Le conflit ukrainien marque un tournant dans l\'histoire militaire moderne, où les nouvelles technologies jouent un rôle déterminant...',
    slug: 'technologies-militaires'
  },
  {
    id: 2,
    title: 'La vérité est une munition : Plongée dans la guerre de l\'information en Ukraine',
    author: 'Antoine TENA',
    date: '2025-12-12',
    excerpt: 'Alors que l\'hiver 2025 fige les lignes de front du Donbass dans la boue et la glace, une autre guerre bat son plein, insensible aux saisons...',
    slug: 'guerre-information'
  },
  {
    id: 3,
    title: 'Guerre en Ukraine : quand l\'algorithme décide de donner la mort',
    author: 'Nathan BARRACHIN',
    date: '2025-12-18',
    excerpt: 'Dans les steppes ukrainiennes, l\'intelligence artificielle a révolutionné la guerre moderne avec une efficacité qui glace le sang...',
    slug: 'enjeux-ethiques'
  }
]
</script>

<style scoped>
.articles-index {
  padding: 40px 20px;
}

.page-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--v-primary);
  margin-bottom: 12px;
}

.page-subtitle {
  font-size: 1.1rem;
  color: rgba(0, 0, 0, 0.6);
  max-width: 600px;
}

@media (max-width: 600px) {
  .page-title {
    font-size: 1.75rem;
  }

  .page-subtitle {
    font-size: 1rem;
  }
}
</style>
