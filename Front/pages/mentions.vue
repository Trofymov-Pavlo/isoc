<template>
  <main class="legal-page">
    <PageHero
      title="Mentions Légales"
      subtitle="Informations légales et administratives"
      badge="Informations"
      badge-icon="⚖️"
    />

    <section class="legal-content">
      <div class="legal-wrapper">
        <h2>Mentions Légales</h2>

        <h3>Informations sur le Site</h3>
        <p><strong>Dénomination :</strong> ISOC501 AXIOM</p>
        <p><strong>Description :</strong> Média indépendant d'analyse et de veille sur le conflit Ukraine-Russie</p>

        <h3>Propriété et Direction</h3>
        <p>Ce site est une initiative éditoriale indépendante dédiée à la couverture rigoureuse et vérifiée de l'actualité.</p>

        <h3>Hébergement</h3>
        <p>Ce site est hébergé et maintenu dans le respect des lois applicables.</p>

        <h3>Propriété Intellectuelle</h3>
        <p>Tous les contenus (textes, images, vidéos) sont la propriété d'AXIOM ou de ses contributeurs. Toute reproduction sans autorisation est interdite.</p>

        <h3>Données Personnelles</h3>
        <p>Consultez notre Politique de Confidentialité pour connaître comment nous traitons vos données.</p>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
import PageHero from '~/components/shared/PageHero.vue';
</script>

<style scoped>
.legal-page {
  min-height: 100vh;
  background: #fff;
}

.legal-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 48px calc(2vw) 60px;
}

.legal-wrapper {
  max-width: 800px;
  margin: 0 auto;
}

.legal-wrapper h2 {
  font-size: 28px;
  font-weight: 700;
  color: #2f0538;
  margin: 0 0 24px;
  padding-bottom: 16px;
  border-bottom: 2px solid #f0f0f0;
}

.legal-wrapper h3 {
  font-size: 20px;
  font-weight: 700;
  color: #2f0538;
  margin: 32px 0 16px;
}

.legal-wrapper p {
  font-size: 16px;
  line-height: 1.75;
  color: #4a4a55;
  margin: 0 0 16px;
}
</style>
