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
    title: 'Les enjeux éthiques et juridiques',
    author: 'Nathan BARRACHIN',
    date: '2025-12-18',
    excerpt: 'Armements autonomes, responsabilité humaine, droit international : les questions éthiques du conflit moderne...',
    content: `Le développement rapide des technologies militaires autonomes soulève des questions éthiques et juridiques fondamentales qui dépassent le cadre du conflit ukrainien. Jusqu'où peut-on déléguer les décisions de vie ou de mort à des machines ? Qui est responsable lorsqu'une arme autonome commet une erreur ou viole le droit international humanitaire ?

Les systèmes d'armes létales autonomes (SALA) posent un défi majeur aux conventions internationales existantes. Le principe de discrimination entre combattants et civils, pierre angulaire du droit de la guerre, peut-il être garanti par des algorithmes ? La notion de responsabilité humaine dans la chaîne de commandement doit être repensée face à ces technologies.

Le débat oppose ceux qui voient dans ces technologies un moyen de limiter les pertes humaines et d'améliorer la précision des frappes, et ceux qui craignent une déshumanisation de la guerre et une prolifération incontrôlée d'armes dangereuses.

1. LES ARMES AUTONOMES ET LE DROIT INTERNATIONAL HUMANITAIRE

PRINCIPE DE DISTINCTION
Le droit international humanitaire exige que les combattants distinguent entre cibles militaires et civils. Les algorithmes peuvent-ils faire cette distinction avec la même fiabilité qu'un soldat humain ? Les systèmes d'IA peuvent se tromper en identifiant un tracteur agricole comme un véhicule militaire, ou confondre des civils avec des combattants.

PRINCIPE DE PROPORTIONNALITÉ
Tout usage de la force doit être proportionnel à l'avantage militaire recherché. Comment une machine peut-elle évaluer la valeur d'une vie humaine ou le coût moral d'une action ? Cette évaluation nécessite un jugement éthique que seul un être humain peut exercer.

PRÉCAUTIONS DANS L'ATTAQUE
Les commandants militaires doivent prendre toutes les précautions possibles pour minimiser les pertes civiles. Un système autonome peut-il manifester cette prudence ? La programmation peut-elle intégrer la complexité des situations humanitaires ?

RESPONSABILITÉ POUR LES VIOLATIONS
Si une arme autonome commet un crime de guerre, qui est responsable ? Le programmeur ? Le commandant qui l'a déployée ? Le fabricant ? L'absence de responsabilité claire crée un vide juridique dangereux.

2. LA QUESTION DE LA RESPONSABILITÉ HUMAINE

LE CONCEPT DE "HUMAN IN THE LOOP"
Certains systèmes maintiennent un opérateur humain dans la boucle décisionnelle pour autoriser chaque action létale. Mais que se passe-t-il lorsque les décisions doivent être prises en millisecondes, trop rapidement pour une intervention humaine ?

LE "HUMAN ON THE LOOP"
D'autres systèmes permettent à un humain de superviser et d'intervenir si nécessaire, mais la machine prend les décisions opérationnelles. Ce modèle pose la question : l'humain peut-il vraiment comprendre et contrôler des systèmes de plus en plus complexes ?

LE "HUMAN OUT OF THE LOOP"
Les systèmes entièrement autonomes qui opèrent sans supervision humaine représentent le scénario le plus problématique. Une fois déployés, ils peuvent prendre des décisions de vie ou de mort sans intervention humaine, soulevant des questions éthiques fondamentales.

RECOURS ET JUSTICE
Comment les victimes de systèmes autonomes peuvent-elles obtenir justice ? Comment enquêter sur les décisions prises par des algorithmes complexes ? Le droit à un recours effectif est un principe fondamental des droits de l'homme.

3. DILEMMES ÉTHIQUES DANS LE CONFLIT UKRAINIEN

UTILISATION DES DRONES KAMIKAZES
Les munitions rôdeuses autonomes soulèvent des questions : peuvent-elles vraiment distinguer combattants et civils ? Que se passe-t-il si elles perdent le contact avec leur contrôleur ? Doivent-elles avoir un mécanisme d'autodestruction ?

CIBLAGE ASSISTÉ PAR IA
Lorsque l'IA suggère des cibles, les opérateurs humains ont-ils tendance à faire confiance aveuglément à la machine ? Cette "automation bias" peut conduire à des erreurs fatales. Comment maintenir le jugement critique humain ?

CYBERATTAQUES CONTRE LES INFRASTRUCTURES CIVILES
Les attaques informatiques contre les réseaux électriques ou les hôpitaux violent-elles le principe de distinction ? Où se situe la limite entre cible militaire légitime et infrastructure civile protégée ?

DÉSINFORMATION PAR IA
Les deepfakes et la désinformation générée par IA peuvent influencer l'opinion publique et manipuler les populations. Est-ce une forme de guerre psychologique légitime ou une violation des droits humains ?

4. PERSPECTIVES RÉGLEMENTAIRES ET DÉBATS INTERNATIONAUX

APPELS À UN MORATOIRE
De nombreuses ONG et experts appellent à un moratoire sur les systèmes d'armes létales autonomes, le temps d'établir un cadre juridique clair. Mais la course technologique rend cette pause difficile à obtenir.

LES CONVENTIONS DE GENÈVE SONT-ELLES SUFFISANTES ?
Les conventions existantes ont été rédigées pour la guerre conventionnelle. Sont-elles adaptées aux défis posés par l'IA et les systèmes autonomes ? Faut-il de nouveaux traités internationaux ?

RÈGLES D'ENGAGEMENT POUR LES SYSTÈMES AUTONOMES
Certains militaires et juristes travaillent à définir des règles d'engagement spécifiques pour les systèmes autonomes : dans quelles conditions peuvent-ils être déployés ? Quelles garanties de sécurité doivent être intégrées ?

VÉRIFICATION ET TRANSPARENCE
Comment vérifier que les États respectent les accords sur les armes autonomes ? Comment assurer la transparence sur les capacités déployées sans compromettre la sécurité nationale ?

5. L'ÉTHIQUE DE L'INNOVATION MILITAIRE

LA RESPONSABILITÉ DES CHERCHEURS ET INGÉNIEURS
Les scientifiques qui développent ces technologies ont-ils une responsabilité éthique particulière ? Doivent-ils refuser de travailler sur certains projets ? Comment concilier liberté de recherche et impératifs éthiques ?

LE RÔLE DES ENTREPRISES PRIVÉES
De plus en plus, l'innovation militaire vient d'entreprises privées. Comment encadrer leur rôle ? Peuvent-elles refuser de vendre leurs technologies à certains clients ?

LES DÉFIS DE LA DOUBLE USAGE
Beaucoup de technologies militaires ont des applications civiles bénéfiques (médecine, transports, recherche scientifique). Comment encourager l'innovation tout en prévenant les usages malveillants ?

CONCLUSION
Les enjeux éthiques et juridiques soulevés par les nouvelles technologies militaires dépassent largement le cadre du conflit ukrainien. Ils posent des questions fondamentales sur la place de l'humain dans la guerre, sur la nature de la responsabilité morale, et sur notre capacité collective à encadrer l'innovation technologique. Le droit international doit évoluer pour répondre à ces défis, mais cette évolution nécessite un consensus international difficile à atteindre dans un contexte de compétition géopolitique. L'équilibre entre efficacité militaire, protection des civils et préservation de la dignité humaine reste le défi central de notre époque.`,
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
