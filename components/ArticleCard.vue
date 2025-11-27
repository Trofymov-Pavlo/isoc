<template>
  <article class="article-card">
    <img :src="article.image" alt="" class="card-image" />
    <div class="card-body">
      <div class="card-meta">Publié • 27 nov</div>
      <h3 class="card-title">{{ article.title }}</h3>
      <p class="card-excerpt">{{ article.excerpt }}</p>
    </div>
  </article>
</template>

<script setup>
defineProps({ article: { type: Object, required: true } })
</script>

<style scoped>
.article-card { display:flex; gap:14px; padding:12px 0; border-bottom:1px solid var(--rule); align-items:flex-start }
.card-image { width:160px; height:100px; object-fit:cover }
.card-meta { color:var(--muted); font-size:12px; text-transform:uppercase; margin-bottom:6px }
.card-title { font-family: 'Merriweather', Georgia, serif; font-size:18px; margin:0 }
.card-excerpt { color:#444; margin-top:6px }
</style>
