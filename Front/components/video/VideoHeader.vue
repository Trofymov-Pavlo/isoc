<template>
  <header class="feed-header">
    <div class="header-top">
      <div class="title-section">
        <h1 class="feed-title">
          <span class="video-indicator">▶</span>
          Analyses & Décryptages Vidéo
        </h1>
        <p class="video-count">Toutes les vidéos d'analyse</p>
      </div>
      <div class="search-controls">
        <div class="search-wrapper">
          <input
            :value="query"
            @input="$emit('update:query', ($event.target as HTMLInputElement).value)"
            class="search-input"
            placeholder="Rechercher une vidéo..."
            @keyup.enter="$emit('search')"
          />
          <svg v-if="!query" class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <path d="m21 21-4.35-4.35"></path>
          </svg>
          <button v-else @click="$emit('update:query', ''); $emit('search')" class="clear-btn">×</button>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
const props = defineProps<{ query: string }>();
</script>

<style scoped>
.feed-header { background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%); color: #fff; padding: 40px 0; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
.header-top { max-width: 1200px; margin: 0 auto; padding: 0 20px; display: flex; justify-content: space-between; align-items: center; gap: 32px; }
.title-section { flex: 1; }
.feed-title { margin: 0; font-size: 32px; font-weight: 800; display: flex; align-items: center; gap: 12px; }
.video-indicator { color: #ff6b6b; font-size: 24px; animation: pulse 2s ease infinite; }
@keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.6; } }
.video-count { margin: 8px 0 0; font-size: 14px; color: rgba(255,255,255,0.8); }
.search-controls { display: flex; gap: 12px; align-items: center; }
.search-wrapper { position: relative; }
.search-input { padding: 12px 40px 12px 16px; border-radius: 8px; border: 2px solid rgba(255,255,255,0.3); background: rgba(255,255,255,0.15); color: #fff; font-size: 14px; width: 280px; transition: all 0.3s ease; backdrop-filter: blur(10px); }
.search-input::placeholder { color: rgba(255,255,255,0.6); }
.search-input:focus { outline: none; border-color: #fff; background: rgba(255,255,255,0.25); }
.search-icon { position: absolute; right: 12px; top: 50%; transform: translateY(-50%); width: 18px; height: 18px; color: rgba(255,255,255,0.6); pointer-events: none; }
.clear-btn { position: absolute; right: 12px; top: 50%; transform: translateY(-50%); background: none; border: none; color: rgba(255,255,255,0.8); font-size: 24px; cursor: pointer; padding: 0; width: 20px; height: 20px; display: flex; align-items: center; justify-content: center; transition: color 0.2s ease; }
.clear-btn:hover { color: #fff; }
@media (max-width: 680px) {
  .header-top { flex-direction: column; align-items: flex-start; }
  .search-controls { width: 100%; }
  .search-input { width: 100%; }
  .feed-title { font-size: 24px; }
}
</style>
