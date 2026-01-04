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
            <v-btn variant="tonal" prepend-icon="mdi-home" @click="$router.push('/')">
              Retour à l'accueil
            </v-btn>
            <v-btn variant="tonal" append-icon="mdi-arrow-right" to="/guerre-information">
              Article suivant
            </v-btn>
          </div>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const articleTitle = 'Les technologies militaires utilisées dans le conflit'
const articleAuthor = 'Hiba ABDESSADAK'
const articleDate = '2025-12-05'

const articleContent = `Le conflit ukrainien marque un tournant dans l'histoire militaire moderne, où les nouvelles technologies jouent un rôle déterminant sur le terrain. Les drones, l'intelligence artificielle et les cyberattaques transforment profondément les stratégies de combat et redéfinissent les notions de supériorité militaire. Cette guerre démontre comment l'innovation technologique peut compenser des désavantages en termes de ressources ou de personnel.

1. DRONES RUSSES ET UKRAINIENS : UNE GUERRE MENÉE À DISTANCE

Depuis quelques années, les drones ont profondément transformé la manière de faire la guerre. Longtemps réservés à des missions de reconnaissance, ils sont aujourd'hui utilisés comme outils offensifs à part entière, capables de frapper des cibles avec précision tout en limitant les pertes humaines du côté de l'attaquant.

En effet depuis le début de l'invasion russe de l'Ukraine en 2022, les drones se sont imposés comme l'un des symboles les plus visibles de ce conflit. Utilisés par les deux camps, ils ont profondément modifié la manière de surveiller, d'attaquer et de se défendre sur le champ de bataille.

L'Ukraine s'est rapidement appuyée sur des drones aériens, souvent peu coûteux, pour compenser son infériorité matérielle face à l'armée russe. Des drones commerciaux modifiés sont employés pour la reconnaissance, l'ajustement de tirs d'artillerie ou encore des frappes ciblées. Cette approche flexible et innovante permet à Kiev de frapper rapidement, parfois loin derrière les lignes ennemies.

De son côté, la Russie utilise des drones plus lourds, notamment des drones d'attaque capables de parcourir de longues distances. Certains sont employés pour saturer les défenses ukrainiennes, d'autres pour collecter du renseignement stratégique. La multiplication de ces appareils a rendu le ciel ukrainien extrêmement dangereux, aussi bien pour les soldats que pour les infrastructures civiles.

Le conflit a également vu l'apparition de drones navals ukrainiens, utilisés pour attaquer des navires russes en mer Noire. Ces opérations, spectaculaires, ont démontré qu'un pays disposant de moyens limités pouvait menacer une flotte militaire grâce à des technologies relativement simples. La guerre en Ukraine montre ainsi que les drones ne sont plus un outil secondaire, mais bien un élément central des stratégies militaires modernes.

2. L'INTELLIGENCE ARTIFICIELLE AU CŒUR DU CONFLIT RUSSO-UKRAINIEN

L'intelligence artificielle s'est imposée comme un pilier essentiel des guerres contemporaines. Sa capacité à analyser rapidement d'immenses volumes de données en fait un atout majeur pour guider les choix militaires, notamment dans la sélection de cibles et l'interprétation d'images satellites ou de vidéos de drones.

Dans le conflit russo-ukrainien, l'IA joue un rôle discret mais déterminant, loin de l'éclat des chars ou de l'artillerie lourde. Elle excelle principalement dans le traitement des données de renseignement, le renforcement de la surveillance et l'accélération des décisions sur le terrain.

L'Ukraine exploite intensivement l'IA pour traiter les flux d'images issus de ses drones et de satellites alliés. Ces outils permettent une détection plus rapide des positions ennemies, des convois ou des sites stratégiques russes. En automatisant l'analyse visuelle – souvent via des systèmes de reconnaissance automatique de cibles –, les forces ukrainiennes gagnent un temps précieux, crucial dans une guerre où la vitesse de réaction peut inverser l'issue d'un affrontement. Des drones équipés d'IA pour la navigation autonome ou le verrouillage final sur cible ont même porté le taux de succès des frappes à environ 80 %, contre 30-50 % auparavant.

Du côté russe, l'IA est également déployée pour le renseignement, la priorisation d'objectifs et la prévision de mouvements adverses. Des systèmes testés sur des drones ou des munitions vagabondes intègrent des éléments d'autonomie, bien que leur efficacité reste moins documentée en raison du secret militaire. La Russie investit par ailleurs dans l'IA pour ses opérations cyber et de désinformation.

Cette intégration croissante de l'IA soulève des interrogations éthiques profondes. Même si la décision finale demeure humaine dans la plupart des cas, la délégation progressive à des algorithmes pose la question de la responsabilité en cas d'erreur, de biais ou de frappes indiscriminées. Le conflit en Ukraine agit comme un laboratoire grandeur nature, préfigurant des guerres futures où l'IA pourrait redéfinir fondamentalement les règles de l'engagement.

3. CYBERATTAQUES ET GUERRE ÉLECTRONIQUE : LE FRONT INVISIBLE ENTRE MOSCOU ET KIEV

Au-delà des combats terrestres, aériens et navals, la guerre entre la Russie et l'Ukraine se joue également dans un espace invisible : le cyberespace. Dès les premiers jours du conflit, des cyberattaques ont ciblé des institutions ukrainiennes, des réseaux de communication et des infrastructures critiques.

La Russie est souvent accusée d'utiliser des attaques informatiques pour désorganiser les systèmes ukrainiens, perturber les communications militaires et diffuser de la désinformation. Ces actions visent à affaiblir l'adversaire sans confrontation directe, en créant de la confusion et de l'instabilité.

L'Ukraine, de son côté, a renforcé sa cyberdéfense avec l'aide de partenaires occidentaux. Elle mène également des opérations de contre-influence, notamment sur les réseaux sociaux, afin de maintenir le soutien international et contrer la propagande russe.

La guerre électronique, notamment le brouillage des signaux GPS et des communications radio, joue aussi un rôle crucial. Elle limite l'efficacité des drones et complique la coordination des troupes sur le terrain. Dans ce conflit, maîtriser l'information est devenu presque aussi important que contrôler un territoire. La guerre en Ukraine montre ainsi que le cyberespace est désormais un champ de bataille à part entière.

CONCLUSION

L'innovation technologique est devenue le facteur décisif de ce conflit. Les trois piliers – drones, intelligence artificielle et cyberguerre – fonctionnent de manière interdépendante pour créer un nouveau paradigme militaire où la vitesse, la précision et le contrôle de l'information déterminent l'issue des batailles. Cette guerre préfigure les conflits de demain, où la supériorité technologique pourrait primer sur les effectifs militaires traditionnels.`

const formattedContent = computed(() => {
  // Échapper seulement les & pour éviter les problèmes d'entités HTML
  let formatted = articleContent.replace(/&/g, '&amp;')
  
  // Appliquer les transformations de formatage
  formatted = formatted
    .replace(/^(\d+\.\s.+)$/gm, '<h2>$1</h2>')
    .replace(/^(CONCLUSION)$/gm, '<h2>$1</h2>')
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
