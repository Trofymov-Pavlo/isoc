<template>
  <main class="live-feed">
    <PageHero
      title="Analyses & Décryptages Vidéo"
      subtitle="Découvrez nos analyses approfondies et décryptages vidéo du conflit"
      badge="Vidéos"
      badge-icon="▶"
    />

    <div class="video-content">
      <div class="search-bar-container">
        <div class="search-wrapper">
          <input
            v-model="localQuery"
            class="search-input"
            placeholder="Rechercher une vidéo..."
            @keyup.enter="filterVideos"
          />
          <svg v-if="!localQuery" class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <path d="m21 21-4.35-4.35"></path>
          </svg>
          <button v-else @click="localQuery = ''; filterVideos()" class="clear-btn">×</button>
        </div>
      </div>

      <EmptyState v-if="filteredVideos.length === 0" @reset="resetSearch" />
      <section v-else class="articles-container">
        <FeaturedVideo v-if="filteredVideos[0]" :video="filteredVideos[0]" />
        <VideosGrid v-if="filteredVideos.length > 1" :videos="filteredVideos.slice(1)" />
      </section>
    </div>
  </main>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import PageHero from '~/components/shared/PageHero.vue';
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

.video-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 calc(2vw);
}

.search-bar-container {
  padding: 32px 0 24px;
  display: flex;
  justify-content: center;
  border-bottom: 1px solid #f0f0f0;
  margin-bottom: 32px;
}

.search-wrapper {
  position: relative;
  width: 100%;
  max-width: 400px;
}

.search-input {
  width: 100%;
  padding: 10px 38px 10px 16px;
  border-radius: 8px;
  border: 1px solid #ddd;
  background: #f8f8f8;
  color: #333;
  font-size: 14px;
  transition: all 0.2s ease;
}

.search-input::placeholder {
  color: #999;
}

.search-input:focus {
  outline: none;
  border-color: #2f0538;
  background: #fff;
  box-shadow: 0 2px 8px rgba(47, 5, 56, 0.1);
}

.search-icon {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: #999;
  pointer-events: none;
}

.clear-btn {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: #666;
  font-size: 24px;
  cursor: pointer;
  padding: 0;
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.2s ease;
}

.clear-btn:hover {
  color: #333;
}

.articles-container {
  max-width: 1200px;
  margin: 0 auto;
}

@media (max-width: 680px) {
  .search-wrapper {
    max-width: 100%;
  }
}
</style>
