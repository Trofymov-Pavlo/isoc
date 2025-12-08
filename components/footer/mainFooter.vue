<template>
  <footer class="footer">
    <div class="container">
      <div class="grid">
        <!-- Brand -->
        <div class="col brand-col">
          <div class="brand">
            <div class="logo-mark">
              <span class="accent"></span>
            </div>
            <div>
              <h3 class="brand-name">ISOC News</h3>
              <p class="brand-tagline">Veille & Analyse</p>
            </div>
          </div>
          <p class="description">Couverture indépendante et vérifiée du conflit ukrainien.</p>
        </div>

        <!-- Quick Links -->
        <div class="col">
          <h4 class="col-title">Explorer</h4>
          <ul class="link-list">
            <li><NuxtLink to="/">Accueil</NuxtLink></li>
            <li><NuxtLink to="/enDirect">En Direct</NuxtLink></li>
            <li><NuxtLink to="/inLivePage">Couverture Live</NuxtLink></li>
          </ul>
        </div>

        <!-- Resources -->
        <div class="col">
          <h4 class="col-title">Ressources</h4>
          <ul class="link-list">
            <li><a href="#">Flux RSS</a></li>
            <li><a href="#">Archive</a></li>
            <li><a href="#">À propos</a></li>
          </ul>
        </div>

        <!-- Legal -->
        <div class="col">
          <h4 class="col-title">Légal</h4>
          <ul class="link-list">
            <li><a href="#">Mentions</a></li>
            <li><a href="#">Conditions</a></li>
            <li><a href="#">Confidentialité</a></li>
          </ul>
        </div>
      </div>

      <!-- Divider -->
      <div class="separator"></div>

      <!-- Bottom Bar -->
      <div class="bottom">
        <p class="credit">© {{ yearRange }} · ISOC News · Analyse indépendante</p>
        <p class="status">Tous les contenus sont vérifiés et sourcés</p>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
const yearRange = `2024-${new Date().getFullYear()}`
</script>

<style scoped>
.footer {
  background: linear-gradient(135deg, #1a1428 0%, #2f0538 50%, #1f1430 100%);
  color: #e8e4f0;
  border-top: 2px solid rgba(123, 92, 224, 0.4);
  padding: 60px 20px 32px;
}

.container {
  max-width: 1400px;
  margin: 0 auto;
}

.grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 48px;
  margin-bottom: 40px;
}

.col { display: grid; gap: 18px; }

.brand-col { grid-column: 1; }

.brand {
  display: flex;
  gap: 14px;
  align-items: flex-start;
  margin-bottom: 8px;
}

.logo-mark {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: linear-gradient(135deg, rgba(123, 92, 224, 0.3), rgba(123, 92, 224, 0.1));
  border: 1px solid rgba(123, 92, 224, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.accent {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: linear-gradient(135deg, #7b5ce0, #c5b3ff);
  box-shadow: 0 0 12px rgba(123, 92, 224, 0.6);
}

.brand-name {
  margin: 0;
  font-size: 18px;
  font-weight: 800;
  letter-spacing: 1px;
  color: #fff;
}

.brand-tagline {
  margin: 2px 0 0;
  font-size: 11px;
  color: #a89ac0;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

.description {
  margin: 0;
  font-size: 13px;
  line-height: 1.6;
  color: #b8afd0;
}

.col-title {
  margin: 0;
  font-size: 13px;
  font-weight: 700;
  color: #7b5ce0;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 4px;
}

.link-list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 10px;
}

.link-list a {
  font-size: 13px;
  color: #d0cae0;
  text-decoration: none;
  transition: all 0.25s ease;
  position: relative;
}

.link-list a::before {
  content: '';
  position: absolute;
  left: -8px;
  width: 0;
  height: 2px;
  background: linear-gradient(90deg, #7b5ce0, transparent);
  transition: width 0.25s ease;
}

.link-list a:hover {
  color: #c5b3ff;
  padding-left: 8px;
}

.link-list a:hover::before {
  width: 8px;
}

.separator {
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(123, 92, 224, 0.4), transparent);
  margin: 40px 0;
}

.bottom {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
  padding: 20px 0;
}

.credit {
  margin: 0;
  font-size: 12px;
  color: #9b92b0;
  letter-spacing: 0.3px;
}

.status {
  margin: 0;
  font-size: 12px;
  color: #7b5ce0;
  font-weight: 600;
}

@media (max-width: 960px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 32px;
  }
  .brand-col { grid-column: 1 / -1; }
}

@media (max-width: 640px) {
  .grid { grid-template-columns: 1fr; gap: 24px; }
  .bottom { flex-direction: column; align-items: flex-start; }
}
</style>
