<template>
  <div class="home-page">
    <HomeCarousel />

    <FeaturedArticlesSection />
  </div>
</template>

<script setup lang="ts">
import HomeCarousel from './HomeCarousel.vue'
import FeaturedArticlesSection from './FeaturedArticlesSection.vue'
</script>

<style scoped>
.home-page { background: #ffffff; }
</style>
