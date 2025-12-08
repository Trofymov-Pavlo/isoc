<template>
  <div class="sub-header">
    <div class="container">
      <nav class="nav">
        <NuxtLink to="/" class="nav-link">Accueil</NuxtLink>
        <NuxtLink to="/inLivePage" class="nav-link active">
          <span class="live-badge">●</span>
          En Direct
        </NuxtLink>
        <div class="nav-divider"></div>
        <NuxtLink to="/" class="nav-link">Analyses</NuxtLink>
        <NuxtLink to="/" class="nav-link">Ressources</NuxtLink>
        <NuxtLink to="/" class="nav-link">À propos</NuxtLink>
      </nav>
      <div class="nav-right">
        <div class="search-icon">🔍</div>
        <div class="theme-toggle">🌙</div>
      </div>
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
  justify-content: space-between;
}

.nav {
  display: flex;
  gap: 0;
  align-items: center;
  padding: 0;
  flex: 1;
}

.nav-link {
  color: #e8e4f0;
  text-decoration: none;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.3px;
  position: relative;
  transition: all 0.22s ease;
  padding: 14px 16px;
  display: flex;
  align-items: center;
  gap: 6px;
  border-right: 1px solid rgba(123, 92, 224, 0.15);
}

.nav-link:last-of-type {
  border-right: none;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 16px;
  right: 16px;
  width: 0;
  height: 3px;
  background: linear-gradient(90deg, #7b5ce0, #c5b3ff);
  transition: width 0.22s ease;
  margin: 0 auto;
}

.nav-link:hover {
  color: #c5b3ff;
  background: rgba(123, 92, 224, 0.08);
}

.nav-link:hover::after {
  width: calc(100% - 32px);
}

.nav-link.active {
  color: #7b5ce0;
}

.nav-link.active::after {
  width: calc(100% - 32px);
}

.live-badge {
  font-size: 10px;
  color: #ff6b6b;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.4;
  }
}

.nav-divider {
  width: 1px;
  height: 20px;
  background: rgba(123, 92, 224, 0.25);
  margin: 0 4px;
}

.nav-right {
  display: flex;
  gap: 12px;
  align-items: center;
  margin-left: auto;
  padding-left: 16px;
  border-left: 1px solid rgba(123, 92, 224, 0.15);
}

.search-icon,
.theme-toggle {
  font-size: 16px;
  cursor: pointer;
  transition: all 0.22s ease;
  padding: 8px;
}

.search-icon:hover,
.theme-toggle:hover {
  color: #7b5ce0;
  transform: scale(1.1);
}

@media (max-width: 1024px) {
  .nav-link {
    font-size: 12px;
    padding: 12px 12px;
  }
  
  .nav-divider {
    display: none;
  }
}

@media (max-width: 768px) {
  .nav-link {
    font-size: 11px;
    padding: 10px 8px;
    border-right: none;
  }

  .nav-divider {
    display: none;
  }

  .nav-right {
    border-left: none;
    gap: 8px;
    padding-left: 8px;
  }

  .search-icon,
  .theme-toggle {
    font-size: 14px;
    padding: 6px;
  }
}

@media (max-width: 480px) {
  .container {
    padding: 0 calc(1vw);
  }

  .nav-link {
    font-size: 10px;
    padding: 8px 6px;
  }

  .nav-link::after {
    display: none;
  }
}
</style>
