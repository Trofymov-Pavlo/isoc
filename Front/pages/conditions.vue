<template>
  <main class="legal-page">
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-content">
        <h1>Conditions Générales d'Utilisation</h1>
      </div>
    </section>

    <section class="legal-content">
      <div class="legal-wrapper">
        <h2>1. Objet</h2>
        <p>
          Les présentes Conditions Générales d'Utilisation (CGU) régissent l'accès et l'utilisation
          de la plateforme AXIOME, un projet étudiant d'agrégation d'informations sur le conflit
          Ukraine-Russie réalisé dans le cadre du cours ISOC531.
        </p>

        <h2>2. Acceptation des conditions</h2>
        <p>
          En accédant à ce site, vous acceptez sans réserve les présentes CGU. Si vous n'acceptez
          pas ces conditions, veuillez ne pas utiliser le site.
        </p>

        <h2>3. Description du service</h2>
        <p>
          AXIOME est une plateforme d'agrégation et de structuration d'informations publiques
          provenant de sources françaises et internationales. Le service propose :
        </p>
        <ul>
          <li>L'agrégation d'articles, vidéos et contenus multimédias</li>
          <li>La structuration thématique de l'information</li>
          <li>Un système de favoris pour les utilisateurs authentifiés</li>
          <li>Des flux RSS personnalisés</li>
        </ul>

        <h2>4. Utilisation acceptable</h2>
        <p>Vous vous engagez à :</p>
        <ul>
          <li>Utiliser le site conformément aux lois en vigueur</li>
          <li>Ne pas tenter d'accéder de manière non autorisée à des parties sécurisées du site</li>
          <li>Ne pas perturber le fonctionnement normal de la plateforme</li>
          <li>Ne pas extraire massivement les données (scraping non autorisé)</li>
          <li>Respecter les droits de propriété intellectuelle des contenus agrégés</li>
        </ul>

        <h2>5. Propriété intellectuelle</h2>
        <p>
          AXIOME agrège des contenus provenant de sources tierces. Chaque contenu reste la propriété
          de son auteur ou éditeur d'origine. La plateforme elle-même (code source, design, interface)
          est protégée par les droits d'auteur.
        </p>
        <p>
          Les contenus agrégés sont affichés avec leurs sources d'origine et liens directs.
          AXIOME ne revendique aucun droit sur ces contenus.
        </p>

        <h2>6. Comptes utilisateurs</h2>
        <p>
          La création d'un compte permet d'accéder à des fonctionnalités supplémentaires
          (favoris, personnalisation). Vous êtes responsable de la confidentialité de vos
          identifiants de connexion.
        </p>

        <h2>7. Limitation de responsabilité</h2>
        <p>
          AXIOME est un projet étudiant fourni "tel quel" sans garantie d'aucune sorte.
          Nous nous efforçons d'assurer la disponibilité du service mais ne pouvons garantir
          son fonctionnement ininterrompu.
        </p>
        <p>
          Nous déclinons toute responsabilité concernant :
        </p>
        <ul>
          <li>L'exactitude des contenus agrégés depuis des sources tierces</li>
          <li>Les interruptions de service</li>
          <li>Les pertes de données</li>
          <li>Les dommages directs ou indirects liés à l'utilisation du site</li>
        </ul>

        <h2>8. Contenus agrégés</h2>
        <p>
          AXIOME agrège automatiquement des contenus publics depuis des sources tierces.
          Si vous êtes titulaire de droits sur un contenu agrégé et souhaitez son retrait,
          contactez-nous via notre page de contact.
        </p>

        <h2>9. Modifications des CGU</h2>
        <p>
          Nous nous réservons le droit de modifier ces conditions à tout moment.
          Les modifications seront effectives dès leur publication sur cette page.
          L'utilisation continue du site après modification vaut acceptation des nouvelles conditions.
        </p>

        <h2>10. Droit applicable</h2>
        <p>
          Les présentes CGU sont régies par le droit français. Tout litige sera soumis
          aux tribunaux compétents.
        </p>

        <h2>11. Contact</h2>
        <p>
          Pour toute question concernant ces conditions d'utilisation, veuillez nous contacter
          via notre <NuxtLink to="/contact" class="inline-link">page de contact</NuxtLink>.
        </p>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
useHead({
  title: 'Conditions Générales d\'Utilisation - AXIOME',
  meta: [
    { name: 'description', content: 'Conditions générales d\'utilisation de la plateforme AXIOME' }
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

  p, li {
    font-size: 15px;
  }
}
</style>
