<template>
  <div class="live-page">
    <!-- Live Header Section -->
    <div class="live-banner">
      <div class="banner-content">
        <div class="live-badge">
          <span class="pulse-dot"></span>
          <span>EN DIRECT</span>
        </div>
        <h1 class="banner-title">Dernières actualités</h1>
        <p class="banner-subtitle">Informations mises à jour en temps réel</p>
      </div>
    </div>

  <!-- Main content -->
    <div class="live-container">
      <div class="search-section">
        <div class="search-wrapper">
          <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <circle cx="11" cy="11" r="8"></circle>
            <path d="m21 21-4.35-4.35"></path>
          </svg>
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Rechercher dans les dernières actualités..."
            class="search-input"
            @keyup.enter="applyFilters"
          />
          <button v-if="searchQuery" @click="clearSearch" class="clear-btn">✕</button>
        </div>
      </div>

      <!-- Results info -->
      <div class="results-info">
        <p v-if="filteredItems.length > 0">
          <strong>{{ filteredItems.length }}</strong> actualités
          <span v-if="searchQuery"> pour "{{ searchQuery }}"</span>
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
        <button v-if="searchQuery" @click="clearSearch" class="retry-btn">
          Effacer la recherche
        </button>
      </div>

      <!-- Grid -->
      <template v-else>
        <div class="items-grid">
          <a 
            v-for="item in paginatedItems" 
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
              <div v-else class="item-placeholder">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                  <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                  <circle cx="8.5" cy="8.5" r="1.5"></circle>
                  <polyline points="21 15 16 10 5 21"></polyline>
                </svg>
              </div>
              <span class="badge" :class="item.type">
                {{ item.type === 'article' ? 'Article' : 'Vidéo' }}
              </span>
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
            <div class="item-info">
              <h3 class="item-title">{{ item.title }}</h3>
              <p v-if="item.summary" class="item-summary">{{ truncate(item.summary, 120) }}</p>
              <div class="item-meta">
                <span v-if="item.source" class="source">{{ item.source }}</span>
                <span class="date">{{ formatDate(item.published) }}</span>
              </div>
            </div>
          </a>
        </div>

        <!-- Pagination -->
        <div class="pagination">
          <button
            :disabled="currentPage === 1"
            @click="prevPage"
            class="pagination-btn"
          >
             ← Précédent
          </button>

          <div class="pagination-info">
             Page <strong>{{ currentPage }}</strong> / <strong>{{ totalPages }}</strong>
          </div>

          <button
            :disabled="currentPage === totalPages"
            @click="nextPage"
            class="pagination-btn"
          >
             Suivant →
          </button>
        </div>
      </template>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import { useArticles } from '~/composables/useArticles'
import { useVideos } from '~/composables/useVideos'
import { useSavedMedia } from '~/composables/useSavedMedia'

const ITEMS_PER_PAGE = [10, 20, 50, 100]

interface MediaItem {
  title: string
  link: string
  published: string | Date
  summary?: string
  description?: string
  source?: string
  image?: string
  thumbnail?: string
  type: 'article' | 'video'
}

interface Item {
  title: string
  link: string
  published: string | Date
  summary?: string
  source?: string
  image?: string
  type: 'article' | 'video'
}

const { all: articles, load: loadArticles } = useArticles()
const { all: videos, load: loadVideos } = useVideos()
const { isSaved, toggleSave } = useSavedMedia()

const searchQuery = ref('')
const currentPage = ref(1)
const itemsPerPage = 20
const isLoading = ref(true)
const error = ref('')
const refreshInterval = ref<NodeJS.Timer>()

const is24HoursOld = (dateString: string | Date): boolean => {
  const date = new Date(dateString)
  const now = new Date()
  const diffHours = (now.getTime() - date.getTime()) / (1000 * 60 * 60)
  return diffHours <= 24
}

const formatDate = (date: string | Date): string => {
  const d = new Date(date)
  const now = new Date()
  const diffMs = now.getTime() - d.getTime()
  const diffMins = Math.floor(diffMs / (1000 * 60))
  const diffHours = Math.floor(diffMs / (1000 * 60 * 60))

  if (diffMins < 1) return 'À l\'instant'
  if (diffMins < 60) return `${diffMins}m`
  if (diffHours < 24) return `${diffHours}h`
  return d.toLocaleDateString('fr-FR')
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
  const liveArticles = articles.value
    .filter(a => is24HoursOld(a.published))
    .map(a => ({
      title: a.title,
      link: a.link,
      published: a.published,
      summary: a.summary,
      source: a.source,
      image: a.image,
      type: 'article' as const,
    }))

  const liveVideos = videos.value
    .filter(v => is24HoursOld(v.publishedTime))
    .map(v => ({
      title: v.title,
      link: v.link,
      published: v.publishedTime,
      summary: v.description,
      source: v.channelName,
      image: v.thumbnail,
      type: 'video' as const,
    }))

  return [...liveArticles, ...liveVideos].sort(
    (a, b) => new Date(b.published).getTime() - new Date(a.published).getTime(),
  )
})

const filteredItems = computed(() => {
  if (!searchQuery.value.trim()) return allItems.value

  const query = searchQuery.value.toLowerCase()
  return allItems.value.filter(item =>
    item.title.toLowerCase().includes(query) ||
    (item.summary && item.summary.toLowerCase().includes(query)) ||
    (item.source && item.source.toLowerCase().includes(query)),
  )
})

const paginatedItems = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  return filteredItems.value.slice(start, start + itemsPerPage)
})

const totalPages = computed(() => {
  return Math.ceil(filteredItems.value.length / itemsPerPage.value)
})

const clearSearch = () => {
  searchQuery.value = ''
  currentPage.value = 1
}

const applyFilters = () => {
  currentPage.value = 1
}

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
}

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
}

const loadData = async () => {
  isLoading.value = true
  error.value = ''
  try {
    await Promise.all([loadArticles('all'), loadVideos('all')])
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

.live-banner {
  background: linear-gradient(135deg, #dc3545 0%, #b81528 100%);
  color: white;
  padding: 48px 32px;
  text-align: center;
  border-bottom: 2px solid #a01222;
}

.banner-content {
  max-width: 1200px;
  margin: 0 auto;
}

.live-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.15);
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 16px;
}

.pulse-dot {
  width: 8px;
  height: 8px;
  background: #ffeb3b;
  border-radius: 50%;
  animation: pulse-live 2s infinite;
}

@keyframes pulse-live {
  0%, 100% {
    opacity: 1;
    transform: scale(1);
  }
  50% {
    opacity: 0.6;
    transform: scale(1.3);
  }
}

.banner-title {
  font-size: 40px;
  font-weight: 700;
  margin: 0 0 16px 0;
  letter-spacing: -0.5px;
}

.banner-subtitle {
  font-size: 16px;
  opacity: 0.9;
  margin: 0 0 8px 0;
}

.last-update {
  font-size: 13px;
  opacity: 0.8;
  margin: 0;
}

.live-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 40px 32px;
}

.search-section {
  margin-bottom: 32px;
}

.search-wrapper {
  position: relative;
  max-width: 600px;
  margin: 0 auto 24px;
}

.search-input {
  width: 100%;
  padding: 14px 40px 14px 16px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 15px;
  background: #f8f9fa;
  transition: all 0.3s ease;
}

.search-input:focus {
  outline: none;
  border-color: #dc3545;
  background: white;
  box-shadow: 0 2px 12px rgba(220, 53, 69, 0.1);
}

.search-icon {
  position: absolute;
  right: 14px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: #999;
  pointer-events: none;
}

.clear-btn {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: #666;
  font-size: 20px;
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
  color: #dc3545;
}

.results-info {
  text-align: center;
  color: #666;
  font-size: 14px;
  margin-bottom: 32px;
}

.results-info strong {
  color: #212529;
  font-weight: 600;
}

.loading-state {
  text-align: center;
  padding: 60px 20px;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 3px solid #f0f0f0;
  border-top-color: #dc3545;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  margin: 0 auto 16px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error-state,
.empty-state {
  text-align: center;
  padding: 60px 20px;
  color: #666;
}

.retry-btn {
  margin-top: 16px;
  padding: 10px 24px;
  background: #dc3545;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s;
}

.retry-btn:hover {
  background: #b81528;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(220, 53, 69, 0.3);
}

.items-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 24px;
  margin-bottom: 48px;
}

.item-card {
  display: flex;
  flex-direction: column;
  border-radius: 12px;
  overflow: hidden;
  background: white;
  border: 1px solid #e0e0e0;
  transition: all 0.3s ease;
  text-decoration: none;
  color: inherit;
  cursor: pointer;
}

.item-card:hover {
  border-color: #dc3545;
  box-shadow: 0 8px 24px rgba(220, 53, 69, 0.15);
  transform: translateY(-4px);
}

.item-image-container {
  position: relative;
  width: 100%;
  aspect-ratio: 16/9;
  background: linear-gradient(135deg, #f0f0f0, #e0e0e0);
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
  color: #ccc;
}

.item-image-placeholder svg {
  width: 40px;
  height: 40px;
}

.media-badge {
  position: absolute;
  top: 12px;
  left: 12px;
  padding: 4px 12px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  z-index: 2;
}

.article-badge {
  background: #2f0538;
  color: white;
}

.video-badge {
  background: #dc3545;
  color: white;
}

.like-btn {
  position: absolute;
  top: 12px;
  right: 12px;
  width: 40px;
  height: 40px;
  background: rgba(255, 255, 255, 0.9);
  border: none;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s;
  z-index: 3;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.like-btn:hover {
  background: white;
  box-shadow: 0 4px 12px rgba(220, 53, 69, 0.3);
  transform: scale(1.1);
}

.like-btn svg {
  width: 22px;
  height: 22px;
  color: #dc3545;
  transition: transform 0.3s;
}

.like-btn svg.liked {
  color: #dc3545;
  filter: drop-shadow(0 0 4px rgba(220, 53, 69, 0.4));
}

.item-content {
  padding: 16px;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.item-title {
  font-size: 15px;
  font-weight: 600;
  margin: 0 0 8px 0;
  color: #212529;
  line-height: 1.4;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.item-summary {
  font-size: 13px;
  color: #666;
  margin: 0 0 12px 0;
  line-height: 1.4;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  flex: 1;
}

.item-meta {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  font-size: 12px;
  color: #999;
  margin-top: auto;
}

.meta-item {
  padding: 4px 8px;
  background: #f8f9fa;
  border-radius: 4px;
}

.pagination {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 32px 0;
  flex-wrap: wrap;
}

.pagination-btn {
  padding: 10px 20px;
  background: #2f0538;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s;
  font-size: 14px;
}

.pagination-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.pagination-btn:not(:disabled):hover {
  background: #dc3545;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(220, 53, 69, 0.3);
}

.pagination-logo {
  display: flex;
  align-items: center;
  justify-content: center;
}

.pagination-logo-img {
  height: 40px;
  width: auto;
  opacity: 0.7;
  transition: opacity 0.3s;
}

.pagination-logo-img:hover {
  opacity: 1;
}

.pagination-info {
  font-size: 14px;
  color: #666;
  white-space: nowrap;
}

@media (max-width: 1024px) {
  .items-grid {
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  }
  
  .banner-title {
    font-size: 32px;
  }
}

@media (max-width: 768px) {
  .live-banner {
    padding: 32px 20px;
  }
  
  .banner-title {
    font-size: 24px;
  }
  
  .banner-subtitle,
  .last-update {
    font-size: 14px;
  }
  
  .live-container {
    padding: 24px 16px;
  }
  
  .items-grid {
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 16px;
  }
  
  .pagination {
    gap: 16px;
  }
  
  .pagination-btn {
    padding: 8px 16px;
    font-size: 13px;
  }
}

@media (max-width: 480px) {
  .live-banner {
    padding: 24px 16px;
  }
  
  .banner-title {
    font-size: 20px;
  }
  
  .live-badge {
    font-size: 12px;
  }
  
  .banner-subtitle {
    display: none;
  }
  
  .live-container {
    padding: 16px;
  }
  
  .search-input {
    font-size: 14px;
    padding: 12px 36px 12px 14px;
  }
  
  .items-grid {
    grid-template-columns: 1fr;
    gap: 12px;
  }
  
  .pagination {
    flex-direction: column;
    gap: 12px;
  }
  
  .pagination-btn {
    width: 100%;
  }
  
  .pagination-info {
    text-align: center;
  }
}
</style>

