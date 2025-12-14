<template>
  <section class="episode-section">
    <h2 class="section-title">À propos de cet épisode</h2>
    <p v-for="(p, i) in paragraphs" :key="i" class="section-text">{{ p }}</p>
  </section>
</template>

<script setup lang="ts">
const props = defineProps<{ paragraphs: string[] }>();
</script>

<style scoped>
.episode-section { display: flex; flex-direction: column; gap: 16px; }
.section-title { font-size: 32px; font-weight: 700; color: #1a1a1a; margin: 0; line-height: 1.2; }
.section-text { font-size: 16px; line-height: 1.8; color: #555; margin: 0; }

@media (max-width: 768px) {
  .section-title { font-size: 24px; }
}

@media (max-width: 480px) {
  .section-title { font-size: 20px; }
}
</style>
