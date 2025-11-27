<template>
  <article class="lead-article">
    <img :src="article.image" alt="" class="lead-image" />
    <div class="lead-content">
      <div class="lead-meta">Par Auteur — 27 novembre 2025</div>
      <h2 class="lead-title">{{ article.title }}</h2>
      <p class="lead-excerpt">{{ article.excerpt }}</p>
    </div>
  </article>
</template>

<script setup>
defineProps({ article: { type: Object, required: true } })
</script>

<style scoped>
.lead-article { display:flex; flex-direction:column; gap:12px; background:var(--paper); padding:18px; border-bottom:1px solid var(--rule) }
.lead-image { width:100%; height:auto; object-fit:cover }
.lead-title { font-family: 'Merriweather', Georgia, serif; font-size:38px; margin:8px 0 }
.lead-excerpt { color:#333; margin-top:8px }
.lead-meta { color:var(--muted); font-size:13px }
</style>
