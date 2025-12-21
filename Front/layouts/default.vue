<template>
  <div class="site-container">
    <HeaderMainHeader />
  </div>

  <HeaderSubHeader />

  <div class="site-container">
    <slot />
  </div>

  <FooterMain />
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import HeaderMainHeader from '~/components/header/mainHeader.vue';
import HeaderSubHeader from '~/components/header/SubHeader.vue';
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
