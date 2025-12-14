<template>
  <section class="newsletter">
    <div class="section-container">
      <div class="newsletter-box">
        <h2 class="newsletter-title">Restez informé</h2>
        <p class="newsletter-subtitle">Recevez les dernières actualités directement dans votre boîte mail</p>
        <div class="newsletter-form">
          <input type="email" placeholder="Votre adresse email" class="newsletter-input">
          <button class="newsletter-btn">S'abonner</button>
        </div>
        <p class="newsletter-disclaimer">Nous respectons votre vie privée. Désinscription facile.</p>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
</script>

<style scoped>
.newsletter {
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  padding: 40px 20px;
}

.section-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.newsletter-box {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  padding: 40px;
  text-align: center;
  color: #fff;
  max-width: 600px;
  margin: 0 auto;
}

.newsletter-title {
  margin: 0;
  font-size: 28px;
  font-weight: 700;
  margin-bottom: 12px;
}

.newsletter-subtitle {
  margin: 0 0 24px 0;
  font-size: 16px;
  opacity: 0.9;
}

.newsletter-form {
  display: flex;
  gap: 12px;
  margin-bottom: 16px;
}

.newsletter-input {
  flex: 1;
  padding: 12px 16px;
  border: none;
  border-radius: 8px;
  font-size: 14px;
}

.newsletter-input::placeholder {
  color: #999;
}

.newsletter-input:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(123, 92, 224, 0.3);
}

.newsletter-btn {
  padding: 12px 24px;
  background: #7b5ce0;
  color: #fff;
  border: none;
  border-radius: 8px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s ease;
}

.newsletter-btn:hover {
  background: #6a4dc7;
  transform: translateY(-2px);
}

.newsletter-disclaimer {
  margin: 0;
  font-size: 12px;
  opacity: 0.8;
}

@media (max-width: 680px) {
  .newsletter-box {
    padding: 30px 20px;
  }

  .newsletter-form {
    flex-direction: column;
  }
}
</style>
