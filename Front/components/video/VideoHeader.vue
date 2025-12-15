<template>
  <header class="feed-header">
    <div class="header-top">
      <div class="title-section">
        <h1 class="feed-title">
          <span class="video-indicator">▶</span>
          Analyses & Décryptages Vidéo
        </h1>
        <p class="article-count">Toutes les vidéos d'analyse</p>
      </div>
      <div class="search-controls">
        <div class="search-wrapper">
          <input
            :value="query"
            class="search-input"
            placeholder="Rechercher une vidéo..."
            @input="$emit('update:query', ($event.target as HTMLInputElement).value)"
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
.feed-header {
  background: transparent;
  border-bottom: none;
  padding: 24px 0;
  margin-bottom: 32px;
  position: sticky;
  top: 0;
  z-index: 10;
}

.header-top {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}

.title-section {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.feed-title {
  margin: 0;
  font-size: 28px;
  font-weight: 700;
  color: #2f0538;
  display: flex;
  align-items: center;
  gap: 10px;
}

.video-indicator {
  font-size: 18px;
  color: #ff6b6b;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.3; }
}

.article-count {
  margin: 0;
  font-size: 13px;
  color: #666;
  font-weight: 500;
}

.search-controls {
  display: flex;
  align-items: center;
  gap: 0;
}

.search-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.search-input {
  padding: 10px 38px 10px 16px;
  border-radius: 8px;
  border: 1px solid #ddd;
  background: #f8f8f8;
  color: #333;
  font-size: 14px;
  width: 280px;
  transition: all 0.2s ease;
}

.search-input::placeholder {
  color: #999;
}

.search-input:focus {
  outline: none;
  border-color: #2f0538;
  background: #fff;
  box-shadow: 0 2px 8px rgba(47, 5, 56, 0.1);
}

.search-icon {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: #999;
  pointer-events: none;
}

.clear-btn {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: #666;
  font-size: 24px;
  cursor: pointer;
  padding: 0;
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.2s ease;
}

.clear-btn:hover {
  color: #333;
}

@media (max-width: 680px) {
  .header-top {
    flex-direction: column;
    align-items: flex-start;
    gap: 16px;
  }
  .search-wrapper {
    width: 100%;
  }
  .search-input {
    width: 100%;
  }
  .feed-title {
    font-size: 24px;
  }
}
</style>
