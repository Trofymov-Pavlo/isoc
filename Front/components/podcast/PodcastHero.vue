<template>
  <section class="podcast-hero">
    <div class="hero-container">
      <div class="podcast-badge">
        <span class="badge-icon">🎙️</span>
        Podcast AXIOM
      </div>
      <h1 class="podcast-title">{{ title }}</h1>
      <p class="podcast-subtitle">{{ subtitle }}</p>

      <div class="hosts-container">
        <div class="host-intro">
          <span class="host-label">Présenté par</span>
          <div class="hosts-list">
            <span v-for="(host, i) in hosts" :key="host" class="host">
              {{ host }}<span v-if="i < hosts.length - 1" class="separator">•</span>
            </span>
          </div>
        </div>
      </div>

      <div class="play-button-container">
        <button class="play-button" @click="$emit('toggle')">
          <span class="play-icon" v-if="!isPlaying">▶</span>
          <span class="pause-icon" v-else>⏸</span>
        </button>
        <div class="play-info">
          <span class="duration">{{ duration }}</span>
          <span class="date">{{ date }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
const props = defineProps<{ title: string; subtitle: string; hosts: string[]; duration: string; date: string; isPlaying: boolean }>();
</script>

<style scoped>
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

.hero-container { max-width: 900px; margin: 0 auto; position: relative; z-index: 1; }

.podcast-badge { display: inline-flex; align-items: center; gap: 8px; background: rgba(255,255,255,0.15); padding: 8px 16px; border-radius: 20px; font-size: 12px; font-weight: 600; margin-bottom: 20px; }
.badge-icon { font-size: 14px; }
.podcast-title { font-size: 56px; font-weight: 800; line-height: 1.1; margin-bottom: 12px; letter-spacing: -0.5px; }
.podcast-subtitle { font-size: 18px; opacity: 0.95; margin-bottom: 32px; line-height: 1.6; }

.hosts-container { margin-bottom: 32px; }
.host-intro { display: flex; align-items: center; gap: 16px; flex-wrap: wrap; }
.host-label { font-size: 12px; opacity: 0.8; text-transform: uppercase; letter-spacing: 0.5px; font-weight: 600; }
.hosts-list { display: flex; align-items: center; gap: 8px; font-size: 16px; font-weight: 600; flex-wrap: wrap; }
.separator { opacity: 0.5; margin: 0 4px; }

.play-button-container { display: flex; align-items: center; gap: 20px; padding-top: 24px; border-top: 1px solid rgba(255, 255, 255, 0.2); }
.play-button { width: 60px; height: 60px; background: linear-gradient(135deg, #7b5ce0, #9d7fee); border: none; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 24px; cursor: pointer; transition: all 0.3s ease; box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25); }
.play-button:hover { transform: scale(1.1); box-shadow: 0 12px 32px rgba(0, 0, 0, 0.35); }
.play-info { display: flex; flex-direction: column; gap: 4px; }
.duration { font-size: 14px; font-weight: 600; }
.date { font-size: 12px; opacity: 0.8; }

@media (max-width: 768px) {
  .podcast-title { font-size: 36px; }
  .play-button-container { flex-direction: column; align-items: flex-start; }
}

@media (max-width: 480px) {
  .podcast-hero { padding: 40px 16px; }
  .podcast-title { font-size: 28px; }
  .podcast-subtitle { font-size: 14px; }
}
</style>
