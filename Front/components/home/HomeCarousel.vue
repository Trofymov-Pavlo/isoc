<template>
  <section class="carousel-container">
    <!-- Tagline -->
    <div class="carousel-tagline">
      <span class="pulse-dot"></span>
      <span class="tagline-text">Média indépendant | Conflit Ukraine-Russie</span>
    </div>

    <!-- Main carousel -->
    <div class="carousel">
      <!-- Images wrapper -->
      <div class="carousel-inner">
        <div
          v-for="(image, idx) in currentSlides"
          :key="idx"
          :class="['carousel-item', { active: idx === activeIndex }]"
        >
          <img
            v-if="image.source === 'article' && image.image"
            :src="image.image"
            :alt="image.title"
            class="carousel-image"
            @error="handleImageError"
          />
          <img
            v-else-if="image.source === 'video' && image.thumbnail"
            :src="image.thumbnail"
            :alt="image.title"
            class="carousel-image"
            @error="handleImageError"
          />
          <div v-else class="carousel-placeholder">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
              <circle cx="8.5" cy="8.5" r="1.5"></circle>
              <polyline points="21 15 16 10 5 21"></polyline>
            </svg>
          </div>

          <!-- Overlay gradient -->
          <div class="carousel-overlay"></div>

          <!-- Content on image -->
          <div class="carousel-content">
            <a :href="image.link" target="_blank" rel="noopener" class="image-title">
              {{ image.title }}
            </a>
          </div>
        </div>
      </div>

      <!-- Navigation arrows -->
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

      <!-- Pagination dots -->
      <div class="carousel-pagination">
        <button
          v-for="(_, idx) in images"
          :key="idx"
          :class="['dot', { active: idx === activeIndex }]"
          @click="goToSlide(idx)"
          :aria-label="`Aller à l'image ${idx + 1}`"
        ></button>
      </div>
    </div>

    <!-- Explore section below carousel -->
    <div class="explore-section">
      <h2>Explorez les médias</h2>
      <div class="explore-content">
        <!-- Search bar -->
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

          <!-- Filters -->
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
          </div>

          <!-- Explore button -->
          <button class="explore-btn" @click="goExplore">Explorer</button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useArticles } from '@/composables/useArticles'
import { useVideos } from '@/composables/useVideos'

const { all: articles, load: loadArticles } = useArticles()
const { all: videos, load: loadVideos } = useVideos()

const activeIndex = ref(0)
const exploreSearch = ref('')
const exploreType = ref<'all' | 'articles' | 'videos'>('all')
const exploreDate = ref<'today' | 'week' | 'month' | '3months' | '6months' | 'year' | 'all'>('today')

let autoplayInterval: NodeJS.Timeout | null = null

// Merge and prepare images
const images = computed(() => {
  const arts = articles.value.map(a => ({
    source: 'article' as const,
    title: a.title,
    image: a.image,
    thumbnail: undefined,
    link: a.link,
  }))
  const vids = videos.value.map(v => ({
    source: 'video' as const,
    title: v.title,
    image: undefined,
    thumbnail: v.thumbnail,
    link: v.link,
  }))
  return [...arts, ...vids]
    .sort(() => Math.random() - 0.5) // Shuffle for variety
    .slice(0, 8) // Take first 8
})

const currentSlides = computed(() => {
  // Return all images as the carousel items
  return images.value
})

function nextSlide() {
  activeIndex.value = (activeIndex.value + 1) % images.value.length
  resetAutoplay()
}

function prevSlide() {
  activeIndex.value = (activeIndex.value - 1 + images.value.length) % images.value.length
  resetAutoplay()
}

function goToSlide(idx: number) {
  activeIndex.value = idx
  resetAutoplay()
}

function handleImageError(event: Event) {
  const img = event.target as HTMLImageElement
  img.style.display = 'none'
}

function resetAutoplay() {
  if (autoplayInterval) {
    clearInterval(autoplayInterval)
  }
  startAutoplay()
}

function startAutoplay() {
  // Auto-advance every 3 seconds
  autoplayInterval = setInterval(() => {
    activeIndex.value = (activeIndex.value + 1) % images.value.length
  }, 3000)
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

onMounted(() => {
  loadArticles()
  loadVideos()
  startAutoplay()
})

onUnmounted(() => {
  if (autoplayInterval) {
    clearInterval(autoplayInterval)
  }
})
</script>

<style scoped>
* {
  box-sizing: border-box;
}

.carousel-container {
  width: 100%;
  background: #ffffff;
}

/* Tagline bar */
.carousel-tagline {
  background: #f1f3f5;
  border-bottom: 1px solid #e5e7eb;
  padding: 10px 40px;
  font-size: 12px;
  display: flex;
  align-items: center;
  gap: 10px;
  color: #343a40;
}

.pulse-dot {
  width: 7px;
  height: 7px;
  background: #dc3545;
  border-radius: 50%;
  flex-shrink: 0;
  animation: pulse-animation 2s ease-in-out infinite;
}

@keyframes pulse-animation {
  0%, 100% {
    opacity: 1;
    box-shadow: 0 0 0 3px rgba(220, 53, 69, 0.2);
  }
  50% {
    opacity: 0.7;
    box-shadow: 0 0 0 8px rgba(220, 53, 69, 0.1);
  }
}

.tagline-text {
  color: #2d2f33;
  font-weight: 600;
  letter-spacing: 0.3px;
}

/* Carousel */
.carousel {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
  background: #000;
}

.carousel-inner {
  position: relative;
  width: 100%;
  height: 100%;
}

.carousel-item {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 0.8s ease-in-out;
  display: flex;
  align-items: center;
  justify-content: center;
}

.carousel-item.active {
  opacity: 1;
  z-index: 10;
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
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.carousel-placeholder svg {
  width: 80px;
  height: 80px;
  opacity: 0.5;
}

.carousel-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(180deg, rgba(0, 0, 0, 0.3) 0%, transparent 50%, rgba(0, 0, 0, 0.4) 100%);
  pointer-events: none;
}

.carousel-content {
  position: absolute;
  bottom: 60px;
  left: 0;
  right: 0;
  padding: 0 40px;
  z-index: 20;
  text-align: left;
}

.image-title {
  display: block;
  color: white;
  font-size: 28px;
  font-weight: 700;
  text-decoration: none;
  max-width: 800px;
  line-height: 1.3;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
  transition: all 0.2s ease;
}

.image-title:hover {
  color: #e8e8e8;
}

/* Navigation arrows */
.carousel-arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 30;
  width: 50px;
  height: 50px;
  background: rgba(255, 255, 255, 0.2);
  border: none;
  border-radius: 50%;
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
}

.carousel-arrow:hover {
  background: rgba(255, 255, 255, 0.3);
}

.carousel-arrow svg {
  width: 24px;
  height: 24px;
}

.carousel-arrow.prev {
  left: 20px;
}

.carousel-arrow.next {
  right: 20px;
}

/* Pagination dots */
.carousel-pagination {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 30;
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  justify-content: center;
  max-width: 400px;
}

.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.4);
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  padding: 0;
}

.dot.active {
  background: white;
  transform: scale(1.2);
}

.dot:hover {
  background: rgba(255, 255, 255, 0.7);
}

/* Explore section */
.explore-section {
  background: #ffffff;
  padding: 80px 40px;
  text-align: center;
}

.explore-section h2 {
  font-size: 32px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 40px 0;
}

.explore-content {
  max-width: 900px;
  margin: 0 auto;
}

.explore-search {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}

.search-input-group {
  flex: 1;
  min-width: 250px;
  position: relative;
  display: flex;
  align-items: center;
}

.search-icon {
  position: absolute;
  left: 14px;
  width: 18px;
  height: 18px;
  color: #adb5bd;
  pointer-events: none;
}

.search-input {
  width: 100%;
  padding: 12px 14px 12px 40px;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  font-size: 14px;
  background: #ffffff;
  color: #212529;
  transition: all 0.2s ease;
}

.search-input:focus {
  outline: none;
  border-color: #7b5ce0;
  box-shadow: 0 0 0 3px rgba(123, 92, 224, 0.1);
}

.search-input::placeholder {
  color: #adb5bd;
}

.explore-filters {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.filter-select {
  padding: 10px 14px;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  font-size: 14px;
  background: #ffffff;
  color: #212529;
  cursor: pointer;
  transition: all 0.2s ease;
}

.filter-select:focus {
  outline: none;
  border-color: #7b5ce0;
  box-shadow: 0 0 0 3px rgba(123, 92, 224, 0.1);
}

.explore-btn {
  padding: 12px 28px;
  background: #7b5ce0;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.explore-btn:hover {
  background: #6a4bc9;
  box-shadow: 0 4px 12px rgba(123, 92, 224, 0.3);
}

/* Responsive */
@media (max-width: 768px) {
  .carousel-tagline {
    padding: 8px 16px;
    font-size: 11px;
    gap: 8px;
  }

  .carousel {
    height: 70vh;
  }

  .carousel-arrow {
    width: 40px;
    height: 40px;
  }

  .carousel-arrow.prev {
    left: 10px;
  }

  .carousel-arrow.next {
    right: 10px;
  }

  .carousel-content {
    padding: 0 20px;
    bottom: 40px;
  }

  .image-title {
    font-size: 18px;
  }

  .explore-section {
    padding: 40px 20px;
  }

  .explore-section h2 {
    font-size: 24px;
    margin-bottom: 30px;
  }

  .explore-search {
    flex-direction: column;
  }

  .search-input-group {
    min-width: unset;
    width: 100%;
  }

  .explore-filters {
    width: 100%;
    justify-content: center;
  }

  .filter-select {
    flex: 1;
    min-width: 120px;
  }

  .explore-btn {
    width: 100%;
  }
}

@media (max-width: 480px) {
  .carousel {
    height: 50vh;
  }

  .carousel-arrow {
    width: 36px;
    height: 36px;
  }

  .carousel-arrow svg {
    width: 18px;
    height: 18px;
  }

  .carousel-content {
    padding: 0 16px;
    bottom: 30px;
  }

  .image-title {
    font-size: 14px;
  }

  .carousel-pagination {
    bottom: 80px;
    gap: 6px;
  }

  .dot {
    width: 8px;
    height: 8px;
  }

  .explore-section {
    padding: 30px 16px;
  }

  .explore-section h2 {
    font-size: 18px;
    margin-bottom: 20px;
  }

  .search-input-group {
    width: 100%;
  }

  .search-input {
    font-size: 12px;
  }

  .filter-select {
    font-size: 12px;
  }
}
</style>
