<template>
  <div class="home">
    <HeroSection />
    <BreakingNews />
    <FeaturedArticle />
    <TopStories />
    <PodcastSection />
    <LiveUpdates />
    <AnalysisSection />
    <NewsletterSection />
  </div>
</template>

<script setup lang="ts">
import HeroSection from './HeroSection.vue';
import BreakingNews from './BreakingNews.vue';
import FeaturedArticle from './FeaturedArticle.vue';
import TopStories from './TopStories.vue';
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
