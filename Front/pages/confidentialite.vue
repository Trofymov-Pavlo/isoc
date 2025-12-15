<template>
  <main class="legal-page">
    <PageHero
      title="Politique de Confidentialité"
      subtitle="Comment nous protégeons vos données personnelles"
      badge="Confidentialité"
      badge-icon="�"
    />

    <section class="legal-content">
      <div class="legal-wrapper">
        <h2>Politique de Confidentialité</h2>

        <h3>Collecte de Données</h3>
        <p>Nous collectons uniquement les informations nécessaires au fonctionnement du site et à la communication avec nos utilisateurs (nom, email, message).</p>

        <h3>Utilisation des Données</h3>
        <p>Vos données sont utilisées exclusivement pour :</p>
        <ul>
          <li>Répondre à vos messages de contact</li>
          <li>Améliorer notre service</li>
          <li>Respecter nos obligations légales</li>
        </ul>

        <h3>Protection des Données</h3>
        <p>Vos données sont protégées par des mesures de sécurité appropriées. Nous ne partageons vos informations avec aucun tiers sans votre consentement explicite.</p>

        <h3>Cookies</h3>
        <p>Ce site utilise des cookies pour améliorer votre expérience utilisateur. Vous pouvez les désactiver via les paramètres de votre navigateur.</p>

        <h3>Vos Droits</h3>
        <p>Vous avez le droit d'accéder, de modifier ou de supprimer vos données personnelles. Contactez-nous pour exercer ces droits.</p>
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
