<template>
  <div class="contact-page">
    <div class="contact-container">
      <div class="contact-header">
        <h1 class="contact-title">Nous contacter</h1>
        <p class="contact-subtitle">Vos questions, vos suggestions, vos retours - tous les messages comptent</p>
      </div>

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
  </div>
</template>

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

.contact-header {
  text-align: center;
  margin-bottom: 40px;
  animation: fadeInDown 0.4s ease;
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

.form-wrapper {
  background: #ffffff;
  border-radius: 12px;
  padding: 40px;
  border: 1px solid rgba(123, 92, 224, 0.15);
  box-shadow: 0 4px 20px rgba(47, 5, 56, 0.08);
  animation: fadeInLeft 0.4s ease 0.05s both;
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

@media (max-width: 1024px) {
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

  .form-wrapper {
    padding: 24px;
  }

  .contact-form {
    gap: 18px;
  }
}
</style>
