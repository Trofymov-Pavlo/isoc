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
            <v-btn variant="tonal" prepend-icon="mdi-arrow-left" to="/technologies-militaires">
              Article précédent
            </v-btn>
            <v-btn variant="tonal" prepend-icon="mdi-home" @click="$router.push('/')">
              Retour à l'accueil
            </v-btn>
            <v-btn variant="tonal" append-icon="mdi-arrow-right" to="/enjeux-ethiques">
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

const articleTitle = 'La vérité est une munition : Plongée dans la guerre de l\'information en Ukraine'
const articleAuthor = 'Antoine TENA'
const articleDate = '2025-12-12'

const articleContent = `Alors que l'hiver 2025 fige les lignes de front du Donbass dans la boue et la glace, une autre guerre bat son plein, insensible aux saisons. Elle ne se mesure pas en kilomètres carrés reconquis, mais en parts de cerveau disponible. De la doctrine russe du « chaos contrôlé » à la guérilla numérique ukrainienne, en passant par le rôle trouble des algorithmes et l'émergence de l'OSINT, plongée dans les entrailles d'un conflit où la vérité est la première victime — et la munition la plus convoitée.

Le 24 février 2022, à l'aube, deux offensives ont été lancées simultanément. La première, terrestre, faite de colonnes de chars fonçant vers Kiev. La seconde, invisible, faite de cyberattaques, de narratifs pré-écrits et de saturation médiatique. Si la première a échoué dans ses objectifs initiaux, la seconde continue de faire rage avec une intensité croissante.

Comme le souligne le Général (2S) Jérôme Pellistrandi, rédacteur en chef de la Revue Défense Nationale, nous assistons à une mutation anthropologique de la guerre : « Le champ de bataille n'est plus seulement physique, il est cognitif. L'objectif n'est plus seulement de détruire le potentiel militaire de l'adversaire, mais de briser sa volonté en manipulant sa perception du réel. »

I. MOSCOU ET LA STRATÉGIE DU « BROUILLARD PERMANENT »

Pour comprendre l'approche russe, il faut remonter aux racines soviétiques de la maskirovka (l'art de la tromperie militaire) et l'adapter à l'ère des réseaux sociaux. La Russie ne cherche pas toujours à convaincre le monde qu'elle a raison. Sa stratégie est plus cynique et, d'une certaine manière, plus redoutable.

La doctrine du « Firehose of Falsehood »

Les analystes de la RAND Corporation ont théorisé cette approche dès 2016 sous le nom de « Firehose of Falsehood » (la lance à incendie du mensonge). Le principe est simple : inonder l'espace informationnel d'un flux continu, rapide et répétitif de versions contradictoires.

Prenons l'exemple du massacre de Boutcha en 2022 ou des frappes sur des infrastructures énergétiques en 2024. En l'espace de quelques heures, l'écosystème médiatique russe (médias d'État, fermes à trolls, diplomates) va propager simultanément : que l'événement n'a pas eu lieu ; qu'il a eu lieu mais a été commis par les Ukrainiens ; que ce sont des acteurs payés (crisis actors) ; que c'est une provocation britannique.

« Le but n'est pas que vous croyiez à l'une de ces versions », explique David Colon, professeur à Sciences Po et auteur de La Guerre de l'information : Les États à la conquête de nos esprits. « Le but est de créer une lassitude cognitive. Face à trop de versions contradictoires, le citoyen occidental finit par hausser les épaules en se disant que "la vérité est impossible à connaître". À ce moment-là, le Kremlin a gagné. »

La fracture du Sud Global

Si cette propagande peine à convaincre en Europe, elle triomphe ailleurs. En Afrique, en Amérique Latine et en Inde, le narratif russe d'une "lutte contre l'impérialisme occidental" trouve un écho puissant. Via des plateformes comme RT (Russia Today) ou Sputnik, qui continuent d'émettre massivement en espagnol, arabe et français (à destination de l'Afrique), Moscou parvient à isoler diplomatiquement l'Ukraine d'une grande partie du monde non-occidental.

II. KIEV OU LA « START-UP NATION » EN TREILLIS

Face au rouleau compresseur russe, l'Ukraine a opposé une agilité stupéfiante. Dès les premiers jours, le président Volodymyr Zelensky a compris que sa survie dépendait de l'internationalisation du conflit.

L'arme de l'émotion et de l'incarnation

Là où Vladimir Poutine apparaît souvent seul, au bout d'une table immense, dans un cadre aseptisé, la communication ukrainienne joue la proximité. Les vidéos sont tournées au smartphone, dans la rue, souvent de nuit.

Cette stratégie vise à créer une connexion empathique immédiate. Mais elle est aussi savamment orchestrée. Le ministère de la Transformation numérique ukrainien, dirigé par Mykhailo Fedorov, a transformé le pays en plateforme de résistance numérique. L'application Diia, initialement prévue pour les démarches administratives, a été mise à jour pour permettre aux citoyens de signaler les mouvements de troupes russes. Chaque smartphone est devenu un capteur de renseignement.

Le phénomène NAFO : L'humour comme bouclier

L'un des chapitres les plus inattendus de cette guerre restera l'émergence de la NAFO (North Atlantic Fella Organization). Ce collectif décentralisé d'internautes, identifiables à leurs avatars de chiens Shiba Inu, s'est lancé dans une guerre de harcèlement contre la propagande russe sur X (ex-Twitter).

En répondant aux discours menaçants des diplomates russes par des mèmes absurdes et de l'argot internet, la NAFO a désamorcé la peur. « On ne peut pas terroriser quelqu'un qui se moque de vous », analyse Phillips O'Brien, professeur d'études stratégiques. Ils ont rendu la propagande russe inopérante en la rendant ridicule.

III. LE CHAMP DE BATAILLE TECHNIQUE : ALGORITHMES ET TELEGRAM

En tant qu'étudiant en informatique et données (IDU), il est fascinant d'observer comment l'architecture même des plateformes façonne le conflit. Le code n'est pas neutre ; il est le terrain.

Telegram : Le "Dark Web" grand public

C'est l'application reine du conflit. Sa politique de modération quasi inexistante en a fait le refuge des deux camps.

Côté Russe : C'est le royaume des "Milbloggers" (blogueurs militaires) comme Rybar ou WarGonzo. Suivis par des millions de personnes, ils sont parfois plus réactifs (et plus critiques) que le Ministère de la Défense russe. Ils fournissent une vision quasi temps réel du front.

Le danger de l'opacité : Contrairement à X ou Facebook, Telegram ne possède pas d'algorithme de recommandation public fort, mais fonctionne par boucles de partage virales. C'est un environnement cloisonné, idéal pour les opérations psychologiques (PSYOPS) où de fausses chaînes se font passer pour des unités militaires pour démoraliser les familles de soldats.

TikTok et la décontextualisation

TikTok a changé la visualité de la guerre. Les vidéos y sont courtes, sans date, sans lieu, souvent accompagnées de musiques tendances qui dramatisent ou banalisent la violence. L'algorithme de TikTok, extrêmement agressif, peut propulser une vidéo de 2014 en la faisant passer pour un événement de 2025, créant des flambées de colère basées sur du vide. C'est le triomphe de l'émotion pure sur l'analyse contextuelle.

IV. L'ÈRE DE L'OSINT : LA CONTRE-ATTAQUE PAR LA PREUVE

Si le mensonge est industriel, la vérité est devenue artisanale. C'est l'avènement de l'OSINT (Open Source Intelligence).

Jamais un conflit n'a été aussi documenté. Des organisations comme Bellingcat (fondé par Eliot Higgins) ou l'Institute for the Study of War (ISW) ne se contentent pas de lire les dépêches : ils scrutent les données satellites, les images radar (SAR), et les métadonnées des photos publiées par les soldats eux-mêmes.

Cas d'école : Le naufrage du Moskva

Lorsque le croiseur amiral russe Moskva a coulé en avril 2022, la Russie a évoqué un "incendie accidentel". La communauté OSINT a prouvé le contraire en quelques heures : analyse de la météo maritime pour contredire la thèse de la tempête, géolocalisation d'une photo volée montrant l'impact de missiles, analyse des ombres pour déterminer l'heure du naufrage.

Cette "bataille de la preuve" force les belligérants à une certaine prudence. Aujourd'hui, un char détruit est géolocalisé en quelques minutes par des bénévoles à 3000 km du front. Comme le dit l'historien militaire Michel Goya, « La transparence du champ de bataille est devenue quasi totale. La surprise stratégique devient extrêmement difficile. »

V. 2025-2026 : LE DÉFI DE L'INTELLIGENCE ARTIFICIELLE

Nous entrons désormais dans une phase encore plus critique. L'IA générative (GenAI) a atteint un niveau de maturité inquiétant.

Le spectre du Deepfake parfait

En 2022, le deepfake de Zelensky se rendant était grossier. En 2025, les outils permettent de cloner une voix avec trois secondes d'audio et de générer des vidéos photoréalistes. Le risque n'est pas seulement de créer de faux événements, mais de saturer les capacités de vérification des journalistes et analystes.

Le "Dividende du Menteur"

Le danger le plus pernicieux de l'IA est le concept du "Liar's Dividend" (le dividende du menteur). Puisque tout peut être faux, les acteurs malveillants peuvent désormais nier des preuves réelles (crimes de guerre, corruption) en affirmant simplement : "C'est une création de l'IA". La charge de la preuve s'inverse. La vérité ne suffit plus ; elle doit être prouvée cryptographiquement.

CONCLUSION : VERS UNE HYGIÈNE NUMÉRIQUE DE GUERRE

La guerre en Ukraine a définitivement aboli la frontière entre le civil et le militaire dans l'espace informationnel. Chaque "J'aime", chaque partage, chaque commentaire participe à la viralité d'un narratif ou d'un autre.

Dans ce contexte, la formation d'ingénieur (IDU) prend une dimension civique. Comprendre comment une donnée est structurée, comment un algorithme favorise la colère, ou comment vérifier les métadonnées d'une image n'est plus seulement une compétence technique. C'est un acte de défense nationale.

La leçon de ce conflit est claire : la liberté ne se défend pas uniquement avec des systèmes sol-air Patriot, mais aussi avec un esprit critique affûté, capable de dissiper le brouillard numérique que les autocraties tentent d'imposer au monde.`

const formattedContent = computed(() => {
  // Échapper seulement les & pour éviter les problèmes d'entités HTML
  let formatted = articleContent.replace(/&/g, '&amp;')
  
  // Appliquer les transformations de formatage
  formatted = formatted
    .replace(/^([IVX]+\.\s.+)$/gm, '<h2>$1</h2>')
    .replace(/^(CONCLUSION\s*:.+)$/gm, '<h2>$1</h2>')
    .replace(/^(La doctrine du.+)$/gm, '<h3>$1</h3>')
    .replace(/^(La fracture du.+)$/gm, '<h3>$1</h3>')
    .replace(/^(L'arme de l'.+)$/gm, '<h3>$1</h3>')
    .replace(/^(Le phénomène NAFO.+)$/gm, '<h3>$1</h3>')
    .replace(/^(Telegram\s*:.+)$/gm, '<h3>$1</h3>')

    .replace(/^(TikTok et la.+)$/gm, '<h3>$1</h3>')
    .replace(/^(Cas d'\u00e9cole.+)$/gm, '<h3>$1</h3>')
    .replace(/^(Le spectre du.+)$/gm, '<h3>$1</h3>')
    .replace(/^(Le "Dividende du.+)$/gm, '<h3>$1</h3>')
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
