<template>
  <main class="legal-page">
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-content">
        <h1>Mentions Légales</h1>
      </div>
    </section>

    <section class="legal-content">
      <div class="legal-wrapper">
        <h2>1. Éditeur du site</h2>
        <p><strong>Nom du projet :</strong> AXIOME</p>
        <p><strong>Nature :</strong> Projet étudiant réalisé dans le cadre du cours ISOC531</p>
        <p><strong>Objet :</strong> Plateforme d'agrégation et de structuration d'informations sur le conflit Ukraine-Russie</p>

        <h2>2. Équipe projet</h2>
        <p>Le projet AXIOME est porté par une équipe de quatre étudiants :</p>
        <ul>
          <li><strong>Antoine TENA</strong> - Chef de projet & développeur</li>
          <li><strong>Nathan BARRACHIN</strong> - Analyste juridique</li>
          <li><strong>Hiba EL HAYANI</strong> - Analyste militaire & design</li>
          <li><strong>Pavel TROFYMOV</strong> - Contributeur</li>
        </ul>

        <h2>3. Hébergement</h2>
        <p><strong>Hébergeur :</strong> GitHub Pages / Vercel (selon déploiement)</p>
        <p>Le site utilise une infrastructure moderne de déploiement continu via des services d'hébergement professionnels.</p>

        <h2>4. Propriété intellectuelle</h2>
        
        <h3>Contenus agrégés</h3>
        <p>
          AXIOME agrège des contenus publics provenant de sources tierces françaises et internationales.
          Ces contenus restent la propriété exclusive de leurs auteurs et éditeurs respectifs.
          Chaque contenu agrégé est accompagné de sa source d'origine et d'un lien direct vers le contenu original.
        </p>

        <h3>Plateforme</h3>
        <p>
          Le code source, le design de l'interface, la structure de la base de données et l'ensemble
          des développements techniques de la plateforme AXIOME sont protégés par le droit d'auteur.
        </p>

        <h3>Utilisation des contenus</h3>
        <p>
          Toute reproduction, représentation, modification, publication ou adaptation de tout ou partie
          des éléments du site, quel que soit le moyen ou le procédé utilisé, est interdite sans
          autorisation écrite préalable.
        </p>

        <h2>5. Responsabilité</h2>
        
        <h3>Contenus agrégés</h3>
        <p>
          AXIOME ne peut être tenu responsable de l'exactitude, de la complétude ou de l'actualité
          des contenus agrégés depuis des sources tierces. Chaque contenu relève de la responsabilité
          de son éditeur d'origine.
        </p>

        <h3>Disponibilité du service</h3>
        <p>
          AXIOME est un projet étudiant. Nous nous efforçons de maintenir le service accessible
          mais ne pouvons garantir une disponibilité continue sans interruption.
        </p>

        <h3>Liens externes</h3>
        <p>
          Le site contient des liens vers des sites externes. AXIOME ne peut être tenu responsable
          du contenu de ces sites tiers ni des pratiques de ces sites en matière de protection
          des données personnelles.
        </p>

        <h2>6. Données personnelles</h2>
        <p>
          Pour toute information concernant la collecte et le traitement de vos données personnelles,
          veuillez consulter notre <NuxtLink to="/donnees-personnelles" class="inline-link">Politique de Confidentialité</NuxtLink>.
        </p>

        <h2>7. Cookies</h2>
        <p>
          Pour toute information concernant l'utilisation des cookies sur ce site,
          veuillez consulter notre <NuxtLink to="/cookies" class="inline-link">Politique des Cookies</NuxtLink>.
        </p>

        <h2>8. Droits de retrait</h2>
        <p>
          Si vous êtes titulaire de droits sur un contenu agrégé par AXIOME et souhaitez son retrait,
          veuillez nous contacter via notre <NuxtLink to="/contact" class="inline-link">page de contact</NuxtLink>
          en précisant l'URL du contenu concerné et la nature de vos droits.
        </p>

        <h2>9. Droit applicable</h2>
        <p>
          Les présentes mentions légales sont régies par le droit français. En cas de litige,
          les tribunaux français seront seuls compétents.
        </p>

        <h2>10. Contact</h2>
        <p>
          Pour toute question concernant ces mentions légales, veuillez nous contacter
          via notre <NuxtLink to="/contact" class="inline-link">page de contact</NuxtLink>.
        </p>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
useHead({
  title: 'Mentions Légales - AXIOME',
  meta: [
    { name: 'description', content: 'Mentions légales et informations éditoriales de la plateforme AXIOME' }
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
