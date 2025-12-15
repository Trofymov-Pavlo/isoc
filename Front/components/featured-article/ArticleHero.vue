<template>
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
</template>

<script setup lang="ts"></script>

<style scoped>
.article-hero {
  padding: 48px 0 32px;
  border-bottom: 1px solid #f0f0f0;
}

.hero-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 0 20px;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  color: #fff;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 24px;
}

.badge-icon {
  font-size: 16px;
}

.article-title {
  font-size: 42px;
  font-weight: 800;
  line-height: 1.2;
  color: #1a1a1a;
  margin: 0 0 20px;
}

.article-subtitle {
  font-size: 20px;
  line-height: 1.5;
  color: #555;
  margin: 0 0 32px;
}

.article-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 24px;
  border-top: 1px solid #f0f0f0;
}

.author-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.author-avatar {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #ff6b6b 0%, #ff8e53 100%);
  color: #fff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 16px;
}

.author-details {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.author-name {
  font-weight: 600;
  font-size: 14px;
  color: #1a1a1a;
}

.publish-date {
  font-size: 13px;
  color: #999;
}

.reading-time {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 14px;
  color: #666;
}

.icon {
  font-size: 18px;
}

@media (max-width: 768px) {
  .article-title {
    font-size: 32px;
  }
  
  .article-subtitle {
    font-size: 18px;
  }
  
  .article-meta {
    flex-direction: column;
    align-items: flex-start;
    gap: 16px;
  }
}
</style>
