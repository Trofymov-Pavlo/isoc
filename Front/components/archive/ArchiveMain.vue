<template>
  <main class="archive-page">
    <PageHero
      title="Archives"
      subtitle="Consultez l'historique complet de nos articles et vidéos"
      badge="Contenu archivé"
      badge-icon="🗃️"
    />

    <section class="shell">
      <div class="header-row">
        <div>
          <p class="meta">Articles : {{ filteredArticles.length }} • Vidéos : {{ filteredVideos.length }}</p>
          <p class="hint">Dernière mise à jour : {{ lastUpdated }}</p>
        </div>
        <div class="search-wrapper">
          <input
            v-model="searchQuery"
            class="search-input"
            placeholder="Rechercher dans les archives..."
            @input="handleSearch"
          />
          <svg v-if="!searchQuery" class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <path d="m21 21-4.35-4.35"></path>
          </svg>
          <button v-else @click="searchQuery = ''" class="clear-btn">×</button>
        </div>
      </div>

      <div v-if="error" class="state error">{{ error }}</div>
      <div v-else-if="loading" class="state">Chargement des archives...</div>
      <div v-else class="grid">
        <div class="col">
          <h2>Articles</h2>
          <ul class="list" v-if="articles.length > 0">
            <li v-for="a in sortedArticles" :key="a.key" class="item">
              <a :href="a.link" target="_blank" rel="noopener" class="item-link">
                <div class="item-content">
                  <div class="icon-placeholder">📰</div>
                  <div class="item-text">
                    <span class="title">{{ a.title }}</span>
                    <span class="meta-line">{{ a.source || 'Source inconnue' }} • {{ formatDate(a.published || a.archived_at) }}</span>
                  </div>
                </div>
              </a>
            </li>
          </ul>
          <p v-else class="empty-message">Aucun article archivé pour le moment</p>
        </div>
        <div class="col">
          <h2>Vidéos</h2>
          <ul class="list" v-if="videos.length > 0">
            <li v-for="v in sortedVideos" :key="v.key" class="item">
              <a :href="v.link" target="_blank" rel="noopener" class="item-link">
                <div class="item-content">
                  <div class="icon-placeholder video-icon">▶</div>
                  <div class="item-text">
                    <span class="title">{{ v.title }}</span>
                    <span class="meta-line">{{ v.channel || v.source || 'Chaîne inconnue' }} • {{ formatDate(v.published || v.archived_at) }}</span>
                  </div>
                </div>
              </a>
            </li>
          </ul>
          <p v-else class="empty-message">Aucune vidéo archivée pour le moment</p>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import PageHero from '~/components/shared/PageHero.vue';

interface ArchiveItem {
  key: string;
  title: string;
  link: string;
  source?: string;
  published?: string;
  archived_at?: string;
  summary?: string;
  publishedTime?: number;
}

interface ArchiveVideo extends ArchiveItem {
  channel?: string;
  thumbnail?: string;
  type?: string;
}

const apiBase = 'http://localhost:5000';
const articles = ref<ArchiveItem[]>([]);
const videos = ref<ArchiveVideo[]>([]);
const loading = ref(false);
const error = ref('');
const searchQuery = ref('');

const toDateValue = (value?: string): number => {
  if (!value) return 0;
  const d = new Date(value);
  return isNaN(+d) ? 0 : d.getTime();
};

const formatDate = (iso?: string): string => {
  if (!iso) return 'Date inconnue';
  try {
    const date = new Date(iso);
    const now = new Date();
    const diffMs = now.getTime() - date.getTime();
    const diffHours = Math.floor(diffMs / (1000 * 60 * 60));
    const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));

    if (diffHours < 1) return "À l'instant";
    if (diffHours < 24) return `Il y a ${diffHours}h`;
    if (diffDays < 7) return `Il y a ${diffDays}j`;

    return date.toLocaleDateString('fr-FR', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
    });
  } catch {
    return iso.substring(0, 10);
  }
};

const filterBySearch = <T extends ArchiveItem>(items: T[], query: string): T[] => {
  if (!query.trim()) return items;
  const q = query.toLowerCase();
  return items.filter(item => 
    item.title.toLowerCase().includes(q) ||
    (item.source && item.source.toLowerCase().includes(q)) ||
    (item.summary && item.summary.toLowerCase().includes(q))
  );
};

const sortByDate = <T extends ArchiveItem>(items: T[]) => {
  return [...items].sort((a, b) => 
    (b.publishedTime || toDateValue(b.published || b.archived_at)) - 
    (a.publishedTime || toDateValue(a.published || a.archived_at))
  );
};

const filteredArticles = computed(() => {
  const filtered = filterBySearch(articles.value, searchQuery.value);
  return sortByDate(filtered);
});

const filteredVideos = computed(() => {
  const filtered = filterBySearch(videos.value, searchQuery.value);
  return sortByDate(filtered);
});

const sortedArticles = computed(() => filteredArticles.value);
const sortedVideos = computed(() => filteredVideos.value);

const handleSearch = () => {
  // La réactivité gère automatiquement le filtrage
};

const normalizeArticle = (raw: any, idx: number): ArchiveItem => {
  const published = raw?.published || raw?.pubDate || raw?.updated || '';
  return {
    key: `${raw?.link || raw?.title || 'article'}-${idx}`,
    title: raw?.title || 'Sans titre',
    link: raw?.link || '#',
    source: raw?.source || raw?.site || raw?.feed || raw?.publisher,
    published,
    archived_at: raw?.archived_at,
    summary: raw?.summary,
    publishedTime: raw?.publishedTime,
  };
};

const normalizeVideo = (raw: any, idx: number): ArchiveVideo => {
  const published = raw?.published || raw?.date || '';
  return {
    key: `${raw?.link || raw?.title || 'video'}-${idx}`,
    title: raw?.title || 'Sans titre',
    link: raw?.link || '#',
    channel: raw?.channel,
    source: raw?.source,
    published,
    archived_at: raw?.archived_at,
    summary: raw?.summary,
    publishedTime: raw?.publishedTime,
    thumbnail: raw?.thumbnail,
    type: raw?.type,
  };
};

const lastUpdated = computed(() => {
  const allDates = [
    ...articles.value.map((a) => a.archived_at || a.published || ''),
    ...videos.value.map((v) => v.archived_at || v.published || ''),
  ].filter(Boolean);
  if (allDates.length === 0) return '—';
  const latest = allDates.reduce((max, curr) => {
    const t = toDateValue(curr);
    return t > max ? t : max;
  }, 0);
  return latest ? formatDate(new Date(latest).toISOString()) : '—';
});

const loadArchive = async () => {
  loading.value = true;
  error.value = '';
  try {
    const res = await fetch(`${apiBase}/archive`, { signal: AbortSignal.timeout(8000) });
    if (!res.ok) throw new Error(`API ${res.status}`);
    const data = await res.json();

    const rawArticles = Array.isArray(data?.articles) ? data.articles : [];
    const rawVideos = Array.isArray(data?.videos) ? data.videos : [];

    articles.value = rawArticles.map((a, idx) => normalizeArticle(a, idx));
    videos.value = rawVideos.map((v, idx) => normalizeVideo(v, idx));
  } catch (e) {
    console.error(e);
    error.value = 'Erreur de chargement des archives. Veuillez réessayer.';
    articles.value = [];
    videos.value = [];
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  void loadArchive();
});
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

.header-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
  gap: 16px;
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

.meta {
  margin: 0;
  color: #2f0538;
  font-weight: 700;
}

.hint {
  margin: 4px 0 0;
  color: #777;
  font-size: 13px;
}

.state {
  background: #f8f5ff;
  border: 1px solid #e5ddff;
  border-radius: 12px;
  padding: 14px 16px;
  color: #2f0538;
}

.state.error {
  background: #fff5f5;
  border-color: #ffd6d6;
  color: #b42318;
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
}

.col h2 {
  font-size: 22px;
  font-weight: 700;
  color: #2f0538;
  margin: 0 0 18px;
  padding-bottom: 12px;
  border-bottom: 2px solid #f0f0f0;
}

.list {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.item {
  list-style: none;
  background: #fafafa;
  border: 1px solid #eee;
  border-radius: 12px;
  padding: 12px 14px;
  transition: border-color 0.18s ease, transform 0.18s ease, box-shadow 0.18s ease;
}

.item:hover {
  border-color: #d8c8ff;
  transform: translateY(-1px);
  box-shadow: 0 8px 18px rgba(0, 0, 0, 0.06);
}

.item-link {
  text-decoration: none;
  color: inherit;
  display: block;
}

.item-content {
  display: flex;
  align-items: flex-start;
  gap: 12px;
}

.icon-placeholder {
  flex-shrink: 0;
  width: 40px;
  height: 40px;
  border-radius: 8px;
  background: linear-gradient(135deg, #f0e8ff 0%, #e5d8ff 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
}

.icon-placeholder.video-icon {
  background: linear-gradient(135deg, #ffe8e8 0%, #ffd8d8 100%);
  color: #ff6b6b;
}

.item-text {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.title {
  font-weight: 700;
  color: #1f1f28;
}

.meta-line {
  color: #666;
  font-size: 13px;
}

.empty-message {
  color: #999;
  font-style: italic;
  margin: 12px 0;
}

@media (max-width: 768px) {
  .grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }

  .header-row {
    flex-direction: column;
    align-items: flex-start;
  }

  .search-wrapper {
    max-width: 100%;
  }

  .item-content {
    gap: 10px;
  }

  .icon-placeholder {
    width: 36px;
    height: 36px;
    font-size: 16px;
  }
}
</style>
