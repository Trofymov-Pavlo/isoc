<template>
  <div class="loading-state">
    <div class="spinner"></div>
    <p>Chargement des actualités...</p>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.loading-state {
  text-align: center;
  padding: 80px 20px;
  color: #666;
}

.spinner {
  width: 40px;
  height: 40px;
  margin: 0 auto 16px;
  border: 3px solid rgba(123, 92, 224, 0.2);
  border-top-color: #7b5ce0;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
</style>
