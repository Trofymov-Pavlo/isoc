<template>
  <div class="sub_header">
    <div class="links">
      <router-link to="/" class="lnk">Accueil</router-link>
      <router-link to="/inLivePage" class="lnk">En Direct</router-link>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.sub_header {
  background-color: #2f0538;
  color: white;
  height: 40px;
  display: flex;
  align-items: center;
  padding: 0 18px;
  gap: 20px;
  font-size: 14px;
  font-weight: 500;
  width: 100%;
  margin-top: 0; /* ensure it sits directly above the header */
  position: relative;
  z-index: 40;
}

.links {
  display: flex;
  gap: 15px;
}

.lnk {
  color: white;
  text-decoration: none;
  font-weight: 600;
}

.lnk:hover {
  color: #ffdf5f;
}
</style>
