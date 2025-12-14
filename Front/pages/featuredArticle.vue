<template>
  <main class="featured-article-page">
    <!-- Header (utilise le header/subheader existants via layout) -->
    
    <!-- Article Hero Section -->
    <section class="article-hero">
      <div class="hero-container">
        <div class="hero-badge">
          <span class="badge-icon">📰</span>
          Article en vedette
        </div>
        <h1 class="article-title">La guerre de l'information : Stratégies d'influence et perceptions du conflit</h1>
        <p class="article-subtitle">Comment les stratégies d'influence façonnent la narrative du conflit Ukraine-Russie et manipulent les perceptions</p>
        
        <div class="article-meta">
          <div class="author-info">
            <span class="author-avatar">AT</span>
            <div class="author-details">
              <span class="author-name">Antoine TENA</span>
              <span class="publish-date">14 décembre 2025</span>
            </div>
          </div>
          <div class="reading-time">
            <span class="icon">⏱️</span>
            <span>12 min de lecture</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Article Featured Image -->
    <section class="article-image-section">
      <img src="@/assets/logoIsoc.png" alt="Guerre de l'information" class="featured-image" />
    </section>

    <!-- Article Content -->
    <article class="article-content">
      <div class="content-container">
        <!-- Table of Contents -->
        <aside class="table-of-contents">
          <h3 class="toc-title">Sommaire</h3>
          <nav class="toc-nav">
            <a href="#introduction" class="toc-link">Introduction</a>
            <a href="#strategies" class="toc-link">Stratégies d'influence</a>
            <a href="#social-media" class="toc-link">Réseaux sociaux</a>
            <a href="#deepfakes" class="toc-link">Deepfakes et désinformation</a>
            <a href="#osint" class="toc-link">OSINT et fact-checking</a>
            <a href="#impact" class="toc-link">Impact sur les perceptions</a>
            <a href="#conclusion" class="toc-link">Conclusion</a>
          </nav>
        </aside>

        <!-- Main Article Content -->
        <div class="main-content">
          <!-- Introduction -->
          <section class="article-section" id="introduction">
            <h2 class="section-title">Introduction</h2>
            <p class="section-text">
              Le conflit Ukraine-Russie ne se joue pas uniquement sur le terrain militaire. Une bataille informationnelle tout aussi cruciale se déploie sur les réseaux sociaux, les médias traditionnels et les plateformes numériques. Les stratégies d'influence, la désinformation coordonnée et la manipulation des perceptions façonnent la narrative globale du conflit.
            </p>
            <p class="section-text">
              Cet article explore comment les acteurs du conflit utilisent les technologies modernes - deepfakes, OSINT, et campagnes de fact-checking - pour contrôler le récit et influencer l'opinion publique internationale.
            </p>
          </section>

          <!-- Stratégies d'influence -->
          <section class="article-section" id="strategies">
            <h2 class="section-title">Stratégies d'influence et campagnes informationnelles</h2>
            <p class="section-text">
              Les stratégies d'influence utilisées dans le contexte du conflit Ukraine-Russie comprennent:
            </p>
            
            <div class="content-box highlight-box">
              <h3 class="box-title">Tactiques principales</h3>
              <ul class="box-list">
                <li><strong>Amplification de naratives</strong> - Promotion sélective de certains récits</li>
                <li><strong>Astroturfing</strong> - Création de mouvements sociaux artificiels</li>
                <li><strong>Campagnes de désinformation</strong> - Propagation coordonnée de fausses informations</li>
                <li><strong>Contournement de modération</strong> - Utilisation de bots et comptes fantômes</li>
              </ul>
            </div>

            <p class="section-text">
              Chaque camp utilise ces techniques pour renforcer sa légitimité et miner la crédibilité de l'adversaire.
            </p>
          </section>

          <!-- Réseaux Sociaux -->
          <section class="article-section" id="social-media">
            <h2 class="section-title">Rôle des réseaux sociaux : Telegram, X et autres plateformes</h2>
            <p class="section-text">
              Les réseaux sociaux jouent un rôle central dans la diffusion de l'information et la manipulation des perceptions.
            </p>

            <div class="platforms-grid">
              <div class="platform-card">
                <div class="platform-icon">✈️</div>
                <h3 class="platform-name">Telegram</h3>
                <p class="platform-desc">Utilisé pour les communications en temps réel, les canaux de propagande militaire et les appels à l'action</p>
              </div>

              <div class="platform-card">
                <div class="platform-icon">𝕏</div>
                <h3 class="platform-name">X (anciennement Twitter)</h3>
                <p class="platform-desc">Plate-forme de choix pour les théories du complot, les campagnes de désinformation et les débats polarisés</p>
              </div>

              <div class="platform-card">
                <div class="platform-icon">f</div>
                <h3 class="platform-name">Facebook</h3>
                <p class="platform-desc">Cible des campagnes de désinformation visant les publics plus âgés</p>
              </div>

              <div class="platform-card">
                <div class="platform-icon">▶️</div>
                <h3 class="platform-name">YouTube</h3>
                <p class="platform-desc">Héberge des vidéos de propagande, des documentaires alternatifs et des témoignages</p>
              </div>
            </div>
          </section>

          <!-- Deepfakes -->
          <section class="article-section" id="deepfakes">
            <h2 class="section-title">Deepfakes et technologie de désinformation</h2>
            <p class="section-text">
              Les deepfakes représentent une menace émergente dans la guerre informationnelle. Capables de créer des vidéos persuasives de personnalités politiques et militaires, ils peuvent rapidement se propager sur les réseaux sociaux.
            </p>

            <div class="content-box warning-box">
              <h3 class="box-title">⚠️ Risques identifiés</h3>
              <p>Les deepfakes peuvent être utilisés pour:</p>
              <ul class="box-list">
                <li>Discréditer des leaders politiques ou militaires</li>
                <li>Créer des incidents diplomatiques fictifs</li>
                <li>Inciter à des actions violentes</li>
                <li>Semer la confusion et la méfiance</li>
              </ul>
            </div>

            <p class="section-text">
              Face à cette menace, le fact-checking et la vérification d'authenticité deviennent essentiels.
            </p>
          </section>

          <!-- OSINT et Fact-checking -->
          <section class="article-section" id="osint">
            <h2 class="section-title">OSINT, Fact-checking et lutte contre la désinformation</h2>
            <p class="section-text">
              L'OSINT (Open Source Intelligence) et le fact-checking jouent un rôle crucial dans la contre-désinformation.
            </p>

            <div class="content-box info-box">
              <h3 class="box-title">Techniques de vérification</h3>
              <ul class="box-list">
                <li><strong>Vérification d'images</strong> - Recherche inversée et analyse de métadonnées</li>
                <li><strong>Vérification de sources</strong> - Traçabilité des récits originaires</li>
                <li><strong>Analyse linguistique</strong> - Détection des bots et comptes de propagande</li>
                <li><strong>Vérification vidéo</strong> - Détection de deepfakes et d'édition</li>
              </ul>
            </div>

            <p class="section-text">
              Des organisations comme Bellingcat, StopFake et des équipes d'OSINT indépendantes contribuent activement à la vérification des informations et à la documentation des faits.
            </p>
          </section>

          <!-- Impact sur les perceptions -->
          <section class="article-section" id="impact">
            <h2 class="section-title">Impact sur les perceptions et l'opinion publique</h2>
            <p class="section-text">
              La guerre informationnelle a un impact direct sur la perception du conflit par le public international. Les études montrent que:
            </p>

            <ul class="section-list">
              <li>Les publics fragmentés reçoivent des informations contradictoires en fonction de leurs bulles de filtre</li>
              <li>La polarisation de l'opinion augmente avec la désinformation</li>
              <li>Les perceptions influencent les politiques nationales et internationales</li>
              <li>La confiance dans les institutions médiatiques décline</li>
            </ul>

            <p class="section-text">
              Comprendre ces mécanismes est essentiel pour les citoyens et les décideurs politiques.
            </p>
          </section>

          <!-- Conclusion -->
          <section class="article-section" id="conclusion">
            <h2 class="section-title">Conclusion</h2>
            <p class="section-text">
              La guerre de l'information est tout aussi importante que le conflit militaire. Les stratégies d'influence, les réseaux sociaux comme vecteurs de propagande, et les technologies comme les deepfakes façonnent notre compréhension du conflit Ukraine-Russie.
            </p>
            <p class="section-text">
              Seule une approche critique, basée sur le fact-checking rigoureux et l'OSINT, permet aux citoyens de naviguer ce paysage informatif complexe et de former des opinions éclairées.
            </p>
          </section>

          <!-- Share Section -->
          <section class="share-section">
            <h3 class="share-title">Partager cet article</h3>
            <div class="share-buttons">
              <a href="#" class="share-btn twitter" title="Partager sur X">X</a>
              <a href="#" class="share-btn facebook" title="Partager sur Facebook">Facebook</a>
              <a href="#" class="share-btn linkedin" title="Partager sur LinkedIn">LinkedIn</a>
              <a href="#" class="share-btn telegram" title="Partager sur Telegram">Telegram</a>
            </div>
          </section>
        </div>
      </div>
    </article>

    <!-- Related Articles -->
    <section class="related-section">
      <div class="section-container">
        <h2 class="section-title">Articles connexes</h2>
        <div class="related-grid">
          <article class="related-card">
            <div class="related-image">📡</div>
            <h3 class="related-title">Propagande militaire et narratives de conflit</h3>
            <p class="related-desc">Comment les forces militaires utilisent la narration pour justifier et maintenir le soutien</p>
          </article>
          <article class="related-card">
            <div class="related-image">🤖</div>
            <h3 class="related-title">Bots, comptes fantômes et manipulation d'algorithmes</h3>
            <p class="related-desc">Les technologies d'amplification artificielles de contenu</p>
          </article>
          <article class="related-card">
            <div class="related-image">🔍</div>
            <h3 class="related-title">Fact-checking et vérification : Guide pratique</h3>
            <p class="related-desc">Comment vérifier les informations sur le conflit</p>
          </article>
        </div>
      </div>
    </section>

    <!-- Newsletter Section -->
    <section class="newsletter-section">
      <div class="section-container newsletter-box">
        <h2 class="newsletter-title">Restez informé</h2>
        <p class="newsletter-desc">Recevez les dernières analyses et articles sur le conflit Ukraine-Russie</p>
        <div class="newsletter-form">
          <input type="email" placeholder="Votre adresse email" class="newsletter-input" />
          <button class="newsletter-btn">S'abonner</button>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
// La page utilise le layout par défaut qui inclut header et subheader
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.featured-article-page {
  background: #ffffff;
  min-height: 100vh;
}

/* Hero Section */
.article-hero {
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  color: #fff;
  padding: 60px 20px;
}

.hero-container {
  max-width: 900px;
  margin: 0 auto;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.15);
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  margin-bottom: 20px;
}

.badge-icon {
  font-size: 14px;
}

.article-title {
  font-size: 48px;
  font-weight: 800;
  line-height: 1.2;
  margin-bottom: 16px;
  letter-spacing: -0.5px;
}

.article-subtitle {
  font-size: 18px;
  opacity: 0.95;
  margin-bottom: 32px;
  line-height: 1.6;
}

.article-meta {
  display: flex;
  align-items: center;
  gap: 32px;
  padding-top: 24px;
  border-top: 1px solid rgba(255, 255, 255, 0.2);
}

.author-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.author-avatar {
  width: 44px;
  height: 44px;
  background: rgba(255, 255, 255, 0.25);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 14px;
}

.author-details {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.author-name {
  font-weight: 600;
}

.publish-date {
  font-size: 13px;
  opacity: 0.9;
}

.reading-time {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  opacity: 0.9;
}

/* Featured Image */
.article-image-section {
  max-width: 100%;
  height: 500px;
  overflow: hidden;
  background: #f5f5f5;
}

.featured-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Article Content */
.article-content {
  padding: 60px 20px;
}

.content-container {
  max-width: 900px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 250px 1fr;
  gap: 40px;
}

/* Table of Contents */
.table-of-contents {
  position: sticky;
  top: 80px;
  height: fit-content;
}

.toc-title {
  margin: 0 0 16px;
  font-size: 14px;
  font-weight: 700;
  text-transform: uppercase;
  color: #2f0538;
  letter-spacing: 0.5px;
}

.toc-nav {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.toc-link {
  color: #666;
  text-decoration: none;
  font-size: 13px;
  line-height: 1.6;
  padding: 6px 0;
  border-left: 2px solid transparent;
  padding-left: 12px;
  transition: all 0.22s ease;
}

.toc-link:hover {
  color: #2f0538;
  border-left-color: #7b5ce0;
  padding-left: 16px;
}

/* Main Content */
.main-content {
  display: flex;
  flex-direction: column;
  gap: 40px;
}

.article-section {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.section-title {
  font-size: 32px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0;
  line-height: 1.2;
}

.section-text {
  font-size: 16px;
  line-height: 1.8;
  color: #555;
  margin: 0;
}

.section-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.section-list li {
  font-size: 16px;
  line-height: 1.7;
  color: #555;
  padding-left: 24px;
  position: relative;
}

.section-list li:before {
  content: "→";
  position: absolute;
  left: 0;
  color: #7b5ce0;
  font-weight: 700;
}

/* Content Boxes */
.content-box {
  padding: 24px;
  border-radius: 10px;
  background: #f9f9f9;
  border-left: 4px solid #7b5ce0;
}

.highlight-box {
  background: linear-gradient(135deg, rgba(123, 92, 224, 0.05), rgba(123, 92, 224, 0.02));
}

.warning-box {
  border-left-color: #ff9800;
  background: rgba(255, 152, 0, 0.05);
}

.info-box {
  border-left-color: #2196f3;
  background: rgba(33, 150, 243, 0.05);
}

.box-title {
  font-size: 16px;
  font-weight: 700;
  color: #2f0538;
  margin: 0 0 12px;
}

.box-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.box-list li {
  font-size: 14px;
  line-height: 1.6;
  color: #555;
}

/* Platforms Grid */
.platforms-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin: 20px 0;
}

.platform-card {
  background: #f9f9f9;
  padding: 24px;
  border-radius: 10px;
  text-align: center;
  border: 2px solid #f0f0f0;
  transition: all 0.3s ease;
}

.platform-card:hover {
  border-color: #7b5ce0;
  box-shadow: 0 4px 12px rgba(123, 92, 224, 0.1);
}

.platform-icon {
  font-size: 36px;
  margin-bottom: 12px;
}

.platform-name {
  font-size: 16px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 8px;
}

.platform-desc {
  font-size: 13px;
  color: #666;
  line-height: 1.5;
  margin: 0;
}

/* Share Section */
.share-section {
  padding: 32px 0;
  border-top: 1px solid #e5e5e5;
  border-bottom: 1px solid #e5e5e5;
  margin-top: 40px;
}

.share-title {
  font-size: 16px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 16px;
}

.share-buttons {
  display: flex;
  align-items: center;
  gap: 12px;
}

.share-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  font-size: 12px;
  transition: all 0.22s ease;
}

.share-btn.twitter {
  background: #000;
  color: #fff;
}

.share-btn.twitter:hover {
  background: #222;
}

.share-btn.facebook {
  background: #1877f2;
  color: #fff;
}

.share-btn.facebook:hover {
  background: #166fe5;
}

.share-btn.linkedin {
  background: #0a66c2;
  color: #fff;
}

.share-btn.linkedin:hover {
  background: #095195;
}

.share-btn.telegram {
  background: #0088cc;
  color: #fff;
}

.share-btn.telegram:hover {
  background: #0077aa;
}

/* Related Articles */
.related-section {
  background: #f9f9f9;
  padding: 60px 20px;
  margin-top: 60px;
}

.section-container {
  max-width: 900px;
  margin: 0 auto;
}

.related-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-top: 32px;
}

.related-card {
  background: #fff;
  padding: 24px;
  border-radius: 10px;
  border: 1px solid #e5e5e5;
  transition: all 0.3s ease;
}

.related-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
}

.related-image {
  font-size: 36px;
  margin-bottom: 16px;
}

.related-title {
  font-size: 16px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 12px;
  line-height: 1.4;
}

.related-desc {
  font-size: 13px;
  color: #666;
  line-height: 1.5;
  margin: 0;
}

/* Newsletter */
.newsletter-section {
  padding: 60px 20px;
}

.newsletter-box {
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  color: #fff;
  padding: 48px;
  border-radius: 12px;
  text-align: center;
  max-width: 600px;
  margin: 0 auto;
}

.newsletter-title {
  font-size: 28px;
  font-weight: 700;
  margin: 0 0 12px;
}

.newsletter-desc {
  font-size: 16px;
  opacity: 0.9;
  margin: 0 0 24px;
}

.newsletter-form {
  display: flex;
  gap: 12px;
}

.newsletter-input {
  flex: 1;
  padding: 12px 16px;
  border: none;
  border-radius: 8px;
  font-size: 14px;
}

.newsletter-input::placeholder {
  color: #999;
}

.newsletter-btn {
  padding: 12px 24px;
  background: #7b5ce0;
  color: #fff;
  border: none;
  border-radius: 8px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s ease;
  white-space: nowrap;
}

.newsletter-btn:hover {
  background: #6a4dc7;
  transform: translateY(-2px);
}

/* Responsive */
@media (max-width: 1200px) {
  .content-container {
    grid-template-columns: 1fr;
  }

  .table-of-contents {
    position: static;
    margin-bottom: 40px;
  }

  .toc-nav {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
  }
}

@media (max-width: 768px) {
  .article-title {
    font-size: 32px;
  }

  .article-meta {
    flex-direction: column;
    align-items: flex-start;
    gap: 16px;
  }

  .section-title {
    font-size: 24px;
  }

  .platforms-grid {
    grid-template-columns: 1fr;
  }

  .related-grid {
    grid-template-columns: 1fr;
  }

  .toc-nav {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .article-hero {
    padding: 40px 16px;
  }

  .article-title {
    font-size: 24px;
  }

  .article-subtitle {
    font-size: 14px;
  }

  .article-image-section {
    height: 250px;
  }

  .article-content {
    padding: 32px 16px;
  }

  .section-title {
    font-size: 20px;
  }

  .section-text {
    font-size: 14px;
  }

  .newsletter-form {
    flex-direction: column;
  }
}
</style>
