<template>
  <section class="related-section">
    <div class="section-container">
      <h2 class="section-title">Articles connexes</h2>
      <div class="related-grid">
        <article class="related-card" v-for="item in items" :key="item.title">
          <div class="related-image">{{ item.icon }}</div>
          <h3 class="related-title">{{ item.title }}</h3>
          <p class="related-desc">{{ item.desc }}</p>
        </article>
      </div>
    </div>
  </section>
</template>
<script setup lang="ts">
const items = [
  { icon: '📡', title: 'Propagande militaire et narratives de conflit', desc: 'Comment les forces militaires utilisent la narration pour justifier et maintenir le soutien' },
  { icon: '🤖', title: "Bots, comptes fantômes et manipulation d'algorithmes", desc: "Les technologies d'amplification artificielles de contenu" },
  { icon: '🔍', title: 'Fact-checking et vérification : Guide pratique', desc: 'Comment vérifier les informations sur le conflit' }
];
</script>
<style scoped>
.related-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}
.related-card{border:1px solid #eee;padding:1rem;border-radius:.5rem}
.related-image{font-size:2rem}
</style>
