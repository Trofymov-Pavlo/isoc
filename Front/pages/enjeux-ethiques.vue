<template>
  <v-container class="article-page">
    <v-row>
      <v-col cols="12" lg="8" offset-lg="2">
        <div class="article-header mb-4">
          <v-btn variant="text" prepend-icon="mdi-arrow-left" @click="$router.push('/')" class="mb-4">
            Retour
          </v-btn>
          <h1 class="article-title mb-4">{{ articleTitle }}</h1>
          <div class="article-meta">
            <div class="meta-item">
              <v-icon small class="me-2">mdi-account</v-icon>
              <strong>{{ articleAuthor }}</strong>
            </div>
            <div class="meta-item">
              <v-icon small class="me-2">mdi-calendar</v-icon>
              {{ formatDate(articleDate) }}
            </div>
          </div>
          <v-divider class="my-4"></v-divider>
        </div>

        <div class="article-content">
          <div v-html="formattedContent"></div>
        </div>

        <div class="article-navigation mt-8">
          <v-divider class="mb-4"></v-divider>
          <div class="d-flex justify-space-between gap-4">
            <v-btn variant="tonal" prepend-icon="mdi-arrow-left" to="/guerre-information">
              Article précédent
            </v-btn>
            <v-btn variant="tonal" prepend-icon="mdi-home" @click="$router.push('/')">
              Retour à l'accueil
            </v-btn>
          </div>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const articleTitle = 'Guerre en Ukraine : quand l\'algorithme décide de donner la mort'
const articleAuthor = 'Nathan BARRACHIN'
const articleDate = '2025-12-18'

const articleContent = `Le conflit en Ukraine agit comme un accélérateur brutal pour l'intégration de l'intelligence artificielle (IA) sur le champ de bataille. Entre nécessité tactique et "ligne rouge" éthique, le déploiement de systèmes de plus en plus indépendants force les puissances mondiales et les experts à redéfinir la place de l'homme dans la guerre.

Une révolution comparable au nucléaire

L'avènement des armes autonomes est désormais perçu par les experts, comme le professeur Noel Sharkey, comme un changement radical de la nature même des conflits, au même titre que l'invention de l'arme nucléaire. Cette "course aux armements" algorithmique voit s'affronter des technologies de pointe : le char russe T-14 Armata, les drones chinois Dark Sword ou les systèmes américains X-47B. Tous recherchent la même chose : une vitesse d'exécution et une puissance de feu dépassant les capacités humaines.

Sur le terrain ukrainien, cette évolution est devenue une nécessité technique pour contrer la guerre électronique intense. Face au brouillage des signaux GPS et radio, les drones perdent le contact avec leurs pilotes. Pour pallier ce "silence numérique", des logiciels de reconnaissance de formes permettent aux machines de finaliser leurs missions de manière autonome en identifiant des cibles (chars, artillerie) sans intervention humaine directe.

Le spectre du "Terminator" face à la réalité technique

Si le grand public craint l'avènement d'un "Terminator", les rapports parlementaires français, notamment celui de Claude de Ganay et Fabien Gouttefarde (2020), nuancent cette vision. Les Systèmes d'Armes Létaux Autonomes (SALA) à proprement parler, capables de choisir et d'engager seuls une cible dans un environnement changeant sans aucune tutelle humaine, n'existent pas encore totalement à l'état opérationnel.

L'autonomie est en réalité un continuum (Une progression ininterrompue) :

• Niveaux 1 à 4 : Systèmes semi-autonomes ou supervisés, déjà maîtrisés par les grandes puissances.
• Niveau 5 : Autonomie totale (SALA), où la machine agit sans aucune tutelle humaine. C'est ce niveau qui cristallise les inquiétudes juridiques et morales.

Le "Contrôle Humain Significatif" : Un impératif moral

Le débat central ne porte pas sur la technologie elle-même, mais sur la qualité du contrôle humain. L'expression "contrôle humain significatif" est devenue le cri de ralliement des ONG et de nombreux pays à l'ONU pour empêcher la déshumanisation des combats.

Sur le plan éthique, déléguer la mort à un algorithme pose des problèmes insolubles :

L'absence de compassion : Contrairement à un soldat, une IA est incapable de discernement moral ou de compassion. Elle ne peut pas interpréter si un véhicule militaire transporte des blessés ou si un ennemi tente de se rendre.

La "boîte noire" algorithmique : Les décisions prises par une IA sont souvent opaques. Ce manque de transparence empêche de comprendre pourquoi une machine a choisi de frapper, ce qui est inacceptable pour la dignité humaine.

La facilité de la violence : Puisque la machine agit seule et que l'humain est loin du combat, on risque de tuer plus facilement. Sans le choc émotionnel de voir sa cible, la guerre pourrait devenir un réflexe plus fréquent et moins grave aux yeux des décideurs.

L'impasse juridique : Le fossé de la responsabilité

Le Droit International Humanitaire (DIH) repose sur des piliers que l'IA ne peut garantir seule : la distinction (civil/combattant), la proportionnalité (évaluer si les dégâts civils sont excessifs par rapport au bénéfice militaire) et la nécessité militaire.

En cas de crime de guerre commis par une machine, un "vide juridique" apparaît. Qui punir ? Le commandant, le programmeur ou l'État ? Pour la France, la létalité est le critère déterminant : un humain doit impérativement rester responsable de l'ouverture du feu pour garantir l'imputabilité des actes.

Une diplomatie mondiale sous tension

À Genève, les discussions au sein de l'ONU stagnent. Si de nombreux pays demandent une interdiction préventive des robots tueurs, ils se heurtent à l'opposition de puissances comme la Russie, Israël et les États-Unis. Ces derniers préfèrent utiliser l'expression plus floue de "niveaux appropriés de jugement humain" plutôt que "contrôle humain significatif".

L'idée clé à retenir : L'enjeu n'est pas d'interdire l'intelligence artificielle militaire, qui reste utile pour la détection ou le déminage, mais d'empêcher que la machine ne sorte de la "boucle de décision". Maintenir l'homme comme seul arbitre de la force létale est l'unique moyen de préserver la morale et le droit, même dans l'hyper-guerre de demain.`

const formattedContent = computed(() => {
  // Échapper seulement les & pour éviter les problèmes d'entités HTML
  let formatted = articleContent.replace(/&/g, '&amp;')
  
  // Appliquer les transformations de formatage
  formatted = formatted
    .replace(/^(Une révolution comparable au nucléaire)$/gm, '<h2>$1</h2>')
    .replace(/^(Le spectre du "Terminator" face à la réalité technique)$/gm, '<h2>$1</h2>')
    .replace(/^(Le "Contrôle Humain Significatif" : Un impératif moral)$/gm, '<h2>$1</h2>')
    .replace(/^(L'absence de compassion.+)$/gm, '<h3>$1</h3>')
    .replace(/^(La "boîte noire" algorithmique.+)$/gm, '<h3>$1</h3>')
    .replace(/^(La facilité de la violence.+)$/gm, '<h3>$1</h3>')
    .replace(/^(L'impasse juridique : Le fossé de la responsabilité)$/gm, '<h2>$1</h2>')
    .replace(/^(Une diplomatie mondiale sous tension)$/gm, '<h2>$1</h2>')
    .replace(/^• (.+)$/gm, '<li>$1</li>')
    .replace(/(<li>.*<\/li>\n)+/g, '<ul style="list-style: disc; margin-left: 20px; margin-bottom: 16px;">$&</ul>')
    .replace(/\n\n+/g, '</p><p style="margin: 16px 0; line-height: 1.8;">')
    .replace(/^(?!<)/gm, '<p style="margin: 16px 0; line-height: 1.8;">')
  
  return formatted + '</p>'
})

const formatDate = (date: string) => {
  if (!date) return ''
  return new Intl.DateTimeFormat('fr-FR', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  }).format(new Date(date))
}
</script>

<style scoped>
.article-page {
  padding: 20px 16px;
}

.article-header {
  text-align: left;
}

.article-title {
  font-size: 2.25rem;
  font-weight: 700;
  line-height: 1.2;
  color: #2f0538;
  margin-bottom: 16px;
}

.article-meta {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  font-size: 0.95rem;
  color: rgba(0, 0, 0, 0.6);
}

.meta-item {
  display: flex;
  align-items: center;
}

.article-content {
  font-size: 1.05rem;
  line-height: 1.7;
  color: rgba(0, 0, 0, 0.8);
}

.article-content :deep(h2) {
  font-size: 1.5rem;
  font-weight: 700;
  margin: 24px 0 12px 0;
  color: #2f0538;
  padding-left: 12px;
  border-left: 4px solid #2f0538;
}

.article-content :deep(h3) {
  font-size: 1.25rem;
  font-weight: 600;
  margin: 16px 0 8px 0;
  color: #2f0538;
}

.article-content :deep(p) {
  margin-bottom: 12px;
}

.article-navigation {
  min-height: 50px;
  margin-top: 32px;
}

@media (max-width: 600px) {
  .article-page {
    padding: 16px 12px;
  }

  .article-title {
    font-size: 1.75rem;
  }

  .article-meta {
    flex-direction: column;
    gap: 8px;
  }

  .article-navigation .d-flex {
    flex-direction: column;
    gap: 8px;
  }

  .article-navigation :deep(.v-btn) {
    width: 100%;
  }
}
</style>
