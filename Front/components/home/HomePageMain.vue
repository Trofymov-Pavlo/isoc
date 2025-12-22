<template>
  <div class="home-page">
    <!-- Hero -->
    <section class="hero">
      <div class="hero-inner">
        <h1 class="title">Axiome</h1>
        <p class="subtitle">Veille média indépendante — Ukraine / Russie</p>

        <div class="searchbar">
          <div class="search-controls">
            <select v-model="type" class="select">
              <option value="all">Tous les médias</option>
              <option value="articles">Articles</option>
              <option value="videos">Vidéos</option>
            </select>
            <select v-model="date" class="select">
              <option value="today">Aujourd'hui</option>
              <option value="week">Cette semaine</option>
              <option value="month">Ce mois-ci</option>
              <option value="3months">3 derniers mois</option>
              <option value="6months">6 derniers mois</option>
              <option value="year">Cette année</option>
              <option value="all">Toutes les dates</option>
            </select>
            <input v-model="q" type="text" class="input" placeholder="Rechercher (ex: 'front sud', 'drone')" />
            <button class="cta" @click="goExplore">Explorer</button>
          </div>
          <div class="quick-links">
            <button @click="navigateTo('/en-direct')">En Direct</button>
            <button @click="navigateTo('/explorer?type=videos&date=today')">Vidéos</button>
            <button @click="navigateTo('/explorer?type=articles&date=week')">Articles</button>
            <button @click="navigateTo('/liked')">Favoris</button>
          </div>
        </div>
      </div>
    </section>
  <!-- Carousel/Slideshow Hero -->
  <HomeCarousel />

    <!-- Latest preview (24h) -->
    <section class="latest">
    </section>

    <!-- Explore tiles -->
    <section class="tiles">
      <div class="tile-grid">
        <button class="tile" @click="navigateTo('/en-direct')">
          <span class="tile-eyebrow">Live</span>
          <span class="tile-title">En Direct</span>
          <span class="tile-desc">Derniers médias des 24 heures</span>
        </button>
        <button class="tile" @click="navigateTo('/explorer?type=videos&date=today')">
          <span class="tile-eyebrow">Focus</span>
          <span class="tile-title">Vidéos</span>
          <span class="tile-desc">Sources officielles et indépendantes</span>
        </button>
        <button class="tile" @click="navigateTo('/explorer?type=articles&date=week')">
          <span class="tile-eyebrow">Analyse</span>
          <span class="tile-title">Articles</span>
          <span class="tile-desc">Synthèses et rapports</span>
        </button>
        <button class="tile" @click="navigateTo('/liked')">
          <span class="tile-eyebrow">Perso</span>
          <span class="tile-title">Favoris</span>
          <span class="tile-desc">Retrouvez vos sauvegardes</span>
        </button>
      </div>
    </section>

    <!-- About -->
    <section class="about">
      <div class="about-box">
        <h3>Notre engagement</h3>
        <p>Couverture indépendante, vérifiée et sourcée. Axiome propose une veille média professionnelle et transparente sur le conflit ukrainien, avec des filtres avancés et une interface claire.</p>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useArticles } from '@/composables/useArticles'
import { useVideos } from '@/composables/useVideos'
import HomeCarousel from './HomeCarousel.vue'

const type = ref<'all'|'articles'|'videos'>('all')
const date = ref<'today'|'week'|'month'|'3months'|'6months'|'year'|'all'>('today')
const q = ref('')

const { all: articles, load: loadArticles } = useArticles()
const { all: videos, load: loadVideos } = useVideos()

function goExplore() {
  const params = new URLSearchParams()
  params.set('type', type.value)
  params.set('date', date.value)
  if (q.value.trim()) params.set('q', q.value.trim())
  navigateTo(`/explorer?${params.toString()}`)
}

const toMs = (val: number | string | Date | undefined): number | undefined => {
  if (val == null) return undefined
  if (typeof val === 'number') return val < 1e12 ? val * 1000 : val
  const d = new Date(val)
  return isNaN(d.getTime()) ? undefined : d.getTime()
}

const formatExactDate = (item: { published?: string | Date; publishedTime?: number }): string => {
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

const latestPreview = computed(() => {
  const now = Date.now()
  const cutoff = now - 24 * 60 * 60 * 1000
  const arts = articles.value.map(a => ({
    type: 'article' as const,
    title: a.title,
    summary: a.summary,
    source: a.source,
    published: a.published,
    publishedTime: a.publishedTime,
    link: a.link,
    image: a.image,
  }))
  const vids = videos.value.map(v => ({
    type: 'video' as const,
    title: v.title,
    summary: v.summary,
    source: v.channel,
    published: v.published,
    publishedTime: v.publishedTime,
    link: v.link,
    image: v.thumbnail,
  }))
  return [...arts, ...vids]
    .filter(i => (i.publishedTime ?? toMs(i.published))! >= cutoff)
    .sort((a, b) => (b.publishedTime ?? 0) - (a.publishedTime ?? 0))
    .slice(0, 8)
})

loadArticles()
loadVideos()
</script>

<style scoped>
.home-page {
  background: #ffffff;
}

.hero {
  background: linear-gradient(180deg, #f7f8fa, #ffffff);
  border-bottom: 1px solid #e9ecef;
  display: none;
}

.hero-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 60px 24px;
  text-align: center;
}

.title {
  margin: 0;
  font-size: 48px;
  font-weight: 800;
  letter-spacing: -0.5px;
  color: #111827;
}

.subtitle {
  margin: 8px 0 24px;
  color: #4b5563;
  font-size: 16px;
}

.searchbar { display: grid; gap: 16px; justify-items: center; }
.search-controls { display: grid; grid-template-columns: 1fr 1fr 2fr auto; gap: 12px; width: 100%; max-width: 880px; }
.select, .input { border: 1px solid #dee2e6; border-radius: 8px; padding: 10px 12px; font-size: 14px; background: #ffffff; color: #212529; }
.select:focus, .input:focus { outline: none; border-color: #7b5ce0; box-shadow: 0 0 0 3px rgba(123, 92, 224, 0.1); }
.cta { padding: 10px 16px; border: 1.5px solid #7b5ce0; border-radius: 8px; background: #7b5ce0; color: #ffffff; font-weight: 700; cursor: pointer; }
.cta:hover { background: #6848c5; }
.quick-links { display: flex; gap: 8px; flex-wrap: wrap; }
.quick-links button { padding: 8px 12px; border: 1px solid #e5e7eb; background: #ffffff; color: #374151; border-radius: 999px; font-size: 12px; font-weight: 600; cursor: pointer; }
.quick-links button:hover { background: #f8fafc; }

.latest { padding: 32px 24px; max-width: 1200px; margin: 0 auto; }

.tiles { padding: 24px; max-width: 1200px; margin: 0 auto; }
.tile-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; }
.tile { background: #ffffff; border: 1px solid #e9ecef; border-radius: 12px; padding: 18px; text-align: left; display: grid; gap: 6px; cursor: pointer; transition: all 0.2s ease; }
.tile:hover { border-color: #7b5ce0; box-shadow: 0 8px 24px rgba(123,92,224,0.12); transform: translateY(-2px); }
.tile-eyebrow { font-size: 11px; font-weight: 700; color: #6b7280; text-transform: uppercase; letter-spacing: 0.5px; }
.tile-title { font-size: 16px; font-weight: 700; color: #111827; }
.tile-desc { font-size: 13px; color: #4b5563; }

.about { padding: 24px; }
.about-box { max-width: 1000px; margin: 0 auto; background: #f8fafc; border: 1px solid #e9ecef; border-radius: 12px; padding: 20px; }
.about-box h3 { margin: 0 0 8px 0; font-size: 18px; color: #111827; }
.about-box p { margin: 0; color: #4b5563; }

@media (max-width: 768px) {
  .title { font-size: 36px; }
  .search-controls { grid-template-columns: 1fr 1fr 1fr auto; }
}

@media (max-width: 520px) {
  .search-controls { grid-template-columns: 1fr; }
  .cta { width: 100%; }
}
</style>
