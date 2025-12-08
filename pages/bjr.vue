<template>
  <div class="page">
    <h1>Bonjour</h1>
    <button class="btn" @click="onClick">Clique moi</button>
  </div>
</template>

<script setup lang="ts">
const onClick = () => {
  alert("Bonjour!");
};
</script>

<style scoped>
.page { padding: 24px; font-family: sans-serif; }
.btn {
  padding: 10px 16px;
  border: none;
  border-radius: 6px;
  background: #2f0538;
  color: #fff;
  cursor: pointer;
  font-weight: 600;
}
.btn:hover { background: #451b52; }
</style>
