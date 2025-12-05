<template>
    <div class="header-container">
        <div class="left-block">
            <div class="language-select">
                <a class="fr" href="/">
                    <p class="language-text">FRENCH</p>
                </a>
            </div>
        </div>

        <p class="date">{{ date }}</p>
        <p class="top-text">Édition du jour</p>
    </div>
    <div class="logoTitre" @click="goIndex">
      <img :src="logo" />
      <p class="slogant">Le meilleur de l’actu</p>
          
    </div>
    <div class="icons">
        <a href="/Contact" target="_blank" class="icon-wrapper">
            <v-icon icon="mdi-email"></v-icon>
            <p class="icon-text">Nous contacter</p>
        </a>
    </div>
</template>

<script setup lang="ts">
import logoImg from '@/assets/logoIsoc.png'

const logo = logoImg

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


.icon-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-decoration: none;
}

.icon-text{
    font-family: 'arial', sans-serif;
    font-size: 10px;
    margin: 4px;
    color: inherit
}

.choixlangue {
    display: flex;
    gap: 5px;
    color: #615d5d;
}

.language-select a {
    display: inline-flex;
    text-decoration: none;
    color: inherit;
}

.fr {
    text-decoration: none;
    color: inherit;
}

.header-container {
    background: #ffffff;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo-title {
    display: flex;
    align-items: center;
    padding: 10px 20px;
    border-radius: 8px;
}

.logo-title a {
    text-decoration: none;
    color: inherit;
}

img {
    width: 200px;
    height: 120px;
}

.slogan {
  font-family: 'arial', sans-serif;
  font-size: 12px;
  letter-spacing: .1px;
  color: #342466; 
  opacity: .9;
  transform: translateX(-130px) translateY(20px);
}

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

.left-block {
    display: flex;
    flex-direction: column;
    gap: 1px;
    column-fill: auto;
    line-height: .9;
}

.language-text {
    font-family: 'arial', serif;
    font-size: 6px;
    color: #615d5d;
    display: flex;
    gap: 0px;
    transform: translateX(20px);
}

.date-text {
    font-family: 'Playfair', serif;
    font-size: 14px;
    color: black;
    text-transform: capitalize;
    transform: translateX(20px);
}

.edition-text {
    font-size: 8px;
    color: #615d5d;
    opacity: 0.8;
    transform: translateX(20px);
}

</style>
