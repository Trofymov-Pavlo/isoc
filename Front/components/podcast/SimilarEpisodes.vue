<template>
  <div class="sidebar-box similar-box">
    <h3 class="sidebar-title">Épisodes similaires</h3>
    <div class="similar-episodes">
      <div v-for="ep in episodes" :key="ep.number" class="similar-episode">
        <span class="episode-number">{{ ep.number }}</span>
        <p class="episode-title">{{ ep.title }}</p>
        <span class="episode-date">{{ ep.date }}</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Episode { number: string; title: string; date: string }
const props = defineProps<{ episodes: Episode[] }>();
</script>

<style scoped>
.sidebar-box { background: #f9f9f9; padding: 24px; border-radius: 12px; border: 1px solid #f0f0f0; }
.sidebar-title { font-size: 16px; font-weight: 700; color: #1a1a1a; margin: 0 0 12px; }
.similar-episodes { display: flex; flex-direction: column; gap: 16px; }
.similar-episode { padding: 12px; background: #fff; border-radius: 6px; border: 1px solid #e5e5e5; }
.episode-number { font-size: 11px; font-weight: 700; color: #7b5ce0; text-transform: uppercase; }
.episode-title { font-size: 13px; font-weight: 600; color: #1a1a1a; margin: 4px 0; line-height: 1.4; }
.episode-date { font-size: 11px; color: #999; }
</style>
