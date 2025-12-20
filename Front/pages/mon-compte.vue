<template>
  <div class="account-only">
    <header class="account-header">
      <div class="account-header-inner">
        <NuxtLink to="/" class="back-left">&lt; Retour</NuxtLink>

        <NuxtLink to="/" class="brand" aria-label="Retour à l'accueil">
          <img :src="logo" alt="ISOC Media" class="brand-logo" />
        </NuxtLink>

        <div class="right-spacer" aria-hidden="true"></div>
      </div>
    </header>

    <main class="account-main">
      <div class="account-container">
        <ProfilMain />
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import ProfilMain from '~/components/compte/ProfilMain.vue';
import logoIsoc from '@/assets/logoIsoc.png'

const logo = logoIsoc

definePageMeta({
  layout: false,
});
</script>

<style scoped>
.account-only {
  min-height: 100vh;
  background: var(--bg-primary);
  color: var(--text-primary);
}

.account-header {
  position: sticky;
  top: 0;
  z-index: 50;
  background: var(--bg-primary);
  border-bottom: 1px solid var(--border-color);
  height: 64px;
}

.account-header-inner {
  max-width: 1400px;
  margin: 0 auto;
  width: 100%;
  height: 64px;
  padding: 0 calc(2vw);
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 12px;
}

.brand {
  justify-self: center;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
}

.brand-logo {
  height: 56px;
  width: auto;
  object-fit: contain;
}

.back-left {
  justify-self: start;
  text-decoration: none;
  color: var(--text-primary);
  font-weight: 900;
  padding: 10px 12px;
  border-radius: 10px;
}

.back-left:hover {
  background: var(--bg-secondary);
  text-decoration: none;
}

.brand:hover {
  text-decoration: none;
}

.right-spacer {
  justify-self: end;
  width: 1px;
  height: 1px;
}

.account-main {
  background: var(--bg-primary);
}

.account-container {
  max-width: 1400px;
  margin: 0 auto;
  width: 100%;
  padding: 0 calc(2vw);
}

@media (max-width: 640px) {
  .account-header-inner { gap: 8px; }
  .back-left { padding: 10px 10px; }
  .brand-logo { height: 48px; }
}
</style>
