<template>
  <div class="contact-page">
    <div class="contact-container">
      <!-- Header Section -->
      <div class="contact-header">
        <h1 class="contact-title">Nous contacter</h1>
        <p class="contact-subtitle">Vos questions, vos suggestions, vos retours - tous les messages comptent</p>
      </div>

      <!-- Two Column Layout -->
      <div class="contact-grid">
        <!-- Form Column -->
        <div class="form-column">
          <div class="form-wrapper">
            <form class="contact-form" action="https://formsubmit.co/nathan.barrachin@gmail.com" method="POST">
              <input type="hidden" name="_subject" value="Nouveau message depuis Axiome">
              <input type="hidden" name="_captcha" value="false">
              <input type="hidden" name="_template" value="table">
              <input type="text" name="_honey" style="display:none">
              <input type="hidden" name="_next" value="https://axiome.local/thank-you">

              <!-- Name Field -->
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

              <!-- Email Field -->
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

              <!-- Subject Field -->
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

              <!-- Message Field -->
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

              <!-- Submit Button -->
              <button type="submit" class="submit-btn">
                <span class="btn-text">Envoyer le message</span>
                <span class="btn-icon">→</span>
              </button>
            </form>
          </div>
        </div>

        <!-- Info Column -->
        <div class="info-column">
          <div class="info-card">
            <h3 class="info-title">📧 Par Email</h3>
            <p class="info-text">Vous pouvez aussi nous écrire directement à :</p>
            <a href="mailto:nathan.barrachin@gmail.com" class="info-link">
              nathan.barrachin@gmail.com
            </a>
          </div>

          <div class="info-card">
            <h3 class="info-title">⏱️ Délai de réponse</h3>
            <p class="info-text">Nous répondons généralement sous 24-48 heures</p>
          </div>

          <div class="info-card">
            <h3 class="info-title">🔒 Confidentialité</h3>
            <p class="info-text">Vos données sont traitées de manière confidentielle et ne seront jamais partagées</p>
          </div>

          <div class="info-card">
            <h3 class="info-title">📰 Suggestions</h3>
            <p class="info-text">Avez-vous une actualité à nous signaler? Un article à analyser?</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import MainHeader from '@/components/header/mainHeader.vue'
import SubHeader from '@/components/header/subHeader.vue'
</script>

<style scoped lang="scss">
.contact-page {
  background: linear-gradient(135deg, #f8f7fc 0%, #fafbff 100%);
  min-height: calc(100vh - 300px);
  padding: 60px 0;
}

.contact-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 calc(2vw);
}

/* Header Section */
.contact-header {
  text-align: center;
  margin-bottom: 60px;
  animation: fadeInDown 0.6s ease;
}

.contact-title {
  font-size: 48px;
  font-weight: 700;
  color: #2f0538;
  margin: 0 0 12px 0;
  letter-spacing: -0.5px;
}

.contact-subtitle {
  font-size: 16px;
  color: #7b5ce0;
  margin: 0;
  font-weight: 500;
}

/* Two Column Grid */
.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: start;
}

/* Form Column */
.form-column {
  animation: fadeInLeft 0.6s ease 0.1s both;
}

.form-wrapper {
  background: #ffffff;
  border-radius: 12px;
  padding: 40px;
  border: 1px solid rgba(123, 92, 224, 0.15);
  box-shadow: 0 4px 20px rgba(47, 5, 56, 0.08);
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
  font-size: 13px;
  font-weight: 600;
  color: #2f0538;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.form-input,
.form-textarea {
  padding: 12px 16px;
  border: 1px solid rgba(123, 92, 224, 0.2);
  border-radius: 8px;
  font-size: 14px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  color: #2f0538;
  transition: all 0.22s ease;
  background: #fafbff;

  &::placeholder {
    color: rgba(47, 5, 56, 0.4);
  }

  &:focus {
    outline: none;
    border-color: #7b5ce0;
    background: #ffffff;
    box-shadow: 0 0 0 3px rgba(123, 92, 224, 0.1);
  }

  &:hover {
    border-color: #7b5ce0;
  }
}

.form-textarea {
  resize: vertical;
  min-height: 120px;
  line-height: 1.6;
}

.submit-btn {
  margin-top: 12px;
  padding: 14px 28px;
  background: linear-gradient(135deg, #2f0538 0%, #3a0f4f 100%);
  color: #ffffff;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 0.3px;
  cursor: pointer;
  transition: all 0.22s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(47, 5, 56, 0.25);
    background: linear-gradient(135deg, #3a0f4f 0%, #450158 100%);
  }

  &:active {
    transform: translateY(0);
  }

  .btn-text {
    flex: 1;
  }

  .btn-icon {
    font-size: 16px;
    transition: transform 0.22s ease;
  }

  &:hover .btn-icon {
    transform: translateX(3px);
  }
}

/* Info Column */
.info-column {
  display: flex;
  flex-direction: column;
  gap: 20px;
  animation: fadeInRight 0.6s ease 0.2s both;
}

.info-card {
  background: #ffffff;
  border-radius: 12px;
  padding: 28px;
  border-left: 4px solid #7b5ce0;
  box-shadow: 0 2px 12px rgba(47, 5, 56, 0.06);
  transition: all 0.22s ease;

  &:hover {
    transform: translateX(4px);
    box-shadow: 0 4px 20px rgba(47, 5, 56, 0.1);
  }
}

.info-title {
  font-size: 16px;
  font-weight: 700;
  color: #2f0538;
  margin: 0 0 8px 0;
  letter-spacing: 0.3px;
}

.info-text {
  font-size: 14px;
  color: #5a5370;
  line-height: 1.6;
  margin: 0;
}

.info-link {
  display: inline-block;
  color: #7b5ce0;
  text-decoration: none;
  font-weight: 600;
  margin-top: 8px;
  transition: all 0.22s ease;
  border-bottom: 1px solid transparent;

  &:hover {
    color: #2f0538;
    border-bottom-color: #7b5ce0;
  }
}

/* Animations */
@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeInLeft {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes fadeInRight {
  from {
    opacity: 0;
    transform: translateX(20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* Responsive Design */
@media (max-width: 1024px) {
  .contact-grid {
    gap: 40px;
  }

  .contact-title {
    font-size: 40px;
  }

  .form-wrapper {
    padding: 32px;
  }
}

@media (max-width: 768px) {
  .contact-page {
    padding: 40px 0;
    min-height: auto;
  }

  .contact-header {
    margin-bottom: 40px;
  }

  .contact-title {
    font-size: 32px;
  }

  .contact-subtitle {
    font-size: 14px;
  }

  .contact-grid {
    grid-template-columns: 1fr;
    gap: 30px;
  }

  .form-wrapper {
    padding: 24px;
  }

  .contact-form {
    gap: 18px;
  }

  .info-column {
    order: -1;
    gap: 16px;
  }

  .info-card {
    padding: 20px;
  }

  .info-title {
    font-size: 15px;
  }

  .info-text {
    font-size: 13px;
  }
}

@media (max-width: 480px) {
  .contact-page {
    padding: 24px 0;
  }

  .contact-container {
    padding: 0 calc(1vw);
  }

  .contact-header {
    margin-bottom: 32px;
  }

  .contact-title {
    font-size: 28px;
  }

  .contact-subtitle {
    font-size: 13px;
  }

  .form-wrapper {
    padding: 20px;
    border-radius: 8px;
  }

  .contact-form {
    gap: 16px;
  }

  .form-input,
  .form-textarea {
    font-size: 13px;
    padding: 10px 12px;
  }

  .form-label {
    font-size: 12px;
  }

  .submit-btn {
    padding: 12px 20px;
    font-size: 13px;
  }

  .info-card {
    padding: 16px;
    border-radius: 8px;
  }

  .info-title {
    font-size: 14px;
    margin-bottom: 6px;
  }

  .info-text {
    font-size: 12px;
  }
}
</style>