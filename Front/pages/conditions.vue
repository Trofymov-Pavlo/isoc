<template>
  <main class="legal-page">
    <PageHero
      title="Conditions d'Utilisation"
      subtitle="Conditions d'accès et d'utilisation du site"
      badge="Conditions"
      badge-icon="📋"
    />

    <section class="legal-content">
      <div class="content-wrapper">
        <h2>Acceptation des conditions</h2>
        <p>
          En accédant et en utilisant ce site, vous acceptez pleinement les conditions 
          d'utilisation exposées ci-dessous. Si vous n'acceptez pas ces conditions, 
          veuillez ne pas utiliser ce site.
        </p>

        <h2>Utilisation du contenu</h2>
        <p>
          Les contenus (articles, vidéos, podcasts) sont fournis à titre informatif 
          pour votre usage personnel. Toute utilisation commerciale ou reproduction 
          est strictement interdite sans autorisation.
        </p>

        <h2>Limitation de responsabilité</h2>
        <p>
          ISOC501 AXIOM décline toute responsabilité pour les dommages directs ou 
          indirects résultant de l'accès ou de l'utilisation de ce site. Les utilisateurs 
          utilisent le site à leurs propres risques.
        </p>

        <h2>Modification des conditions</h2>
        <p>
          ISOC501 AXIOM se réserve le droit de modifier ces conditions à tout moment. 
          Les modifications entreront en vigueur immédiatement. Votre utilisation continue 
          du site implique votre acceptation des nouvelles conditions.
        </p>

        <h2>Liens externes</h2>
        <p>
          Ce site peut contenir des liens vers d'autres sites. ISOC501 AXIOM n'est pas 
          responsable du contenu de ces sites externes et ne les endosse pas.
        </p>

        <h2>Résiliation</h2>
        <p>
          ISOC501 AXIOM se réserve le droit de refuser le service ou de résilier 
          l'accès à tout moment, avec ou sans préavis.
        </p>
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

.content-wrapper {
  max-width: 800px;
  margin: 0 auto;
}

.content-wrapper h2 {
  font-size: 24px;
  font-weight: 700;
  color: #2f0538;
  margin: 40px 0 20px;
  padding-bottom: 12px;
  border-bottom: 2px solid #f0f0f0;
}

.content-wrapper h2:first-child {
  margin-top: 0;
}

.content-wrapper p {
  font-size: 16px;
  line-height: 1.75;
  color: #4a4a55;
  margin: 0 0 16px;
}
</style>
