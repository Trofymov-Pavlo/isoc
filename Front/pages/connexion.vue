<template>
  <main class="shell">
    <div class="card">
      <h1>Connexion</h1>
      <p>Connectez-vous pour accéder à vos contenus personnalisés. Cette page arrive très bientôt.</p>
    </div>
  </main>
</template>

<script setup lang="ts">
</script>

<style scoped>
.shell {
  min-height: 70vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #f7f7fb;
  padding: 40px 16px;
}

.card {
  max-width: 760px;
  width: 100%;
  background: #ffffff;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
  padding: 32px;
}

h1 {
  margin: 0 0 12px;
  font-size: 28px;
}

p {
  margin: 0;
  color: #4a4a55;
}
</style>
