<template>
  <section class="episode-section">
    <h2 class="section-title">Sommaire de l'épisode</h2>
    <div class="timeline">
      <div v-for="item in items" :key="item.time" class="timeline-item">
        <div class="timeline-marker">{{ item.time }}</div>
        <div class="timeline-content">
          <h3>{{ item.title }}</h3>
          <p>{{ item.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
interface TimelineItem { time: string; title: string; description: string }
const props = defineProps<{ items: TimelineItem[] }>();
</script>

<style scoped>
.episode-section { display: flex; flex-direction: column; gap: 16px; }
.section-title { font-size: 32px; font-weight: 700; color: #1a1a1a; margin: 0; line-height: 1.2; }
.timeline { display: flex; flex-direction: column; gap: 24px; }
.timeline-item { display: grid; grid-template-columns: 80px 1fr; gap: 20px; padding: 16px; background: #f9f9f9; border-radius: 8px; border-left: 4px solid #7b5ce0; transition: all 0.22s ease; }
.timeline-item:hover { background: #f5f0ff; transform: translateX(4px); }
.timeline-marker { font-weight: 700; color: #7b5ce0; font-size: 14px; }
.timeline-content h3 { font-size: 15px; font-weight: 700; color: #1a1a1a; margin: 0 0 6px; }
.timeline-content p { font-size: 13px; color: #666; margin: 0; line-height: 1.5; }

@media (max-width: 768px) {
  .section-title { font-size: 24px; }
  .timeline-item { grid-template-columns: 60px 1fr; }
}

@media (max-width: 480px) {
  .section-title { font-size: 20px; }
}
</style>
