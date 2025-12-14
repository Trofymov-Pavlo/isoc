<template>
  <section class="newsletter-section">
    <div class="section-container newsletter-box">
      <h2 class="newsletter-title">Restez informé</h2>
      <p class="newsletter-desc">Abonnez-vous pour recevoir les derniers épisodes et analyses</p>
      <div class="newsletter-form">
        <input type="email" placeholder="Votre adresse email" class="newsletter-input" />
        <button class="newsletter-btn">S'abonner</button>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
</script>

<style scoped>
.newsletter-section { padding: 60px 20px; }
.section-container { max-width: 900px; margin: 0 auto; }
.newsletter-box { background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%); color: #fff; padding: 48px; border-radius: 12px; text-align: center; }
.newsletter-title { font-size: 28px; font-weight: 700; margin: 0 0 12px; }
.newsletter-desc { font-size: 16px; opacity: 0.9; margin: 0 0 24px; }
.newsletter-form { display: flex; gap: 12px; max-width: 500px; margin: 0 auto; flex-wrap: wrap; }
.newsletter-input { flex: 1; min-width: 200px; padding: 12px 16px; border: none; border-radius: 8px; font-size: 14px; }
.newsletter-input::placeholder { color: #999; }
.newsletter-btn { padding: 12px 24px; background: #7b5ce0; color: #fff; border: none; border-radius: 8px; font-weight: 700; cursor: pointer; transition: all 0.3s ease; white-space: nowrap; }
.newsletter-btn:hover { background: #6a4dc7; transform: translateY(-2px); }

@media (max-width: 480px) { .newsletter-form { flex-direction: column; } }
</style>
