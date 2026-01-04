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

const articleContent = `Dans les steppes ukrainiennes, l'intelligence artificielle a révolutionné la guerre moderne avec une efficacité qui glace le sang. Des drones autonomes patrouillent le ciel, capables de sélectionner et d'éliminer leurs cibles sans intervention humaine. Ce conflit force l'humanité à se poser une question aussi urgente que vertigineuse : jusqu'où sommes-nous prêts à aller dans l'automatisation de la mort ?

UNE RÉVOLUTION COMPARABLE AU NUCLÉAIRE

L'IA militaire redéfinit la guerre de manière aussi radicale que l'arme nucléaire au XXe siècle, selon le Secrétaire général de l'ONU. Aujourd'hui, des systèmes intègrent du machine learning pour analyser des images satellites, optimiser la logistique, et prendre des décisions létales en temps réel, parfois sans délai de validation humaine.

En Ukraine, ces technologies ont transformé le champ de bataille. Le système ukrainien Clearview AI et l'utilisation de drones autonomes FPV (First Person View) modifiés permettent d'identifier et de frapper des cibles en quelques secondes. Côté russe, les drones Lancet, équipés de reconnaissance automatique de cibles, ont détruit des centaines de véhicules blindés. Leur précision est stupéfiante, leur froideur absolue.

LE SPECTRE DU "TERMINATOR"

La menace n'est plus de la science-fiction. L'armée turque a déjà utilisé en Libye le drone kamikaze Kargu-2, capable de traquer et détruire ses cibles sans ordre humain. En Ukraine, des vidéos troublantes montrent des essaims de drones coopérant entre eux pour saturer les défenses anti-aériennes, une stratégie autrefois réservée aux joueurs d'échecs.

L'ABSENCE DE COMPASSION

Le risque moral est immense. Comme l'explique le philosophe Paul Scharre, ancien ranger américain, dans son ouvrage Army of None : "Un soldat humain peut hésiter devant un enfant tenant un objet suspect. Un algorithme ne connaît pas l'hésitation. Il optimise une probabilité de menace."

Cette absence d'empathie peut conduire à des "erreurs" aux conséquences dramatiques. En 2020, un algorithme israélien de ciblage a identifié à tort des civils comme combattants en raison d'un biais de données d'entraînement. L'IA ne comprend pas la complexité humaine du contexte de guerre : un adolescent portant un sac peut être un écolier ou un combattant. L'algorithme choisit la probabilité, pas la nuance.

LE "CONTRÔLE HUMAIN SIGNIFICATIF"

Face à ces enjeux, les Nations Unies et des ONG comme Human Rights Watch plaident pour l'interdiction des "systèmes d'armes létaux autonomes" (LAWS). Le concept central est le "meaningful human control" (contrôle humain significatif) : toute décision de tuer doit rester l'apanage d'un être humain capable de jugement éthique.

Mais la définition reste floue. Où placer le curseur ? Un drone qui identifie automatiquement une cible mais nécessite une validation humaine pour tirer respecte-t-il ce principe ? Que se passe-t-il si cette validation se fait en 0,2 seconde par un opérateur déjà saturé d'informations ?

UN RISQUE D'ESCALADE AUTOMATISÉE

Pire encore : l'IA pourrait créer des conflits non intentionnels. Imaginez deux systèmes de défense autonomes détectant mutuellement des comportements "suspects". Chacun interprète l'activation de l'autre comme une menace. En millisecondes, sans que personne n'ait appuyé sur un bouton, une bataille se déclenche. C'est le cauchemar du "flash war", l'équivalent militaire du krach boursier algorithmique de 2010.

Stuart Russell, pionnier de l'IA et professeur à Berkeley, avertit : "Le danger n'est pas une Skynet consciente qui décide d'exterminer l'humanité. Le danger, c'est une IA parfaitement obéissante mais mal programmée, ou mise en service trop rapidement dans un contexte qu'elle ne comprend pas."

LA COURSE RÉGLEMENTAIRE EST PERDUE

Technologiquement, nous sommes déjà trop loin. La Russie, la Chine, les États-Unis, Israël, et la Turquie investissent massivement dans les systèmes autonomes. En 2024, le Pentagone a annoncé sa stratégie "Replicator", visant à déployer des milliers de drones autonomes pour contrer la Chine. Pékin de son côté développe des essaims de drones marins et aériens capables de coordonner des attaques sans intervention extérieure.

Le problème est double. D'une part, aucun État ne veut renoncer unilatéralement à une technologie aussi stratégique (dilemme du prisonnier classique). D'autre part, les entreprises privées (startups de la Silicon Valley, sociétés israéliennes comme Elbit Systems) ont déjà commercialisé ces outils. L'interdiction devrait concerner aussi le secteur privé, ce qui est quasi impossible.

UNE RESPONSABILITÉ ÉTHIQUE COLLECTIVE

En tant qu'étudiants ingénieurs, nous sommes en première ligne de ce débat. Contrairement à nos prédécesseurs du nucléaire qui ont compris les implications éthiques après Hiroshima, nous avons la chance (et le devoir) de réfléchir avant la catastrophe.

Certains de nos camarades travailleront demain pour des entreprises comme Palantir, Anduril, ou Thales. Ils devront se poser la question : est-ce que je veux contribuer à créer une arme qui tue sans jugement humain ? La réponse n'est pas binaire. Développer un système de défense anti-missile autonome (protéger) est-il moralement équivalent à créer un drone tueur autonome (attaquer) ?

LES PISTES DE RÉGULATION

Tout n'est pas perdu. Plusieurs propositions émergent :

Transparence algorithmique obligatoire : Toute IA militaire devrait être auditée par un tiers indépendant.

"Kill switch" universel : Un mécanisme de désactivation d'urgence accessible aux commandants sur le terrain.

Interdiction des essaims totalement autonomes : Limiter le nombre d'IA pouvant coopérer sans supervision.

Responsabilité pénale : En cas de crime de guerre commis par une IA, qui est responsable ? Le programmeur ? Le commandant ? Le fabricant ? Le droit international doit évoluer.

CONCLUSION : LA GUERRE, C'EST LA PAIX ?

Le titre de cette section fait écho à 1984 d'Orwell, mais il résume l'absurdité où nous mène l'automatisation totale : des machines qui tuent pour, soi-disant, protéger des vies humaines. L'argument classique est que l'IA réduit les pertes civiles par sa précision. Mais cette logique est trompeuse. Si la guerre devient "propre" et sans risque pour l'agresseur (plus de pilotes en danger), le seuil d'entrée en guerre s'abaisse. On bombarde plus facilement quand nos soldats ne meurent plus.

La vraie question n'est pas technique, elle est anthropologique : voulons-nous vivre dans un monde où la décision de tuer est déléguée à des lignes de code ? Comme le résume Toby Walsh, chercheur en IA : "Certaines choses doivent rester humaines. La mort en fait partie."

Le conflit ukrainien n'est qu'un aperçu. Dans les 10 prochaines années, chaque guerre mobilisera des IA de plus en plus autonomes. Si nous n'établissons pas maintenant des lignes rouges éthiques et juridiques, nous risquons de créer un futur où l'humanité aura perdu le contrôle de ses propres moyens de destruction. Et à ce moment-là, il sera trop tard pour regretter.`

const formattedContent = computed(() => {
  // Échapper seulement les & pour éviter les problèmes d'entités HTML
  let formatted = articleContent.replace(/&/g, '&amp;')
  
  // Appliquer les transformations de formatage
  formatted = formatted
    .replace(/^(UNE RÉVOLUTION COMPARABLE AU NUCLÉAIRE)$/gm, '<h2>$1</h2>')
    .replace(/^(LE SPECTRE DU “TERMINATOR”)$/gm, '<h3>$1</h3>')
    .replace(/^(L’ABSENCE DE COMPASSION)$/gm, '<h3>$1</h3>')
    .replace(/^(LE “CONTRÔLE HUMAIN SIGNIFICATIF”)$/gm, '<h3>$1</h3>')
    .replace(/^(UN RISQUE D’ESCALADE AUTOMATISÉE)$/gm, '<h3>$1</h3>')
    .replace(/^(LA COURSE RÉGLEMENTAIRE EST PERDUE)$/gm, '<h2>$1</h2>')
    .replace(/^(UNE RESPONSABILITÉ ÉTHIQUE COLLECTIVE)$/gm, '<h2>$1</h2>')
    .replace(/^(LES PISTES DE RÉGULATION)$/gm, '<h2>$1</h2>')
    .replace(/^(CONCLUSION\s*:.+)$/gm, '<h2>$1</h2>')
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
