<template>
  <footer class="footer">
    <div class="shell">
      <div class="top">
        <div class="brand">
          <span class="dot"></span>
          <div>
            <p class="name">ISOC News</p>
            <p class="tagline">Veille & analyse du conflit ukrainien</p>
          </div>
        </div>

        <nav class="nav">
          <NuxtLink to="/" class="link">Accueil</NuxtLink>
          <NuxtLink to="/enDirect" class="link">En Direct</NuxtLink>
          <NuxtLink to="/inLivePage" class="link">Live</NuxtLink>
        </nav>

        <div class="contact">
          <p class="label">Contact</p>
          <p class="line">Université ISOC531</p>
          <p class="line">Janvier 2025</p>
        </div>
      </div>

      <div class="bottom">
        <p class="meta">© {{ yearRange }} · Sources citées et vérifiées</p>
        <div class="chips">
          <span class="chip">RSS</span>
          <span class="chip">Fact-check</span>
          <span class="chip">Analyse</span>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
const yearRange = `2024-${new Date().getFullYear()}`
</script>

<style scoped>
.footer {
  background: radial-gradient(circle at 20% 20%, rgba(255, 223, 95, 0.12), transparent 35%),
              radial-gradient(circle at 80% 10%, rgba(112, 76, 182, 0.18), transparent 40%),
              #0c0b14;
  color: #f6f6f9;
  padding: 28px 20px 24px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.shell {
  max-width: 1280px;
  margin: 0 auto;
  display: grid;
  gap: 18px;
}

.top {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 18px;
  align-items: center;
}

.brand {
  display: flex;
  gap: 12px;
  align-items: center;
}

.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: linear-gradient(135deg, #ffdf5f, #ff9f3f);
  box-shadow: 0 0 0 6px rgba(255, 223, 95, 0.12);
}

.name {
  margin: 0;
  font-weight: 800;
  letter-spacing: 0.5px;
  font-size: 16px;
}

.tagline {
  margin: 2px 0 0;
  color: #cdd0df;
  font-size: 13px;
}

.nav {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  justify-content: center;
}

.link {
  color: #f6f6f9;
  text-decoration: none;
  padding: 8px 12px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  transition: all 0.2s ease;
  font-weight: 600;
  font-size: 13px;
}

.link:hover {
  background: rgba(255, 223, 95, 0.16);
  color: #ffdf5f;
  border-color: rgba(255, 223, 95, 0.4);
}

.contact {
  justify-self: end;
  text-align: right;
  color: #d6d8e3;
  font-size: 13px;
}

.label { margin: 0 0 4px; font-weight: 700; color: #ffdf5f; }
.line { margin: 0; opacity: 0.8; }

.bottom {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding-top: 12px;
}

.meta {
  margin: 0;
  color: #cdd0df;
  font-size: 13px;
}

.chips {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.chip {
  padding: 6px 10px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 12px;
  color: #f6f6f9;
}

@media (max-width: 720px) {
  .contact { justify-self: start; text-align: left; }
  .bottom { gap: 12px; flex-direction: column; align-items: flex-start; }
}
</style>
