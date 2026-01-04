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
    author: 'Hiba EL HAYANI',
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
    title: 'La guerre de l\'information',
    author: 'Antoine TENA',
    date: '2025-12-12',
    excerpt: 'Les stratégies médiatiques, réseaux sociaux et désinformation jouent un rôle crucial dans le conflit moderne...',
    content: `LA GUERRE DE L'INFORMATION : UN ENJEU STRATÉGIQUE MODERNE

INTRODUCTION
Le conflit entre l'Ukraine et la Russie n'est pas seulement militaire. C'est aussi une bataille informationnelle féroce où chaque partie tente de contrôler le récit et d'influencer l'opinion publique mondiale.

1. LES STRATÉGIES MÉDIATIQUES ET LES NARRATIONS RIVALES

LA RUSSIE
• Désinformation systématique : Campagnes de fausses informations coordonnées visant à semer le doute
• Discours de victimisation : Présentation de l'intervention comme une "opération spéciale" défensive
• Attaques contre les sources : Discréditer les médias occidentaux comme "propagande"

L'UKRAINE
• Transparence et authenticité : Communications directes du gouvernement et de la société civile
• Narration d'une nation en défense : Mobilisation autour de l'indépendance et de la démocratie
• Engagement des influenceurs : Utilisation des personnalités pour amplifier le message

2. LES RÉSEAUX SOCIAUX : TERRAINS DE BATAILLES NUMÉRIQUES

TELEGRAM
- Canal privilégié pour les informations militaires et civiles
- Spread rapide de contenu (vidéos, photos de combats)
- Difficile à vérifier en temps réel

TWITTER/X
- Source majeure de breaking news et de commentaires d'experts
- Bots et comptes inautentiques amplifient la désinformation
- Hashtags comme #StandWithUkraine créent des mouvements de solidarité

TIKTOK
- Jeune audience exposée à du contenu émotionnel
- Vidéos de destruction et de courage côtoient la propagande
- Viralité rapide sans vérification

3. LES DEEPFAKES ET LA MANIPULATION D'IMAGES

EXEMPLES NOTABLES
- Vidéos deepfake du président Zelensky (avant les vrais appels vidéo)
- Images de destructions manipulées ou sorties de contexte
- Montages trompeurs de déclarations politiques

IMPACT
- Confiance publique dans les médias diminuée
- Difficulté à distinguer le vrai du faux
- Arme de désinformation particulièrement efficace

4. L'OSINT (OPEN SOURCE INTELLIGENCE)

RÔLE CRUCIAL
- Citoyens enquêteurs : Vérification d'images satellite, d'enregistrements audio
- Geolocalisation : Identification d'emplacements militaires via les métadonnées
- Chaînes comme Bellingcat : Enquêtes approfondies basées sur des sources ouvertes

EXEMPLES
- Identification de soldats russes par leurs insignes
- Localisation de convois militaires
- Vérification des cibles de bombardements

5. FACT-CHECKING ET VÉRIFICATION

INITIATIVES
- Reuters, AFP, BBC : Vérification systématique des images et récits
- PolitiFact et similaires : Débunking des fausses affirmations
- Fact-checkers locales : Vérification en temps réel en Ukraine et Russie

DÉFIS
- Vitesse de propagation > vitesse de vérification
- Confirmation bias : les gens croient ce qui confirme leurs croyances
- Difficultés à atteindre les populations dans les zones de désinformation

CONCLUSION
La guerre de l'information est un élément crucial du conflit, déterminant l'engagement international, le moral des populations et la légitimité des narratives. La vérité devient une arme stratégique, et la capacité à la discerner un enjeu majeur pour les démocraties.`,
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
