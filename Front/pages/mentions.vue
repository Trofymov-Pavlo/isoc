<template>
  <main class="legal-page">
    <PageHero
      title="Mentions Légales"
      subtitle="Informations légales et administratives"
      badge="Informations"
      badge-icon="⚖️"
    />

    <section class="legal-content">
      <div class="content-wrapper">
        <h2>Directeur de la publication</h2>
        <p>ISOC501 AXIOM</p>

        <h2>Hébergeur</h2>
        <p>Ce site est hébergé chez [Hébergeur à préciser]</p>

        <h2>Développement</h2>
        <p>Site développé avec Nuxt.js et Vue 3</p>

        <h2>Responsabilité</h2>
        <p>
          Les informations présentes sur ce site sont fournies à titre informatif. 
          Bien que nous nous efforçons de garantir l'exactitude de nos contenus, 
          ISOC501 AXIOM ne peut être tenu responsable de toute erreur ou omission.
        </p>

        <h2>Propriété intellectuelle</h2>
        <p>
          Tous les contenus de ce site (articles, vidéos, podcasts) sont protégés 
          par les droits d'auteur. Toute reproduction, même partielle, est interdite 
          sans autorisation préalable.
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
