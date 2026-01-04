<template>
  <AuthShell
    hero-title="AXIOME"
    hero-subtitle="Rejoignez la veille indépendante"
    eyebrow="Création de compte"
  >
    <CompteMainSignup />
  </AuthShell>
</template>

<script setup lang="ts">
import AuthShell from '~/components/compte/AuthShell.vue';
import CompteMainSignup from '~/components/compte/MainSignup.vue';

definePageMeta({
  layout: false,
});
</script>
