<template>
  <header class="site-header masthead">
    <div class="container header-inner">
      <div class="header-left">
        <div class="lang">FRANÇAIS | <span class="lang-link">RUSSE</span></div>
      </div>

      <div class="header-center">
        <div class="site-logo">Axium</div>
      </div>

      <div class="header-right">
        <div class="auth">Se connecter</div>
        <button class="subscribe">S'abonner</button>
      </div>
    </div>

    <nav class="main-nav">
      <div class="container nav-inner">
        <a href="#">Actualités</a>
        <a href="#">Économie</a>
        <a href="#">Vidéos</a>
        <a href="#">Débats</a>
        <a href="#">Culture</a>
        <a href="#">Services</a>
      </div>
    </nav>
  </header>
</template>

<style scoped>
.header-inner { display:flex; align-items:center; justify-content:space-between; padding:8px 20px }
.header-left .lang { font-size:12px; color:var(--muted) }
.header-center { text-align:center }
.site-logo { font-family: 'Merriweather', Georgia, serif; font-size:52px; letter-spacing:1px }
.header-right { display:flex; gap:12px; align-items:center }
.auth { color:var(--muted); font-size:14px }
.subscribe { background:#ffd400; border: none; padding:8px 12px; border-radius:4px; cursor:pointer }
.main-nav { border-top:3px solid #137388; border-bottom:3px solid #137388; background:white }
.nav-inner { display:flex; gap:18px; padding:12px 20px; font-weight:600 }
.nav-inner a { color:#0b3b46; text-decoration:none }
</style>
