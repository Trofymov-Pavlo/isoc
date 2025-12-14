<template>
  <section class="cta-section">
    <div class="section-container cta-box">
      <h2 class="cta-title">{{ title }}</h2>
      <p class="cta-desc">{{ description }}</p>
      <button class="cta-button">{{ ctaText }}</button>
    </div>
  </section>
</template>

<script setup lang="ts">
const props = defineProps<{ title: string; description: string; ctaText: string }>();
</script>

<style scoped>
.cta-section { background: linear-gradient(135deg, #7b5ce0, #9d7fee); color: #fff; padding: 60px 20px; }
.section-container { max-width: 900px; margin: 0 auto; }
.cta-box { text-align: center; }
.cta-title { font-size: 36px; font-weight: 700; margin: 0 0 12px; }
.cta-desc { font-size: 16px; opacity: 0.95; margin: 0 0 24px; }
.cta-button { padding: 14px 32px; background: #fff; color: #7b5ce0; border: none; border-radius: 8px; font-weight: 700; cursor: pointer; transition: all 0.3s ease; font-size: 15px; }
.cta-button:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2); }

@media (max-width: 480px) {
  .cta-title { font-size: 24px; }
}
</style>
