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
            <template>
              <main>
                <MainContact />
              </main>
            </template>

            <script setup lang="ts">
            import MainContact from '~/components/Contact/mainContact.vue';
            </script>
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