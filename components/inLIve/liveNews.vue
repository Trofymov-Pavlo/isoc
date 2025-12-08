<template>
  <main class="live-feed">
    <header class="feed-header">
      <div class="header-top">
        <div class="title-section">
          <h1 class="feed-title">
            <span class="live-indicator">●</span>
            En Direct
          </h1>
          <p class="article-count">{{ filtered.length }} article{{ filtered.length !== 1 ? 's' : '' }}</p>
        </div>
        <div class="search-controls">
          <div class="search-wrapper">
            <input 
              v-model="localQuery" 
              class="search-input" 
              placeholder="Rechercher..." 
              @keyup.enter="reload"
            />
            <svg v-if="!localQuery" class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="8"></circle>
              <path d="m21 21-4.35-4.35"></path>
            </svg>
            <button v-else @click="localQuery = ''" class="clear-btn">×</button>
          </div>
          <button class="refresh-btn" :disabled="loading" @click="reload" title="Actualiser">
            <span class="refresh-icon" :class="{ spinning: loading }">↻</span>
          </button>
        </div>
      </div>
    </header>

    <div v-if="error" class="alert alert-error">
      <span class="alert-icon">⚠️</span>
      <span>{{ error }}</span>
    </div>

    <div v-else-if="loading" class="loading-state">
      <div class="spinner"></div>
      <p>Chargement des actualités...</p>
    </div>

    <div v-else-if="filtered.length === 0" class="empty-state">
      <span class="empty-icon">🔍</span>
      <p class="empty-text">Aucun article ne correspond à votre recherche</p>
      <button class="reset-btn" @click="localQuery = ''; reload()">Réinitialiser</button>
    </div>

    <section v-else class="articles-grid">
      <article 
        v-for="(article, i) in filtered" 
        :key="(article.link || article.title) + i" 
        class="article-card"
      >
        <a 
          v-if="article.image" 
          :href="article.link" 
          target="_blank" 
          rel="noopener" 
          class="article-image"
        >
          <img :src="article.image" :alt="article.title" loading="lazy" />
          <div class="image-overlay"></div>
        </a>
        <div v-else class="article-image placeholder">
          <span class="placeholder-icon">📰</span>
        </div>

        <div class="article-content">
          <p v-if="article.source" class="article-source">{{ article.source }}</p>
          <h2 class="article-title">
            <a :href="article.link" target="_blank" rel="noopener">{{ article.title }}</a>
          </h2>
          <p v-if="article.summary" class="article-summary">
            {{ truncate(article.summary, 120) }}
          </p>
          <div class="article-footer">
            <time v-if="article.published" class="article-time">
              {{ formatTime(article.published) }}
            </time>
            <a :href="article.link" target="_blank" rel="noopener" class="read-link">
              Lire →
            </a>
          </div>
        </div>
      </article>
    </section>
  </main>
</template>

<script setup lang="ts">
import { computed, onMounted, ref, onUnmounted } from "vue";
import { useArticles } from "@/composables/useArticles";

const { all, loading, error, load } = useArticles({
  apiBase: "http://127.0.0.1:5000",
  query: "ukraine",
  hours: 48,
  meta: 1,
});

const localQuery = ref("");
let refreshInterval: number | null = null;

const filtered = computed(() => {
  const query = localQuery.value.trim().toLowerCase();
  if (!query) return all.value;
  return all.value.filter(a =>
    a.title.toLowerCase().includes(query) ||
    (a.summary ?? "").toLowerCase().includes(query) ||
    (a.source ?? "").toLowerCase().includes(query)
  );
});

function reload() {
  load();
}

function truncate(text: string, max: number): string {
  if (text.length <= max) return text;
  return text.substring(0, max).trim() + '...';
}

function formatTime(dateString: string): string {
  if (!dateString) return "";
  
  try {
    // Si la date est déjà formatée (contient "déc" ou autre mois), la retourner telle quelle
    if (/jan|fév|mar|avr|mai|jui|aoû|sep|oct|nov|déc/i.test(dateString)) {
      return dateString;
    }

    const date = new Date(dateString);
    
    // Vérifier si la date est valide
    if (isNaN(date.getTime())) {
      return dateString; // Retourner la date originale si invalide
    }

    const now = new Date();
    const diffMs = now.getTime() - date.getTime();
    const diffMins = Math.floor(diffMs / 60000);
    const diffHours = Math.floor(diffMs / 3600000);
    const diffDays = Math.floor(diffMs / 86400000);

    if (diffMins < 1) return "À l'instant";
    if (diffMins < 60) return `Il y a ${diffMins}m`;
    if (diffHours < 24) return `Il y a ${diffHours}h`;
    if (diffDays < 7) return `Il y a ${diffDays}j`;
    
    return date.toLocaleDateString("fr-FR", { day: "numeric", month: "short" });
  } catch {
    return dateString;
  }
}

onMounted(() => {
  load();
  refreshInterval = window.setInterval(load, 5 * 60 * 1000);
});

onUnmounted(() => {
  if (refreshInterval) clearInterval(refreshInterval);
});
</script>

<style scoped>
.live-feed {
  min-height: 100vh;
  background: #fafbff;
  padding-bottom: 60px;
}

/* Header */
.feed-header {
  background: #ffffff;
  border-bottom: 1px solid #e5e5e5;
  padding: 24px 0;
  margin-bottom: 32px;
  position: sticky;
  top: 0;
  z-index: 10;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
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
  gap: 12px;
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

.refresh-btn {
  padding: 10px 14px;
  background: transparent;
  border: 1px solid #ddd;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.22s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 42px;
}

.refresh-btn:hover:not(:disabled) {
  border-color: #7b5ce0;
  background: rgba(123, 92, 224, 0.05);
}

.refresh-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.refresh-icon {
  font-size: 18px;
  color: #7b5ce0;
  display: inline-block;
  transition: transform 0.3s ease;
}

.refresh-icon.spinning {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Alerts */
.alert {
  max-width: 1200px;
  margin: 0 auto 24px;
  padding: 14px 18px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 14px;
}

.alert-error {
  background: rgba(255, 107, 107, 0.1);
  border: 1px solid rgba(255, 107, 107, 0.3);
  color: #d32f2f;
}

.alert-icon {
  font-size: 18px;
  flex-shrink: 0;
}

/* Loading State */
.loading-state {
  text-align: center;
  padding: 80px 20px;
  color: #666;
}

.spinner {
  width: 40px;
  height: 40px;
  margin: 0 auto 16px;
  border: 3px solid rgba(123, 92, 224, 0.2);
  border-top-color: #7b5ce0;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 80px 20px;
}

.empty-icon {
  font-size: 64px;
  display: block;
  margin-bottom: 16px;
  opacity: 0.4;
}

.empty-text {
  font-size: 16px;
  color: #666;
  margin: 0 0 20px;
}

.reset-btn {
  padding: 10px 24px;
  background: #7b5ce0;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.22s ease;
}

.reset-btn:hover {
  background: #6a4dc7;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(123, 92, 224, 0.3);
}

/* Articles Grid */
.articles-grid {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.article-card {
  background: #ffffff;
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid #e5e5e5;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
}

.article-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  border-color: #d0d0d0;
}

.article-image {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 9;
  overflow: hidden;
  background: #f5f5f5;
  display: block;
}

.article-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.article-card:hover .article-image img {
  transform: scale(1.05);
}

.image-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.1), transparent);
  pointer-events: none;
}

.article-image.placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #f5f5f5 0%, #fafafa 100%);
}

.placeholder-icon {
  font-size: 48px;
  opacity: 0.3;
}

.article-content {
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  flex: 1;
}

.article-source {
  margin: 0;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: #ff6b6b;
}

.article-title {
  margin: 0;
  font-size: 16px;
  font-weight: 700;
  line-height: 1.4;
  color: #1a1a1a;
}

.article-title a {
  color: inherit;
  text-decoration: none;
  transition: color 0.22s ease;
}

.article-title a:hover {
  color: #7b5ce0;
}

.article-summary {
  margin: 0;
  font-size: 14px;
  line-height: 1.5;
  color: #555;
  flex: 1;
}

.article-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 8px;
  padding-top: 12px;
  border-top: 1px solid #f0f0f0;
}

.article-time {
  font-size: 12px;
  color: #999;
  font-weight: 500;
}

.read-link {
  font-size: 13px;
  font-weight: 600;
  color: #7b5ce0;
  text-decoration: none;
  transition: all 0.22s ease;
  padding: 4px 8px;
  border-radius: 4px;
}

.read-link:hover {
  background: rgba(123, 92, 224, 0.1);
  color: #6a4dc7;
}

/* Responsive */
@media (max-width: 1100px) {
  .articles-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
  }
  
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
  .articles-grid {
    grid-template-columns: 1fr;
    gap: 16px;
  }
  
  .feed-header {
    padding: 16px 0;
  }
  
  .header-top {
    padding: 0 16px;
  }
  
  .feed-title {
    font-size: 24px;
  }
  
  .article-count {
    font-size: 12px;
  }
  
  .search-input {
    font-size: 13px;
    padding: 8px 32px 8px 12px;
  }
  
  .articles-grid {
    padding: 0 16px;
  }
  
  .article-content {
    padding: 14px;
  }
  
  .article-title {
    font-size: 15px;
  }
  
  .article-summary {
    font-size: 13px;
  }
}
</style>

