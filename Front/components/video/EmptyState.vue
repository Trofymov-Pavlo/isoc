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
.empty-state {
  text-align: center;
  padding: 80px 20px;
}

.empty-icon {
  font-size: 64px;
  display: block;
  margin-bottom: 16px;
  opacity: 0.4;
}

.empty-text {
  font-size: 16px;
  color: #666;
  margin: 0 0 20px;
}

.reset-btn {
  padding: 10px 24px;
  background: #2f0538;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.22s ease;
}

.reset-btn:hover {
  background: #4b2faa;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(47, 5, 56, 0.3);
}
</style>
