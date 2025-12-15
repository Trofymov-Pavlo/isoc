<template>
  <main class="apropos-page">
    <PageHero
      title="À Propos"
      subtitle="Découvrez ISOC501 AXIOM, votre source d'information sur le conflit Ukraine-Russie"
      badge="Notre mission"
      badge-icon="📌"
    />

    <section class="apropos">
      <div class="content-wrapper">
        <div class="intro-section">
          <h2>Qui sommes-nous ?</h2>
          <p>
            ISOC501 AXIOM est un projet média explorant l'actualité,
            la technologie et les enjeux sociétaux avec rigueur et indépendance.
          </p>
          <p>
            Notre objectif est de fournir des analyses claires, des dossiers
            approfondis et des formats variés (articles, vidéos, podcasts).
          </p>
        </div>

        <div class="mission-section">
          <h2>Notre mission</h2>
          <p>
            Dans un paysage médiatique fragmenté et souvent polarisé, nous nous engageons à fournir
            une information vérifiée, contextuelle et accessible sur le conflit Ukraine-Russie.
          </p>
        </div>

        <div class="values-grid">
          <div class="value-card">
            <div class="value-icon">🔍</div>
            <h3>Vérification rigoureuse</h3>
            <p>Chaque information est vérifiée et croissée avec plusieurs sources</p>
          </div>
          <div class="value-card">
            <div class="value-icon">🎯</div>
            <h3>Indépendance</h3>
            <p>Aucune affiliation politique, une analyse objective des faits</p>
          </div>
          <div class="value-card">
            <div class="value-icon">📚</div>
            <h3>Pédagogie</h3>
            <p>Expliquer les enjeux complexes de manière claire et accessible</p>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
import PageHero from '~/components/shared/PageHero.vue';
</script>

<style scoped>
.apropos-page {
  min-height: 100vh;
  background: #fff;
}

.apropos {
  max-width: 1400px;
  margin: 0 auto;
  padding: 48px calc(2vw) 60px;
}

.content-wrapper {
  max-width: 900px;
  margin: 0 auto;
}

.intro-section,
.mission-section {
  margin-bottom: 48px;
}

.intro-section h2,
.mission-section h2 {
  font-size: 28px;
  font-weight: 700;
  color: #2f0538;
  margin: 0 0 20px;
}

.intro-section p,
.mission-section p {
  font-size: 16px;
  line-height: 1.75;
  color: #4a4a55;
  margin: 0 0 16px;
}

.values-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-top: 48px;
}

.value-card {
  background: #fff;
  border: 1px solid #e5e5e5;
  border-radius: 12px;
  padding: 32px 24px;
  text-align: center;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.value-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  border-color: #d0d0d0;
}

.value-icon {
  font-size: 48px;
  margin-bottom: 16px;
}

.value-card h3 {
  font-size: 18px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 12px;
}

.value-card p {
  font-size: 14px;
  line-height: 1.6;
  color: #666;
  margin: 0;
}

@media (max-width: 968px) {
  .values-grid {
    grid-template-columns: 1fr;
  }
}
</style>
