import { ref, reactive } from 'vue'

export interface FeaturedArticle {
  id: number
  title: string
  author: string
  date: string
  excerpt: string
  content: string
  slug: string
}

const articles = reactive<FeaturedArticle[]>([
  {
    id: 1,
    title: 'Les technologies militaires utilisées dans le conflit',
    author: 'Hiba ABDESSADAK',
    date: '2025-12-05',
    excerpt: 'Le conflit ukrainien marque un tournant dans l\'histoire militaire moderne, où les nouvelles technologies jouent un rôle déterminant...',
    content: `Le conflit ukrainien marque un tournant dans l'histoire militaire moderne, où les nouvelles technologies jouent un rôle déterminant sur le terrain. Les drones, l'intelligence artificielle et les cyberattaques transforment profondément les stratégies de combat et redéfinissent les notions de supériorité militaire. Cette guerre démontre comment l'innovation technologique peut compenser des désavantages en termes de ressources ou de personnel.

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

L'innovation technologique est devenue le facteur décisif de ce conflit. Les trois piliers – drones, intelligence artificielle et cyberguerre – fonctionnent de manière interdépendante pour créer un nouveau paradigme militaire où la vitesse, la précision et le contrôle de l'information déterminent l'issue des batailles. Cette guerre préfigure les conflits de demain, où la supériorité technologique pourrait primer sur les effectifs militaires traditionnels.`,
    slug: 'technologies-militaires'
  },
  {
    id: 2,
    title: 'La vérité est une munition : Plongée dans la guerre de l\'information en Ukraine',
    author: 'Antoine TENA',
    date: '2025-12-12',
    excerpt: 'Alors que l\'hiver 2025 fige les lignes de front du Donbass dans la boue et la glace, une autre guerre bat son plein, insensible aux saisons. De la doctrine russe du « chaos contrôlé » à la guérilla numérique ukrainienne, plongée dans un conflit où la vérité est la première victime — et la munition la plus convoitée.',
    content: `Alors que l'hiver 2025 fige les lignes de front du Donbass dans la boue et la glace, une autre guerre bat son plein, insensible aux saisons. Elle ne se mesure pas en kilomètres carrés reconquis, mais en parts de cerveau disponible. De la doctrine russe du « chaos contrôlé » à la guérilla numérique ukrainienne, en passant par le rôle trouble des algorithmes et l'émergence de l'OSINT, plongée dans les entrailles d'un conflit où la vérité est la première victime — et la munition la plus convoitée.

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

La leçon de ce conflit est claire : la liberté ne se défend pas uniquement avec des systèmes sol-air Patriot, mais aussi avec un esprit critique affûté, capable de dissiper le brouillard numérique que les autocraties tentent d'imposer au monde.`,
    slug: 'guerre-information'
  },
  {
    id: 3,
    title: 'Guerre en Ukraine : quand l\'algorithme décide de donner la mort',
    author: 'Nathan BARRACHIN',
    date: '2025-12-18',
    excerpt: 'Le conflit en Ukraine agit comme un accélérateur brutal pour l\'intégration de l\'intelligence artificielle sur le champ de bataille...',
    content: `Le conflit en Ukraine agit comme un accélérateur brutal pour l'intégration de l'intelligence artificielle (IA) sur le champ de bataille. Entre nécessité tactique et "ligne rouge" éthique, le déploiement de systèmes de plus en plus indépendants force les puissances mondiales et les experts à redéfinir la place de l'homme dans la guerre.

UNE RÉVOLUTION COMPARABLE AU NUCLÉAIRE

L'avènement des armes autonomes est désormais perçu par les experts, comme le professeur Noel Sharkey, comme un changement radical de la nature même des conflits, au même titre que l'invention de l'arme nucléaire. Cette "course aux armements" algorithmique voit s'affronter des technologies de pointe : le char russe T-14 Armata, les drones chinois Dark Sword ou les systèmes américains X-47B. Tous recherchent la même chose : une vitesse d'exécution et une puissance de feu dépassant les capacités humaines.

Sur le terrain ukrainien, cette évolution est devenue une nécessité technique pour contrer la guerre électronique intense. Face au brouillage des signaux GPS et radio, les drones perdent le contact avec leurs pilotes. Pour pallier ce "silence numérique", des logiciels de reconnaissance de formes permettent aux machines de finaliser leurs missions de manière autonome en identifiant des cibles (chars, artillerie) sans intervention humaine directe.

LE SPECTRE DU "TERMINATOR" FACE À LA RÉALITÉ TECHNIQUE

Si le grand public craint l'avènement d'un "Terminator", les rapports parlementaires français, notamment celui de Claude de Ganay et Fabien Gouttefarde (2020), nuancent cette vision. Les Systèmes d'Armes Létaux Autonomes (SALA) à proprement parler, capables de choisir et d'engager seuls une cible dans un environnement changeant sans aucune tutelle humaine, n'existent pas encore totalement à l'état opérationnel.

L'autonomie est en réalité un continuum (une progression ininterrompue) :
• Niveaux 1 à 4 : Systèmes semi-autonomes ou supervisés, déjà maîtrisés par les grandes puissances.
• Niveau 5 : Autonomie totale (SALA), où la machine agit sans aucune tutelle humaine. C'est ce niveau qui cristallise les inquiétudes juridiques et morales.

LE "CONTRÔLE HUMAIN SIGNIFICATIF" : UN IMPÉRATIF MORAL

Le débat central ne porte pas sur la technologie elle-même, mais sur la qualité du contrôle humain. L'expression "contrôle humain significatif" est devenue le cri de ralliement des ONG et de nombreux pays à l'ONU pour empêcher la déshumanisation des combats.

Sur le plan éthique, déléguer la mort à un algorithme pose des problèmes insolubles :

L'ABSENCE DE COMPASSION
Contrairement à un soldat, une IA est incapable de discernement moral ou de compassion. Elle ne peut pas interpréter si un véhicule militaire transporte des blessés ou si un ennemi tente de se rendre.

LA "BOÎTE NOIRE" ALGORITHMIQUE
Les décisions prises par une IA sont souvent opaques. Ce manque de transparence empêche de comprendre pourquoi une machine a choisi de frapper, ce qui est inacceptable pour la dignité humaine.

LA FACILITÉ DE LA VIOLENCE
Puisque la machine agit seule et que l'humain est loin du combat, on risque de tuer plus facilement. Sans le choc émotionnel de voir sa cible, la guerre pourrait devenir un réflexe plus fréquent et moins grave aux yeux des décideurs.

L'IMPASSE JURIDIQUE : LE FOSSÉ DE LA RESPONSABILITÉ

Le Droit International Humanitaire (DIH) repose sur des piliers que l'IA ne peut garantir seule : la distinction (civil/combattant), la proportionnalité (évaluer si les dégâts civils sont excessifs par rapport au bénéfice militaire) et la nécessité militaire.

En cas de crime de guerre commis par une machine, un "vide juridique" apparaît. Qui punir ? Le commandant, le programmeur ou l'État ? Pour la France, la létalité est le critère déterminant : un humain doit impérativement rester responsable de l'ouverture du feu pour garantir l'imputabilité des actes.

UNE DIPLOMATIE MONDIALE SOUS TENSION

À Genève, les discussions au sein de l'ONU stagnent. Si de nombreux pays demandent une interdiction préventive des robots tueurs, ils se heurtent à l'opposition de puissances comme la Russie, Israël et les États-Unis. Ces derniers préfèrent utiliser l'expression plus floue de "niveaux appropriés de jugement humain" plutôt que "contrôle humain significatif".

L'idée clé à retenir : L'enjeu n'est pas d'interdire l'intelligence artificielle militaire, qui reste utile pour la détection ou le déminage, mais d'empêcher que la machine ne sorte de la "boucle de décision". Maintenir l'homme comme seul arbitre de la force létale est l'unique moyen de préserver la morale et le droit, même dans l'hyper-guerre de demain.`,
    slug: 'enjeux-ethiques'
  }
])

export const useFeaturedArticles = () => {
  const getArticle = (slug: string): FeaturedArticle | undefined => {
    return articles.find(a => a.slug === slug)
  }

  const updateArticle = (id: number, updates: Partial<FeaturedArticle>) => {
    const article = articles.find(a => a.id === id)
    if (article) {
      Object.assign(article, updates)
    }
  }

  const getExcerpt = (content: string, lines: number = 3): string => {
    const contentLines = content.split('\n').filter(l => l.trim())
    return contentLines.slice(0, lines).join('\n')
  }

  return {
    articles,
    getArticle,
    updateArticle,
    getExcerpt
  }
}
