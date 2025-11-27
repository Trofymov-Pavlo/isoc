
<!-- layouts/default.vue -->
<template>
  <div class="site">
    <HeaderBar />
    <TickerBar />
    <AdBanner />

    <div class="container">
      <main class="content">
        <slot />
      </main>

      <aside class="aside">
        <div class="sidebar-box">
          <h3>À la une</h3>
          <ul>
            <li><a href="#">Économie</a></li>
            <li><a href="#">Culture</a></li>
            <li><a href="#">Science</a></li>
            <li><a href="#">Idées</a></li>
            <li><a href="#">Archives</a></li>
          </ul>
        </div>
      </aside>
    </div>

    <FooterBar />
  </div>
</template>

