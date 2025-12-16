<template>
  <main class="legal-page">
    <PageHero
      title="Gestion des Données Personnelles"
      subtitle="Vos droits concernant vos données personnelles"
      badge="Données"
      badge-icon="🔒"
    />

    <section class="legal-content">
      <div class="legal-wrapper">
        <h2>Gestion des Données Personnelles</h2>

        <h3>Collecte de Données</h3>
        <p>Nous collectons et traitons vos données personnelles dans les cas suivants :</p>
        <ul>
          <li>Lors de votre inscription et création de compte</li>
          <li>Lors de l'utilisation de nos formulaires (contact, feedback)</li>
          <li>Lors de votre interaction avec nos services</li>
          <li>Via les cookies et technologies de suivi (avec votre consentement)</li>
        </ul>

        <h3>Types de Données Collectées</h3>
        <p>Les types de données personnelles que nous collectons incluent :</p>
        <ul>
          <li>Données d'identification (nom, email, téléphone)</li>
          <li>Données de localisation (ville, pays)</li>
          <li>Données d'utilisation (pages visitées, temps de visite)</li>
          <li>Données de communication (messages, préférences)</li>
        </ul>

        <h3>Utilisation de Vos Données</h3>
        <p>Vos données personnelles sont utilisées pour :</p>
        <ul>
          <li>Fournir et améliorer nos services</li>
          <li>Personnaliser votre expérience</li>
          <li>Vous contacter et vous envoyer des mises à jour</li>
          <li>Analyser l'utilisation du site</li>
          <li>Respecter nos obligations légales</li>
        </ul>

        <h3>Partage de Données</h3>
        <p>
          Nous ne partageons vos données personnelles avec aucun tiers sans votre consentement explicite, 
          sauf si la loi nous y oblige. Nos partenaires de service (hébergement, analyse) sont soumis à 
          des obligations strictes de confidentialité.
        </p>

        <h3>Sécurité des Données</h3>
        <p>
          Vos données sont protégées par des mesures de sécurité appropriées incluant le chiffrement, 
          les pare-feu et les systèmes de contrôle d'accès. Cependant, aucune transmission internet 
          n'est totalement sécurisée.
        </p>

        <h3>Vos Droits</h3>
        <p>Conformément au RGPD et aux lois applicables, vous avez le droit de :</p>
        <ul>
          <li>Accéder à vos données personnelles</li>
          <li>Corriger vos données inexactes</li>
          <li>Demander la suppression de vos données</li>
          <li>Vous opposer au traitement de vos données</li>
          <li>Demander la portabilité de vos données</li>
        </ul>

        <h3>Durée de Conservation</h3>
        <p>
          Vos données personnelles sont conservées aussi longtemps que nécessaire pour atteindre 
          les objectifs définis, sauf si une période de rétention plus longue est requise par la loi. 
          Vous pouvez demander la suppression de vos données à tout moment.
        </p>

        <h3>Contact</h3>
        <p>
          Pour toute question concernant vos données personnelles ou pour exercer vos droits, 
          veuillez nous contacter à travers notre formulaire de contact.
        </p>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
import PageHero from '~/components/shared/PageHero.vue';
</script>

<style scoped>
.legal-page {
  min-height: 100vh;
  background: #fff;
}

.legal-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 48px calc(2vw) 60px;
}

.legal-wrapper {
  max-width: 800px;
  margin: 0 auto;
}

.legal-wrapper h2 {
  font-size: 28px;
  font-weight: 700;
  color: #2f0538;
  margin: 0 0 24px;
  padding-bottom: 16px;
  border-bottom: 2px solid #f0f0f0;
}

.legal-wrapper h3 {
  font-size: 20px;
  font-weight: 700;
  color: #2f0538;
  margin: 32px 0 16px;
}

.legal-wrapper p {
  font-size: 16px;
  line-height: 1.75;
  color: #4a4a55;
  margin: 0 0 16px;
}

.legal-wrapper ul {
  margin: 16px 0 16px 24px;
  padding: 0;
  color: #4a4a55;
}

.legal-wrapper li {
  margin: 8px 0;
  line-height: 1.6;
}
</style>
