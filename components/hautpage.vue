<template>
  <div class="emplacement">
    <div class="left">
        <div class="choixlangue">
            <a class= "fr" href="/">
                <p class="langue">FRANCAIS</p>
            </a>
            <a class= "choixlangue" href="/">
                <p class="langue">RUSSE</p>
            </a>
        </div>
        <p class="date">{{ date }}</p>
        <p class="top-text">Édition du jour</p>
    </div>
    <div class="logoTitre" @click="goIndex">
      <img :src="logo" />
      <p class="slogant">Le meilleur de l’actu</p>
          
    </div>
    <div class="icons">
        <a href="https://mail.google.com" target="_blank">
            <v-icon icon="mdi-email"></v-icon>
        </a>
    </div>
  </div>
</template>

<script setup lang="ts">

import logo from '@/assets/logoIsoc.png'

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

.choixlangue {
    display: flex;
    gap: 5px;
    color: #615d5d;
}
.choixlangue a{
    display: inline-flex;
    text-decoration: none;
    color: inherit;

}

.fr {
    text-decoration: none;
    color: inherit;
}

.emplacement {
    background: #ffffff;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

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


.left {
    display: flex;
    flex-direction: column;
    gap: 1px;
    column-fill: auto;
    line-height: .9;
}
.langue {
    font-family: 'arial', serif;
    font-size: 6px;
    color: #615d5d;
    display: flex;
    gap: 0px;
    transform: translateX(20px);
}
.date {
    font-family: 'Playfair', serif;
    font-size: 14px;
    color: black;
    text-transform: capitalize;
    transform: translateX(20px);
}

.top-text {
    font-size: 8px;
    color: #615d5d;
    opacity: 0.8;
    transform: translateX(20px);
}


</style>
