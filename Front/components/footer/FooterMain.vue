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
              <h3 class="brand-name">AXIOME</h3>
              <p class="brand-tagline">Information & Analyse</p>
            </div>
          </div>
          <p class="description">Agrégation et structuration de l'information francophone sur le conflit Ukraine-Russie.</p>
        </div>

        <!-- Quick Links -->
        <div class="col">
          <h4 class="col-title">Navigation</h4>
          <ul class="link-list">
            <li><NuxtLink to="/">Accueil</NuxtLink></li>
            <li><NuxtLink to="/en-direct">En Direct</NuxtLink></li>
            <li><NuxtLink to="/explorer">Explorer</NuxtLink></li>
            <li><NuxtLink to="/liked">Mes Favoris</NuxtLink></li>
          </ul>
        </div>

        <!-- Resources -->
        <div class="col">
          <h4 class="col-title">Ressources</h4>
          <ul class="link-list">
            <li><a href="/rss.xml" target="_blank" rel="noopener">Flux RSS</a></li>
            <li><NuxtLink to="/contact">Contact</NuxtLink></li>
            <li><NuxtLink to="/a-propos">À propos</NuxtLink></li>
          </ul>
        </div>

        <!-- Legal -->
        <div class="col">
          <h4 class="col-title">Légal</h4>
          <ul class="link-list">
            <li><NuxtLink to="/conditions">Conditions Générales</NuxtLink></li>
            <li><NuxtLink to="/mentions">Mentions Légales</NuxtLink></li>
            <li><NuxtLink to="/cookies">Cookies</NuxtLink></li>
          </ul>
        </div>
      </div>

      <!-- Divider -->
      <div class="separator"></div>

      <!-- Bottom Bar -->
      <div class="bottom">
        <p class="credit">© 2025-2026 · AXIOME · Projet étudiant ISOC531</p>
        <p class="meta-links">
          <a href="/sitemap.xml" target="_blank">Sitemap</a>
          <span class="sep">·</span>
          <a href="/robots.txt" target="_blank">Robots</a>
          <span class="sep">·</span>
          <a href="/humans.txt" target="_blank">Humans</a>
          <span class="sep">·</span>
          <a href="/security.txt" target="_blank">Security</a>
          <span class="sep">·</span>
          <a href="/archive.json" target="_blank">Archive</a>
        </p>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
</script>

<style scoped>
.footer {
  background: #ffffff;
  color: #212529;
  border-top: 1px solid #e5e7eb;
  padding: 0;
}

.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 40px 40px 20px;
}

.grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 40px;
  margin-bottom: 24px;
}

.col { display: grid; gap: 12px; }
.brand-col { grid-column: 1; }

.brand { display: flex; gap: 10px; align-items: center; }
.logo-mark { width: 36px; height: 36px; border-radius: 8px; background: #f1f3f5; border: 1px solid #e5e7eb; display: flex; align-items: center; justify-content: center; }
.accent { width: 8px; height: 8px; border-radius: 50%; background: #7b5ce0; }
.brand-name { margin: 0; font-size: 16px; font-weight: 800; color: #2f0538; letter-spacing: 0.5px; }
.brand-tagline { margin: 2px 0 0; font-size: 11px; color: #6b7280; letter-spacing: 0.5px; text-transform: uppercase; font-weight: 600; }
.description { margin: 0; font-size: 13px; line-height: 1.6; color: #4b5563; }

.col-title { margin: 0; font-size: 12px; font-weight: 700; color: #6b7280; text-transform: uppercase; letter-spacing: 0.6px; }
.link-list { margin: 0; padding: 0; list-style: none; display: grid; gap: 8px; }
.link-list a { font-size: 12px; color: #3b4048; text-decoration: none; transition: color 0.2s ease; }
.link-list a:hover { color: #7b5ce0; }

.separator { height: 1px; background: #e9ecef; margin: 20px 0; }

.bottom { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 12px; padding: 12px 0; border-top: 1px solid #e9ecef; }
.credit { margin: 0; font-size: 11px; color: #6b7280; }
.status { margin: 0; font-size: 11px; color: #7b5ce0; font-weight: 600; }

.meta-links { margin: 0; font-size: 10px; color: #9ca3af; display: flex; gap: 6px; align-items: center; }
.meta-links a { color: #9ca3af; text-decoration: none; transition: color 0.2s ease; }
.meta-links a:hover { color: #7b5ce0; }
.meta-links .sep { color: #d1d5db; }

@media (max-width: 960px) {
  .grid { grid-template-columns: repeat(2, 1fr); gap: 24px; }
  .brand-col { grid-column: 1 / -1; }
}

@media (max-width: 640px) {
  .grid { grid-template-columns: 1fr; gap: 16px; }
  .bottom { flex-direction: column; align-items: flex-start; }
}
</style>
