<template>
  <!-- Exemples d'usage dynamiques -->
  <p>{{ textes[lang].edition }}</p>
  <p>{{ textes[lang].slogan }}</p>

  <div class="emplacement">
    <div class="left">
      <!-- Sélecteur de langues (utilise NuxtLink si tu es en Nuxt) -->
      <div class="choixlangue">
        <NuxtLink class="fr" to="/" :class="{ active: lang === 'fr' }">
          <p class="langue">FRANÇAIS</p>
        </NuxtLink>
        <NuxtLink class="ru" to="/ru" :class="{ active: lang === 'ru' }">
          <p class="langue">РУССКИЙ</p>
        </NuxtLink>
      </div>

      <p class="date">{{ date }}</p>
      <p class="top-text">{{ textes[lang].edition }}</p>
    </div>

    <div class="logoTitre" @click="goIndex">
      <img :src="logo" alt="AXIOME" />
      <p class="slogant">{{ textes[lang].slogan }}</p>
    </div>

    <div class="icons">
      <a href="https://mail.google.com" target="_blank" rel="noopener">
        <v-icon icon="mdi-email"></v-icon>
      </a>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import logo from '@/assets/logoIsoc.png'

/** Langues supportées */
type Lang = 'fr' | 'ru'

/** Prop langue (typée en union) */
const { lang } = defineProps<{ lang: Lang }>()

/** Textes par langue (figés via `as const`) */
const textes = {
  fr: {
    langue: 'FRANÇAIS',
    edition: 'Édition du jour',
    slogan: 'Le meilleur de l’actu'
  },
  ru: {
    langue: 'РУССКИЙ',
    edition: 'Выпуск дня',
    slogan: 'Лучшее из новостей'
  }
} as const

/** Date formatée selon la langue */
const localeMap: Record<Lang, string> = { fr: 'fr-FR', ru: 'ru-RU' }
const date = computed(() =>
  new Date().toLocaleDateString(localeMap[lang], {
    weekday: 'long',
    month: 'long',
    day: 'numeric'
  })
)

/** Navigation vers la page d’accueil (route `/`) */
function goIndex() {
  window.location.href = '/'
}
</script>

<style scoped>
.emplacement {
  background: linear-gradient(to right, #ffffff, #dbc2f8, #ffffff);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* LANG SWITCHER */
.choixlangue {
  display: flex;
  gap: 8px;
  align-items: center;
}
.choixlangue a,
.choixlangue :deep(a) {
  display: inline-flex;
  text-decoration: none;
  color: inherit;
}
.choixlangue .active .langue {
  font-weight: 700;
  text-decoration: underline;
}

.left {
  display: flex;
  flex-direction: column;
  gap: 2px;
  line-height: 1;
}

.langue {
  font-family: 'arial', serif;
  font-size: 10px; /* 6px était trop petit */
  color: #615d5d;
}

/* DATE / TITRE */
.date {
  font-family: 'Playfair', serif;
  font-size: 14px;
  color: black;
  text-transform: capitalize;
}
.top-text {
  font-size: 8px;
  color: #615d5d;
  opacity: 0.8;
}

/* LOGO + SLOGAN */
.logoTitre {
  display: flex;
  align-items: center;
  padding: 10px 20px;
  border-radius: 8px;
}
.logoTitre a {
  text-decoration: none;
  color: inherit;
}
img {
  width: 200px;
  height: 120px;
}
.slogant {
  font-family: 'arial', sans-serif;
  font-size: 12px;
  letter-spacing: 0.1px;
  color: #342466;
  opacity: 0.9;
  transform: translateX(-130px) translateY(20px);
}

/* ICONS */
.icons {
  font-size: 15px;
  color: black;
  display: flex;
  gap: 10px;
  transform: translateX(-50px);
}
.icons :deep(.v-icon:hover) {
  color: #7b5ce0;
  transform: scale(1.1);
}
.icons a {
  text-decoration: none;
  color: inherit;
}
</style>
