<template>
  <main class="video-feed">
    <header class="feed-header">
      <div class="header-top">
        <div class="title-section">
          <h1 class="feed-title">
            <span class="video-indicator">▶</span>
            Analyses & Décryptages Vidéo
          </h1>
          <p class="video-count">Toutes les vidéos d'analyse</p>
        </div>
        <div class="search-controls">
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
      </div>
    </header>

    <div v-if="filteredVideos.length === 0" class="empty-state">
      <span class="empty-icon">🎥</span>
      <p class="empty-text">Aucune vidéo ne correspond à votre recherche</p>
      <button class="reset-btn" @click="localQuery = ''; filterVideos()">Réinitialiser</button>
    </div>

    <section v-else class="videos-container">
      <!-- Featured Video -->
      <article v-if="filteredVideos[0]" class="featured-video">
        <div class="featured-video-player">
          <div class="video-placeholder">
            <span class="play-icon">▶</span>
          </div>
        </div>

        <div class="featured-content">
          <span class="featured-source">{{ filteredVideos[0].source }}</span>
          <h2 class="featured-title">{{ filteredVideos[0].title }}</h2>
          <p class="featured-summary">{{ filteredVideos[0].description }}</p>
          <div class="featured-footer">
            <time class="featured-time">{{ filteredVideos[0].date }}</time>
            <a :href="filteredVideos[0].link" target="_blank" rel="noopener" class="watch-link">
              ▶ Regarder la vidéo
            </a>
          </div>
        </div>
      </article>

      <!-- Grid of remaining videos -->
      <div v-if="filteredVideos.length > 1" class="videos-grid">
        <article 
          v-for="(video, i) in filteredVideos.slice(1)" 
          :key="i" 
          class="video-card"
        >
          <a 
            :href="video.link" 
            target="_blank" 
            rel="noopener" 
            class="video-thumbnail"
          >
            <div class="video-placeholder-small">
              <span class="play-icon-small">▶</span>
            </div>
            <div class="video-overlay"></div>
          </a>

          <div class="video-content">
            <span class="video-source">{{ video.source }}</span>
            <h3 class="video-title">
              <a :href="video.link" target="_blank" rel="noopener">{{ video.title }}</a>
            </h3>
            <p class="video-description">{{ video.description }}</p>
            <time class="video-time">{{ video.date }}</time>
          </div>
        </article>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';

const localQuery = ref('');

// Mock data - will be replaced by API data later
const videos = ref([
  {
    id: 1,
    title: 'La guerre de l\'information : Stratégies et manipulation',
    description: 'Analyse approfondie des mécanismes de propagande et de désinformation dans le conflit Ukraine-Russie.',
    source: 'Médias partenaires',
    date: 'Il y a 3h',
    link: '#video-1'
  },
  {
    id: 2,
    title: 'OSINT et fact-checking : Outils d\'analyse',
    description: 'Comment les outils open-source permettent de vérifier l\'information en temps réel.',
    source: 'Médias partenaires',
    date: 'Il y a 5h',
    link: '#video-2'
  },
  {
    id: 3,
    title: 'Deepfakes et technologie : Nouveaux défis',
    description: 'L\'impact des deepfakes sur la perception du conflit et les méthodes de détection.',
    source: 'Médias partenaires',
    date: 'Il y a 8h',
    link: '#video-3'
  },
  {
    id: 4,
    title: 'Réseaux sociaux et influence',
    description: 'Le rôle des plateformes sociales dans la diffusion de l\'information et de la propagande.',
    source: 'Médias partenaires',
    date: 'Hier',
    link: '#video-4'
  },
  {
    id: 5,
    title: 'Analyse géopolitique du conflit',
    description: 'Comprendre les enjeux stratégiques et les implications internationales.',
    source: 'Médias partenaires',
    date: 'Il y a 2 jours',
    link: '#video-5'
  },
  {
    id: 6,
    title: 'Cybersécurité et cyberguerre',
    description: 'Les opérations de cyberattaques et leur impact sur le conflit.',
    source: 'Médias partenaires',
    date: 'Il y a 3 jours',
    link: '#video-6'
  }
]);

const filteredVideos = computed(() => {
  if (!localQuery.value) {
    return videos.value;
  }
  const query = localQuery.value.toLowerCase();
  return videos.value.filter(video => 
    video.title.toLowerCase().includes(query) ||
    video.description.toLowerCase().includes(query)
  );
});

const filterVideos = () => {
  // Trigger computed property update
};
</script>

<style scoped>
.video-feed {
  min-height: 100vh;
  background: #fafafa;
}

.feed-header {
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  color: #fff;
  padding: 40px 0;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.header-top {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 32px;
}

.title-section {
  flex: 1;
}

.feed-title {
  margin: 0;
  font-size: 32px;
  font-weight: 800;
  display: flex;
  align-items: center;
  gap: 12px;
}

.video-indicator {
  color: #ff6b6b;
  font-size: 24px;
  animation: pulse 2s ease infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.6; }
}

.video-count {
  margin: 8px 0 0;
  font-size: 14px;
  color: rgba(255, 255, 255, 0.8);
}

.search-controls {
  display: flex;
  gap: 12px;
  align-items: center;
}

.search-wrapper {
  position: relative;
}

.search-input {
  padding: 12px 40px 12px 16px;
  border-radius: 8px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  background: rgba(255, 255, 255, 0.15);
  color: #fff;
  font-size: 14px;
  width: 280px;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
}

.search-input::placeholder {
  color: rgba(255, 255, 255, 0.6);
}

.search-input:focus {
  outline: none;
  border-color: #fff;
  background: rgba(255, 255, 255, 0.25);
}

.search-icon {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: rgba(255, 255, 255, 0.6);
  pointer-events: none;
}

.clear-btn {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: rgba(255, 255, 255, 0.8);
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
  color: #fff;
}

.empty-state {
  max-width: 1200px;
  margin: 80px auto;
  padding: 60px 20px;
  text-align: center;
}

.empty-icon {
  font-size: 64px;
  display: block;
  margin-bottom: 20px;
}

.empty-text {
  font-size: 18px;
  color: #666;
  margin-bottom: 24px;
}

.reset-btn {
  padding: 12px 24px;
  border-radius: 8px;
  border: none;
  background: linear-gradient(135deg, #2f0538, #4b2faa);
  color: #fff;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.reset-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(47, 5, 56, 0.3);
}

.videos-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 20px;
}

.featured-video {
  background: #fff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  margin-bottom: 48px;
  display: grid;
  grid-template-columns: 1.5fr 1fr;
  gap: 32px;
}

.featured-video-player {
  position: relative;
  aspect-ratio: 16/9;
  background: linear-gradient(135deg, #2f0538, #4b2faa);
}

.video-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.play-icon {
  font-size: 72px;
  color: rgba(255, 255, 255, 0.8);
  transition: all 0.3s ease;
}

.video-placeholder:hover .play-icon {
  color: #fff;
  font-size: 84px;
}

.featured-content {
  padding: 32px 32px 32px 0;
  display: flex;
  flex-direction: column;
  gap: 16px;
  justify-content: center;
}

.featured-source {
  color: #7b5ce0;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.8px;
}

.featured-title {
  margin: 0;
  font-size: 28px;
  font-weight: 700;
  line-height: 1.3;
  color: #1a1a1a;
}

.featured-summary {
  margin: 0;
  font-size: 15px;
  line-height: 1.6;
  color: #555;
}

.featured-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-top: 8px;
}

.featured-time {
  font-size: 13px;
  color: #999;
}

.watch-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: #7b5ce0;
  text-decoration: none;
  font-weight: 600;
  font-size: 14px;
  transition: all 0.3s ease;
}

.watch-link:hover {
  color: #2f0538;
  gap: 12px;
}

.videos-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.video-card {
  background: #fff;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  transition: all 0.3s ease;
  cursor: pointer;
}

.video-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

.video-thumbnail {
  display: block;
  position: relative;
  text-decoration: none;
}

.video-placeholder-small {
  width: 100%;
  aspect-ratio: 16/9;
  background: linear-gradient(135deg, #2f0538, #4b2faa);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.play-icon-small {
  font-size: 42px;
  color: rgba(255, 255, 255, 0.7);
  transition: all 0.3s ease;
}

.video-card:hover .play-icon-small {
  font-size: 48px;
  color: #fff;
}

.video-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0);
  transition: background 0.3s ease;
}

.video-card:hover .video-overlay {
  background: rgba(0, 0, 0, 0.1);
}

.video-content {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.video-source {
  color: #7b5ce0;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.video-title {
  margin: 0;
  font-size: 16px;
  font-weight: 700;
  line-height: 1.4;
  color: #1a1a1a;
}

.video-title a {
  color: inherit;
  text-decoration: none;
  transition: color 0.2s ease;
}

.video-title a:hover {
  color: #7b5ce0;
}

.video-description {
  margin: 0;
  font-size: 13px;
  line-height: 1.5;
  color: #666;
}

.video-time {
  font-size: 12px;
  color: #999;
}

@media (max-width: 1100px) {
  .featured-video {
    grid-template-columns: 1fr;
  }

  .featured-content {
    padding: 0 32px 32px;
  }

  .videos-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 680px) {
  .header-top {
    flex-direction: column;
    align-items: flex-start;
  }

  .search-controls {
    width: 100%;
  }

  .search-input {
    width: 100%;
  }

  .feed-title {
    font-size: 24px;
  }

  .videos-grid {
    grid-template-columns: 1fr;
  }

  .featured-title {
    font-size: 22px;
  }
}
</style>
