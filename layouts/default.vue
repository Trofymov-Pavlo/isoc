<template>
  <div class="site-container">
    <MainHeader />
    <slot />
  </div>
</template>

<script setup lang="ts">
</script>

<style>
.site-container {
  max-width: 1300px;   /* largeur du site comme Mediapart */
  margin: 0 auto;      /* centre le contenu */
  padding: 0 18;     /* marges gauche et droite */
}
</style>
