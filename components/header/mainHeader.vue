<template>
    <div class="header">
        <div class="main-bar">
            <div class="main-left">
                <span class="pulse-dot"></span>
                <span class="tagline">Média indépendant — Conflit Ukraine / Russie</span>
            </div>

            <div class="logo-block" @click="goIndex">
                <img :src="logo" alt="ISOC Media" class="logo" />
                <p class="logo-date">{{ date }}</p>
            </div>

            <div class="main-right">
                <a class="language" href="/">FR</a>
                <NuxtLink to="/Contact" class="icon-link" title="Contact">
                    <v-icon icon="mdi-email-outline"></v-icon>
                </NuxtLink>
                <a href="/rss.xml" class="icon-link" title="Flux RSS">
                    <v-icon icon="mdi-rss"></v-icon>
                </a>
                <button class="support-btn" type="button" title="Soutenir le média">Soutenir</button>
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
    border-bottom: none;
    box-shadow: none;
    display: flex;
    flex-direction: column;
}

.main-bar {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    align-items: center;
    padding: 8px 12px;
    gap: 12px;
    font-size: 11px;
    color: #3b3650;
}

.main-left {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
    min-height: 1px;
}

.language {
    font-weight: 700;
    letter-spacing: 0.4px;
    color: #2f0538;
    text-decoration: none;
    padding: 3px 7px;
    border: 1px solid rgba(47, 5, 56, 0.15);
    border-radius: 6px;
    background: rgba(47, 5, 56, 0.04);
}

.meta-sep {
    color: rgba(47, 5, 56, 0.35);
}

.tagline {
    letter-spacing: 0.15px;
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

@keyframes pulse {
    0%, 100% { opacity: 1; box-shadow: 0 0 0 6px rgba(255, 107, 107, 0.18); }
    50% { opacity: 0.65; box-shadow: 0 0 0 10px rgba(255, 107, 107, 0.08); }
}

.logo-block {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
    cursor: pointer;
}

.logo {
    width: 160px;
    height: auto;
    object-fit: contain;
    filter: drop-shadow(0 4px 12px rgba(0, 0, 0, 0.08));
}

.logo-date {
    margin: 0;
    font-size: 11px;
    letter-spacing: 0.2px;
    color: #3b3650;
    text-align: center;
    font-weight: 600;
    text-transform: capitalize;
}

.main-right {
    display: flex;
    justify-content: flex-end;
    gap: 8px;
    align-items: center;
}

.icon-link {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 32px;
    height: 32px;
    border-radius: 8px;
    background: rgba(47, 5, 56, 0.05);
    color: #2f0538;
    text-decoration: none;
    transition: all 0.2s ease;
    border: 1px solid rgba(47, 5, 56, 0.08);
}

.icon-link :deep(.v-icon) {
    font-size: 16px;
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

.support-btn {
    border: 1px solid #2f0538;
    background: linear-gradient(120deg, #2f0538, #4b2faa);
    color: #fff;
    padding: 6px 9px;
    border-radius: 8px;
    font-weight: 700;
    letter-spacing: 0.2px;
    cursor: pointer;
    transition: all 0.2s ease;
    box-shadow: 0 4px 14px rgba(47, 5, 56, 0.18);
}

.support-btn:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 18px rgba(47, 5, 56, 0.24);
}

.support-btn:active {
    transform: translateY(0);
}

@media (max-width: 960px) {
    .main-bar {
        grid-template-columns: 1fr;
        grid-template-rows: auto auto;
        grid-template-areas:
            "logo"
            "info";
        row-gap: 6px;
        text-align: center;
        justify-items: center;
    }

    .logo-block { grid-area: logo; }
    .main-left { grid-area: info; justify-content: center; }
    .main-right { grid-area: info; justify-content: center; flex-wrap: wrap; gap: 6px; }
}

@media (max-width: 640px) {
    .main-bar { padding: 6px 12px 10px 12px; }

    .logo { width: 150px; }

    .icon-link { width: 30px; height: 30px; }
    .support-btn { padding: 6px 8px; font-size: 12px; }
}

@media (max-width: 480px) {
    .main-bar { gap: 8px; }
    .main-left { gap: 6px; font-size: 10px; }
    .tagline { display: none; }
    .support-btn { width: 100%; text-align: center; padding: 6px 8px; }
}
</style>
