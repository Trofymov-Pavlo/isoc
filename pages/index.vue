<template>
  <MainHeader />

  <div class="page-layout">
    <div class="article-main">
      <MainArticle1
        category="Financement du terrorisme"
        title="Au procès Lafarge, la thèse de la complicité tacite de l’État français prend du plomb dans l’aile"
        chapo="L’ancien numéro deux du cimentier a avoué jeudi avoir caché la vérité à un diplomate concernant les versements à des organisations terroristes..."
        author="Matthieu Suc"
        image="/images/lafarge-proces.png"
        imageCredit="Dessin d’audience Matthieu Fayette"
      />
    </div>

    <MainInfo :articles="sideArticles" />
  </div>
</template>

<script setup lang="ts">
import MainHeader from '@/components/header/mainHeader.vue'
import MainInfo from '@/components/main/mainInfo.vue'
import MainArticle1 from '@/components/main/mainArticle1.vue'

const sideArticles = [
  {
    id: 1,
    slug: 'sainte-soline-revelations',
    title: 'Sainte-Soline : nos révélations',
    category: 'Enquête',
    image: 'https://via.placeholder.com/140x90'
  },
  {
    id: 2,
    slug: 'saint-etienne-affaire',
    title: 'Affaire de Saint-Étienne : toutes nos enquêtes',
    category: 'Politique',
    image: 'https://via.placeholder.com/140x90'
  },
  {
    id: 3,
    slug: 'lettre-americaine',
    title: 'Recevez la lettre américaine',
    category: 'Newsletter',
    image: 'https://via.placeholder.com/140x90'
  }
]
</script>

<style scoped lang="scss">
.page-layout {
  display: grid;
  grid-template-columns: minmax(0, 2.2fr) 260px;
  gap: 32px;
  padding: 24px 60px 40px;
}

.article-main {
  max-width: 800px;
}

/* si tu veux que la sidebar colle en haut */
:deep(.mini-sidebar) {
  align-self: flex-start;
}

@media (max-width: 900px) {
  .page-layout {
    grid-template-columns: 1fr;
  }
}
</style>
