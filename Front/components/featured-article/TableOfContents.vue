<template>
  <aside class="table-of-contents">
    <h3 class="toc-title">Sommaire</h3>
    <nav class="toc-nav">
      <a href="#introduction" class="toc-link">Introduction</a>
      <a href="#strategies" class="toc-link">Stratégies d'influence</a>
      <a href="#social-media" class="toc-link">Réseaux sociaux</a>
      <a href="#deepfakes" class="toc-link">Deepfakes et désinformation</a>
      <a href="#osint" class="toc-link">OSINT et fact-checking</a>
      <a href="#impact" class="toc-link">Impact sur les perceptions</a>
      <a href="#conclusion" class="toc-link">Conclusion</a>
    </nav>
  </aside>
</template>
<script setup lang="ts"></script>
<style scoped>
.table-of-contents{position:sticky;top:1rem;align-self:flex-start;border:1px solid #eee;padding:1rem;border-radius:.5rem}
.toc-title{margin:0 0 .5rem;font-weight:600}
.toc-nav{display:flex;flex-direction:column;gap:.25rem}
.toc-link{color:#1976d2;text-decoration:none}
</style>
