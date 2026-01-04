<template>
  <div class="home-page">
    <HomeCarousel />

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

.about { padding: 40px 24px; }
.about-box { max-width: 1000px; margin: 0 auto; background: #f8fafc; border: 1px solid #e9ecef; border-radius: 12px; padding: 20px; }
.about-box h3 { margin: 0 0 8px 0; font-size: 18px; color: #111827; }
.about-box p { margin: 0; color: #4b5563; }
</style>
