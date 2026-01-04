<template>
  <main class="apropos-page">
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-content">
        <h1>À propos d'AXIOME</h1>
        <p class="hero-slogan">
          Dans un monde saturé d'informations contradictoires, AXIOME vous offre un accès structuré
          et contextualisé à l'actualité francophone du conflit Ukraine-Russie. Parce qu'une information
          de qualité ne dicte pas ce qu'il faut penser, mais donne les moyens de comprendre.
        </p>
      </div>
    </section>

    <!-- Mission Section -->
    <section class="mission-section">
      <div class="content-wrapper">
        <h2>Notre mission</h2>
        <p class="lead">
          AXIOME facilite l'accès à l'information francophone sur le conflit Ukraine-Russie.
          Nous ne remplaçons pas votre esprit critique, nous l'alimentons.
        </p>
        <p>
          Le conflit Ukraine-Russie génère quotidiennement des centaines d'articles, de reportages et d'analyses.
          Face à cette abondance, il devient difficile de s'informer de manière exhaustive et équilibrée.
          AXIOME agrège, structure et contextualise ces informations provenant de plus de 50 sources françaises
          et internationales, pour vous permettre d'accéder rapidement à une vision d'ensemble.
        </p>
        <p>
          Notre conviction : une information de qualité ne dicte pas ce qu'il faut penser, mais offre les
          éléments nécessaires pour se forger sa propre opinion. Dans un contexte où la désinformation
          et la polarisation dominent, AXIOME s'efforce de présenter les faits avec nuance, en mettant en
          lumière la complexité d'un conflit qui dépasse les récits simplistes.
        </p>
        <p>
          Nous sommes indépendants de toute affiliation politique ou financière. Notre seul engagement :
          rendre l'information francophone sur ce conflit plus accessible, plus structurée, plus complète.
        </p>
      </div>
    </section>

    <!-- Methodology Section -->
    <section class="methodology-section">
      <div class="content-wrapper">
        <h2>Notre démarche</h2>
        <div class="methodology-grid">
          <div class="methodology-item">
            <h3>Agrégation multi-sources</h3>
            <p>
              Nous surveillons quotidiennement plus de 50 sources d'information : presse généraliste
              (Le Monde, Le Figaro, Libération), médias spécialisés (France 24, RFI), agences de presse
              internationales (Reuters, AFP, AP), et 27 chaînes YouTube d'analyse géopolitique.
            </p>
          </div>
          <div class="methodology-item">
            <h3>Structuration thématique</h3>
            <p>
              Les informations sont organisées par catégories (politique, militaire, humanitaire, économie)
              et formats (articles, vidéos, podcasts) pour faciliter la navigation et permettre à chacun
              de s'informer selon ses préférences.
            </p>
          </div>
          <div class="methodology-item">
            <h3>Contextualisation</h3>
            <p>
              Au-delà de l'agrégation brute, nous mettons en perspective les informations en croisant
              les sources, en identifiant les angles morts et en offrant des analyses de fond pour
              comprendre les enjeux sous-jacents.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Team Section -->
    <section class="team-section">
      <div class="content-wrapper">
        <h2>L'équipe</h2>
        <p class="team-intro">
          AXIOME est porté par une équipe pluridisciplinaire réunie autour d'une conviction commune :
          l'information de qualité est un pilier essentiel de la démocratie.
        </p>
        <div class="team-grid">
          <div class="team-member">
            <div class="member-avatar">AT</div>
            <h3>Antoine TENA</h3>
            <p class="member-role">Chef de projet & développeur</p>
            <p class="member-bio">
              Coordination et gestion de l'ensemble du projet. Développement de la plateforme web
              et rédaction de l'article de fond sur la désinformation dans le conflit.
              Co-création de la présentation du projet.
            </p>
          </div>
          <div class="team-member">
            <div class="member-avatar">NB</div>
            <h3>Nathan BARRACHIN</h3>
            <p class="member-role">Analyste juridique</p>
            <p class="member-bio">
              Rédaction de l'article sur les enjeux éthiques et juridiques du conflit Ukraine-Russie.
              Analyse des aspects légaux et des questions de droit international.
              Co-création de la présentation du projet.
            </p>
          </div>
          <div class="team-member">
            <div class="member-avatar">HA</div>
            <h3>Hiba ABDESSADAK</h3>
            <p class="member-role">Analyste militaire & design</p>
            <p class="member-bio">
              Rédaction de l'article sur les technologies militaires utilisées dans le conflit.
              Design des supports visuels. Co-création de la présentation du projet.
            </p>
          </div>
          <div class="team-member">
            <div class="member-avatar">PT</div>
            <h3>Pavel TROFYMOV</h3>
            <p class="member-role">Contributeur</p>
            <p class="member-bio">
              Membre de l'équipe projet. Co-création de la présentation du projet.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Project Note Section -->
    <section class="project-note-section">
      <div class="content-wrapper">
        <p>
          <strong>Note :</strong> AXIOME est un projet étudiant réalisé dans le cadre du cours ISOC531
          à l'université, portant sur les sociétés numériques et l'information en ligne.
        </p>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
// Page metadata
useHead({
  title: 'À propos - AXIOME',
  meta: [
    { name: 'description', content: 'Découvrez AXIOME, média indépendant dédié à l\'analyse du conflit Ukraine-Russie. Notre mission, nos valeurs et notre équipe.' }
  ]
});
</script>

<style scoped>
.apropos-page {
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
  max-width: 1000px;
  margin: 0 auto;
}

.hero-section h1 {
  font-size: 40px;
  font-weight: 800;
  margin: 0 0 24px;
  letter-spacing: -1px;
  color: #2f0538;
  text-align: center;
}

.hero-slogan {
  font-size: 18px;
  line-height: 1.7;
  color: #4a4a55;
  margin: 0;
  font-weight: 400;
  max-width: 850px;
  margin: 0 auto;
  text-align: center;
}

/* Content Sections */
section {
  padding: 60px calc(2vw);
}

.content-wrapper {
  max-width: 1000px;
  margin: 0 auto;
}

h2 {
  font-size: 30px;
  font-weight: 700;
  color: #2f0538;
  margin: 0 0 40px;
  text-align: center;
  letter-spacing: -0.3px;
}

.lead {
  font-size: 22px;
  line-height: 1.8;
  color: #1a1a1a;
  margin-bottom: 32px;
  font-weight: 600;
}

p {
  font-size: 16px;
  line-height: 1.8;
  color: #4a4a55;
  margin: 0 0 20px;
}

/* Mission Section */
.mission-section {
  background: #fff;
  padding: 70px calc(2vw);
}

/* Methodology Section */
.methodology-section {
  background: #f8f9fa;
  padding: 70px calc(2vw);
}

.methodology-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 32px;
  margin-top: 40px;
}

.methodology-item h3 {
  font-size: 18px;
  font-weight: 700;
  color: #2f0538;
  margin: 0 0 16px;
  position: relative;
  padding-left: 20px;
}

.methodology-item h3::before {
  content: '';
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 8px;
  height: 8px;
  background: #4b2faa;
  border-radius: 50%;
}

.methodology-item p {
  font-size: 15px;
  line-height: 1.7;
  color: #4a4a55;
  margin: 0;
}

/* Team Section */
.team-section {
  background: #fff;
  padding: 70px calc(2vw);
}

.team-intro {
  text-align: center;
  font-size: 16px;
  color: #666;
  margin-bottom: 48px;
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 32px;
  margin-top: 40px;
}

.team-member {
  text-align: center;
}

.member-avatar {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 32px;
  font-weight: 700;
  margin: 0 auto 20px;
  box-shadow: 0 4px 16px rgba(47, 5, 56, 0.2);
}

.team-member h3 {
  font-size: 20px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 8px;
}

.member-role {
  font-size: 14px;
  color: #4b2faa;
  font-weight: 600;
  margin: 0 0 12px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.member-bio {
  font-size: 14px;
  color: #4a4a55;
  line-height: 1.7;
  margin: 0;
}

/* Sources Section */
.sources-categories {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 24px;
  margin-top: 32px;
}

.source-category {
  background: #f8f9fa;
  padding: 24px;
  border-radius: 8px;
  border-left: 4px solid #4b2faa;
}

.source-category h4 {
  font-size: 16px;
  font-weight: 700;
  color: #2f0538;
  margin: 0 0 12px;
}

.source-category p {
  font-size: 14px;
  color: #666;
  margin: 0;
  line-height: 1.6;
}

/* Contact Section */
.contact-section {
  background: #f8f9fa;
  text-align: center;
}

.link {
  color: #4b2faa;
  font-weight: 600;
  text-decoration: none;
  border-bottom: 2px solid transparent;
  transition: border-color 0.2s;
}

.link:hover {
  border-bottom-color: #4b2faa;
}

.project-note-section {
  text-align: center;
  padding: 50px calc(2vw);
  background: #f8f9fa;
  border-top: 1px solid #e5e5e5;
}

.project-note-section p {
  font-size: 14px;
  color: #666;
  margin: 0;
  line-height: 1.7;
  max-width: 800px;
  margin: 0 auto;
}

.project-note-section strong {
  color: #2f0538;
}

/* Responsive */
@media (max-width: 768px) {
  .hero-section {
    padding: 40px calc(2vw) 35px;
  }

  .hero-section h1 {
    font-size: 28px;
    margin-bottom: 20px;
    letter-spacing: -0.5px;
  }

  .hero-slogan {
    font-size: 16px;
  }

  h2 {
    font-size: 24px;
  }

  .lead {
    font-size: 18px;
  }

  .mission-section,
  .methodology-section,
  .team-section {
    padding: 50px calc(2vw);
  }

  .project-note-section {
    padding: 40px calc(2vw);
  }

  .values-grid,
  .team-grid,
  .methodology-grid {
    grid-template-columns: 1fr;
    gap: 24px;
  }

  .member-avatar {
    width: 100px;
    height: 100px;
    font-size: 28px;
  }
}
</style>
