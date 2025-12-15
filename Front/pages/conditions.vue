<template>
  <main class="legal-page">
    <PageHero
      title="Conditions d'Utilisation"
      subtitle="Conditions d'accès et d'utilisation du site"
      badge="Conditions"
      badge-icon="���"
    />

    <section class="legal-content">
      <div class="legal-wrapper">
        <h2>Conditions d'Utilisation</h2>
        <p>
          En accédant et en utilisant ce site, vous acceptez de respecter ces conditions d'utilisation. Si vous n'acceptez pas ces termes, veuillez ne pas utiliser ce site.
        </p>

        <h3>Utilisation Acceptable</h3>
        <p>Vous vous engagez à ne pas :</p>
        <ul>
          <li>Utiliser le site à des fins illégales ou frauduleuses</li>
          <li>Diffuser du contenu haineux, harcelant ou diffamatoire</li>
          <li>Copier ou reproduire le contenu sans autorisation</li>
          <li>Perturber le fonctionnement normal du site</li>
        </ul>

        <h3>Limitation de Responsabilité</h3>
        <p>
          Le site est fourni "tel quel" sans garanties. Nous déclinons toute responsabilité pour les dommages directs ou indirects résultant de l'utilisation du site.
        </p>

        <h3>Modifications</h3>
        <p>
          Nous nous réservons le droit de modifier ces conditions à tout moment. Les modifications seront effectives immédiatement après leur publication.
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

.legal-wrapper ul {
  margin: 16px 0 16px 24px;
  padding: 0;
  color: #4a4a55;
}

.legal-wrapper li {
  margin: 8px 0;
  line-height: 1.6;
}
</style>
