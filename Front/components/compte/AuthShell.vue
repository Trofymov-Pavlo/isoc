<template>
  <div class="auth-shell">
    <div class="hero-panel">
      <div class="hero-overlay"></div>
      <div class="hero-content">
        <p class="eyebrow">{{ eyebrow }}</p>
        <h1 class="hero-title">{{ heroTitle }}</h1>
        <p class="hero-subtitle">{{ heroSubtitle }}</p>
      </div>
    </div>
    <div class="card-panel">
      <div class="card">
        <slot />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps({
  heroTitle: { type: String, default: 'AXIOME' },
  heroSubtitle: { type: String, default: 'Accès sécurisé à vos services' },
  eyebrow: { type: String, default: 'Espace membre' },
});
</script>

<style scoped lang="scss">
.auth-shell {
  min-height: 100vh;
  display: grid;
  grid-template-columns: 1fr 1fr;
  background: linear-gradient(135deg, #1d0c3a 0%, #35105c 35%, #0f1528 100%);
  color: #fff;
}

.hero-panel {
  position: relative;
  padding: 56px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 20% 30%, rgba(255, 255, 255, 0.08), transparent 35%),
              radial-gradient(circle at 80% 20%, rgba(255, 255, 255, 0.12), transparent 35%),
              radial-gradient(circle at 40% 70%, rgba(255, 255, 255, 0.06), transparent 35%);
  opacity: 0.9;
}

.hero-content {
  position: relative;
  max-width: 460px;
  text-align: left;
  display: grid;
  gap: 14px;
}

.eyebrow {
  letter-spacing: 0.18em;
  text-transform: uppercase;
  font-size: 12px;
  font-weight: 700;
  margin: 0;
  color: #b9a7ff;
}

.hero-title {
  margin: 0;
  font-size: clamp(36px, 4vw, 52px);
  font-weight: 900;
  letter-spacing: 2px;
  background: linear-gradient(90deg, #ffffff, #cbb7ff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-subtitle {
  margin: 0;
  font-size: 18px;
  line-height: 1.5;
  color: rgba(255, 255, 255, 0.88);
}

.card-panel {
  background: #f7f7fb;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 36px;
}

.card {
  width: min(620px, 100%);
  background: #ffffff;
  border-radius: 18px;
  padding: 32px;
  box-shadow: 0 18px 45px rgba(0, 0, 0, 0.08);
}

/* Ensure slotted content stretches nicely */
.card :deep(> *) {
  width: 100%;
}

@media (max-width: 1100px) {
  .auth-shell {
    grid-template-columns: 1fr;
  }
  .hero-panel {
    min-height: 220px;
    padding: 32px;
  }
  .card-panel {
    padding: 32px 20px;
  }
}
</style>
