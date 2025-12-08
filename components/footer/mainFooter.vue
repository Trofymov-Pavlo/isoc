<template>
  <footer class="footer">
    <div class="container">
      <!-- Main footer content -->
      <div class="grid">
        <!-- Column 1: About -->
        <div class="col">
          <h4 class="heading">À propos</h4>
          <p class="text">ISOC News est une plateforme de veille et d'analyse du conflit ukrainien, fondée sur des sources fiables et vérifiées.</p>
          <div class="social-links">
            <a href="#" class="soc-link" title="RSS Feed">RSS</a>
            <a href="#" class="soc-link" title="Archive">Archive</a>
          </div>
        </div>

        <!-- Column 2: Navigation -->
        <div class="col">
          <h4 class="heading">Navigation</h4>
          <ul class="link-list">
            <li><NuxtLink to="/">Accueil</NuxtLink></li>
            <li><NuxtLink to="/enDirect">En Direct</NuxtLink></li>
            <li><NuxtLink to="/inLivePage">Couverture Live</NuxtLink></li>
          </ul>
        </div>

        <!-- Column 3: Legal & Info -->
        <div class="col">
          <h4 class="heading">Information</h4>
          <ul class="link-list">
            <li><a href="#">Mentions Légales</a></li>
            <li><a href="#">Conditions d'Utilisation</a></li>
            <li><a href="#">Politique de Confidentialité</a></li>
          </ul>
        </div>

        <!-- Column 4: Contact -->
        <div class="col">
          <h4 class="heading">Contact</h4>
          <p class="text small">Université ISOC531<br/>Janvier 2025</p>
          <p class="text small">Pour toute question :<br/><a href="mailto:contact@isoc.news" class="email-link">contact@isoc.news</a></p>
        </div>
      </div>

      <!-- Divider -->
      <div class="divider"></div>

      <!-- Footer bar -->
      <div class="footer-bar">
        <p class="copyright">© {{ yearRange }} ISOC News. Tous droits réservés.</p>
        <p class="credit">Sources citées et vérifiées | Analyse indépendante</p>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
const yearRange = `2024-${new Date().getFullYear()}`
</script>

<style scoped>
.footer {
  background: #2f0538;
  color: #f0f0f3;
  border-top: 1px solid rgba(123, 92, 224, 0.3);
  padding: 40px 20px 20px;
}

.container {
  max-width: 1280px;
  margin: 0 auto;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 32px;
  margin-bottom: 24px;
}

.col { display: grid; gap: 12px; }

.heading {
  margin: 0;
  font-size: 14px;
  font-weight: 700;
  color: #7b5ce0;
  text-transform: uppercase;
  letter-spacing: 0.8px;
}

.text {
  margin: 0;
  font-size: 13px;
  line-height: 1.5;
  color: #d0d0d8;
}

.text.small { font-size: 12px; }

.link-list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 8px;
}

.link-list a {
  font-size: 13px;
  color: #d0d0d8;
  text-decoration: none;
  transition: color 0.2s ease;
}

.link-list a:hover {
  color: #7b5ce0;
}

.email-link {
  color: #7b5ce0;
  text-decoration: none;
}

.email-link:hover {
  text-decoration: underline;
}

.social-links {
  display: flex;
  gap: 10px;
}

.soc-link {
  display: inline-block;
  padding: 6px 10px;
  border: 1px solid rgba(123, 92, 224, 0.4);
  border-radius: 6px;
  color: #d0d0d8;
  text-decoration: none;
  font-size: 11px;
  font-weight: 600;
  transition: all 0.2s ease;
}

.soc-link:hover {
  background: rgba(123, 92, 224, 0.16);
  color: #7b5ce0;
  border-color: rgba(123, 92, 224, 0.6);
}

.divider {
  height: 1px;
  background: rgba(123, 92, 224, 0.2);
  margin: 24px 0;
}

.footer-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  align-items: center;
  justify-content: space-between;
  padding: 12px 0;
  text-align: center;
}

.copyright {
  margin: 0;
  font-size: 12px;
  color: #b0b0b8;
  flex: 1;
}

.credit {
  margin: 0;
  font-size: 12px;
  color: #b0b0b8;
}

@media (max-width: 768px) {
  .grid { gap: 24px; }
  .footer-bar { flex-direction: column; gap: 10px; }
  .copyright, .credit { text-align: center; }
}
</style>
