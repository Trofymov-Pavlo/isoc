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
    excerpt: 'Découvrez les innovations technologiques qui façonnent le conflit moderne. Des drones terrestres aux systèmes de cyberattaques...',
    content: `Le conflit ukrainien marque un tournant dans l'histoire militaire moderne, où les nouvelles technologies jouent un rôle déterminant sur le terrain. Les drones, l'intelligence artificielle et les cyberattaques transforment profondément les stratégies de combat et redéfinissent les notions de supériorité militaire. Cette guerre démontre comment l'innovation technologique peut compenser des désavantages en termes de ressources ou de personnel.

Les drones terrestres, aériens et navals sont devenus des outils essentiels pour la reconnaissance, le ciblage et les frappes de précision. Du côté de l'intelligence artificielle, des systèmes automatisés analysent des images satellites et des données en temps réel pour identifier des cibles et optimiser les décisions tactiques.

Les cyberattaques constituent un front invisible mais crucial, où les intrusions dans les réseaux adverses, le brouillage des communications et la collecte de renseignements électroniques créent un avantage stratégique considérable.

1. LES DRONES : UNE RÉVOLUTION TACTIQUE

DRONES AÉRIENS
Les drones de reconnaissance comme le Bayraktar TB2 turc ou les drones commerciaux modifiés sont omniprésents sur le champ de bataille. Ils permettent une surveillance continue, l'identification de cibles et même des frappes de précision avec des munitions guidées. Leur coût relativement faible comparé aux aéronefs pilotés en fait des armes démocratisées.

DRONES TERRESTRES
Les véhicules terrestres sans pilote sont utilisés pour le déminage, la livraison de munitions et la reconnaissance en zones dangereuses. Leur capacité à opérer dans des environnements hostiles sans mettre en danger des vies humaines représente un avantage tactique majeur.

DRONES NAVALS
Les drones maritimes de surface et sous-marins ont été utilisés pour des attaques contre des navires militaires et des infrastructures portuaires. Ces systèmes peu coûteux peuvent infliger des dégâts considérables à des cibles de grande valeur, transformant l'équilibre des forces navales.

DRONES KAMIKAZES
Les munitions rôdeuses comme le Switchblade américain ou le Lancet russe combinent reconnaissance et frappe. Elles peuvent patrouiller une zone, identifier une cible et s'y écraser avec une charge explosive, offrant une précision inégalée.

2. INTELLIGENCE ARTIFICIELLE ET CIBLAGE AUTOMATISÉ

ANALYSE D'IMAGES SATELLITE
L'IA permet d'analyser des milliers d'images satellites quotidiennement pour détecter des mouvements de troupes, identifier des équipements militaires et prédire des manœuvres ennemies. Cette capacité de traitement massif dépasse largement les capacités humaines.

SYSTÈMES DE CIBLAGE ASSISTÉS
Des algorithmes d'IA assistent les opérateurs dans l'identification et la priorisation des cibles. Ils peuvent calculer les trajectoires optimales, évaluer les dommages collatéraux potentiels et suggérer les munitions les plus appropriées.

FUSION DE DONNÉES
L'IA agrège des données provenant de multiples sources (satellites, drones, radars, capteurs au sol) pour créer une image tactique unifiée en temps réel. Cette fusion permet une prise de décision plus rapide et mieux informée.

MAINTENANCE PRÉDICTIVE
Les systèmes d'IA analysent l'état des équipements militaires et prédisent les pannes avant qu'elles ne surviennent, optimisant ainsi la disponibilité opérationnelle des armes et véhicules.

3. CYBERGUERRE ET GUERRE ÉLECTRONIQUE

INTRUSIONS DANS LES RÉSEAUX
Les attaques contre les systèmes informatiques ennemis visent à voler des informations sensibles, perturber les communications et saboter les infrastructures critiques. Les tentatives de piratage des réseaux militaires et gouvernementaux sont constantes.

BROUILLAGE ET CONTRE-MESURES ÉLECTRONIQUES
Le brouillage des signaux GPS, des communications radio et des systèmes de guidage de missiles crée un avantage tactique en aveuglant l'adversaire. Les systèmes de guerre électronique peuvent neutraliser des drones ennemis ou dévier des missiles guidés.

ATTAQUES CONTRE LES INFRASTRUCTURES CIVILES
Les cyberattaques ne se limitent pas aux cibles militaires. Les réseaux électriques, les systèmes de transport et les services publics sont également visés pour démoraliser la population et affaiblir l'économie.

RECHERCHE DE RENSEIGNEMENT ÉLECTRONIQUE (SIGINT)
L'interception et l'analyse des communications adverses fournissent des informations cruciales sur les intentions, les positions et les capacités de l'ennemi. Les systèmes SIGINT modernes peuvent traiter d'énormes volumes de données pour extraire des renseignements exploitables.

4. IMPLICATIONS ET DÉFIS

ACCESSIBILITÉ DES TECHNOLOGIES
La disponibilité commerciale de nombreuses technologies (drones, logiciels d'IA, outils de piratage) réduit la barrière d'entrée technologique. Des acteurs non-étatiques peuvent désormais accéder à des capacités autrefois réservées aux grandes puissances.

VULNÉRABILITÉ DES SYSTÈMES CONNECTÉS
La dépendance aux technologies numériques crée de nouvelles vulnérabilités. Un système compromis peut devenir un point d'entrée pour paralyser toute une chaîne de commandement.

COURSE À L'INNOVATION
Le conflit stimule une course à l'innovation où chaque avancée technologique d'un camp pousse l'autre à développer des contre-mesures. Cette dynamique accélère le développement de nouvelles armes et tactiques.

CONCLUSION
Les technologies militaires modernes redéfinissent la nature même de la guerre. Les drones omniprésents, l'intelligence artificielle qui assiste les décisions humaines et les cyberattaques invisibles créent un environnement de combat multidimensionnel où la supériorité technologique peut compenser d'autres faiblesses. Cette évolution pose des questions fondamentales sur l'avenir des conflits armés et sur la place de l'humain dans la conduite de la guerre.`,
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
