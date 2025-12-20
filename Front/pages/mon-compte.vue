<template>
  <AuthShell
    hero-title="AXIOME"
    hero-subtitle="Votre espace membre sécurisé"
    eyebrow="Espace membre"
  >
    <ProfilMain />
  </AuthShell>
</template>

<script setup lang="ts">
import AuthShell from '~/components/compte/AuthShell.vue';
import ProfilMain from '~/components/compte/ProfilMain.vue';

definePageMeta({
  layout: false,
});
</script>
