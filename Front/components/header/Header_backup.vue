<template>
  <header class="header">
    <nav class="header-nav">
      <div class="container">
        <div class="nav-content">
          <!-- Left: logo + tagline badge -->
          <div class="nav-left">
            <div class="logo-block" @click="goIndex">
              <img :src="logo" alt="ISOC AXIOM" class="logo-img" />
            </div>
            <div class="tagline-pill">
              <span class="pulse-indicator"></span>
              <span class="tagline">Média indépendant | Conflit Ukraine-Russie</span>
            </div>
          </div>

          <!-- Navigation links centered -->
          <div class="nav-links">
            <NuxtLink to="/" exact-active-class="active">Accueil</NuxtLink>
            <NuxtLink to="/en-direct" exact-active-class="active">
              <span class="live-dot"></span>En Direct
            </NuxtLink>
            <NuxtLink to="/explorer" exact-active-class="active">Explorer</NuxtLink>
            <NuxtLink to="/liked" exact-active-class="active">Mes Favoris</NuxtLink>
            <NuxtLink to="/a-propos" exact-active-class="active">À Propos</NuxtLink>
            <NuxtLink to="/contact" exact-active-class="active">Contact</NuxtLink>
          </div>

          <!-- Right side: Search, RSS, Account -->
          <div class="nav-right">
            <div class="search-box">
              <button class="search-toggle" @click="toggleSearch" title="Rechercher">
                <style scoped>
                * { box-sizing: border-box; }

                .header {
                  position: sticky;
                  top: 0;
                  z-index: 1000;
                  background: #ffffff;
                  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
                }

                .header-nav {
                  padding: 12px 0;
                  border-bottom: 1px solid #e9ecf1;
                  background: #ffffff;
                }

                .container {
                  max-width: 1400px;
                  margin: 0 auto;
                  padding: 0 32px;
                }

                .nav-content {
                  display: grid;
                  grid-template-columns: auto 1fr auto;
                  align-items: center;
                  gap: 20px;
                }

                .nav-left {
                  display: flex;
                  align-items: center;
                  gap: 12px;
                  min-width: 0;
                }

                .logo-block {
                  display: flex;
                  align-items: center;
                  cursor: pointer;
                  transition: opacity 0.2s ease;
                }

                .logo-block:hover { opacity: 0.85; }

                .logo-img {
                  height: 42px;
                  width: auto;
                }

                .tagline-pill {
                  display: inline-flex;
                  align-items: center;
                  gap: 8px;
                  padding: 8px 12px;
                  background: rgba(15, 23, 42, 0.06);
                  border: 1px solid rgba(15, 23, 42, 0.08);
                  border-radius: 999px;
                  font-size: 12px;
                  color: #1f2937;
                  white-space: nowrap;
                }

                .pulse-indicator {
                  width: 8px;
                  height: 8px;
                  background: #ff5c5c;
                  border-radius: 50%;
                  box-shadow: 0 0 0 8px rgba(255, 92, 92, 0.14);
                  animation: pulse 1.8s ease-in-out infinite;
                }

                @keyframes pulse {
                  0%, 100% { opacity: 1; box-shadow: 0 0 0 8px rgba(255, 92, 92, 0.14); }
                  50% { opacity: 0.6; box-shadow: 0 0 0 14px rgba(255, 92, 92, 0.08); }
                }

                .tagline { font-weight: 700; letter-spacing: 0.2px; }

                .nav-links {
                  display: flex;
                  justify-content: center;
                  gap: 26px;
                  flex: 1;
                  min-width: 0;
                }

                .nav-links a {
                  position: relative;
                  color: #1f2937;
                  text-decoration: none;
                  font-size: 13px;
                  font-weight: 600;
                  letter-spacing: 0.2px;
                  display: inline-flex;
                  align-items: center;
                  gap: 6px;
                  padding: 6px 0;
                  transition: color 0.2s ease;
                }

                .nav-links a:hover { color: #111827; }

                .nav-links a.active {
                  color: #6d5dd3;
                }

                .nav-links a.active::after {
                  content: '';
                  position: absolute;
                  left: 0;
                  right: 0;
                  bottom: -8px;
                  height: 3px;
                  background: linear-gradient(90deg, #6d5dd3 0%, #8c7cff 100%);
                  border-radius: 999px;
                }

                .live-dot {
                  width: 6px;
                  height: 6px;
                  background: #ff5c5c;
                  border-radius: 50%;
                  display: inline-block;
                  animation: pulse 1.8s ease-in-out infinite;
                }

                .nav-right {
                  display: flex;
                  align-items: center;
                  gap: 14px;
                }

                .search-box { position: relative; }

                .search-toggle {
                  display: inline-flex;
                  align-items: center;
                  justify-content: center;
                  width: 38px;
                  height: 38px;
                  background: #ffffff;
                  border: 1px solid #d9dce3;
                  border-radius: 10px;
                  color: #5b6170;
                  cursor: pointer;
                  transition: all 0.2s ease;
                }

                .search-toggle:hover {
                  border-color: #6d5dd3;
                  color: #6d5dd3;
                  box-shadow: 0 6px 18px rgba(109, 93, 211, 0.18);
                }

                .search-toggle svg { width: 18px; height: 18px; }

                .search-dropdown {
                  position: absolute;
                  top: 100%;
                  right: 0;
                  margin-top: 10px;
                  background: #ffffff;
                  border: 1px solid #e4e7ed;
                  border-radius: 12px;
                  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.14);
                  padding: 12px;
                  min-width: 320px;
                }

                .search-input {
                  width: 100%;
                  padding: 10px 14px;
                  border: 1px solid #d9dce3;
                  border-radius: 10px;
                  font-size: 13px;
                  color: #111827;
                  background: #ffffff;
                  transition: all 0.2s ease;
                }

                .search-input:focus {
                  outline: none;
                  border-color: #6d5dd3;
                  box-shadow: 0 0 0 3px rgba(109, 93, 211, 0.15);
                }

                .icon-link {
                  display: inline-flex;
                  align-items: center;
                  justify-content: center;
                  width: 28px;
                  height: 28px;
                  color: #5b6170;
                  text-decoration: none;
                  transition: all 0.2s ease;
                }

                .icon-link:hover { color: #111827; }

                .icon-link svg { width: 100%; height: 100%; }

                .account-btn {
                  padding: 9px 16px;
                  background: linear-gradient(120deg, #6d5dd3, #8c7cff);
                  border: 1px solid #6d5dd3;
                  border-radius: 10px;
                  color: #ffffff;
                  font-size: 13px;
                  font-weight: 700;
                  text-decoration: none;
                  transition: all 0.2s ease;
                  white-space: nowrap;
                }

                .account-btn:hover {
                  box-shadow: 0 10px 30px rgba(109, 93, 211, 0.3);
                  transform: translateY(-1px);
                }

                .search-panel-enter-active,
                .search-panel-leave-active { transition: all 0.2s ease; }
                .search-panel-enter-from,
                .search-panel-leave-to { opacity: 0; transform: translateY(-6px); }

                @media (max-width: 1100px) {
                  .container { padding: 0 24px; }
                  .nav-links { gap: 18px; }
                }

                @media (max-width: 900px) {
                  .nav-content { grid-template-columns: 1fr; gap: 14px; }
                  .nav-left { justify-content: center; }
                  .nav-right { justify-content: center; flex-wrap: wrap; }
                  .nav-links { justify-content: center; flex-wrap: wrap; }
                }

                @media (max-width: 640px) {
                  .container { padding: 0 16px; }
                  .logo-img { height: 34px; }
                  .tagline { display: none; }
                  .tagline-pill { padding: 6px 10px; }
                  .nav-links { gap: 12px; }
                  .nav-links a { font-size: 12px; }
                  .search-dropdown { min-width: 260px; right: 0; }
                }

                @media (max-width: 480px) {
                  .nav-right { gap: 10px; }
                  .account-btn { padding: 8px 12px; font-size: 12px; }
                  .search-dropdown {
                    position: fixed;
                    left: 16px;
                    right: 16px;
                    width: auto;
                    min-width: unset;
                  }
                }
                </style>
    height: 36px;
  }

  .nav-links {
    gap: 16px;
  }

  .nav-links a {
    font-size: 11px;
  }

  .nav-right {
    gap: 12px;
  }

  .search-dropdown {
    min-width: 260px;
    right: -12px;
  }
}

@media (max-width: 480px) {
  .tagline-bar {
    padding: 8px 12px;
    font-size: 11px;
    gap: 8px;
  }

  .header-nav {
    padding: 10px 0;
  }

  .tagline-bar,
  .nav-content {
    padding: 0 12px;
  }

  .tagline {
    display: none;
  }

  .logo-img {
    height: 32px;
  }

  .nav-links {
    gap: 12px;
    flex: 1;
  }

  .nav-links a {
    font-size: 10px;
  }

  .nav-right {
    gap: 8px;
  }

  .search-dropdown {
    position: fixed;
    left: 16px;
    right: 16px;
    width: auto;
    min-width: unset;
  }
}
</style>
