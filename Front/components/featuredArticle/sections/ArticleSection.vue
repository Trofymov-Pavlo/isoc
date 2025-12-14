<template>
  <section class="article-section" :id="id">
    <h2 class="section-title"><slot name="title" /></h2>
    <div class="section-body">
      <slot />
    </div>
  </section>
</template>
<script setup lang="ts">
defineProps<{ id: string }>();
</script>
<style scoped>
.article-section{margin:2rem 0}
.section-title{font-size:1.5rem;margin-bottom:.75rem}
.section-body{color:#333}
</style>
