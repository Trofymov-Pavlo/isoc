<template>
  <section class="rss">
    <h1>Flux RSS</h1>
    <p>
      Retrouvez le flux RSS du site ici :
      <a href="/rss.xml" target="_blank" rel="noopener">rss.xml</a>
    </p>
    <p>
      Vous pouvez l'ajouter à votre lecteur RSS pour suivre nos
      dernières publications.
    </p>
  </section>
</template>

<script setup lang="ts">
// Component displays a link to the RSS XML available under public/
</script>

<style scoped>
.rss {
  max-width: 800px;
  margin: 2rem auto;
  padding: 1rem;
}
.rss h1 {
  font-size: 1.8rem;
  margin-bottom: 0.75rem;
}
.rss a {
  color: #1976d2;
}
</style>
