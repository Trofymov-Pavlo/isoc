<template>
  <section class="episode-section">
    <h2 class="section-title">Ressources mentionnées</h2>
    <div class="resources-list">
      <div v-for="resource in resources" :key="resource.title" class="resource-item">
        <div class="resource-icon">🔗</div>
        <div class="resource-content">
          <h3 class="resource-title">{{ resource.title }}</h3>
          <p class="resource-desc">{{ resource.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
interface Resource { title: string; description: string }
const props = defineProps<{ resources: Resource[] }>();
</script>

<style scoped>
.episode-section { display: flex; flex-direction: column; gap: 16px; }
.section-title { font-size: 32px; font-weight: 700; color: #1a1a1a; margin: 0; line-height: 1.2; }
.resources-list { display: grid; gap: 16px; }
.resource-item { display: flex; gap: 16px; padding: 16px; background: #f9f9f9; border-radius: 8px; transition: all 0.22s ease; }
.resource-item:hover { background: #f5f0ff; }
.resource-icon { font-size: 24px; flex-shrink: 0; }
.resource-title { font-size: 15px; font-weight: 700; color: #1a1a1a; margin: 0 0 4px; }
.resource-desc { font-size: 13px; color: #666; margin: 0; line-height: 1.5; }

@media (max-width: 768px) { .section-title { font-size: 24px; } }
@media (max-width: 480px) { .section-title { font-size: 20px; } }
</style>
