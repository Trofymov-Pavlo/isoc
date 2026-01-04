<template>
  <ConnexionLayout />
</template>

<script setup lang="ts">
import ConnexionLayout from '~/components/compte/ConnexionLayout.vue';

// Layout personnalisé : pas de header, footer ou subheader
definePageMeta({
  layout: false,
});
</script>

<style scoped>
/* Le style est entièrement dans ConnexionLayout */
</style>
