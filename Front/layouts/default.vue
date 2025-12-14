<template>
  <div class="site-container">
    <HeaderMain />
  </div>

  <HeaderSubHeader />

  <div class="site-container">
    <slot />
  </div>

  <FooterMain />
</template>

<style>
.site-container {
  max-width: 1400px;
  margin: 0 auto;
  width: 100%;
  padding: 0 calc(2vw);
}

html, body {
  margin: 0;
}
</style>
