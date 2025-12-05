<template>
  <div class="site-container">
    <MainHeader />
  </div>

  <SubHeader />

  <div class="site-container">
    <slot />
  </div>
</template>

<script setup lang="ts">
import MainHeader from "@/components/header/mainHeader.vue"
import SubHeader from "@/components/header/subHeader.vue"
</script>

<style>
.site-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 0px;
}

html, body {
  margin: 0;
}
</style>
