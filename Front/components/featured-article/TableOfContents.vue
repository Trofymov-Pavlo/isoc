<template>
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
</template>

<script setup lang="ts"></script>

<style scoped>
.table-of-contents {
  position: sticky;
  top: 24px;
  align-self: flex-start;
  background: #fff;
  border: 1px solid #e5e5e5;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.toc-title {
  margin: 0 0 16px;
  font-size: 16px;
  font-weight: 700;
  color: #2f0538;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.toc-nav {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.toc-link {
  color: #666;
  text-decoration: none;
  padding: 10px 12px;
  border-radius: 6px;
  font-size: 14px;
  transition: all 0.2s ease;
  border-left: 3px solid transparent;
}

.toc-link:hover {
  color: #2f0538;
  background: #f8f8f8;
  border-left-color: #ff6b6b;
}

@media (max-width: 968px) {
  .table-of-contents {
    position: relative;
    top: 0;
    margin-bottom: 32px;
  }
}
</style>
