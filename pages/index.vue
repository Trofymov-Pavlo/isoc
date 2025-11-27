
<!-- pages/index.vue -->

<template>
  <div class="home">
    <LeadArticle :article="lead" />

    <section class="grid">
      <div class="main-list">
        <ArticleCard v-for="a in articles" :key="a.id" :article="a" />
      </div>
    </section>
  </div>
</template>

<script setup>
const lead = {
  id: 1,
  title: "Titre principal — Crise et perspectives",
  excerpt: "Un aperçu approfondi des événements marquants du jour, analysés par la rédaction.",
  image: "https://via.placeholder.com/1200x600.png?text=%C3%80+la+une"
}

const articles = Array.from({ length: 8 }).map((_, i) => ({
  id: i + 2,
  title: `Article ${i + 1} — Sujet important`,
  excerpt: 'Un court résumé informatif qui donne envie de lire la suite.',
  image: 'https://via.placeholder.com/320x200'
}))
</script>

<style scoped>
.home { max-width:1060px; margin:18px auto }
.main-list { display:flex; flex-direction:column; gap:6px }
.grid { margin-top:16px }
</style>

