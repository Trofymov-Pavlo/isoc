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
  // Vérifier la résolution minimale (meilleure qualité)
  const minW = 450
  const minH = 300
  if (img.naturalWidth < minW || img.naturalHeight < minH) return true

  const canvas = document.createElement('canvas')
  const size = 150
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

  // Convertir en niveaux de gris
  const gray: number[] = []
  for (let i = 0; i < data.length; i += 4) {
    const lum = 0.299 * data[i]! + 0.587 * data[i + 1]! + 0.114 * data[i + 2]!
    gray.push(lum)
  }

  // Détection simple de contours
  let edgeCount = 0
  const edgeThreshold = 45

  for (let y = 1; y < size - 1; y++) {
    for (let x = 1; x < size - 1; x++) {
      const idx = y * size + x
      const gx = Math.abs(gray[idx + 1]! - gray[idx - 1]!)
      const gy = Math.abs(gray[idx + size]! - gray[idx - size]!)
      
      if (gx > edgeThreshold || gy > edgeThreshold) edgeCount++
    }
  }

  const totalPixels = (size - 2) * (size - 2)
  const edgeDensity = edgeCount / totalPixels

  // Rejeter seulement si vraiment beaucoup de contours (texte évident)
  if (edgeDensity > 0.25) return true

  // Analyse de variance pour détecter zones de texte
  const blockSize = 10
  let highVarianceBlocks = 0
  let totalBlocks = 0

  for (let by = 0; by < size; by += blockSize) {
    for (let bx = 0; bx < size; bx += blockSize) {
      let sum = 0
      let sumSq = 0
      let count = 0

      for (let y = by; y < Math.min(by + blockSize, size); y++) {
        for (let x = bx; x < Math.min(bx + blockSize, size); x++) {
          const val = gray[y * size + x]!
          sum += val
          sumSq += val * val
          count++
        }
      }

      if (count > 0) {
        const mean = sum / count
        const variance = (sumSq / count) - (mean * mean)
        if (variance > 1800) highVarianceBlocks++
        totalBlocks++
      }
    }
  }

  const varianceRatio = highVarianceBlocks / totalBlocks
  
  // Score combiné - être sélectif mais pas trop
  return edgeDensity > 0.18 && varianceRatio > 0.30
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
  
  // Afficher immédiatement les premières images sans attendre la validation
  const immediate = candidates.filter(s => imageUrl(s)).slice(0, 5)
  if (immediate.length > 0) {
    slides.value = immediate
    activeIndex.value = 0
    startAutoplay()
  }
  
  // Puis filtrer en arrière-plan et remplacer
  const checked: Slide[] = []
  const fallback: Slide[] = []
  
  for (const s of candidates) {
    const url = imageUrl(s)
    if (!url) continue
    
    if (fallback.length < 10) {
      fallback.push(s)
    }
    
    if (await isUsableImage(url)) {
      checked.push(s)
    }
    if (checked.length >= 8) break
  }
  
  // Remplacer par les images validées seulement si elles sont différentes
  const validatedSlides = checked.length > 0 ? checked : fallback.slice(0, 5)
  const currentLinks = slides.value.map(s => s.link).join(',')
  const validatedLinks = validatedSlides.map(s => s.link).join(',')
  
  // Ne remplacer que si la liste est vraiment différente
  if (currentLinks !== validatedLinks) {
    // Garder l'index actuel pour éviter le saut visuel
    const currentIndex = activeIndex.value
    slides.value = validatedSlides
    // Ajuster l'index si nécessaire
    if (currentIndex >= slides.value.length) {
      activeIndex.value = 0
    }
  }
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

@media (max-width: 900px) {
  .carousel { height: 80vh; }
  .carousel-content { top: 40px; gap: 6px; }
  .carousel-bottom { bottom: 90px; padding: 0 24px; }
  .image-title { font-size: 18px; }
}

@media (max-width: 540px) {
  .carousel { height: 68vh; }
  .carousel-arrow { width: 42px; height: 42px; }
  .carousel-pagination { bottom: 16px; }
  .carousel-bottom { bottom: 70px; padding: 0 20px; }
  .image-title { font-size: 16px; }
  .image-source { font-size: 11px; }
}
</style>
