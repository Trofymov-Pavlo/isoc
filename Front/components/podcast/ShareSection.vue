<template>
  <section class="share-section">
    <h3 class="share-title">Partager ce podcast</h3>
    <div class="share-buttons">
      <a href="#" class="share-btn twitter" title="Partager sur X">X</a>
      <a href="#" class="share-btn facebook" title="Partager sur Facebook">Facebook</a>
      <a href="#" class="share-btn linkedin" title="Partager sur LinkedIn">LinkedIn</a>
      <a href="#" class="share-btn telegram" title="Partager sur Telegram">Telegram</a>
    </div>
  </section>
</template>

<script setup lang="ts">
</script>

<style scoped>
.share-section { padding: 32px 0; border-top: 1px solid #e5e5e5; border-bottom: 1px solid #e5e5e5; margin-top: 40px; }
.share-title { font-size: 16px; font-weight: 700; color: #1a1a1a; margin: 0 0 16px; }
.share-buttons { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }
.share-btn { display: inline-flex; align-items: center; justify-content: center; width: 44px; height: 44px; border-radius: 8px; text-decoration: none; font-weight: 600; font-size: 12px; transition: all 0.22s ease; color: #fff; }
.share-btn.twitter { background: #000; }
.share-btn.twitter:hover { background: #222; }
.share-btn.facebook { background: #1877f2; }
.share-btn.facebook:hover { background: #166fe5; }
.share-btn.linkedin { background: #0a66c2; }
.share-btn.linkedin:hover { background: #095195; }
.share-btn.telegram { background: #0088cc; }
.share-btn.telegram:hover { background: #0077aa; }
</style>
