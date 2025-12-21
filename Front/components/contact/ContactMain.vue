<template>
  <main class="contact-page">

    <div class="contact-wrapper">
      <div class="form-wrapper">
        <form class="contact-form" action="https://formsubmit.co/nathan.barrachin@gmail.com" method="POST">
          <input type="hidden" name="_subject" value="Nouveau message depuis Axiome">
          <input type="hidden" name="_captcha" value="false">
          <input type="hidden" name="_template" value="table">
          <input type="text" name="_honey" style="display:none">
          <input type="hidden" name="_next" value="https://axiome.local/thank-you">

          <div class="form-group">
            <label for="name" class="form-label">Nom *</label>
            <input
              type="text"
              id="name"
              name="name"
              class="form-input"
              placeholder="Votre nom complet"
              required
            />
          </div>

          <div class="form-group">
            <label for="email" class="form-label">Email *</label>
            <input
              type="email"
              id="email"
              name="email"
              class="form-input"
              placeholder="votre.email@exemple.com"
              required
            />
          </div>

          <div class="form-group">
            <label for="subject" class="form-label">Sujet</label>
            <input
              type="text"
              id="subject"
              name="subject"
              class="form-input"
              placeholder="Objet de votre message"
            />
          </div>

          <div class="form-group">
            <label for="message" class="form-label">Message *</label>
            <textarea
              id="message"
              name="message"
              class="form-textarea"
              rows="6"
              placeholder="Écrivez votre message ici..."
              required
            ></textarea>
          </div>

          <button type="submit" class="submit-btn">
            <span class="btn-text">Envoyer le message</span>
            <span class="btn-icon">→</span>
          </button>
        </form>
      </div>
    </div>
  </main>
</template>

<script setup lang="ts">

</script>

<style scoped>
.contact-page {
  min-height: 100vh;
  background: #fff;
}

.contact-wrapper {
  max-width: 1400px;
  margin: 0 auto;
  padding: 48px calc(2vw) 60px;
}

.form-wrapper {
  max-width: 600px;
  margin: 0 auto;
}

.contact-form {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-label {
  font-size: 14px;
  font-weight: 600;
  color: #2f0538;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.form-input,
.form-textarea {
  padding: 12px 16px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-family: inherit;
  font-size: 14px;
  transition: all 0.2s ease;
}

.form-input::placeholder,
.form-textarea::placeholder {
  color: #999;
}

.form-input:focus,
.form-textarea:focus {
  outline: none;
  border-color: #2f0538;
  background: #fff;
  box-shadow: 0 2px 8px rgba(47, 5, 56, 0.1);
}

.form-textarea {
  resize: vertical;
  min-height: 150px;
}

.submit-btn {
  padding: 14px 32px;
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  color: #fff;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.submit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(47, 5, 56, 0.3);
}

@media (max-width: 680px) {
  .contact-wrapper {
    padding: 32px calc(2vw) 40px;
  }
}
</style>
