<template>
  <main class="legal-page">
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-content">
        <h1>Politique des Cookies</h1>
      </div>
    </section>

    <section class="legal-content">
      <div class="legal-wrapper">
        <h2>1. Qu'est-ce qu'un cookie ?</h2>
        <p>
          Un cookie est un petit fichier texte déposé sur votre appareil (ordinateur, smartphone, tablette)
          lors de la visite d'un site web. Les cookies permettent au site de mémoriser vos préférences
          et d'améliorer votre expérience de navigation.
        </p>

        <h2>2. Types de cookies utilisés sur AXIOME</h2>

        <h3>Cookies strictement nécessaires</h3>
        <p>
          Ces cookies sont essentiels au fonctionnement du site. Ils permettent l'utilisation
          des fonctionnalités de base comme l'authentification et la sauvegarde de vos favoris.
        </p>
        <ul>
          <li><strong>Cookies de session</strong> : maintiennent votre connexion active</li>
          <li><strong>Cookies d'authentification (JWT)</strong> : stockent votre token de connexion sécurisé</li>
          <li><strong>Cookies de préférences</strong> : mémorisent vos paramètres de langue et de thème</li>
        </ul>
        <p>
          Ces cookies ne peuvent pas être désactivés car ils sont indispensables au bon fonctionnement
          du site. Ils ne sont pas utilisés à des fins de suivi ou de publicité.
        </p>

        <h3>Cookies de fonctionnalité</h3>
        <p>
          Ces cookies permettent d'améliorer votre expérience utilisateur en mémorisant vos choix :
        </p>
        <ul>
          <li>Préférence de thème (clair/sombre)</li>
          <li>Catégories favorites sélectionnées</li>
          <li>Paramètres d'affichage personnalisés</li>
        </ul>

        <h3>Cookies analytiques</h3>
        <p>
          AXIOME n'utilise actuellement pas de cookies analytiques tiers. Les données de navigation
          anonymes peuvent être collectées via les logs serveur pour des analyses internes du projet.
        </p>

        <h2>3. Durée de conservation</h2>
        <p>Les cookies utilisés sur AXIOME ont les durées de conservation suivantes :</p>
        <ul>
          <li><strong>Cookies de session</strong> : supprimés à la fermeture du navigateur</li>
          <li><strong>Token d'authentification</strong> : 7 jours maximum</li>
          <li><strong>Préférences utilisateur</strong> : 365 jours</li>
        </ul>

        <h2>4. Gestion de vos cookies</h2>
        
        <h3>Paramétrage du navigateur</h3>
        <p>
          Vous pouvez configurer votre navigateur pour refuser les cookies ou être alerté
          lors de l'enregistrement d'un cookie. Voici les liens vers les pages d'aide des
          principaux navigateurs :
        </p>
        <ul>
          <li><strong>Chrome</strong> : Paramètres → Confidentialité et sécurité → Cookies</li>
          <li><strong>Firefox</strong> : Options → Vie privée et sécurité → Cookies</li>
          <li><strong>Safari</strong> : Préférences → Confidentialité</li>
          <li><strong>Edge</strong> : Paramètres → Confidentialité → Cookies</li>
        </ul>

        <h3>Impact du refus des cookies</h3>
        <p>
          Le refus des cookies strictement nécessaires peut entraîner l'impossibilité d'utiliser
          certaines fonctionnalités du site, notamment :
        </p>
        <ul>
          <li>La connexion à votre compte</li>
          <li>La sauvegarde de vos favoris</li>
          <li>La mémorisation de vos préférences</li>
        </ul>

        <h2>5. Consentement</h2>
        <p>
          En utilisant AXIOME, vous consentez à l'utilisation des cookies strictement nécessaires
          au fonctionnement du site. Pour les cookies facultatifs, votre consentement explicite
          est requis via le bandeau de gestion des cookies affiché lors de votre première visite.
        </p>

        <h2>6. Modifications de la politique</h2>
        <p>
          Nous nous réservons le droit de modifier cette politique à tout moment. Les modifications
          seront effectives dès leur publication sur cette page. Nous vous encourageons à consulter
          régulièrement cette page pour rester informé.
        </p>

        <h2>7. Contact</h2>
        <p>
          Pour toute question concernant notre utilisation des cookies, veuillez nous contacter
          via notre <NuxtLink to="/contact" class="inline-link">page de contact</NuxtLink>.
        </p>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
useHead({
  title: 'Politique des Cookies - AXIOME',
  meta: [
    { name: 'description', content: 'Politique d\'utilisation des cookies sur la plateforme AXIOME' }
  ]
});
</script>

<style scoped>
.legal-page {
  min-height: 100vh;
  background: #fff;
}

/* Hero Section */
.hero-section {
  background: linear-gradient(180deg, #f3f4f6 0%, #ffffff 100%);
  padding: 60px calc(2vw) 50px;
  position: relative;
}

.hero-section::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 3px;
  background: linear-gradient(90deg, #2f0538 0%, #4b2faa 100%);
}

.hero-content {
  max-width: 900px;
  margin: 0 auto;
}

.hero-section h1 {
  font-size: 40px;
  font-weight: 800;
  margin: 0;
  letter-spacing: -1px;
  color: #2f0538;
  text-align: center;
}

/* Legal Content */
.legal-content {
  max-width: 900px;
  margin: 0 auto;
  padding: 60px calc(2vw);
}

.legal-wrapper {
  line-height: 1.8;
}

.last-update {
  font-size: 14px;
  color: #666;
  margin-bottom: 32px;
  padding: 12px 20px;
  background: #f8f9fa;
  border-left: 3px solid #4b2faa;
  border-radius: 4px;
}

h2 {
  font-size: 24px;
  font-weight: 700;
  color: #2f0538;
  margin: 40px 0 20px;
  padding-top: 20px;
}

h2:first-of-type {
  margin-top: 0;
  padding-top: 0;
}

h3 {
  font-size: 20px;
  font-weight: 600;
  color: #2f0538;
  margin: 24px 0 16px;
}

p {
  font-size: 16px;
  line-height: 1.8;
  color: #4a4a55;
  margin: 0 0 16px;
}

ul {
  margin: 16px 0;
  padding-left: 24px;
}

li {
  font-size: 16px;
  line-height: 1.8;
  color: #4a4a55;
  margin-bottom: 8px;
}

strong {
  font-weight: 600;
  color: #2f0538;
}

.inline-link {
  color: #4b2faa;
  font-weight: 600;
  text-decoration: none;
  border-bottom: 1px solid transparent;
  transition: border-color 0.2s;
}

.inline-link:hover {
  border-bottom-color: #4b2faa;
}

.external-link {
  color: #4b2faa;
  font-weight: 500;
  text-decoration: underline;
  text-decoration-style: dotted;
}

.external-link:hover {
  text-decoration-style: solid;
}

@media (max-width: 768px) {
  .hero-section {
    padding: 50px calc(2vw) 40px;
  }

  .hero-section h1 {
    font-size: 30px;
    letter-spacing: -0.7px;
  }

  .legal-content {
    padding: 50px calc(2vw);
  }

  h2 {
    font-size: 20px;
  }

  h3 {
    font-size: 18px;
  }

  p, li {
    font-size: 15px;
  }
}
</style>
