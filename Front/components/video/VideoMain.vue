<template>
  <main class="live-feed">
    <VideoHeader v-model:query="localQuery" @search="filterVideos" />

    <EmptyState v-if="filteredVideos.length === 0" @reset="resetSearch" />
    <section v-else class="articles-container">
      <FeaturedVideo v-if="filteredVideos[0]" :video="filteredVideos[0]" />
      <VideosGrid v-if="filteredVideos.length > 1" :videos="filteredVideos.slice(1)" />
    </section>
  </main>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import VideoHeader from '~/components/video/VideoHeader.vue';
import EmptyState from '~/components/video/EmptyState.vue';
import FeaturedVideo from '~/components/video/FeaturedVideo.vue';
import VideosGrid from '~/components/video/VideosGrid.vue';

const localQuery = ref('');

const videos = ref([
  { id: 1, title: "La guerre de l'information : Stratégies et manipulation", description: "Analyse approfondie des mécanismes de propagande et de désinformation dans le conflit Ukraine-Russie.", source: 'Médias partenaires', date: 'Il y a 3h', link: '#video-1' },
  { id: 2, title: "OSINT et fact-checking : Outils d'analyse", description: "Comment les outils open-source permettent de vérifier l'information en temps réel.", source: 'Médias partenaires', date: 'Il y a 5h', link: '#video-2' },
  { id: 3, title: 'Deepfakes et technologie : Nouveaux défis', description: "L'impact des deepfakes sur la perception du conflit et les méthodes de détection.", source: 'Médias partenaires', date: 'Il y a 8h', link: '#video-3' },
  { id: 4, title: 'Réseaux sociaux et influence', description: "Le rôle des plateformes sociales dans la diffusion de l'information et de la propagande.", source: 'Médias partenaires', date: 'Hier', link: '#video-4' },
  { id: 5, title: 'Analyse géopolitique du conflit', description: 'Comprendre les enjeux stratégiques et les implications internationales.', source: 'Médias partenaires', date: 'Il y a 2 jours', link: '#video-5' },
  { id: 6, title: 'Cybersécurité et cyberguerre', description: "Les opérations de cyberattaques et leur impact sur le conflit.", source: 'Médias partenaires', date: 'Il y a 3 jours', link: '#video-6' }
]);

const filteredVideos = computed(() => {
  if (!localQuery.value) return videos.value;
  const q = localQuery.value.toLowerCase();
  return videos.value.filter(v =>
    v.title.toLowerCase().includes(q) ||
    v.description.toLowerCase().includes(q)
  );
});

const filterVideos = () => {};

const resetSearch = () => {
  localQuery.value = '';
  filterVideos();
};
</script>

<style scoped>
.live-feed {
  min-height: 100vh;
  background: #ffffff;
  padding-bottom: 60px;
}

.articles-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}
@media (max-width: 680px) {
  .articles-container { padding: 0 16px; }
}
</style>
