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
    title: 'Guerre de l\'information : le champ de bataille invisible',
    author: 'Antoine TENA',
    date: '2025-12-12',
    excerpt: 'Le conflit russo-ukrainien se joue aussi sur un front invisible : images, récits, réseaux sociaux et vérification deviennent des armes stratégiques...',
    content: `Le conflit russo-ukrainien ne se joue pas uniquement à coups d'artillerie, de drones et de manœuvres terrestres. Il se joue aussi dans les fils d'actualité, dans les chaînes Telegram, dans les titres des médias et jusque dans les conversations quotidiennes. En Ukraine comme en Russie, convaincre peut parfois produire des effets aussi décisifs que vaincre : obtenir des armes et des sanctions, maintenir le moral, isoler l'adversaire, ou au contraire semer le doute.

Cette "guerre de l'information" n'est pas un simple bruit de fond : c'est un théâtre à part entière, avec ses doctrines, ses acteurs et ses outils. Elle combine des stratégies d'État (propagande, censure, communication officielle), la mécanique des plateformes (viralité, algorithmes, communautés) et une bataille de la preuve (images, géolocalisations, fact-checking). Comprendre ce front invisible, c'est comprendre une partie de la dynamique du conflit.

MAÎTRISER LE RÉCIT : DEUX STRATÉGIES, UN OBJECTIF

Côté russe, l'information est largement pensée comme un instrument de contrôle. La communication officielle vise d'abord un public intérieur : maintenir la cohésion, justifier l'intervention, minimiser les revers et délégitimer les sources contradictoires. La rhétorique s'appuie sur des éléments récurrents (menace, protection, "opération spéciale") et sur une posture de défi face aux médias occidentaux, présentés comme partiaux.

Côté ukrainien, la communication s'inscrit davantage dans une logique de mobilisation et d'internationalisation. Les messages cherchent à tenir la population, à documenter les destructions, et à convaincre des partenaires étrangers. Les prises de parole régulières, directes et incarnées, la mise en avant des civils, ainsi qu'un discours centré sur la souveraineté et la défense, participent à installer une lecture du conflit favorable à Kiev.

Dans les deux cas, l'objectif est identique : imposer un cadre d'interprétation du réel. Ce n'est pas seulement "informer", c'est orienter : quels faits compter, quels mots employer, quelles images montrer, quels silences maintenir.

PLATEFORMES ET VIRALITÉ : L'INFO CIRCULE COMME UNE MUNITION

Les réseaux sociaux n'ont pas remplacé les médias traditionnels : ils les ont accélérés, fragmentés et parfois court-circuités. La rapidité de circulation crée une pression constante : publier vite, avant l'adversaire, avant le démenti, avant la vérification. Cette temporalité favorise les contenus émotionnels et spectaculaires, et rend l'espace informationnel plus vulnérable aux manipulations.

Telegram s'est imposé comme un carrefour stratégique. On y trouve des canaux officiels, des sources militantes, des communautés locales et des relais pseudo-journalistiques. Son avantage : une diffusion rapide, une audience fidèle, une circulation en "circuit fermé". Son problème : l'opacité, la difficulté de tracer l'origine et la multiplication des contenus non vérifiés.

X (Twitter) joue un autre rôle : celui du temps réel et du commentaire. Observateurs OSINT, journalistes, institutions et comptes anonymes s'y croisent. La plateforme sert à diffuser des images, à interpréter, à contester, mais aussi à amplifier. Entre algorithmes, effets de meute et comptes automatisés, certaines narratives prennent de l'ampleur non parce qu'elles sont vraies, mais parce qu'elles sont répétées.

TikTok, enfin, influe sur un public différent : format court, forte charge émotionnelle, montage dynamique. Cette logique peut sensibiliser… mais aussi simplifier, dramatiser et faciliter l'essor de contenus trompeurs. Dans un contexte de guerre, la forme peut parfois compter autant que le fond.

MANIPULATION VISUELLE ET IA : DEEPFAKES, MONTAGES, CONTEXTES DÉTOURNÉS

Une grande partie de la bataille se joue sur les images. Photos, vidéos et extraits audio circulent en masse, souvent sans contexte. Les manipulations ne reposent pas uniquement sur des deepfakes sophistiqués : le plus efficace reste souvent le détournement.

Un extrait coupé, une vidéo d'un autre conflit recyclée, un plan sans géolocalisation, une date absente : ces détails suffisent à orienter une interprétation. La désinformation moderne n'a pas toujours besoin d'inventer, elle peut simplement déplacer.

L'IA générative ajoute un niveau de complexité. Elle rend la fabrication plus accessible et augmente le volume de contenus potentiellement trompeurs. Mais elle renforce aussi les capacités de détection (analyse d'artefacts, recoupements, outils de vérification). Dans ce duel, l'important n'est pas seulement la technologie : c'est l'écosystème qui décide de ce qui est crédible.

OSINT ET FACT-CHECKING : LA CONTRE-ATTAQUE PAR LA PREUVE

Face à la désinformation, un contre-pouvoir s'est structuré : l'OSINT (Open Source Intelligence) et le fact-checking. Des analystes, journalistes et citoyens utilisent des sources ouvertes (images satellites, vidéos, cartes, données publiques) pour vérifier des événements, confirmer des lieux, dater des séquences et recouper les affirmations.

La méthode repose sur des gestes simples mais rigoureux : comparer des images, identifier des repères, analyser l'ombre et la météo, vérifier des métadonnées, confronter plusieurs sources. Cette pratique ne rend pas la vérité automatique, mais elle élève le niveau d'exigence. Elle réintroduit de la preuve dans un espace dominé par la vitesse.

Le fact-checking institutionnel (agences, médias, organisations spécialisées) complète cet effort. Son défi est structurel : la correction circule souvent moins vite que l'erreur. Pourtant, dans la durée, ces mécanismes permettent de limiter l'impact de certaines campagnes et de maintenir une base minimale de confiance.

POURQUOI C'EST DÉCISIF : MORALE, ALLIANCES, LÉGITIMITÉ

La guerre de l'information a des effets concrets. Le moral des populations dépend du sentiment de contrôle, de la cohérence du récit et de la perception des succès. Les alliances dépendent du soutien des opinions publiques et de la crédibilité des preuves présentées. La légitimité internationale se construit à travers des images et des récits capables de convaincre.

Dans ce contexte, l'enjeu n'est pas seulement de "gagner" une bataille de communication, mais de stabiliser un espace de vérité minimale : suffisamment solide pour décider, soutenir, sanctionner, négocier. Quand l'information devient une arme, la capacité à vérifier devient une défense.

Le conflit en Ukraine montre à quel point l'information n'est plus un simple accompagnement de la guerre : elle en est une dimension structurante. Propagande, réseaux sociaux, IA, OSINT et fact-checking composent un champ de bataille où la vitesse et l'émotion affrontent la preuve et la méthode. La leçon centrale est simple : dans un environnement saturé de contenus, la vérité n'est pas seulement un fait, c'est aussi un effort collectif.`,
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
