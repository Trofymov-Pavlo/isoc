<template>
  <section class="episode-section">
    <h2 class="section-title">Les animateurs</h2>
    <div class="hosts-grid">
      <div v-for="host in hosts" :key="host.name" class="host-card">
        <div class="host-avatar">{{ host.initials }}</div>
        <h3 class="host-name">{{ host.name }}</h3>
        <p class="host-role">{{ host.role }}</p>
        <p class="host-bio">{{ host.bio }}</p>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
interface Host { initials: string; name: string; role: string; bio: string }
const props = defineProps<{ hosts: Host[] }>();
</script>

<style scoped>
.episode-section { display: flex; flex-direction: column; gap: 16px; }
.section-title { font-size: 32px; font-weight: 700; color: #1a1a1a; margin: 0; line-height: 1.2; }
.hosts-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
.host-card { background: #f9f9f9; padding: 28px; border-radius: 12px; text-align: center; border: 2px solid #f0f0f0; transition: all 0.3s ease; }
.host-card:hover { border-color: #7b5ce0; box-shadow: 0 8px 24px rgba(123, 92, 224, 0.1); transform: translateY(-4px); }
.host-avatar { width: 80px; height: 80px; background: linear-gradient(135deg, #7b5ce0, #9d7fee); color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 20px; margin: 0 auto 16px; }
.host-name { font-size: 18px; font-weight: 700; color: #1a1a1a; margin: 0 0 4px; }
.host-role { font-size: 13px; color: #7b5ce0; margin: 0 0 12px; font-weight: 600; }
.host-bio { font-size: 13px; line-height: 1.6; color: #666; margin: 0; }

@media (max-width: 1200px) { .hosts-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 768px) { .section-title { font-size: 24px; } .hosts-grid { grid-template-columns: 1fr; } }
@media (max-width: 480px) { .section-title { font-size: 20px; } }
</style>
