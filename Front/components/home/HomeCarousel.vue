<template>
  <section class="carousel-container">
    <div class="carousel">
      <div class="carousel-inner">
        <div
          v-for="(image, idx) in slides"
          :key="idx"
          :class="['carousel-item', { active: idx === activeIndex }]"
        >
          <a :href="image.link" target="_blank" rel="noopener" class="carousel-image-link">
            <img
              v-if="imageUrl(image)"
              :src="imageUrl(image)"
              :alt="image.title"
              class="carousel-image"
              @error="handleImageError(idx)"
            />
            <div v-else class="carousel-placeholder">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                <circle cx="8.5" cy="8.5" r="1.5"></circle>
                <polyline points="21 15 16 10 5 21"></polyline>
              </svg>
            </div>
          </a>

          <div class="carousel-overlay"></div>

          <div class="carousel-content">
            <div class="tagline-chip">
              <span class="pulse-dot"></span>
              <span>Média indépendant | Conflit Ukraine-Russie</span>
            </div>
          </div>
          <div class="carousel-bottom">
            <a :href="image.link" target="_blank" rel="noopener" class="image-title">
              {{ image.title }}
            </a>
            <p v-if="image.sourceName" class="image-source">{{ image.sourceName }}</p>
          </div>
        </div>
      </div>

      <button class="carousel-arrow prev" @click="prevSlide" aria-label="Image précédente">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
      </button>
      <button class="carousel-arrow next" @click="nextSlide" aria-label="Image suivante">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="9 18 15 12 9 6"></polyline>
        </svg>
      </button>

      <div class="carousel-pagination">
        <button
          v-for="(_, idx) in slides"
          :key="idx"
          :class="['dot', { active: idx === activeIndex }]"
          @click="goToSlide(idx)"
          :aria-label="`Aller à l'image ${idx + 1}`"
        ></button>
      </div>

      <div class="explore-overlay">
        <div class="explore-search">
          <div class="search-input-group">
            <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="11" cy="11" r="8"></circle>
              <path d="m21 21-4.35-4.35"></path>
            </svg>
            <input
              v-model="exploreSearch"
              type="text"
              placeholder="Rechercher articles, vidéos..."
              class="search-input"
              @keyup.enter="performSearch"
            />
          </div>
          <div class="explore-filters">
            <select v-model="exploreType" class="filter-select">
              <option value="all">Tous les médias</option>
              <option value="articles">Articles</option>
              <option value="videos">Vidéos</option>
            </select>
            <select v-model="exploreDate" class="filter-select">
              <option value="today">Aujourd'hui</option>
              <option value="week">Cette semaine</option>
              <option value="month">Ce mois-ci</option>
              <option value="3months">3 derniers mois</option>
              <option value="6months">6 derniers mois</option>
              <option value="year">Cette année</option>
              <option value="all">Toutes les dates</option>
            </select>
            <button class="explore-btn" @click="goExplore">Explorer</button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import { useArticles } from '@/composables/useArticles'
import { useVideos } from '@/composables/useVideos'

const { all: articles, load: loadArticles } = useArticles()
const { all: videos, load: loadVideos } = useVideos()

type Slide = {
  source: 'article' | 'video'
  title: string
  image?: string
  thumbnail?: string
  link?: string
  sourceName?: string
}

const activeIndex = ref(0)
const exploreSearch = ref('')
const exploreType = ref<'all' | 'articles' | 'videos'>('all')
const exploreDate = ref<'today' | 'week' | 'month' | '3months' | '6months' | 'year' | 'all'>('today')

let autoplayInterval: ReturnType<typeof setInterval> | null = null

const baseSlides = computed<Slide[]>(() => {
  const arts = articles.value
    .filter(a => !!a.image)
    .map(a => ({ source: 'article' as const, title: a.title, image: a.image!, link: a.link, sourceName: a.source }))
  const vids = videos.value
    .filter(v => !!v.thumbnail)
    .map(v => ({ source: 'video' as const, title: v.title, thumbnail: v.thumbnail, link: v.link, sourceName: v.channel }))
  return [...arts, ...vids]
})

const slides = ref<Slide[]>([])

function nextSlide() {
  if (!slides.value.length) return
  activeIndex.value = (activeIndex.value + 1) % slides.value.length
  resetAutoplay()
}

function prevSlide() {
  if (!slides.value.length) return
  activeIndex.value = (activeIndex.value - 1 + slides.value.length) % slides.value.length
  resetAutoplay()
}

function goToSlide(idx: number) {
  if (!slides.value.length) return
  activeIndex.value = idx
  resetAutoplay()
}

function imageUrl(slide: Slide): string | undefined {
  return slide.image ?? slide.thumbnail
}

function resetAutoplay() {
  if (autoplayInterval) {
    clearInterval(autoplayInterval)
  }
  startAutoplay()
}

function startAutoplay() {
  if (autoplayInterval) clearInterval(autoplayInterval)
  if (slides.value.length <= 1) return
  autoplayInterval = setInterval(() => {
    activeIndex.value = (activeIndex.value + 1) % slides.value.length
  }, 7000)
}

function performSearch() {
  goExplore()
}

function goExplore() {
  const params = new URLSearchParams()
  params.set('type', exploreType.value)
  params.set('date', exploreDate.value)
  if (exploreSearch.value.trim()) {
    params.set('q', exploreSearch.value.trim())
  }
  navigateTo(`/explorer?${params.toString()}`)
}

function handleImageError(idx: number) {
  slides.value.splice(idx, 1)
  if (activeIndex.value >= slides.value.length) activeIndex.value = 0
}

function loadImage(url: string): Promise<HTMLImageElement> {
  return new Promise((resolve, reject) => {
    const img = new Image()
    img.crossOrigin = 'anonymous'
    img.onload = () => resolve(img)
    img.onerror = reject
    img.src = url
  })
}

function detectTextPresence(img: HTMLImageElement): boolean {
  const minW = 320
  const minH = 200
  if (img.naturalWidth < minW || img.naturalHeight < minH) return true

  const canvas = document.createElement('canvas')
  const size = 64
  canvas.width = size
  canvas.height = size
  const ctx = canvas.getContext('2d')
  if (!ctx) return false
  ctx.drawImage(img, 0, 0, size, size)

  let data: Uint8ClampedArray
  try {
    data = ctx.getImageData(0, 0, size, size).data
  } catch {
    return false
  }

  let edgeCount = 0
  let total = 0
  for (let y = 0; y < size; y++) {
    for (let x = 1; x < size; x++) {
      const idx = (y * size + x) * 4
      const idxPrev = (y * size + (x - 1)) * 4
      const lum = 0.299 * data[idx]! + 0.587 * data[idx + 1]! + 0.114 * data[idx + 2]!
      const lumPrev = 0.299 * data[idxPrev]! + 0.587 * data[idxPrev + 1]! + 0.114 * data[idxPrev + 2]!
      if (Math.abs(lum - lumPrev) > 38) edgeCount++
      total++
    }
  }
  const edgeDensity = edgeCount / total
  return edgeDensity > 0.28
}

async function isUsableImage(url?: string): Promise<boolean> {
  if (!url) return false
  try {
    const img = await loadImage(url)
    return !detectTextPresence(img)
  } catch {
    return false
  }
}

async function refreshSlides() {
  const candidates = baseSlides.value
  const checked: Slide[] = []
  for (const s of candidates) {
    const url = imageUrl(s)
    if (!url) continue
    if (await isUsableImage(url)) {
      checked.push(s)
    }
    if (checked.length >= 8) break
  }
  slides.value = checked
  activeIndex.value = 0
  startAutoplay()
}

onMounted(() => {
  loadArticles()
  loadVideos()
  refreshSlides()
})

onUnmounted(() => {
  if (autoplayInterval) {
    clearInterval(autoplayInterval)
  }
})

watch(baseSlides, () => {
  refreshSlides()
})
</script>

<style scoped>
* { box-sizing: border-box; }

.carousel-container {
  width: 100vw;
  margin-left: calc(50% - 50vw);
  background: #000;
}

.carousel {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
  background: #000;
}

.carousel-inner { position: relative; width: 100%; height: 100%; }

.carousel-item {
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity 0.8s ease-in-out;
}

.carousel-item.active { opacity: 1; z-index: 10; }

.carousel-image-link {
  display: block;
  width: 100%;
  height: 100%;
  text-decoration: none;
  cursor: pointer;
}

.carousel-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
}

.carousel-placeholder {
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #0f172a, #1f2937);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.carousel-placeholder svg { width: 80px; height: 80px; opacity: 0.5; }

.carousel-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.15) 40%, rgba(0,0,0,0.65) 100%);
  pointer-events: none;
}

.carousel-content {
  position: absolute;
  top: 40px;
  left: 50%;
  transform: translateX(-50%);
  color: #ffffff;
  z-index: 20;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.tagline-chip {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.16);
  padding: 6px 12px;
  border-radius: 999px;
  backdrop-filter: blur(8px);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.2px;
}

.pulse-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #ff6b6b;
  box-shadow: 0 0 0 6px rgba(255, 107, 107, 0.16);
  animation: pulse 1.8s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; box-shadow: 0 0 0 6px rgba(255, 107, 107, 0.16); }
  50% { opacity: 0.6; box-shadow: 0 0 0 12px rgba(255, 107, 107, 0.08); }
}

.carousel-bottom {
  position: absolute;
  bottom: 120px;
  left: 0;
  right: 0;
  padding: 0 48px;
  z-index: 20;
  text-align: left;
}

.image-title {
  display: block;
  font-size: 20px;
  font-weight: 700;
  max-width: 100%;
  color: #ffffff;
  text-decoration: none;
  line-height: 1.4;
  text-shadow: 0 8px 20px rgba(0, 0, 0, 0.6);
  transition: color 0.2s ease;
  margin-bottom: 6px;
}

.image-title:hover { color: #f5f5f5; }

.image-source {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.8);
  font-weight: 500;
  margin: 0;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
}

.carousel-arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 30;
  width: 52px;
  height: 52px;
  border: none;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.16);
  color: #ffffff;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  backdrop-filter: blur(10px);
  transition: all 0.2s ease;
}

.carousel-arrow:hover { background: rgba(255, 255, 255, 0.26); }

.carousel-arrow svg { width: 22px; height: 22px; }

.carousel-arrow.prev { left: 20px; }
.carousel-arrow.next { right: 20px; }

.carousel-pagination {
  position: absolute;
  bottom: 26px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 10px;
  z-index: 30;
}

.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  border: 1px solid rgba(255,255,255,0.5);
  background: rgba(255, 255, 255, 0.28);
  cursor: pointer;
  transition: all 0.2s ease;
}

.dot.active { background: #ffffff; transform: scale(1.15); }

.explore-overlay {
  position: absolute;
  top: 85px;
  left: 50%;
  transform: translateX(-50%);
  width: min(280px, 45vw);
  padding: 6px 8px;
  background: rgba(0, 0, 0, 0.65);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 10px;
  z-index: 25;
}

.explore-search {
  display: flex;
  flex-direction: column;
  gap: 6px;
  align-items: stretch;
}

.search-input-group {
  position: relative;
  width: 100%;
}

.search-icon {
  position: absolute;
  left: 10px;
  top: 50%;
  transform: translateY(-50%);
  width: 14px;
  height: 14px;
  color: #cbd5e1;
  pointer-events: none;
}

.search-input {
  width: 100%;
  padding: 6px 8px 6px 28px;
  border: 1px solid rgba(255, 255, 255, 0.35);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.12);
  color: #ffffff;
  font-size: 11px;
  height: 30px;
  line-height: 1;
  box-sizing: border-box;
}

.search-input::placeholder { color: #cbd5e1; }

.explore-filters {
  display: grid;
  grid-template-columns: 1fr 1fr auto;
  gap: 6px;
  align-items: center;
}

.filter-select {
  padding: 6px 8px;
  border-radius: 8px;
  border: 1px solid rgba(255,255,255,0.35);
  background: rgba(255,255,255,0.12);
  color: #ffffff;
  font-size: 11px;
  height: 30px;
  line-height: 1;
  box-sizing: border-box;
  cursor: pointer;
}

.filter-select option {
  background: #1a1a1a;
  color: #ffffff;
}

.explore-btn {
  padding: 6px 8px;
  border-radius: 8px;
  border: none;
  background: linear-gradient(120deg, #6d5dd3, #8c7cff);
  color: #ffffff;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 6px 16px rgba(109, 93, 211, 0.4);
  font-size: 11px;
  white-space: nowrap;
  height: 30px;
  line-height: 1;
  box-sizing: border-box;
  display: flex;
  align-items: center;
  justify-content: center;
}

@media (max-width: 900px) {
  .carousel { height: 80vh; }
  .carousel-content { top: 40px; gap: 6px; }
  .carousel-bottom { bottom: 90px; padding: 0 24px; }
  .image-title { font-size: 18px; }
  .explore-overlay { top: 80px; left: 50%; transform: translateX(-50%); padding: 6px 8px; width: 90vw; }
  .explore-filters { grid-template-columns: 1fr; }
}

@media (max-width: 540px) {
  .carousel { height: 68vh; }
  .carousel-arrow { width: 42px; height: 42px; }
  .carousel-pagination { bottom: 16px; }
  .carousel-bottom { bottom: 70px; padding: 0 20px; }
  .image-title { font-size: 16px; }
  .image-source { font-size: 11px; }
  .explore-overlay { top: 75px; left: 50%; transform: translateX(-50%); width: 92vw; }
  .explore-btn { width: 100%; }
}
</style>
