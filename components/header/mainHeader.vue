<template>
    <div class="header">
        <div class="meta-bar">
            <div class="meta-left">
                <a class="language" href="/">FR</a>
                <span class="meta-sep">•</span>
                <span class="date">{{ date }}</span>
                <span class="edition">Édition du jour</span>
            </div>
            <div class="meta-right">
                <span class="pulse-dot"></span>
                <span class="tagline">Observatoire indépendant — Conflit Ukraine / Russie</span>
            </div>
        </div>

        <div class="main-bar">
            <div class="main-left">
                <span class="pill">Temps réel</span>
                <span class="pill alt">Sources vérifiées</span>
            </div>

            <div class="logo-block" @click="goIndex">
                <img :src="logo" alt="ISOC Media" class="logo" />
                <p class="slogan">Le meilleur de l’actu, sans filtre</p>
            </div>

            <div class="main-right">
                <NuxtLink to="/Contact" class="icon-link" title="Contact">
                    <v-icon icon="mdi-email-outline"></v-icon>
                </NuxtLink>
                <a href="/" class="icon-link" title="Accueil">
                    <v-icon icon="mdi-home-outline"></v-icon>
                </a>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import logoIsoc from '@/assets/logoIsoc.png'

const logo = logoIsoc

const date = new Date().toLocaleDateString('fr-FR', {
  weekday: 'long',
  month: 'long',
  day: 'numeric'
});

function goIndex() {
  window.location.href = '/'
}
</script>

<style scoped>
.header {
    background: #ffffff;
    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.05);
    display: flex;
    flex-direction: column;
    gap: 6px;
}

.meta-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px 0 20px;
    font-size: 12px;
    color: #3b3650;
}

.meta-left {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
}

.language {
    font-weight: 700;
    letter-spacing: 0.4px;
    color: #2f0538;
    text-decoration: none;
    padding: 4px 8px;
    border: 1px solid rgba(47, 5, 56, 0.15);
    border-radius: 6px;
    background: rgba(47, 5, 56, 0.04);
}

.meta-sep {
    color: rgba(47, 5, 56, 0.35);
}

.date {
    font-weight: 600;
    text-transform: capitalize;
}

.edition {
    color: #7a758f;
}

.meta-right {
    display: flex;
    align-items: center;
    gap: 8px;
    color: #2f0538;
    font-weight: 600;
}

.pulse-dot {
    width: 8px;
    height: 8px;
    background: #ff6b6b;
    border-radius: 50%;
    box-shadow: 0 0 0 6px rgba(255, 107, 107, 0.18);
    animation: pulse 2s infinite;
}

.tagline {
    letter-spacing: 0.15px;
}

@keyframes pulse {
    0%, 100% { opacity: 1; box-shadow: 0 0 0 6px rgba(255, 107, 107, 0.18); }
    50% { opacity: 0.65; box-shadow: 0 0 0 10px rgba(255, 107, 107, 0.08); }
}

.main-bar {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    align-items: center;
    padding: 6px 20px 14px 20px;
    gap: 16px;
}

.main-left {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}

.pill {
    padding: 6px 10px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.2px;
    background: rgba(47, 5, 56, 0.05);
    color: #2f0538;
    border: 1px solid rgba(47, 5, 56, 0.12);
}

.pill.alt {
    background: rgba(123, 92, 224, 0.08);
    color: #4b2faa;
    border-color: rgba(123, 92, 224, 0.18);
}

.logo-block {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
    cursor: pointer;
}

.logo {
    width: 200px;
    height: auto;
    object-fit: contain;
    filter: drop-shadow(0 4px 12px rgba(0, 0, 0, 0.08));
}

.slogan {
    margin: 0;
    font-size: 12px;
    letter-spacing: 0.25px;
    color: #4b2faa;
    text-align: center;
    font-weight: 600;
}

.main-right {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
    align-items: center;
}

.icon-link {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    border-radius: 10px;
    background: rgba(47, 5, 56, 0.05);
    color: #2f0538;
    text-decoration: none;
    transition: all 0.2s ease;
    border: 1px solid rgba(47, 5, 56, 0.08);
}

.icon-link :deep(.v-icon) {
    font-size: 18px;
}

.icon-link:hover {
    background: rgba(123, 92, 224, 0.12);
    color: #4b2faa;
    border-color: rgba(123, 92, 224, 0.2);
    transform: translateY(-1px);
}

.icon-link:active {
    transform: translateY(0);
}

@media (max-width: 960px) {
    .meta-bar {
        flex-direction: column;
        align-items: flex-start;
        gap: 6px;
    }

    .main-bar {
        grid-template-columns: 1fr 1fr;
        grid-template-areas:
            "logo logo"
            "left right";
    }

    .logo-block { grid-area: logo; }
    .main-left { grid-area: left; }
    .main-right { grid-area: right; justify-content: flex-end; }
}

@media (max-width: 640px) {
    .meta-bar { padding: 10px 14px 0 14px; }
    .main-bar { padding: 6px 14px 12px 14px; }

    .logo { width: 160px; }
    .slogan { font-size: 11px; }

    .pill { font-size: 11px; padding: 5px 9px; }

    .icon-link { width: 34px; height: 34px; }
}

@media (max-width: 480px) {
    .meta-right { font-size: 11px; }
    .tagline { display: none; }
    .main-bar { gap: 10px; }
    .main-left { gap: 6px; }
    .pill { font-size: 10px; }
}
</style>
