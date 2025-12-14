<template>
  <section class="liked-shell">
    <div class="card">
      <h1>Articles likés</h1>
      <p>Vos articles sauvegardés s'afficheront ici.</p>
      <div class="grid" v-if="items.length">
        <article v-for="it in items" :key="it.id" class="item">
          <h3 class="title">{{ it.title }}</h3>
          <p class="meta">{{ it.source }} — {{ it.date }}</p>
        </article>
      </div>
      <div class="empty" v-else>
        <p>Aucun article liké pour le moment.</p>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
// Placeholder data until backend is wired.
const items: Array<{ id:number; title:string; source:string; date:string; }>= []
</script>

<style scoped>
.liked-shell { min-height: 70vh; display: flex; justify-content: center; align-items: center; background:#f7f7fb; padding:40px 16px; }
.card { max-width: 900px; width:100%; background:#fff; border-radius:16px; box-shadow:0 10px 30px rgba(0,0,0,0.08); padding:24px; display:grid; gap:12px; }
.grid { display:grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap:16px; }
.item { border:1px solid #eee; border-radius:12px; padding:12px; }
.title { margin:0 0 6px; font-size:16px; }
.meta { margin:0; font-size:12px; color:#666; }
.empty { text-align:center; color:#4a4a55; }
</style>
