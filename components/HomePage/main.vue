<template>
  <div class="home">
    <HeroSection />
    <AlertBar />
    <FeaturedArticle />
    <HighlightedArticles />
    <PodcastSection />
    <LiveUpdates />
    <AnalysisSection />
    <NewsletterSection />
  </div>
</template>

<script setup lang="ts">
import HeroSection from './HeroSection.vue';
import AlertBar from './AlertBar.vue';
import FeaturedArticle from './FeaturedArticle.vue';
import HighlightedArticles from './HighlightedArticles.vue';
import PodcastSection from './PodcastSection.vue';
import LiveUpdates from './LiveUpdates.vue';
import AnalysisSection from './AnalysisSection.vue';
import NewsletterSection from './NewsletterSection.vue';
</script>

<style scoped>
.home {
  background: #ffffff;
  min-height: 100vh;
  padding-bottom: 60px;
}
</style>
