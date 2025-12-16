<template>
  <section class="analysis">
    <div class="section-container">
      <h2 class="section-title">Vidéos</h2>
      <div v-if="loading" class="loading-state">Chargement des vidéos...</div>
      <div v-else-if="videos.length === 0" class="empty-state">Aucune vidéo disponible</div>
      <div v-else class="analysis-grid">
        <article class="analysis-card" v-for="video in videos.slice(0, 3)" :key="video.link">
          <a :href="video.link" target="_blank" rel="noopener" class="analysis-image" :style="getBackgroundStyle(video.thumbnail)">
            <div class="video-placeholder">▶</div>
          </a>
          <div class="analysis-content">
            <span class="analysis-badge">Vidéo</span>
            <h3 class="analysis-title">{{ video.title }}</h3>
            <p class="analysis-author">{{ video.channel || 'Chaîne inconnue' }}</p>
            <p class="analysis-excerpt">{{ truncate(video.summary, 100) }}</p>
            <a :href="video.link" target="_blank" rel="noopener" class="video-link">▶ Regarder la vidéo</a>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';

interface Video {
  channel: string;
  title: string;
  link: string;
  published: string;
  publishedTime: number;
  thumbnail?: string;
  summary?: string;
}

const videos = ref<Video[]>([]);
const loading = ref(false);

const getBackgroundStyle = (thumbnail?: string) => {
  if (thumbnail) {
    return { backgroundImage: `url('${thumbnail}')`, backgroundSize: 'cover', backgroundPosition: 'center' };
  }
  return { background: 'linear-gradient(135deg, #2f0538, #4b2faa)' };
};

const truncate = (text?: string, length = 100) => {
  if (!text) return 'Analyse approfondie et décryptage du conflit Ukraine-Russie.';
  return text.length > length ? text.substring(0, length) + '...' : text;
};

const fetchVideos = async () => {
  loading.value = true;
  
  // 1) Fallback archive immédiat
  try {
    const resArch = await fetch('http://localhost:5000/archive', { signal: AbortSignal.timeout(8000) });
    if (resArch.ok) {
      const dataArch = await resArch.json();
      const listArch: Video[] = Array.isArray(dataArch) ? dataArch : (dataArch?.videos ?? []);
      if (listArch?.length) videos.value = listArch;
    }
  } catch (err) {
    console.warn('Archive fallback vidéos indisponible', err);
  }

  // 2) Requête live
  try {
    const res = await fetch('http://localhost:5000/videos?hours=0&limit=100', { signal: AbortSignal.timeout(12000) });
    if (!res.ok) throw new Error('API error');
    const data = await res.json();
    if (data?.videos) videos.value = data.videos;
  } catch (e) {
    console.error('Erreur chargement vidéos:', e);
    // on garde les vidéos de l'archive si elles ont été chargées
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  void fetchVideos();
});
</script>

<style scoped>
.analysis {
  background: #ffffff;
  padding: 24px 20px;
}

.loading-state,
.empty-state {
  text-align: center;
  padding: 40px 20px;
  color: #999;
  font-size: 14px;
}

.section-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.section-title {
  margin: 0;
  font-size: 28px;
  font-weight: 700;
  color: #2f0538;
  margin-bottom: 32px;
  padding-top: 24px;
}

.section-title::before {
  content: "";
  display: inline-block;
  vertical-align: middle;
  width: 6px;
  height: 28px;
  background: linear-gradient(180deg, #2f0538, #4b2faa);
  margin-right: 12px;
  border-radius: 3px;
}

.analysis-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.analysis-card {
  background: #fff;
  border-radius: 10px;
  overflow: hidden;
  transition: all 0.3s ease;
  cursor: pointer;
  border: 2px solid #f0f0f0;
}

.analysis-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 32px rgba(47, 5, 56, 0.15);
  border-color: #7b5ce0;
}

.analysis-image {
  width: 100%;
  aspect-ratio: 16/9;
  background: linear-gradient(135deg, #2f0538, #4b2faa);
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  position: relative;
  overflow: hidden;
}

.video-placeholder {
  font-size: 48px;
  color: rgba(255, 255, 255, 0.7);
  cursor: pointer;
  transition: all 0.3s ease;
}

.analysis-card:hover .video-placeholder {
  font-size: 56px;
  color: #fff;
}

.video-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: #7b5ce0;
  text-decoration: none;
  font-weight: 600;
  font-size: 13px;
  transition: all 0.3s ease;
  margin-top: 8px;
}

.video-link:hover {
  color: #2f0538;
  gap: 10px;
}

.analysis-content {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.analysis-badge {
  display: inline-block;
  background: #2f0538;
  color: #fff;
  padding: 6px 12px;
  border-radius: 4px;
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  width: fit-content;
}

.analysis-title {
  margin: 0;
  font-size: 16px;
  font-weight: 700;
  color: #1a1a1a;
  line-height: 1.4;
}

.analysis-author {
  margin: 0;
  font-size: 12px;
  color: #7b5ce0;
  font-weight: 600;
}

.analysis-excerpt {
  margin: 0;
  font-size: 13px;
  color: #666;
  line-height: 1.5;
}

@media (max-width: 1100px) {
  .analysis-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 680px) {
  .section-title {
    font-size: 22px;
  }

  .analysis-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .section-title {
    font-size: 18px;
    padding-top: 24px;
  }
}
</style>
