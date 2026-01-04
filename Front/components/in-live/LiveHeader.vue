<template>
  <header class="feed-header">
    <div class="header-top">
      <div class="title-section">
        <h1 class="feed-title">
          <span class="live-indicator">●</span>
          Live en cours
        </h1>
        <p class="article-count">Mis à jour aujourd'hui à {{ updateTime }}</p>
      </div>
      <div class="search-controls">
        <div class="search-wrapper">
          <input
            :value="query"
            class="search-input"
            placeholder="Rechercher..."
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
const props = defineProps<{ query: string; updateTime: string }>();
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

.live-indicator {
  font-size: 12px;
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
  width: 280px;
  padding: 10px 36px 10px 14px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 14px;
  transition: all 0.22s ease;
}

.search-input:focus {
  outline: none;
  border-color: #7b5ce0;
  box-shadow: 0 0 0 3px rgba(123, 92, 224, 0.1);
}

.search-icon {
  position: absolute;
  right: 12px;
  width: 18px;
  height: 18px;
  opacity: 0.5;
  pointer-events: none;
  color: #666;
}

.clear-btn {
  position: absolute;
  right: 8px;
  width: 24px;
  height: 24px;
  border: none;
  background: rgba(123, 92, 224, 0.1);
  color: #7b5ce0;
  border-radius: 50%;
  cursor: pointer;
  font-size: 18px;
  line-height: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.22s ease;
}

.clear-btn:hover {
  background: rgba(123, 92, 224, 0.2);
}

@media (max-width: 1100px) {
  .header-top {
    flex-direction: column;
    align-items: stretch;
  }

  .search-controls {
    flex-direction: column;
  }

  .search-input {
    width: 100%;
  }
}

@media (max-width: 680px) {
  .feed-header { padding: 16px 0; }
  .header-top { padding: 0 16px; }
  .feed-title { font-size: 24px; }
  .article-count { font-size: 12px; }
  .search-input { font-size: 13px; padding: 8px 32px 8px 12px; }
}
</style>
