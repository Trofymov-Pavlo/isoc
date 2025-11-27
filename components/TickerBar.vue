<template>
  <div class="ticker">
    <div class="ticker-inner">
      <div class="tick-item" v-for="(t, i) in items" :key="i">{{ t }}</div>
    </div>
  </div>
</template>

<script setup>
const items = [
  "14:45 Hongkong : le bilan du violent incendie monte à 65 morts",
  "14:30 Inde : la Chine réitère ses revendications sur l'Arunachal Pradesh",
  "14:17 LIVE Guerre en Ukraine : les dernières informations",
  "14:11 Emmanuel Macron en Isère : suivez les annonces"
]
</script>

<style scoped>
.ticker { background:#0f5f72; color:white; padding:10px 0; font-size:13px }
.ticker-inner { display:flex; gap:28px; max-width:1060px; margin:0 auto; padding:0 20px }
.tick-item { flex:0 0 auto }
</style>
