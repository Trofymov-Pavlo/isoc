<template>
  <section class="episode-section">
    <h2 class="section-title">Points clés du débat</h2>
    <div class="key-points">
      <div v-for="point in points" :key="point.title" class="key-point">
        <h3 class="point-title">{{ point.title }}</h3>
        <p>{{ point.description }}</p>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
interface KeyPoint { title: string; description: string }
const props = defineProps<{ points: KeyPoint[] }>();
</script>

<style scoped>
.episode-section { display: flex; flex-direction: column; gap: 16px; }
.section-title { font-size: 32px; font-weight: 700; color: #1a1a1a; margin: 0; line-height: 1.2; }
.key-points { display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; }
.key-point { padding: 20px; background: linear-gradient(135deg, rgba(123, 92, 224, 0.05), rgba(123, 92, 224, 0.02)); border-radius: 8px; border-left: 4px solid #7b5ce0; }
.point-title { font-size: 15px; font-weight: 700; color: #1a1a1a; margin: 0 0 8px; }
.key-point p { font-size: 13px; line-height: 1.6; color: #666; margin: 0; }

@media (max-width: 1200px) { .key-points { grid-template-columns: 1fr; } }
@media (max-width: 768px) { .section-title { font-size: 24px; } }
@media (max-width: 480px) { .section-title { font-size: 20px; } }
</style>
