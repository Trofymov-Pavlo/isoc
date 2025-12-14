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
.article-hero{padding:2rem 0}
.hero-container{max-width:1000px;margin:0 auto}
.hero-badge{display:flex;align-items:center;gap:.5rem;color:#555}
.article-title{font-size:2rem;margin:.5rem 0}
.article-subtitle{color:#666}
.article-meta{display:flex;justify-content:space-between;align-items:center;margin-top:1rem}
.author-info{display:flex;align-items:center;gap:.75rem}
.author-avatar{background:#eee;border-radius:50%;padding:.4rem .6rem}
</style>
