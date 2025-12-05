<template>
  <div class="sub_header">
    <div class="marquee">
      <div class="marquee__content" :style="{ animationDuration: speed + 's' }">
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

    <button class="btn" @click="loadArticles" title="Recharger">↻</button>
  </div>
</template>


<script setup lang="ts">
import { ref, onMounted } from "vue";

type Article = {
  title: string;
  link?: string;
  published?: string;
  _meta?: any;
  [k: string]: any;
};

const articles = ref<Article[]>([]);
const speed = 100; // durée du défilement (en secondes)

async function loadArticles() {
  try {
    const res = await fetch("http://127.0.0.1:5000/articles?q=ukraine&hours=24&meta=1");
    const data = await res.json();

    // Accepte un tableau direct OU un objet { articles: [...] }
    const list: any[] = Array.isArray(data) ? data : (data?.articles ?? []);

    // Normalise -> toujours { title: string, ... }
    articles.value = list
      .filter((x) => x != null)                               // enlève null/undefined
      .map((x) => (typeof x === "string" ? { title: x } : x)) // convertit string -> objet
      .filter((x) => typeof x.title === "string" && x.title.trim().length > 0); // garde ceux qui ont un title

    console.log("Articles (normalisés):", articles.value);
  } catch (error) {
    console.error("Erreur API :", error);
    articles.value = [];
  }
}

// Charge au montage
onMounted(loadArticles);
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
}

.marquee {
  position: relative;
  overflow: hidden;
  white-space: nowrap;
  flex: 1;
}

/* Marquee : part de la droite (100%) vers la gauche (-100%) */
.marquee__content {
  display: inline-block;
  will-change: transform;
  animation-name: marquee;
  animation-timing-function: linear;
  animation-iteration-count: infinite;
  /* NB: la durée vient du :style="{ animationDuration: speed + 's' }" */
}

.marquee__content span {
  margin-right: 20px;
}

@keyframes marquee {
  0%   { transform: translateX(100%); }
  100% { transform: translateX(-100%); }
}
</style>
