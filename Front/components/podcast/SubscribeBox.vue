<template>
  <div class="sidebar-box subscribe-box">
    <h3 class="sidebar-title">S'abonner au podcast</h3>
    <p class="sidebar-desc">Recevez les nouveaux épisodes directement dans votre lecteur préféré</p>
    <div class="subscribe-links">
      <a v-for="link in links" :key="link.label" :href="link.href" class="subscribe-link">
        <span class="app-icon">{{ link.icon }}</span>
        {{ link.label }}
      </a>
    </div>
  </div>
</template>

<script setup lang="ts">
interface SubscribeLink { label: string; icon: string; href: string }
const props = defineProps<{ links: SubscribeLink[] }>();
</script>

<style scoped>
.sidebar-box { background: #f9f9f9; padding: 24px; border-radius: 12px; border: 1px solid #f0f0f0; }
.sidebar-title { font-size: 16px; font-weight: 700; color: #1a1a1a; margin: 0 0 12px; }
.sidebar-desc { font-size: 13px; color: #666; line-height: 1.5; margin: 0 0 16px; }
.subscribe-links { display: flex; flex-direction: column; gap: 10px; }
.subscribe-link { display: flex; align-items: center; gap: 10px; padding: 10px; background: #fff; border-radius: 6px; text-decoration: none; color: #555; font-size: 13px; font-weight: 600; transition: all 0.22s ease; border: 1px solid #e5e5e5; }
.subscribe-link:hover { color: #7b5ce0; border-color: #7b5ce0; }
.app-icon { font-size: 16px; }
</style>
