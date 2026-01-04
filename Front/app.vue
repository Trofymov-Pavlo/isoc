<!-- app.vue -->
<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>
<script setup lang="ts">
import { useTheme } from '~/composables/useTheme';

// Initialize theme on app load
const { initTheme } = useTheme();
initTheme();
</script>