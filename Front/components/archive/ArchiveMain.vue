<template>
  <main class="archive-page">
    <PageHero
      title="Archives"
      subtitle="Consultez l'historique complet de nos articles et vidéos"
      badge="Contenu archivé"
      badge-icon="🗃️"
    />

    <section class="shell">
      <div class="grid">
        <div class="col">
          <h2>Articles</h2>
          <ul class="list" v-if="articles.length > 0">
            <li v-for="a in articles" :key="a.id">{{ a.title }}</li>
          </ul>
          <p v-else class="empty-message">Aucun article archivé pour le moment</p>
        </div>
        <div class="col">
          <h2>Vidéos</h2>
          <ul class="list" v-if="videos.length > 0">
            <li v-for="v in videos" :key="v.id">{{ v.title }}</li>
          </ul>
          <p v-else class="empty-message">Aucune vidéo archivée pour le moment</p>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
import PageHero from '~/components/shared/PageHero.vue';

const articles: Array<{ id:number; title:string; }> = []
const videos: Array<{ id:number; title:string; }> = []
</script>

<style scoped>
.archive-page {
  min-height: 100vh;
  background: #fff;
}

.shell {
  max-width: 1400px;
  margin: 0 auto;
  padding: 48px calc(2vw) 60px;
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
}

.col h2 {
  font-size: 24px;
  font-weight: 700;
  color: #2f0538;
  margin: 0 0 24px;
  padding-bottom: 16px;
  border-bottom: 2px solid #f0f0f0;
}

.list {
  margin: 0;
  padding-left: 24px;
  color: #4a4a55;
}

.list li {
  margin: 12px 0;
  line-height: 1.6;
}

.empty-message {
  color: #999;
  font-style: italic;
  margin: 24px 0;
}

@media (max-width: 768px) {
  .grid {
    grid-template-columns: 1fr;
    gap: 32px;
  }
}
</style>
