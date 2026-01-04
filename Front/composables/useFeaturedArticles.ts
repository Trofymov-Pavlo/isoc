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
    date: '2025-01-15',
    excerpt: 'Découvrez les innovations technologiques qui façonnent le conflit moderne. Des drones terrestres aux systèmes de cyberattaques...',
    content: `Le conflit ukrainien marque un tournant dans l'histoire militaire moderne, où les nouvelles technologies jouent un rôle déterminant sur le terrain. Les drones, l'intelligence artificielle et les cyberattaques transforment profondément les stratégies de combat et redéfinissent les notions de supériorité militaire. Cette guerre démontre comment l'innovation technologique peut compenser des désavantages en termes de ressources ou de personnel.

Les drones terrestres, aériens et navals sont devenus des outils essentiels pour la reconnaissance, le ciblage et les frappes de précision. Du côté de l'intelligence artificielle, des systèmes automatisés analysent des images satellites et des données en temps réel pour identifier des cibles et optimiser les décisions tactiques.

Les cyberattaques constituent un front invisible mais crucial, où les intrusions dans les réseaux adverses, le brouillage des communications et la collecte de renseignements électroniques créent un avantage stratégique considérable.

À COMPLÉTER PAR HIBA EL HAYANI`,
    slug: 'technologies-militaires'
  },
  {
    id: 2,
    title: 'La guerre de l\'information',
    author: 'Antoine TENA',
    date: '2025-01-20',
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
    date: '2025-02-01',
    excerpt: 'Armements autonomes, responsabilité humaine, droit international : les questions éthiques du conflit moderne...',
    content: `Le développement rapide des technologies militaires autonomes soulève des questions éthiques et juridiques fondamentales qui dépassent le cadre du conflit ukrainien. Jusqu'où peut-on déléguer les décisions de vie ou de mort à des machines ? Qui est responsable lorsqu'une arme autonome commet une erreur ou viole le droit international humanitaire ?

Les systèmes d'armes létales autonomes (SALA) posent un défi majeur aux conventions internationales existantes. Le principe de discrimination entre combattants et civils, pierre angulaire du droit de la guerre, peut-il être garanti par des algorithmes ? La notion de responsabilité humaine dans la chaîne de commandement doit être repensée face à ces technologies.

Le débat oppose ceux qui voient dans ces technologies un moyen de limiter les pertes humaines et d'améliorer la précision des frappes, et ceux qui craignent une déshumanisation de la guerre et une prolifération incontrôlée d'armes dangereuses.

À COMPLÉTER PAR NATHAN BARRACHIN`,
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
