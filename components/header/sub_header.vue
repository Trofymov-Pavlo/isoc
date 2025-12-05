<template>
  <div class="sub_header">
    <div class="links">
      <router-link to="/" class="lnk">Accueil</router-link>
      <router-link to="/topStories" class="lnk">Top Stories</router-link>
    </div>

    <div class="titles">
      <span 
        v-for="(a, i) in articles" 
        :key="i" 
        class="title-item"
      >
        {{ a.title }}
      </span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";

type Article = {
  title: string;
  link?: string;
  image?: string;
  source?: string;
  summary?: string;
  published?: string;
};

const articles = ref<Article[]>([]);
const loading = ref(false);

async function loadArticles() {
  loading.value = true;

  try {
    const res = await fetch(
      "http://127.0.0.1:5000/articles?q=ukraine&hours=24&meta=1"
    );

    const data = await res.json();
    const list: any[] = Array.isArray(data) ? data : data.articles ?? [];

    // → correction ici : typage de x
    articles.value = list
      .filter((x: any) => x && x.title)
      .slice(0, 4); // 4 titres fixes
  } catch (e) {
    console.error(e);
    articles.value = [{ title: "Erreur de chargement" }];
  } finally {
    loading.value = false;
  }
}

onMounted(() => loadArticles());
</script>

<style scoped>
.sub_header {
  background-color: #2f0538;
  color: white;
  height: 40px;
  display: flex;
  align-items: center;
  padding: 0 18px;
  gap: 20px;
  font-size: 14px;
  font-weight: 500;
  width: 100%;
  margin-top: 0; /* ensure it sits directly above the header */
  position: relative;
  z-index: 40;
}

.links {
  display: flex;
  gap: 15px;
}

.lnk {
  color: white;
  text-decoration: none;
  font-weight: 600;
}

.lnk:hover {
  color: #ffdf5f;
}

.titles {
  flex: 1;
  display: flex;
  gap: 25px;
  overflow: hidden;
  white-space: nowrap;
}

.title-item {
  color: #fff;
  opacity: 0.95;
}
</style>
