<template>
  <div class="sub_header">
    <div class="marquee">
      <div v-if="articles.length === 0" class="marquee__empty">
        Chargement des actualités...
      </div>
      <div v-else class="marquee__content" :style="{ animationDuration: speed + 's' }">
        <span v-for="(a, i) in articles" :key="(a.link || a.title || '') + i">
          <a
            :href="a.link || '#'"
            target="_blank"
            rel="noopener"
            class="marquee-link"
          >
            {{ a.title }}
          </a>
          •
        </span>
      </div>
    </div>

    <button 
      class="btn" 
      @click="loadArticles" 
      title="Recharger"
      :disabled="loading"
    >
      ↻
    </button>
  </div>
</template>


<script setup lang="ts">
import { ref, onMounted } from "vue";

type Article = {
  title: string;
  link?: string;
  published?: string;
  source?: string;
  media?: any;
  author?: string;
  categories?: string[];
  [k: string]: any;
};

const articles = ref<Article[]>([]);
const loading = ref(false);
const speed = 120; // durée du défilement (en secondes)

async function loadArticles() {
  if (loading.value) return; // Évite les appels multiples
  loading.value = true;

  try {
    const res = await fetch("http://127.0.0.1:5000/articles?q=ukraine&hours=24&meta=1", {
      signal: AbortSignal.timeout(10000), // Timeout 10s
    });

    if (!res.ok) throw new Error(`API error: ${res.status}`);

    const data = await res.json();

    // Accepte un tableau direct OU un objet { articles: [...] }
    const list: any[] = Array.isArray(data) ? data : (data?.articles ?? []);

    // Normalise -> toujours { title: string, ... }
    articles.value = list
      .filter((x) => x != null)                               // enlève null/undefined
      .map((x) => (typeof x === "string" ? { title: x } : x)) // convertit string -> objet
      .filter((x) => typeof x.title === "string" && x.title.trim().length > 0); // garde ceux qui ont un title

    console.log("✓ Articles chargés:", articles.value.length);
  } catch (error) {
    console.error("✗ Erreur API:", error);
    articles.value = [{ title: "Erreur de chargement. Cliquez ↻ pour réessayer." }];
  } finally {
    loading.value = false;
  }
}

// Charge au montage + auto-refresh toutes les 5 minutes
onMounted(() => {
  loadArticles();
  setInterval(loadArticles, 5 * 60 * 1000);
});
</script>

<style scoped>
.sub_header {
  background-color: #2f0538;
  height: 30px;
  display: flex;
  align-items: center;
  padding: 0 10px;
  font-size: 14px;
  color: white;
  overflow: hidden;
  gap: 8px;
}

.btn {
  background: transparent;
  border: none;
  color: white;
  cursor: pointer;
  font-size: 16px;
  flex-shrink: 0;
  padding: 4px;
  opacity: 1;
  transition: opacity 0.2s;
}

.btn:hover {
  opacity: 0.8;
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.btn:active {
  transform: rotate(45deg);
}

.marquee {
  position: relative;
  overflow: hidden;
  white-space: nowrap;
  flex: 1;
  min-width: 0;
}

.marquee__empty {
  display: inline-block;
  color: #ccc;
  font-style: italic;
  padding: 0 10px;
}

/* Marquee : part de la droite (100%) vers la gauche (-100%) */
.marquee__content {
  display: inline-block;
  will-change: transform;
  animation-name: marquee;
  animation-timing-function: linear;
  animation-iteration-count: infinite;
  padding-left: 100%;
  /* NB: la durée vient du :style="{ animationDuration: speed + 's' }" */
}

.marquee__content span {
  margin-right: 20px;
  display: inline-block;
}

.marquee-link {
  color: #fff;
  text-decoration: none;
  transition: color 0.2s;
}

.marquee-link:hover {
  color: #ffd700;
  text-decoration: underline;
}

@keyframes marquee {
  0%   { transform: translateX(0); }
  100% { transform: translateX(-100%); }
}
</style>
</style>
