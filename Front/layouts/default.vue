<template>
  <HeaderNewHeader />

  <div class="site-container">
    <slot />
  </div>

  <FooterMain />
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import HeaderNewHeader from '~/components/header/NewHeader.vue';
import FooterMain from '~/components/footer/FooterMain.vue';
import { useSavedMedia } from '~/composables/useSavedMedia';
import { useAuthState } from '~/composables/useAuthState';

const { initialize } = useSavedMedia();
const { isAuthenticated } = useAuthState();

// Initialize saved media on mount if user is authenticated
onMounted(() => {
  if (isAuthenticated.value) {
    initialize();
  }
});
</script>

<style>
.site-container {
  max-width: 1400px;
  margin: 0 auto;
  width: 100%;
  padding: 0 calc(2vw);
}

html, body {
  margin: 0;
}
</style>
