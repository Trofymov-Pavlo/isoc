<template>
  <div class="sub-header">
    <div class="container">
      <nav class="nav">
        <NuxtLink to="/" class="nav-link">Accueil</NuxtLink>
        <NuxtLink to="/inLivePage" class="nav-link">En Direct</NuxtLink>
      </nav>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.sub-header {
  background: linear-gradient(90deg, #2f0538 0%, #3a0f4f 100%);
  color: #f0f0f3;
  border-bottom: 1px solid rgba(123, 92, 224, 0.25);
  padding: 0;
}

.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 calc(2vw);
  display: flex;
  align-items: center;
}

.nav {
  display: flex;
  gap: 28px;
  align-items: center;
  padding: 12px 0;
}

.nav-link {
  color: #e8e4f0;
  text-decoration: none;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.3px;
  position: relative;
  transition: all 0.22s ease;
  padding-bottom: 2px;
  border-bottom: 2px solid transparent;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: linear-gradient(90deg, #7b5ce0, #c5b3ff);
  transition: width 0.22s ease;
}

.nav-link:hover {
  color: #c5b3ff;
}

.nav-link:hover::after {
  width: 100%;
}

@media (max-width: 768px) {
  .nav {
    gap: 16px;
    font-size: 12px;
  }
}
</style>
