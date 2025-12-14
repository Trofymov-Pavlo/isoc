<template>
  <div class="empty-state">
    <span class="empty-icon">🎥</span>
    <p class="empty-text">Aucune vidéo ne correspond à votre recherche</p>
    <button class="reset-btn" @click="$emit('reset')">Réinitialiser</button>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.empty-state { max-width: 1200px; margin: 80px auto; padding: 60px 20px; text-align: center; }
.empty-icon { font-size: 64px; display: block; margin-bottom: 20px; }
.empty-text { font-size: 18px; color: #666; margin-bottom: 24px; }
.reset-btn { padding: 12px 24px; border-radius: 8px; border: none; background: linear-gradient(135deg, #2f0538, #4b2faa); color: #fff; font-size: 14px; font-weight: 600; cursor: pointer; transition: all 0.3s ease; }
.reset-btn:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(47, 5, 56, 0.3); }
</style>
