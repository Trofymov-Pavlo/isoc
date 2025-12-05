<template>
  <main class="page">
    <header class="page__header">
      <h1>En Direct</h1>
      <div class="controls">
        <input v-model="localQuery" class="input" placeholder="Filtrer par mot-clé" />
        <button class="btn" :disabled="loading" @click="reload">↻</button>
      </div>
    </header>

    <p v-if="error" class="state state--error">
      {{ error }}
    </p>
    <p v-else-if="loading" class="state">Chargement…</p>

    <section v-else class="grid">
      <article v-for="(it, i) in filtered" :key="(it.link || it.title) + i" class="card">
        <a v-if="it.image" :href="it.link" target="_blank" rel="noopener" class="media">
          <img :src="it.image" :alt="it.title" loading="lazy" />
        </a>
        <div class="body">
          <p v-if="it.source" class="source">{{ it.source }}</p>
          <h2 class="title">
            <a :href="it.link" target="_blank" rel="noopener">{{ it.title }}</a>
          </h2>
          <p v-if="it.summary" class="summary">{{ it.summary }}</p>
          <time v-if="it.published" class="time">{{ it.published }}</time>
        </div>
      </article>
    </section>
  </main>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import { useArticles } from "@/composables/useArticles";

const { all, loading, error, load } = useArticles({
  apiBase: "http://127.0.0.1:5000",
  query: "ukraine",
  hours: 24,
  meta: 1,
});

const localQuery = ref("");

const filtered = computed(() => {
  const q = localQuery.value.trim().toLowerCase();
  if (!q) return all.value;
  return all.value.filter(a =>
    a.title.toLowerCase().includes(q) ||
    (a.summary ?? "").toLowerCase().includes(q) ||
    (a.source ?? "").toLowerCase().includes(q)
  );
});

function reload() {
  load();
}

onMounted(() => {
  load();
});
</script>

<style scoped>
.page { padding: 12px 10px 40px; }
.page__header {
  display: flex; align-items: center; justify-content: space-between; gap: 12px; margin-bottom: 12px;
}
.controls { display: flex; gap: 8px; align-items: center; }
.input { padding: 8px 10px; border: 1px solid #ddd; border-radius: 6px; min-width: 220px; }
.btn { background: transparent; border: 1px solid #ddd; border-radius: 6px; padding: 8px 10px; cursor: pointer; }
.btn:disabled { opacity: .5; cursor: not-allowed; }

.state { color: #555; margin: 8px 0 16px; }
.state--error { color: #b00020; }

.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}
.card { background: #fff; border: 1px solid #eee; border-radius: 10px; overflow: hidden; display: grid; }
.media img { width: 100%; height: 180px; object-fit: cover; display: block; }
.body { padding: 12px; display: grid; gap: 6px; }
.source { margin: 0; color: #a00; font-size: 12px; font-weight: 700; text-transform: uppercase; }
.title { margin: 0; font-size: 18px; font-weight: 800; line-height: 1.25; }
.title a { color: inherit; text-decoration: none; }
.title a:hover { text-decoration: underline; }
.summary { color: #444; font-size: 14px; }
.time { color: #777; font-size: 12px; }

@media (max-width: 1100px) { .grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 680px) { .grid { grid-template-columns: 1fr; } .media img { height: 220px; } }
</style>

