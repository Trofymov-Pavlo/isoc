<template>
  <section class="shell">
    <div class="head">
      <h1>Archive</h1>
      <p>Historique des contenus (articles et vidéos).</p>
    </div>
    <div class="grid">
      <div class="col">
        <h2>Articles</h2>
        <ul class="list">
          <li v-for="a in articles" :key="a.id">{{ a.title }}</li>
        </ul>
      </div>
      <div class="col">
        <h2>Vidéos</h2>
        <ul class="list">
          <li v-for="v in videos" :key="v.id">{{ v.title }}</li>
        </ul>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
const articles: Array<{ id:number; title:string; }> = []
const videos: Array<{ id:number; title:string; }> = []
</script>

<style scoped>
.shell { max-width: 1200px; margin: 0 auto; padding: 32px calc(2vw); }
.head { margin-bottom: 16px; }
.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
.list { margin:0; padding-left: 18px; }
@media (max-width: 768px){ .grid { grid-template-columns: 1fr; } }
</style>
