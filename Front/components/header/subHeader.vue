<template>
  <div class="sub-header">
    <div class="container">
      <nav class="nav">
        <NuxtLink to="/" class="nav-link" exact-active-class="is-active">Accueil</NuxtLink>
        <NuxtLink to="/inLivePage" class="nav-link" exact-active-class="is-active">
          <span class="live-badge">●</span>
          En Direct
        </NuxtLink>
        <div class="nav-divider"></div>
        <NuxtLink to="/featuredArticle" class="nav-link" exact-active-class="is-active">Article en Vedette</NuxtLink>
        <NuxtLink to="/podcast" class="nav-link" exact-active-class="is-active">Podcast</NuxtLink>
        <NuxtLink to="/video" class="nav-link" exact-active-class="is-active">Vidéo</NuxtLink>
      </nav>
      <div class="nav-right">
        <button class="icon-btn search-btn" title="Rechercher">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <path d="m21 21-4.35-4.35"></path>
          </svg>
        </button>
        <button class="icon-btn theme-btn" title="Changer de thème">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
          </svg>
        </button>
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
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 calc(2vw);
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 56px;
}

.nav {
  display: flex;
  gap: 0;
  align-items: center;
  padding: 0;
  flex: 1;
  height: 100%;
}

.nav-link {
  color: #e8e4f0;
  text-decoration: none;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.3px;
  position: relative;
  transition: all 0.22s ease;
  padding: 0 16px;
  display: flex;
  align-items: center;
  gap: 6px;
  height: 100%;
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

/* Active state - only when on that page */
.nav-link.is-active {
  color: #c5b3ff;
}

.nav-link.is-active::after {
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
  gap: 8px;
  align-items: center;
  margin-left: auto;
  padding-left: 16px;
  border-left: 1px solid rgba(123, 92, 224, 0.15);
  height: 100%;
}

.icon-btn {
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  transition: all 0.22s ease;
  color: #e8e4f0;
}

.icon-btn:hover {
  background: rgba(123, 92, 224, 0.15);
  color: #c5b3ff;
  transform: translateY(-2px);
}

.icon-btn:active {
  transform: translateY(0);
  background: rgba(123, 92, 224, 0.25);
}

.icon {
  width: 20px;
  height: 20px;
  stroke: currentColor;
}

@media (max-width: 1024px) {
  .nav-link {
    font-size: 12px;
    padding: 0 12px;
  }
  
  .nav-divider {
    display: none;
  }

  .icon {
    width: 18px;
    height: 18px;
  }
}

@media (max-width: 768px) {
  .nav-link {
    font-size: 11px;
    padding: 0 8px;
    border-right: none;
  }

  .nav-divider {
    display: none;
  }

  .nav-right {
    border-left: none;
    gap: 6px;
    padding-left: 8px;
  }

  .icon-btn {
    padding: 6px;
  }

  .icon {
    width: 18px;
    height: 18px;
  }
}

@media (max-width: 480px) {
  .container {
    padding: 0 calc(1vw);
  }

  .nav-link {
    font-size: 10px;
    padding: 0 6px;
  }

  .nav-link::after {
    display: none;
  }

  .icon-btn {
    padding: 4px;
  }

  .icon {
    width: 16px;
    height: 16px;
  }
}
</style>
