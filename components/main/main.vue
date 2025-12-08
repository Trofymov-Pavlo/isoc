<template>
  <div class="home">
    <!-- Hero Section with Breaking News -->
    <section class="hero">
      <div class="section-container">
        <div class="hero-badge">
          <span class="badge-dot"></span>
          En continu
        </div>
        <h1 class="hero-title">Média indépendant dédié au conflit Ukraine-Russie</h1>
        <p class="hero-subtitle">Suivez en direct les derniers développements, analyses et reportages</p>
      </div>
    </section>

    <!-- Breaking News Banner -->
    <section class="breaking-news">
      <div class="section-container">
        <div class="breaking-item">
          <span class="breaking-badge">DIRECT</span>
          <p class="breaking-text">Actualités en temps réel</p>
          <a href="/inLivePage" class="breaking-link">Voir le live →</a>
        </div>
      </div>
    </section>

    <!-- Featured Article (Full Width) -->
    <section class="featured-main">
      <div class="section-container">
        <article class="featured-article">
          <div class="featured-image">
            <!-- Featured image will go here -->
          </div>
          <div class="featured-content">
            <span class="featured-category">Gros plan</span>
            <h2 class="featured-title">Article principal en vedette</h2>
            <p class="featured-desc">Résumé de l'article principal avec contexte et analyse détaillée sur le conflit...</p>
            <div class="featured-meta">
              <span class="featured-author">Par ISOC Media</span>
              <span class="featured-date">Il y a 2h</span>
            </div>
            <a href="#" class="read-more">Lire l'article complet →</a>
          </div>
        </article>
      </div>
    </section>

    <!-- Top Stories Grid (2 columns) -->
    <section class="top-stories">
      <div class="section-container">
        <h2 class="section-title">À la une</h2>
        <div class="stories-grid">
          <article class="story-card" v-for="i in 2" :key="i">
            <div class="story-image"></div>
            <div class="story-content">
              <span class="story-category">Actualité</span>
              <h3 class="story-title">Titre de l'article principal</h3>
              <p class="story-excerpt">Extrait de l'article avec les points clés...</p>
              <div class="story-meta">
                <span class="story-time">Il y a 4h</span>
                <span class="story-read">5 min de lecture</span>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- Live Updates Section -->
    <section class="live-updates">
      <div class="section-container">
        <h2 class="section-title">Mises à jour en direct</h2>
        <div class="live-ticker">
          <div class="ticker-item" v-for="i in 3" :key="i">
            <span class="ticker-time">{{ getCurrentTime }}</span>
            <p class="ticker-text">Mise à jour en direct du conflit...</p>
          </div>
        </div>
        <a href="/inLivePage" class="view-all-link">Voir tous les mises à jour →</a>
      </div>
    </section>

    <!-- Latest Articles Grid (3 columns) -->
    <section class="latest-articles">
      <div class="section-container">
        <h2 class="section-title">Dernières actualités</h2>
        <div class="articles-grid">
          <article class="article-card" v-for="i in 6" :key="i">
            <div class="article-image"></div>
            <div class="article-content">
              <span class="article-category">Reportage</span>
              <h3 class="article-title">Titre de l'article</h3>
              <p class="article-excerpt">Extrait de l'article...</p>
              <div class="article-footer">
                <span class="article-date">Il y a 6h</span>
                <span class="read-time">3 min</span>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- Analysis & Opinion Section -->
    <section class="analysis">
      <div class="section-container">
        <h2 class="section-title">Analyses et décryptage</h2>
        <div class="analysis-grid">
          <article class="analysis-card" v-for="i in 3" :key="i">
            <div class="analysis-image"></div>
            <div class="analysis-content">
              <span class="analysis-badge">Analyse</span>
              <h3 class="analysis-title">Analyse approfondie du sujet</h3>
              <p class="analysis-author">Par un expert</p>
              <p class="analysis-excerpt">Point de vue et analyse détaillée...</p>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- Topics/Sections -->
    <section class="topics">
      <div class="section-container">
        <h2 class="section-title">Thèmes</h2>
        <div class="topics-grid">
          <a href="#" class="topic-card" v-for="topic in ['Militaire', 'Politique', 'Humanitaire', 'Économie']" :key="topic">
            <span class="topic-name">{{ topic }}</span>
          </a>
        </div>
      </div>
    </section>

    <!-- Newsletter CTA -->
    <section class="newsletter">
      <div class="section-container">
        <div class="newsletter-box">
          <h2 class="newsletter-title">Restez informé</h2>
          <p class="newsletter-subtitle">Recevez les dernières actualités directement dans votre boîte mail</p>
          <div class="newsletter-form">
            <input type="email" placeholder="Votre adresse email" class="newsletter-input">
            <button class="newsletter-btn">S'abonner</button>
          </div>
          <p class="newsletter-disclaimer">Nous respectons votre vie privée. Désinscription facile.</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';

const getCurrentTime = computed(() => {
  const now = new Date();
  return now.toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' });
});
</script>

<style scoped>
.home {
  background: #ffffff;
  min-height: 100vh;
  padding-bottom: 60px;
}

.section-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Hero Section */
.hero {
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  padding: 80px 20px;
  text-align: center;
  color: #fff;
  margin-bottom: 0;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 107, 107, 0.2);
  border: 1px solid rgba(255, 107, 107, 0.5);
  color: #ff9999;
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  margin-bottom: 24px;
}

.badge-dot {
  width: 8px;
  height: 8px;
  background: #ff6b6b;
  border-radius: 50%;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.3; }
}

.hero-title {
  font-size: 48px;
  font-weight: 700;
  line-height: 1.2;
  margin: 0 0 16px 0;
  color: #fff;
}

.hero-subtitle {
  font-size: 18px;
  color: rgba(255, 255, 255, 0.9);
  margin: 0;
  font-weight: 400;
}

/* Breaking News */
.breaking-news {
  background: #fff5f5;
  border-bottom: 1px solid #f0f0f0;
  padding: 24px 20px;
  margin-bottom: 48px;
}

.breaking-item {
  display: flex;
  align-items: center;
  gap: 16px;
  max-width: 1200px;
  margin: 0 auto;
}

.breaking-badge {
  background: #ff6b6b;
  color: #fff;
  padding: 6px 12px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.5px;
  flex-shrink: 0;
}

.breaking-text {
  margin: 0;
  font-size: 14px;
  color: #2f0538;
  font-weight: 600;
  flex: 1;
}

.breaking-link {
  color: #7b5ce0;
  text-decoration: none;
  font-weight: 600;
  white-space: nowrap;
}

.breaking-link:hover {
  text-decoration: underline;
}

/* Featured Main Article */
.featured-main {
  padding: 48px 20px;
  margin-bottom: 48px;
}

.featured-article {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  align-items: center;
}

.featured-image {
  width: 100%;
  aspect-ratio: 16/9;
  background: linear-gradient(135deg, #f5f5f5, #e8e8e8);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #999;
  font-size: 14px;
}

.featured-content {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.featured-category {
  display: inline-block;
  background: #7b5ce0;
  color: #fff;
  padding: 6px 12px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  width: fit-content;
}

.featured-title {
  margin: 0;
  font-size: 36px;
  font-weight: 700;
  line-height: 1.3;
  color: #1a1a1a;
}

.featured-desc {
  margin: 0;
  font-size: 16px;
  line-height: 1.6;
  color: #555;
}

.featured-meta {
  display: flex;
  align-items: center;
  gap: 24px;
  font-size: 13px;
  color: #999;
}

.featured-author {
  font-weight: 600;
  color: #2f0538;
}

.read-more {
  color: #7b5ce0;
  text-decoration: none;
  font-weight: 600;
  width: fit-content;
}

.read-more:hover {
  text-decoration: underline;
}

/* Section Title */
.section-title {
  margin: 0;
  font-size: 28px;
  font-weight: 700;
  color: #2f0538;
  margin-bottom: 32px;
  padding-top: 48px;
}

/* Top Stories */
.top-stories {
  padding: 0 20px 48px 20px;
  background: #ffffff;
}

.stories-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 32px;
}

.story-card {
  display: flex;
  flex-direction: column;
  gap: 16px;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.story-card:hover {
  transform: translateY(-4px);
}

.story-image {
  width: 100%;
  aspect-ratio: 16/9;
  background: linear-gradient(135deg, #f5f5f5, #e8e8e8);
  border-radius: 10px;
}

.story-content {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.story-category {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  color: #ff6b6b;
  letter-spacing: 0.5px;
}

.story-title {
  margin: 0;
  font-size: 18px;
  font-weight: 700;
  color: #1a1a1a;
  line-height: 1.4;
}

.story-excerpt {
  margin: 0;
  font-size: 14px;
  color: #555;
  line-height: 1.5;
}

.story-meta {
  display: flex;
  gap: 16px;
  font-size: 12px;
  color: #999;
}

/* Live Updates */
.live-updates {
  background: #f5f5f5;
  padding: 48px 20px;
  margin-bottom: 48px;
}

.live-ticker {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-bottom: 24px;
}

.ticker-item {
  background: #fff;
  padding: 16px;
  border-radius: 8px;
  border-left: 3px solid #ff6b6b;
  display: flex;
  gap: 16px;
  align-items: flex-start;
}

.ticker-time {
  font-size: 12px;
  font-weight: 700;
  color: #ff6b6b;
  white-space: nowrap;
}

.ticker-text {
  margin: 0;
  font-size: 14px;
  color: #555;
  flex: 1;
}

.view-all-link {
  color: #7b5ce0;
  text-decoration: none;
  font-weight: 600;
}

.view-all-link:hover {
  text-decoration: underline;
}

/* Articles Grid */
.latest-articles {
  padding: 48px 20px;
}

.articles-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.article-card {
  background: #ffffff;
  border: 1px solid #e5e5e5;
  border-radius: 10px;
  overflow: hidden;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
}

.article-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
  border-color: #d0d0d0;
}

.article-image {
  width: 100%;
  aspect-ratio: 16/9;
  background: linear-gradient(135deg, #f5f5f5, #e8e8e8);
}

.article-content {
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  flex: 1;
}

.article-category {
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  color: #7b5ce0;
  letter-spacing: 0.5px;
}

.article-title {
  margin: 0;
  font-size: 16px;
  font-weight: 700;
  color: #1a1a1a;
  line-height: 1.4;
}

.article-excerpt {
  margin: 0;
  font-size: 13px;
  color: #666;
  line-height: 1.5;
  flex: 1;
}

.article-footer {
  display: flex;
  justify-content: space-between;
  font-size: 11px;
  color: #999;
  margin-top: auto;
  padding-top: 12px;
  border-top: 1px solid #f0f0f0;
}

/* Analysis Section */
.analysis {
  background: #f9f9f9;
  padding: 48px 20px;
}

.analysis-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.analysis-card {
  background: #fff;
  border-radius: 10px;
  overflow: hidden;
  transition: all 0.3s ease;
  cursor: pointer;
}

.analysis-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.analysis-image {
  width: 100%;
  aspect-ratio: 16/9;
  background: linear-gradient(135deg, #2f0538, #4b2faa);
}

.analysis-content {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.analysis-badge {
  display: inline-block;
  background: #2f0538;
  color: #fff;
  padding: 6px 12px;
  border-radius: 4px;
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  width: fit-content;
}

.analysis-title {
  margin: 0;
  font-size: 16px;
  font-weight: 700;
  color: #1a1a1a;
  line-height: 1.4;
}

.analysis-author {
  margin: 0;
  font-size: 12px;
  color: #7b5ce0;
  font-weight: 600;
}

.analysis-excerpt {
  margin: 0;
  font-size: 13px;
  color: #666;
  line-height: 1.5;
}

/* Topics */
.topics {
  padding: 48px 20px;
  background: #ffffff;
}

.topics-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}

.topic-card {
  background: linear-gradient(135deg, rgba(123, 92, 224, 0.1), rgba(75, 47, 170, 0.1));
  border: 1px solid rgba(123, 92, 224, 0.2);
  padding: 24px;
  border-radius: 10px;
  text-align: center;
  text-decoration: none;
  color: #2f0538;
  font-weight: 600;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100px;
}

.topic-card:hover {
  background: linear-gradient(135deg, rgba(123, 92, 224, 0.2), rgba(75, 47, 170, 0.2));
  border-color: rgba(123, 92, 224, 0.4);
  transform: translateY(-4px);
}

.topic-name {
  font-size: 16px;
}

/* Newsletter */
.newsletter {
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  padding: 60px 20px;
}

.newsletter-box {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  padding: 40px;
  text-align: center;
  color: #fff;
  max-width: 600px;
  margin: 0 auto;
}

.newsletter-title {
  margin: 0;
  font-size: 28px;
  font-weight: 700;
  margin-bottom: 12px;
}

.newsletter-subtitle {
  margin: 0 0 24px 0;
  font-size: 16px;
  opacity: 0.9;
}

.newsletter-form {
  display: flex;
  gap: 12px;
  margin-bottom: 16px;
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

.newsletter-input:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(123, 92, 224, 0.3);
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
}

.newsletter-btn:hover {
  background: #6a4dc7;
  transform: translateY(-2px);
}

.newsletter-disclaimer {
  margin: 0;
  font-size: 12px;
  opacity: 0.8;
}

/* Responsive */
@media (max-width: 1100px) {
  .hero-title {
    font-size: 36px;
  }

  .featured-article {
    grid-template-columns: 1fr;
  }

  .stories-grid {
    grid-template-columns: 1fr;
  }

  .articles-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .analysis-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .topics-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 680px) {
  .hero {
    padding: 50px 16px;
  }

  .hero-title {
    font-size: 28px;
  }

  .hero-subtitle {
    font-size: 16px;
  }

  .breaking-item {
    flex-direction: column;
    text-align: center;
  }

  .featured-article {
    grid-template-columns: 1fr;
  }

  .featured-content {
    order: 2;
  }

  .featured-image {
    order: 1;
  }

  .featured-title {
    font-size: 24px;
  }

  .section-title {
    font-size: 22px;
  }

  .stories-grid {
    gap: 16px;
  }

  .articles-grid {
    grid-template-columns: 1fr;
  }

  .analysis-grid {
    grid-template-columns: 1fr;
  }

  .topics-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .newsletter-box {
    padding: 30px 20px;
  }

  .newsletter-form {
    flex-direction: column;
  }
}

@media (max-width: 480px) {
  .hero-title {
    font-size: 22px;
  }

  .featured-title {
    font-size: 20px;
  }

  .topics-grid {
    grid-template-columns: 1fr;
  }

  .section-title {
    font-size: 18px;
    padding-top: 24px;
  }
}
</style>
