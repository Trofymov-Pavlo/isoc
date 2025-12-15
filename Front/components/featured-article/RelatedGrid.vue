<template>
  <section class="related-section">
    <div class="section-container">
      <h2 class="section-title">Articles connexes</h2>
      <div class="related-grid">
        <article class="related-card" v-for="item in items" :key="item.title">
          <div class="related-image">{{ item.icon }}</div>
          <h3 class="related-title">{{ item.title }}</h3>
          <p class="related-desc">{{ item.desc }}</p>
          <a href="#" class="read-more">Lire l'article →</a>
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
.related-section {
  margin-top: 64px;
  padding-top: 48px;
  border-top: 2px solid #f0f0f0;
}

.section-container {
  max-width: 100%;
}

.section-title {
  font-size: 28px;
  font-weight: 700;
  color: #2f0538;
  margin: 0 0 32px;
}

.related-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.related-card {
  background: #fff;
  border: 1px solid #e5e5e5;
  border-radius: 12px;
  padding: 28px;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  gap: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.related-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  border-color: #d0d0d0;
}

.related-image {
  font-size: 48px;
  margin-bottom: 8px;
}

.related-title {
  font-size: 18px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0;
  line-height: 1.3;
}

.related-desc {
  font-size: 14px;
  color: #666;
  line-height: 1.6;
  margin: 0;
  flex: 1;
}

.read-more {
  color: #2f0538;
  text-decoration: none;
  font-weight: 600;
  font-size: 14px;
  transition: all 0.2s ease;
  margin-top: 8px;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.read-more:hover {
  color: #ff6b6b;
  gap: 8px;
}

@media (max-width: 968px) {
  .related-grid {
    grid-template-columns: 1fr;
  }
}

@media (min-width: 969px) and (max-width: 1200px) {
  .related-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>
