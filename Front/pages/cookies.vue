<template>
  <main class="legal-page">
    <PageHero
      title="Politique des Cookies"
      subtitle="Comment nous utilisons les cookies sur ce site"
      badge="Cookies"
      badge-icon="🍪"
    />

    <section class="legal-content">
      <div class="legal-wrapper">
        <h2>Politique des Cookies</h2>

        <h3>Qu'est-ce qu'un Cookie ?</h3>
        <p>
          Un cookie est un petit fichier texte stocké sur votre appareil (ordinateur, smartphone, tablette) 
          par votre navigateur web. Les cookies permettent aux sites web de se souvenir de vos préférences 
          et d'améliorer votre expérience utilisateur.
        </p>

        <h3>Types de Cookies que nous Utilisons</h3>

        <h4>Cookies Essentiels (Strictement Nécessaires)</h4>
        <p>
          Ces cookies sont essentiels au fonctionnement du site. Ils permettent les fonctionnalités 
          basiques comme la navigation et l'accès aux zones sécurisées. Vous ne pouvez pas les désactiver.
        </p>
        <ul>
          <li>Cookies de session</li>
          <li>Cookies d'authentification</li>
          <li>Cookies de préférences de langue</li>
        </ul>

        <h4>Cookies de Préférences</h4>
        <p>
          Ces cookies mémorisent vos préférences pour personnaliser votre expérience, 
          comme votre choix de langue ou votre préférence pour le mode sombre.
        </p>

        <h4>Cookies d'Analyse</h4>
        <p>
          Ces cookies nous aident à comprendre comment vous utilisez notre site. 
          Ils collectent des données anonymes sur le nombre de visiteurs, les pages visitées et les erreurs.
        </p>

        <h4>Cookies Publicitaires</h4>
        <p>
          Ces cookies peuvent être utilisés par nos partenaires publicitaires pour vous afficher 
          des publicités pertinentes basées sur votre historique de navigation.
        </p>

        <h3>Contrôle de Vos Cookies</h3>
        <p>
          Vous pouvez contrôler et/ou supprimer les cookies selon vos souhaits. Pour plus d'informations, 
          consultez le site <strong>aboutcookies.org</strong>.
        </p>

        <h4>Via Votre Navigateur</h4>
        <p>La plupart des navigateurs vous permettent de refuser les cookies ou de vous alerter quand un cookie est envoyé.</p>
        <ul>
          <li>Chrome : Paramètres > Confidentialité > Cookies et autres données de site</li>
          <li>Firefox : Paramètres > Vie privée et sécurité > Cookies et données de site</li>
          <li>Safari : Préférences > Confidentialité > Gérer les données de site</li>
          <li>Edge : Paramètres > Confidentialité > Cookies et autres données de site</li>
        </ul>

        <h3>Conséquences de la Désactivation des Cookies</h3>
        <p>
          Si vous désactivez les cookies essentiels, certaines fonctionnalités du site peuvent ne pas 
          fonctionner correctement. Nous vous recommandons de conserver au moins les cookies essentiels activés.
        </p>

        <h3>Cookies de Tiers</h3>
        <p>
          Notre site peut contenir des cookies d'autres domaines (par exemple, YouTube, Google Maps). 
          Nous ne sommes pas responsables de ces cookies. Consultez les politiques des tiers concernés 
          pour plus d'informations.
        </p>

        <h3>Mise à Jour de Cette Politique</h3>
        <p>
          Nous pouvons mettre à jour cette politique des cookies. Les modifications entreront en vigueur 
          dès leur publication sur le site. La dernière mise à jour a eu lieu le 1er janvier 2025.
        </p>

        <h3>Contact</h3>
        <p>
          Si vous avez des questions concernant notre utilisation des cookies, veuillez nous contacter 
          via notre formulaire de contact.
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

.legal-wrapper h4 {
  font-size: 16px;
  font-weight: 600;
  color: #2f0538;
  margin: 20px 0 12px;
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
