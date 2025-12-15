<template>
  <main class="legal-page">
    <PageHero
      title="Politique de Confidentialité"
      subtitle="Comment nous protégeons vos données"
      badge="Confidentialité"
      badge-icon="🔒"
    />

    <section class="legal-content">
      <div class="content-wrapper">
        <h2>Collecte des données</h2>
        <p>
          ISOC501 AXIOM collecte uniquement les données nécessaires pour le fonctionnement 
          du site et pour améliorer votre expérience. Nous ne collectons pas d'informations 
          personnelles sans votre consentement.
        </p>

        <h2>Utilisation des données</h2>
        <p>
          Les données collectées sont utilisées uniquement à des fins d'amélioration du service 
          et de communication. Nous ne partageons vos données avec aucun tiers sans votre 
          consentement explicite.
        </p>

        <h2>Cookies</h2>
        <p>
          Ce site utilise des cookies pour améliorer votre expérience. Vous pouvez contrôler 
          l'utilisation des cookies dans les paramètres de votre navigateur.
        </p>

        <h2>Droits de l'utilisateur</h2>
        <p>
          Conformément aux lois sur la protection des données, vous disposez de droits concernant 
          vos données personnelles, notamment le droit d'accès, de modification et de suppression.
        </p>

        <h2>Sécurité</h2>
        <p>
          Nous mettons en place des mesures de sécurité appropriées pour protéger vos données 
          contre les accès non autorisés, l'altération, la divulgation ou la destruction.
        </p>

        <h2>Contact</h2>
        <p>
          Pour toute question concernant votre confidentialité ou l'utilisation de vos données, 
          veuillez nous <a href="/Contact">contacter</a>.
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

.content-wrapper a {
  color: #2f0538;
  text-decoration: none;
  font-weight: 600;
  transition: color 0.2s ease;
}

.content-wrapper a:hover {
  color: #ff6b6b;
}
</style>
