<template>
  <main class="podcast-page">
    <!-- Header (utilise le header/subheader existants via layout) -->

    <!-- Podcast Hero Section -->
    <section class="podcast-hero">
      <div class="hero-container">
        <div class="podcast-badge">
          <span class="badge-icon">🎙️</span>
          Podcast AXIOM
        </div>
        <h1 class="podcast-title">La Guerre de l'information</h1>
        <p class="podcast-subtitle">Analyse approfondie des enjeux informationnels du conflit Ukraine-Russie</p>
        
        <div class="hosts-container">
          <div class="host-intro">
            <span class="host-label">Présenté par</span>
            <div class="hosts-list">
              <span class="host">Antoine TENA</span>
              <span class="separator">•</span>
              <span class="host">Nathan BARRACHIN</span>
              <span class="separator">•</span>
              <span class="host">Pavel TROFYMOV</span>
            </div>
          </div>
        </div>

        <div class="play-button-container">
          <button class="play-button" @click="togglePlayback">
            <span class="play-icon" v-if="!isPlaying">▶</span>
            <span class="pause-icon" v-else>⏸</span>
          </button>
          <div class="play-info">
            <span class="duration">45 min</span>
            <span class="date">Publié le 14 décembre 2025</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Podcast Content -->
    <section class="podcast-content">
      <div class="content-grid">
        <!-- Main Content -->
        <div class="main-content">
          <!-- Épisode Description -->
          <section class="episode-section">
            <h2 class="section-title">À propos de cet épisode</h2>
            <p class="section-text">
              Dans cet épisode, nos trois animateurs explorent les mécanismes de la guerre informationnelle au cœur du conflit Ukraine-Russie. Comment les stratégies d'influence façonnent-elles la narration mondiale ? Quel rôle jouent les réseaux sociaux dans la diffusion de la propagande ? Et comment distinguer la désinformation de l'information vérifiée ?
            </p>
            <p class="section-text">
              Rejoignez-nous pour une discussion captivante sur le fact-checking, l'OSINT, les deepfakes et les défis contemporains de la vérité à l'ère numérique.
            </p>
          </section>

          <!-- Sommaire -->
          <section class="episode-section">
            <h2 class="section-title">Sommaire de l'épisode</h2>
            <div class="timeline">
              <div class="timeline-item">
                <div class="timeline-marker">00:00</div>
                <div class="timeline-content">
                  <h3>Introduction et présentation du sujet</h3>
                  <p>Les enjeux de la guerre informationnelle contemporaine</p>
                </div>
              </div>

              <div class="timeline-item">
                <div class="timeline-marker">05:12</div>
                <div class="timeline-content">
                  <h3>Stratégies d'influence et narratives</h3>
                  <p>Comment les acteurs du conflit façonnent le récit global</p>
                </div>
              </div>

              <div class="timeline-item">
                <div class="timeline-marker">15:34</div>
                <div class="timeline-content">
                  <h3>Rôle des réseaux sociaux</h3>
                  <p>Telegram, X, Facebook : des vecteurs de propagande et de désinformation</p>
                </div>
              </div>

              <div class="timeline-item">
                <div class="timeline-marker">25:47</div>
                <div class="timeline-content">
                  <h3>Deepfakes et technologies de tromperie</h3>
                  <p>Comment identifier et combattre les vidéos manipulées</p>
                </div>
              </div>

              <div class="timeline-item">
                <div class="timeline-marker">35:20</div>
                <div class="timeline-content">
                  <h3>OSINT, fact-checking et contre-désinformation</h3>
                  <p>Les outils et techniques pour vérifier l'information</p>
                </div>
              </div>

              <div class="timeline-item">
                <div class="timeline-marker">42:15</div>
                <div class="timeline-content">
                  <h3>Conclusion et ressources</h3>
                  <p>Recommandations et appels à l'action</p>
                </div>
              </div>
            </div>
          </section>

          <!-- Guest Hosts Section -->
          <section class="episode-section">
            <h2 class="section-title">Les animateurs</h2>
            <div class="hosts-grid">
              <div class="host-card">
                <div class="host-avatar">AT</div>
                <h3 class="host-name">Antoine TENA</h3>
                <p class="host-role">Rédacteur en chef, Spécialiste en géopolitique</p>
                <p class="host-bio">
                  Antoine est un journaliste d'investigation spécialisé dans les enjeux géopolitiques. Il couvre le conflit Ukraine-Russie depuis 2022 pour AXIOM.
                </p>
              </div>

              <div class="host-card">
                <div class="host-avatar">NB</div>
                <h3 class="host-name">Nathan BARRACHIN</h3>
                <p class="host-role">Analyste en désinformation</p>
                <p class="host-bio">
                  Nathan est un expert en fact-checking et vérification d'informations. Il travaille avec plusieurs organisations de fact-checking internationales.
                </p>
              </div>

              <div class="host-card">
                <div class="host-avatar">PT</div>
                <h3 class="host-name">Pavel TROFYMOV</h3>
                <p class="host-role">Développeur et expert en OSINT</p>
                <p class="host-bio">
                  Pavel est un spécialiste en open-source intelligence et technologies de vérification. Il contribue à des projets de lutte contre la désinformation.
                </p>
              </div>
            </div>
          </section>

          <!-- Resources Section -->
          <section class="episode-section">
            <h2 class="section-title">Ressources mentionnées</h2>
            <div class="resources-list">
              <div class="resource-item">
                <div class="resource-icon">🔗</div>
                <div class="resource-content">
                  <h3 class="resource-title">Bellingcat</h3>
                  <p class="resource-desc">Plateforme collaborative de journalisme d'investigation et d'OSINT</p>
                </div>
              </div>

              <div class="resource-item">
                <div class="resource-icon">🔗</div>
                <div class="resource-content">
                  <h3 class="resource-title">StopFake</h3>
                  <p class="resource-desc">Initiative ukrainienne de fact-checking sur le conflit</p>
                </div>
              </div>

              <div class="resource-item">
                <div class="resource-icon">🔗</div>
                <div class="resource-content">
                  <h3 class="resource-title">First Draft News</h3>
                  <p class="resource-desc">Ressources sur la vérification et la lutte contre la désinformation</p>
                </div>
              </div>

              <div class="resource-item">
                <div class="resource-icon">🔗</div>
                <div class="resource-content">
                  <h3 class="resource-title">Media Bias/Fact Check</h3>
                  <p class="resource-desc">Base de données de sources médiatiques avec analyse de biais</p>
                </div>
              </div>

              <div class="resource-item">
                <div class="resource-icon">🔗</div>
                <div class="resource-content">
                  <h3 class="resource-title">TweetDeck</h3>
                  <p class="resource-desc">Outil pour surveiller les tendances et désinformations sur X</p>
                </div>
              </div>

              <div class="resource-item">
                <div class="resource-icon">🔗</div>
                <div class="resource-content">
                  <h3 class="resource-title">Reverse Image Search</h3>
                  <p class="resource-desc">Google Images, TinEye, Yandex - outils de vérification d'images</p>
                </div>
              </div>
            </div>
          </section>

          <!-- Discussion Points -->
          <section class="episode-section">
            <h2 class="section-title">Points clés du débat</h2>
            <div class="key-points">
              <div class="key-point">
                <h3 class="point-title">Authentification vs Désinformation</h3>
                <p>Comment les techniques d'authentification aident à distinguer le vrai du faux dans un paysage médiatique fragmenté.</p>
              </div>

              <div class="key-point">
                <h3 class="point-title">Bulles de filtre et polarisation</h3>
                <p>Les algorithmes des réseaux sociaux créent des bulles informationnelles qui amplifient la polarisation.</p>
              </div>

              <div class="key-point">
                <h3 class="point-title">Responsabilité des plateformes</h3>
                <p>Les débats autour de la modération de contenu et de la responsabilité des géants de la tech.</p>
              </div>

              <div class="key-point">
                <h3 class="point-title">Éducation aux médias</h3>
                <p>L'importance de l'alphabétisation médiatique face aux défis contemporains de l'information.</p>
              </div>
            </div>
          </section>

          <!-- Share Section -->
          <section class="share-section">
            <h3 class="share-title">Partager ce podcast</h3>
            <div class="share-buttons">
              <a href="#" class="share-btn twitter" title="Partager sur X">X</a>
              <a href="#" class="share-btn facebook" title="Partager sur Facebook">Facebook</a>
              <a href="#" class="share-btn linkedin" title="Partager sur LinkedIn">LinkedIn</a>
              <a href="#" class="share-btn telegram" title="Partager sur Telegram">Telegram</a>
            </div>
          </section>
        </div>

        <!-- Sidebar -->
        <aside class="sidebar">
          <!-- Subscribe Box -->
          <div class="sidebar-box subscribe-box">
            <h3 class="sidebar-title">S'abonner au podcast</h3>
            <p class="sidebar-desc">Recevez les nouveaux épisodes directement dans votre lecteur préféré</p>
            <div class="subscribe-links">
              <a href="#" class="subscribe-link">
                <span class="app-icon">🎧</span>
                Apple Podcasts
              </a>
              <a href="#" class="subscribe-link">
                <span class="app-icon">🎙️</span>
                Spotify
              </a>
              <a href="#" class="subscribe-link">
                <span class="app-icon">📻</span>
                Google Podcasts
              </a>
              <a href="#" class="subscribe-link">
                <span class="app-icon">🎵</span>
                RSS Feed
              </a>
            </div>
          </div>

          <!-- Similar Episodes -->
          <div class="sidebar-box similar-box">
            <h3 class="sidebar-title">Épisodes similaires</h3>
            <div class="similar-episodes">
              <div class="similar-episode">
                <span class="episode-number">Ep. 3</span>
                <p class="episode-title">Propagande militaire et narratives de conflit</p>
                <span class="episode-date">21 nov 2025</span>
              </div>

              <div class="similar-episode">
                <span class="episode-number">Ep. 1</span>
                <p class="episode-title">Les racines géopolitiques du conflit Ukraine-Russie</p>
                <span class="episode-date">30 oct 2025</span>
              </div>
            </div>
          </div>

          <!-- Speakers' Articles -->
          <div class="sidebar-box articles-box">
            <h3 class="sidebar-title">Articles des animateurs</h3>
            <div class="author-articles">
              <div class="author-section">
                <span class="author-name">Antoine TENA</span>
                <a href="#" class="article-link">Géopolitique du conflit Ukraine-Russie</a>
              </div>
              <div class="author-section">
                <span class="author-name">Nathan BARRACHIN</span>
                <a href="#" class="article-link">Guide pratique du fact-checking</a>
              </div>
              <div class="author-section">
                <span class="author-name">Pavel TROFYMOV</span>
                <a href="#" class="article-link">OSINT et vérification d'images</a>
              </div>
            </div>
          </div>
        </aside>
      </div>
    </section>

    <!-- Call to Action Section -->
    <section class="cta-section">
      <div class="section-container cta-box">
        <h2 class="cta-title">Vous avez une information à vérifier ?</h2>
        <p class="cta-desc">Contactez notre équipe de fact-checking pour contribuer à la lutte contre la désinformation</p>
        <button class="cta-button">Nous contacter</button>
      </div>
    </section>

    <!-- Newsletter Section -->
    <section class="newsletter-section">
      <div class="section-container newsletter-box">
        <h2 class="newsletter-title">Restez informé</h2>
        <p class="newsletter-desc">Abonnez-vous pour recevoir les derniers épisodes et analyses</p>
        <div class="newsletter-form">
          <input type="email" placeholder="Votre adresse email" class="newsletter-input" />
          <button class="newsletter-btn">S'abonner</button>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const isPlaying = ref(false)

const togglePlayback = () => {
  isPlaying.value = !isPlaying.value
  // In a real implementation, this would control audio playback
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.podcast-page {
  background: #ffffff;
  min-height: 100vh;
}

/* Hero Section */
.podcast-hero {
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  color: #fff;
  padding: 60px 20px;
  position: relative;
  overflow: hidden;
}

.podcast-hero::before {
  content: '';
  position: absolute;
  top: -50%;
  right: -10%;
  width: 400px;
  height: 400px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 50%;
  pointer-events: none;
}

.hero-container {
  max-width: 900px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
}

.podcast-badge {
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

.podcast-title {
  font-size: 56px;
  font-weight: 800;
  line-height: 1.1;
  margin-bottom: 12px;
  letter-spacing: -0.5px;
}

.podcast-subtitle {
  font-size: 18px;
  opacity: 0.95;
  margin-bottom: 32px;
  line-height: 1.6;
}

.hosts-container {
  margin-bottom: 32px;
}

.host-intro {
  display: flex;
  align-items: center;
  gap: 16px;
}

.host-label {
  font-size: 12px;
  opacity: 0.8;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-weight: 600;
}

.hosts-list {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 16px;
  font-weight: 600;
}

.separator {
  opacity: 0.5;
}

/* Play Button */
.play-button-container {
  display: flex;
  align-items: center;
  gap: 20px;
  padding-top: 24px;
  border-top: 1px solid rgba(255, 255, 255, 0.2);
}

.play-button {
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, #7b5ce0, #9d7fee);
  border: none;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
}

.play-button:hover {
  transform: scale(1.1);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.35);
}

.play-icon,
.pause-icon {
  display: block;
}

.play-info {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.duration {
  font-size: 14px;
  font-weight: 600;
}

.date {
  font-size: 12px;
  opacity: 0.8;
}

/* Podcast Content */
.podcast-content {
  padding: 60px 20px;
}

.content-grid {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 320px;
  gap: 40px;
}

.main-content {
  display: flex;
  flex-direction: column;
  gap: 50px;
}

.episode-section {
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

/* Timeline */
.timeline {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.timeline-item {
  display: grid;
  grid-template-columns: 80px 1fr;
  gap: 20px;
  padding: 16px;
  background: #f9f9f9;
  border-radius: 8px;
  border-left: 4px solid #7b5ce0;
  transition: all 0.22s ease;
}

.timeline-item:hover {
  background: #f5f0ff;
  transform: translateX(4px);
}

.timeline-marker {
  font-weight: 700;
  color: #7b5ce0;
  font-size: 14px;
}

.timeline-content h3 {
  font-size: 15px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 6px;
}

.timeline-content p {
  font-size: 13px;
  color: #666;
  margin: 0;
  line-height: 1.5;
}

/* Hosts Grid */
.hosts-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.host-card {
  background: #f9f9f9;
  padding: 28px;
  border-radius: 12px;
  text-align: center;
  border: 2px solid #f0f0f0;
  transition: all 0.3s ease;
}

.host-card:hover {
  border-color: #7b5ce0;
  box-shadow: 0 8px 24px rgba(123, 92, 224, 0.1);
  transform: translateY(-4px);
}

.host-avatar {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #7b5ce0, #9d7fee);
  color: #fff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 20px;
  margin: 0 auto 16px;
}

.host-name {
  font-size: 18px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 4px;
}

.host-role {
  font-size: 13px;
  color: #7b5ce0;
  margin: 0 0 12px;
  font-weight: 600;
}

.host-bio {
  font-size: 13px;
  line-height: 1.6;
  color: #666;
  margin: 0;
}

/* Resources */
.resources-list {
  display: grid;
  gap: 16px;
}

.resource-item {
  display: flex;
  gap: 16px;
  padding: 16px;
  background: #f9f9f9;
  border-radius: 8px;
  transition: all 0.22s ease;
}

.resource-item:hover {
  background: #f5f0ff;
}

.resource-icon {
  font-size: 24px;
  flex-shrink: 0;
}

.resource-title {
  font-size: 15px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 4px;
}

.resource-desc {
  font-size: 13px;
  color: #666;
  margin: 0;
  line-height: 1.5;
}

/* Key Points */
.key-points {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}

.key-point {
  padding: 20px;
  background: linear-gradient(135deg, rgba(123, 92, 224, 0.05), rgba(123, 92, 224, 0.02));
  border-radius: 8px;
  border-left: 4px solid #7b5ce0;
}

.point-title {
  font-size: 15px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 8px;
}

.key-point p {
  font-size: 13px;
  line-height: 1.6;
  color: #666;
  margin: 0;
}

/* Sidebar */
.sidebar {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.sidebar-box {
  background: #f9f9f9;
  padding: 24px;
  border-radius: 12px;
  border: 1px solid #f0f0f0;
}

.sidebar-title {
  font-size: 16px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 12px;
}

.sidebar-desc {
  font-size: 13px;
  color: #666;
  line-height: 1.5;
  margin: 0 0 16px;
}

/* Subscribe Links */
.subscribe-links {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.subscribe-link {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px;
  background: #fff;
  border-radius: 6px;
  text-decoration: none;
  color: #555;
  font-size: 13px;
  font-weight: 600;
  transition: all 0.22s ease;
  border: 1px solid #e5e5e5;
}

.subscribe-link:hover {
  color: #7b5ce0;
  border-color: #7b5ce0;
}

.app-icon {
  font-size: 16px;
}

/* Similar Episodes */
.similar-episodes {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.similar-episode {
  padding: 12px;
  background: #fff;
  border-radius: 6px;
  border: 1px solid #e5e5e5;
}

.episode-number {
  font-size: 11px;
  font-weight: 700;
  color: #7b5ce0;
  text-transform: uppercase;
}

.episode-title {
  font-size: 13px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 4px 0;
  line-height: 1.4;
}

.episode-date {
  font-size: 11px;
  color: #999;
}

/* Author Articles */
.author-articles {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.author-section {
  padding: 12px;
  background: #fff;
  border-radius: 6px;
  border: 1px solid #e5e5e5;
}

.author-name {
  font-size: 11px;
  font-weight: 700;
  color: #7b5ce0;
  text-transform: uppercase;
  display: block;
  margin-bottom: 6px;
}

.article-link {
  color: #1a1a1a;
  text-decoration: none;
  font-size: 13px;
  font-weight: 600;
  line-height: 1.4;
  transition: all 0.22s ease;
  display: block;
}

.article-link:hover {
  color: #7b5ce0;
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

/* CTA Section */
.cta-section {
  background: linear-gradient(135deg, #7b5ce0, #9d7fee);
  color: #fff;
  padding: 60px 20px;
}

.section-container {
  max-width: 900px;
  margin: 0 auto;
}

.cta-box {
  text-align: center;
}

.cta-title {
  font-size: 36px;
  font-weight: 700;
  margin: 0 0 12px;
}

.cta-desc {
  font-size: 16px;
  opacity: 0.95;
  margin: 0 0 24px;
}

.cta-button {
  padding: 14px 32px;
  background: #fff;
  color: #7b5ce0;
  border: none;
  border-radius: 8px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 15px;
}

.cta-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
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
  max-width: 500px;
  margin: 0 auto;
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
  .content-grid {
    grid-template-columns: 1fr;
  }

  .hosts-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .key-points {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .podcast-title {
    font-size: 36px;
  }

  .hosts-grid {
    grid-template-columns: 1fr;
  }

  .timeline-item {
    grid-template-columns: 60px 1fr;
  }

  .key-points {
    grid-template-columns: 1fr;
  }

  .section-title {
    font-size: 24px;
  }

  .play-button-container {
    flex-direction: column;
    align-items: flex-start;
  }
}

@media (max-width: 480px) {
  .podcast-hero {
    padding: 40px 16px;
  }

  .podcast-title {
    font-size: 28px;
  }

  .podcast-subtitle {
    font-size: 14px;
  }

  .hosts-list {
    flex-wrap: wrap;
  }

  .podcast-content {
    padding: 32px 16px;
  }

  .section-title {
    font-size: 20px;
  }

  .newsletter-form {
    flex-direction: column;
  }

  .cta-title {
    font-size: 24px;
  }
}
</style>
