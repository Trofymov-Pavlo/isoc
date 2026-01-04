<template>
  <div class="home-page">
    <HomeCarousel />

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

    <FeaturedArticlesSection />

    <section class="about">
      <div class="about-box">
        <h3>Notre engagement</h3>
        <p>Couverture indépendante, vérifiée et sourcée. Axiome propose une veille média professionnelle et transparente sur le conflit ukrainien, avec des filtres avancés et une interface claire.</p>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import HomeCarousel from './HomeCarousel.vue'
import FeaturedArticlesSection from './FeaturedArticlesSection.vue'
</script>

<style scoped>
.home-page { background: #ffffff; }

.tiles { padding: 28px 24px; max-width: 1200px; margin: 0 auto; }
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
</style>
