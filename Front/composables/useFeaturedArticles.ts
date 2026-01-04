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
    excerpt: 'Découvrez les innovations technologiques qui façonnent le conflit moderno. Des drones terrestres aux systèmes de cyberattaques...',
    content: 'À remplir par Hiba EL HAYANI',
    slug: 'technologies-militaires'
  },
  {
    id: 2,
    title: 'La guerre de l\'information',
    author: 'Antoine TENA',
    date: '2025-01-20',
    excerpt: 'Les stratégies médiatiques, réseaux sociaux et désinformation jouent un rôle crucial dans le conflit moderne...',
    content: `## La guerre de l'information : Un enjeu stratégique moderne

### Introduction
Le conflit entre l'Ukraine et la Russie n'est pas seulement militaire. C'est aussi une bataille informationnelle féroce où chaque partie tente de contrôler le récit et d'influencer l'opinion publique mondiale.

### 1. Les stratégies médiatiques et les narrations rivales

#### La Russie
- **Désinformation systématique** : Campagnes de fausses informations coordonnées visant à semer le doute
- **Discours de victimisation** : Présentation de l'intervention comme une "opération spéciale" défensive
- **Attaques contre les sources** : Discréditer les médias occidentaux comme "propagande"

#### L'Ukraine
- **Transparence et authenticité** : Communications directes du gouvernement et de la société civile
- **Narration d'une nation en défense** : Mobilisation autour de l'indépendance et de la démocratie
- **Engagement des influenceurs** : Utilisation des personnalités pour amplifier le message

### 2. Les réseaux sociaux : Terrains de batailles numériques

#### Telegram
- Canal privilégié pour les informations militaires et civiles
- Spread rapide de contenu (vidéos, photos de combats)
- Difficile à vérifier en temps réel

#### Twitter/X
- Source majeure de breaking news et de commentaires d'experts
- Bots et comptes inautentiques amplifient la désinformation
- Hashtags comme #StandWithUkraine créent des mouvements de solidarité

#### TikTok
- Jeune audience expose à du contenu émotionnel
- Vidéos de destruction et de courage côtoient la propagande
- Viralité rapide sans vérification

### 3. Les deepfakes et la manipulation d'images

#### Exemples notables
- Vidéos deepfake du président Zelensky (avant les vrais appels vidéo)
- Images de destructions manipulées ou sorties de contexte
- Montages trompeurs de déclarations politiques

#### Impact
- Confiance publique dans les médias diminuée
- Difficulté à distinguer le vrai du faux
- Arme de désinformation particulièrement efficace

### 4. L'OSINT (Open Source Intelligence)

#### Rôle crucial
- **Citoyens enquêteurs** : Vérification d'images satellite, d'enregistrements audio
- **Geolocalisation** : Identification d'emplacements militaires via les métadonnées
- **Chaînes comme Bellingcat** : Enquêtes approfondies basées sur des sources ouvertes

#### Exemples
- Identification de soldats russes par leurs insignes
- Localisation de convois militaires
- Vérification des cibles de bombardements

### 5. Fact-checking et vérification

#### Initiatives
- **Reuters, AFP, BBC** : Vérification systématique des images et récits
- **PolitiFact et similaires** : Débunking des fausses affirmations
- **Fact-checkers locales** : Vérification en temps réel en Ukraine et Russie

#### Défis
- Vitesse de propagation > vitesse de vérification
- Confirmation bias : les gens croient ce qui confirme leurs croyances
- Difficultés à atteindre les populations dans les zones de désinformation

### Conclusion
La guerre de l'information est un élément crucial du conflit, déterminant l'engagement international, le moral des populations et la légitimité des narratives. La vérité devient une arme stratégique, et la capacité à la discerner un enjeu majeur pour les démocraties.`,
    slug: 'guerre-information'
  },
  {
    id: 3,
    title: 'Les enjeux éthiques et juridiques',
    author: 'Nathan BARRACHIN',
    date: '2025-02-01',
    excerpt: 'Armements autonomes, responsabilité humaine, droit international : les questions éthiques du conflit moderne...',
    content: 'À remplir par Nathan BARRACHIN',
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
