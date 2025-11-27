<template>
  <div class="ticker">
    <div class="ticker-inner">
      <div v-if="pending" class="loading">Chargement...</div>
      <div v-else-if="error" class="error">Erreur de chargement</div>

      <div
        v-else
        class="tick-item"
        v-for="(item, i) in data"
        :key="i"
      >
        <a :href="item.link" target="_blank" rel="noopener">
          {{ item.title }}
        </a>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const { data, pending, error } = await useAsyncData("articles", () =>
  $fetch("http://127.0.0.1:5000/articles", {
    query: {
      q: "ukraine",
      page: 1
    }
  })
);
</script>

<style scoped>
.ticker { background:#0f5f72; color:white; padding:10px 0; font-size:13px }
.ticker-inner { display:flex; gap:28px; max-width:1060px; margin:0 auto; padding:0 20px }
.tick-item { flex:0 0 auto }
.tick-item a { color:white; text-decoration:none; }
.loading { opacity:0.7; }
</style>
