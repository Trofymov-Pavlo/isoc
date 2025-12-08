<template>
  <section class="analysis">
    <div class="section-container">
      <h2 class="section-title">Analyses et décryptage</h2>
      <div class="analysis-grid">
        <article class="analysis-card" v-for="n in 3" :key="n">
          <div class="analysis-image"></div>
          <div class="analysis-content">
            <span class="analysis-badge">Analyse</span>
            <h3 class="analysis-title">Analyse {{ n }}</h3>
            <p class="analysis-author">Par un expert</p>
            <p class="analysis-excerpt">Vidéo à venir sur le conflit Ukraine-Russie.</p>
            <a :href="'#video-' + n" class="video-link" target="_blank">Voir la vidéo</a>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
</script>

<style scoped>
.analysis {
  background: #f9f9f9;
  padding: 48px 20px;
}

.section-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.section-title {
  margin: 0;
  font-size: 28px;
  font-weight: 700;
  color: #2f0538;
  margin-bottom: 32px;
  padding-top: 48px;
}

.analysis-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.analysis-card {
  background: #fff;
  border-radius: 10px;
  overflow: hidden;
  transition: all 0.3s ease;
  cursor: pointer;
}

.analysis-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.analysis-image {
  width: 100%;
  aspect-ratio: 16/9;
  background: linear-gradient(135deg, #2f0538, #4b2faa);
}

.analysis-content {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.analysis-badge {
  display: inline-block;
  background: #2f0538;
  color: #fff;
  padding: 6px 12px;
  border-radius: 4px;
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  width: fit-content;
}

.analysis-title {
  margin: 0;
  font-size: 16px;
  font-weight: 700;
  color: #1a1a1a;
  line-height: 1.4;
}

.analysis-author {
  margin: 0;
  font-size: 12px;
  color: #7b5ce0;
  font-weight: 600;
}

.analysis-excerpt {
  margin: 0;
  font-size: 13px;
  color: #666;
  line-height: 1.5;
}

@media (max-width: 1100px) {
  .analysis-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 680px) {
  .section-title {
    font-size: 22px;
  }

  .analysis-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .section-title {
    font-size: 18px;
    padding-top: 24px;
  }
}
</style>
