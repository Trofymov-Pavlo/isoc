<template>
  <div class="live-page">
    <div class="live-container">
      <!-- Latest item featured (most recent media) -->
      <section v-if="latestItem" class="panel panel-wide latest">
        <a :href="latestItem.link" target="_blank" class="item-card latest-card">
          <div class="item-image-container featured-image-container">
            <img v-if="latestItem.image" :src="latestItem.image" :alt="latestItem.title" class="item-image" />
            <div v-else class="item-image-placeholder">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                <circle cx="8.5" cy="8.5" r="1.5"></circle>
                <polyline points="21 15 16 10 5 21"></polyline>
              </svg>
            </div>
            <span v-if="latestItem.type === 'article'" class="media-badge article-badge">Article</span>
            <span v-else class="media-badge video-badge">Vidéo</span>
          </div>
          <div class="item-content">
            <h3 class="item-title">{{ latestItem.title }}</h3>
            <p v-if="latestItem.summary" class="item-summary">{{ truncate(latestItem.summary, 180) }}</p>
            <div class="item-meta">
              <span v-if="latestItem.source" class="meta-item source">{{ latestItem.source }}</span>
              <span class="meta-item date">{{ formatExactLiveDate(latestItem) }}</span>
            </div>
          </div>
        </a>
      </section>

      <!-- Results info -->
      <div class="results-info">
        <p v-if="filteredItems.length > 0">
          <strong>{{ filteredItems.length }}</strong> actualités des dernières 24h
        </p>
        <p v-else class="no-results">Aucune actualité trouvée</p>
      </div>

      <!-- Loading state -->
      <div v-if="isLoading" class="loading-state">
        <div class="spinner"></div>
        <p>Chargement...</p>
      </div>

      <!-- Error state -->
      <div v-else-if="error" class="error-state">
        <p>⚠️ {{ error }}</p>
        <button @click="loadData" class="retry-btn">Réessayer</button>
      </div>

      <!-- Empty state -->
      <div v-else-if="filteredItems.length === 0" class="empty-state">
        <p>Aucune actualité disponible</p>
        <button @click="loadData" class="retry-btn">Rafraîchir</button>
      </div>

      <!-- Grid -->
      <template v-else>
        <div class="items-grid">
          <a 
            v-for="item in filteredItems" 
            :key="item.link" 
            :href="item.link" 
            target="_blank" 
            class="item-card"
          >
            <div class="item-image-container">
              <img 
                v-if="item.image" 
                :src="item.image" 
                :alt="item.title"
                class="item-image"
                loading="lazy"
              />
              <div v-else class="item-image-placeholder">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                  <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                  <circle cx="8.5" cy="8.5" r="1.5"></circle>
                  <polyline points="21 15 16 10 5 21"></polyline>
                </svg>
              </div>
              <span v-if="item.type === 'article'" class="media-badge article-badge">Article</span>
              <span v-else class="media-badge video-badge">Vidéo</span>
              <button 
                class="like-btn" 
                @click.prevent.stop="toggleLike(item.link)"
                 :title="isSavedItem(item.link) ? 'Retirer' : 'Favoris'"
              >
                <svg :class="{ liked: isSavedItem(item.link) }" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
                </svg>
              </button>
            </div>
            <div class="item-content">
              <h3 class="item-title">{{ item.title }}</h3>
              <p v-if="item.summary" class="item-summary">{{ truncate(item.summary, 150) }}</p>
              <div class="item-meta">
                <span v-if="item.source" class="meta-item source">{{ item.source }}</span>
                <span class="meta-item date">{{ formatExactLiveDate(item) }}</span>
              </div>
            </div>
          </a>
        </div>

        <!-- Pagination removed: showing all items in a continuous list -->
      </template>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import { useArticles } from '~/composables/useArticles'
import { useVideos } from '~/composables/useVideos'
import { useSavedMedia } from '~/composables/useSavedMedia'
  

interface Item {
  title: string
  link: string
  published?: string | Date
  publishedTime?: number
  summary?: string
  source?: string
  image?: string
  type: 'article' | 'video'
}

const { all: articles, load: loadArticles } = useArticles()
const { all: videos, load: loadVideos } = useVideos()
const { isSaved, toggleSave } = useSavedMedia()

const isLoading = ref(true)
const error = ref('')
const refreshInterval = ref<ReturnType<typeof setInterval> | null>(null)

const toMs = (val: number | string | Date | undefined): number | undefined => {
  if (val == null) return undefined
  if (typeof val === 'number') return val < 1e12 ? val * 1000 : val
  const d = new Date(val)
  return isNaN(d.getTime()) ? undefined : d.getTime()
}

const formatExactLiveDate = (item: { published?: string | Date; publishedTime?: number }): string => {
  const ts = item.publishedTime ?? toMs(item.published)
  if (!ts) return ''
  const d = new Date(ts)
  return d
    .toLocaleString('fr-FR', {
      day: 'numeric',
      month: 'short',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    })
    .replace(',', ' ·')
}

const truncate = (text: string, length: number): string => {
  if (!text) return ''
  return text.length > length ? text.substring(0, length) + '...' : text
}

const isSavedItem = (link: string): boolean => {
  return isSaved(link)
}

const toggleLike = (link: string) => {
  toggleSave(link)
}

const allItems = computed(() => {
  const now = Date.now()
  const cutoff = now - 24 * 60 * 60 * 1000

  const liveArticles = articles.value
    .map(a => ({
      title: a.title,
      link: a.link,
      published: a.published,
      publishedTime: a.publishedTime,
      summary: a.summary,
      source: a.source,
      image: a.image,
      type: 'article' as const,
    }))
    .filter(a => (a.publishedTime ?? toMs(a.published))! >= cutoff)

  const liveVideos = videos.value
    .map(v => ({
      title: v.title,
      link: v.link,
      published: v.published,
      publishedTime: v.publishedTime,
      summary: v.summary,
      source: v.channel,
      image: v.thumbnail,
      type: 'video' as const,
    }))
    .filter(v => (v.publishedTime ?? toMs(v.published))! >= cutoff)

  return [...liveArticles, ...liveVideos].sort(
    (a, b) => (b.publishedTime ?? 0) - (a.publishedTime ?? 0),
  )
})

const latestItem = computed(() => allItems.value[0])
const restItems = computed(() => allItems.value.slice(1))
const filteredItems = computed(() => restItems.value)

const loadData = async () => {
  isLoading.value = true
  error.value = ''
  try {
    await Promise.all([loadArticles(), loadVideos()])
  } catch (err) {
    error.value = 'Erreur de chargement'
  } finally {
    isLoading.value = false
  }
}

onMounted(async () => {
  await loadData()
  refreshInterval.value = setInterval(loadData, 5 * 60 * 1000) // Refresh every 5 minutes
})

onBeforeUnmount(() => {
  if (refreshInterval.value) clearInterval(refreshInterval.value)
})
</script>

<style scoped>
.live-page {
  min-height: 100vh;
  background: #ffffff;
}

.live-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 32px 24px 48px;
}

/* Panels for featured block */
.panel {
  background: #ffffff;
  border: 1px solid #e9ecef;
  border-radius: 12px;
  box-shadow: 0 8px 20px rgba(15, 23, 42, 0.04);
  padding: 16px;
}
.panel-wide { grid-column: 1 / -1; }
.latest-card { display: block; }
/* Featured height: taller and responsive */
.featured-image-container { height: 560px; }

@media (max-width: 1024px) {
  .featured-image-container { height: 420px; }
}
@media (max-width: 768px) {
  .featured-image-container { height: 320px; }
}
@media (max-width: 540px) {
  .featured-image-container { height: 240px; }
}

.head-text h1 {
  margin: 4px 0 6px;
  font-size: 24px;
  color: #111827;
  letter-spacing: -0.2px;
}

.head-text .eyebrow {
  margin: 0;
  text-transform: uppercase;
  font-weight: 700;
  font-size: 11px;
  letter-spacing: 0.5px;
  color: #6b7280;
}

.head-text .subtitle {
  margin: 0;
  color: #4b5563;
  font-size: 14px;
}

.head-actions {
  display: flex;
  gap: 10px;
  align-items: center;
  flex-shrink: 0;
}

.pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 12px;
  border-radius: 999px;
  background: #f1f3f5;
  color: #374151;
  font-weight: 700;
  font-size: 12px;
  border: 1px solid #e5e7eb;
}

.pill.muted {
  color: #6b7280;
  background: #f8fafc;
}

.search-section {
  margin-bottom: 16px;
}

.search-wrapper {
  position: relative;
  max-width: 560px;
  margin: 0 auto;
}

.search-input {
  width: 100%;
  padding: 12px 44px 12px 14px;
  border: 1px solid #dee2e6;
  border-radius: 10px;
  font-size: 14px;
  background: #ffffff;
  transition: all 0.2s ease;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
}

.search-input:focus {
  outline: none;
  border-color: #7b5ce0;
  box-shadow: 0 0 0 3px rgba(123, 92, 224, 0.1);
}

.search-icon {
  position: absolute;
  right: 14px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: #9ca3af;
  pointer-events: none;
}

.clear-btn {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: #6b7280;
  font-size: 18px;
  cursor: pointer;
  padding: 0;
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.2s;
}

.clear-btn:hover {
  color: #ef4444;
}

.results-info {
  text-align: center;
  color: #6c757d;
  font-size: 14px;
  margin: 18px 0 26px;
}

.results-info strong {
  color: #111827;
  font-weight: 700;
}

.loading-state,
.error-state,
.empty-state {
  text-align: center;
  padding: 64px 20px;
  color: #4b5563;
  background: #ffffff;
  border: 1px solid #e9ecef;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(15, 23, 42, 0.04);
}

.spinner {
  width: 40px;
  height: 40px;
  border: 3px solid #f1f3f5;
  border-top-color: #7b5ce0;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  margin: 0 auto 16px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.retry-btn {
  margin-top: 14px;
  padding: 10px 20px;
  background: #7b5ce0;
  color: #ffffff;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 700;
  transition: all 0.2s ease;
}

.retry-btn:hover {
  background: #6848c5;
  box-shadow: 0 8px 18px rgba(123, 92, 224, 0.25);
}

.items-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 24px;
  margin: 24px 0;
}

.item-card {
  display: flex;
  flex-direction: column;
  background: white;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  overflow: hidden;
  transition: all 0.2s ease;
  text-decoration: none;
  color: inherit;
  cursor: pointer;
}

.item-card:hover {
  border-color: #7b5ce0;
  box-shadow: 0 8px 24px rgba(123, 92, 224, 0.15);
  transform: translateY(-2px);
}

.item-image-container {
  position: relative;
  width: 100%;
  height: 200px;
  background: #f8f9fa;
  overflow: hidden;
}

.item-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.item-card:hover .item-image {
  transform: scale(1.05);
}

.item-image-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #ced4da;
}

.item-image-placeholder svg {
  width: 60px;
  height: 60px;
}

.media-badge {
  position: absolute;
  top: 12px;
  left: 12px;
  font-size: 11px;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 6px;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  backdrop-filter: blur(8px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}
.article-badge { background: rgba(231, 245, 255, 0.95); color: #0066cc; }
.video-badge { background: rgba(255, 243, 191, 0.95); color: #997404; }

.like-btn {
  position: absolute;
  top: 12px;
  right: 12px;
  background: rgba(255, 255, 255, 0.95);
  border: none;
  cursor: pointer;
  padding: 8px;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  color: #dee2e6;
  transition: all 0.2s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(8px);
}
.like-btn:hover { background: white; color: #dc3545; transform: scale(1.1); }
.like-btn svg { width: 20px; height: 20px; }
.like-btn svg.liked { color: #dc3545; }

.item-content { padding: 16px; flex: 1; display: flex; flex-direction: column; gap: 12px; }
.item-title { margin: 0; font-size: 15px; font-weight: 600; color: #212529; line-height: 1.4; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.item-summary { margin: 0; font-size: 13px; color: #6c757d; line-height: 1.5; flex: 1; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
.item-meta { display: flex; gap: 12px; flex-wrap: wrap; padding-top: 8px; border-top: 1px solid #e9ecef; }
.meta-item { font-size: 12px; color: #adb5bd; }
.meta-item.source { color: #7b5ce0; font-weight: 500; }

.pagination { display: flex; justify-content: center; align-items: center; gap: 20px; padding: 40px 0; border-top: 1px solid #e9ecef; }
.pagination-btn { padding: 10px 20px; background: white; border: 1.5px solid #dee2e6; border-radius: 6px; color: #212529; font-size: 13px; font-weight: 500; cursor: pointer; transition: all 0.2s ease; }
.pagination-btn:hover:not(:disabled) { border-color: #7b5ce0; color: #7b5ce0; background: #f8f9ff; }
.pagination-btn:disabled { opacity: 0.5; cursor: not-allowed; }
.pagination-info { font-size: 13px; color: #6c757d; white-space: nowrap; }
.pagination-info strong { color: #212529; font-weight: 600; }

@media (max-width: 1024px) {
  .live-container {
    padding: 28px 18px 40px;
  }

  .page-head {
    flex-direction: column;
    align-items: flex-start;
  }

  .items-grid {
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  }
}

@media (max-width: 768px) {
  .live-container {
    padding: 22px 14px 32px;
  }

  .head-text h1 {
    font-size: 20px;
  }

  .search-wrapper {
    max-width: 100%;
  }

  .items-grid {
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  }
}

@media (max-width: 540px) {
  .page-head {
    padding: 16px;
  }

  .head-actions {
    width: 100%;
    justify-content: flex-start;
    flex-wrap: wrap;
  }

  .items-grid {
    grid-template-columns: 1fr;
  }

  .pagination {
    flex-direction: column;
    gap: 12px;
  }

  .pagination-btn {
    width: 100%;
  }
}
</style>

