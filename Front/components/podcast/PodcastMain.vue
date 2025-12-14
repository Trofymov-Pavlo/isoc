<template>
  <main class="podcast-page">
    <PodcastHero
      :title="hero.title"
      :subtitle="hero.subtitle"
      :hosts="hero.hosts"
      :duration="hero.duration"
      :date="hero.date"
      :is-playing="isPlaying"
      @toggle="togglePlayback"
    />

    <section class="podcast-content">
      <div class="content-grid">
        <div class="main-content">
          <EpisodeSummary :paragraphs="summaryTexts" />
          <TimelineSection :items="timeline" />
          <HostsSection :hosts="hosts" />
          <ResourcesSection :resources="resources" />
          <KeyPointsSection :points="keyPoints" />
          <ShareSection />
        </div>

        <aside class="sidebar">
          <SubscribeBox :links="subscribeLinks" />
          <SimilarEpisodes :episodes="similarEpisodes" />
          <AuthorArticles :authors="authorArticles" />
        </aside>
      </div>
    </section>

    <CtaSection :title="cta.title" :description="cta.description" :cta-text="cta.button" />
    <NewsletterSection />
  </main>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import AuthorArticles from '~/components/podcast/AuthorArticles.vue';
import CtaSection from '~/components/podcast/CtaSection.vue';
import EpisodeSummary from '~/components/podcast/EpisodeSummary.vue';
import HostsSection from '~/components/podcast/HostsSection.vue';
import KeyPointsSection from '~/components/podcast/KeyPointsSection.vue';
import NewsletterSection from '~/components/podcast/NewsletterSection.vue';
import PodcastHero from '~/components/podcast/PodcastHero.vue';
import ResourcesSection from '~/components/podcast/ResourcesSection.vue';
import ShareSection from '~/components/podcast/ShareSection.vue';
import SimilarEpisodes from '~/components/podcast/SimilarEpisodes.vue';
import SubscribeBox from '~/components/podcast/SubscribeBox.vue';
import TimelineSection from '~/components/podcast/TimelineSection.vue';

const isPlaying = ref(false);
const togglePlayback = () => { isPlaying.value = !isPlaying.value; };

const hero = {
  title: "La Guerre de l'information",
  subtitle: "Analyse approfondie des enjeux informationnels du conflit Ukraine-Russie",
  hosts: ['Antoine TENA', 'Nathan BARRACHIN', 'Pavel TROFYMOV'],
  duration: '45 min',
  date: 'Publié le 14 décembre 2025',
};

const summaryTexts = [
  "Dans cet épisode, nos trois animateurs explorent les mécanismes de la guerre informationnelle au cœur du conflit Ukraine-Russie. Comment les stratégies d'influence façonnent-elles la narration mondiale ? Quel rôle jouent les réseaux sociaux dans la diffusion de la propagande ? Et comment distinguer la désinformation de l'information vérifiée ?",
  "Rejoignez-nous pour une discussion captivante sur le fact-checking, l'OSINT, les deepfakes et les défis contemporains de la vérité à l'ère numérique.",
];

const timeline = [
  { time: '00:00', title: 'Introduction et présentation du sujet', description: 'Les enjeux de la guerre informationnelle contemporaine' },
  { time: '05:12', title: "Stratégies d'influence et narratives", description: 'Comment les acteurs du conflit façonnent le récit global' },
  { time: '15:34', title: 'Rôle des réseaux sociaux', description: 'Telegram, X, Facebook : des vecteurs de propagande et de désinformation' },
  { time: '25:47', title: 'Deepfakes et technologies de tromperie', description: 'Comment identifier et combattre les vidéos manipulées' },
  { time: '35:20', title: 'OSINT, fact-checking et contre-désinformation', description: "Les outils et techniques pour vérifier l'information" },
  { time: '42:15', title: 'Conclusion et ressources', description: "Recommandations et appels à l'action" },
];

const hosts = [
  { initials: 'AT', name: 'Antoine TENA', role: 'Rédacteur en chef, Spécialiste en géopolitique', bio: "Antoine est un journaliste d'investigation spécialisé dans les enjeux géopolitiques. Il couvre le conflit Ukraine-Russie depuis 2022 pour AXIOM." },
  { initials: 'NB', name: 'Nathan BARRACHIN', role: 'Analyste en désinformation', bio: "Nathan est un expert en fact-checking et vérification d'informations. Il travaille avec plusieurs organisations de fact-checking internationales." },
  { initials: 'PT', name: 'Pavel TROFYMOV', role: 'Développeur et expert en OSINT', bio: "Pavel est un spécialiste en open-source intelligence et technologies de vérification. Il contribue à des projets de lutte contre la désinformation." },
];

const resources = [
  { title: 'Bellingcat', description: "Plateforme collaborative de journalisme d'investigation et d'OSINT" },
  { title: 'StopFake', description: 'Initiative ukrainienne de fact-checking sur le conflit' },
  { title: 'First Draft News', description: 'Ressources sur la vérification et la lutte contre la désinformation' },
  { title: 'Media Bias/Fact Check', description: 'Base de données de sources médiatiques avec analyse de biais' },
  { title: 'TweetDeck', description: 'Outil pour surveiller les tendances et désinformations sur X' },
  { title: 'Reverse Image Search', description: 'Google Images, TinEye, Yandex - outils de vérification d\'images' },
];

const keyPoints = [
  { title: 'Authentification vs Désinformation', description: "Comment les techniques d'authentification aident à distinguer le vrai du faux dans un paysage médiatique fragmenté." },
  { title: 'Bulles de filtre et polarisation', description: 'Les algorithmes des réseaux sociaux créent des bulles informationnelles qui amplifient la polarisation.' },
  { title: 'Responsabilité des plateformes', description: 'Les débats autour de la modération de contenu et de la responsabilité des géants de la tech.' },
  { title: 'Éducation aux médias', description: "L'importance de l'alphabétisation médiatique face aux défis contemporains de l'information." },
];

const subscribeLinks = [
  { label: 'Apple Podcasts', icon: '🎧', href: '#' },
  { label: 'Spotify', icon: '🎙️', href: '#' },
  { label: 'Google Podcasts', icon: '📻', href: '#' },
  { label: 'RSS Feed', icon: '🎵', href: '#' },
];

const similarEpisodes = [
  { number: 'Ep. 3', title: 'Propagande militaire et narratives de conflit', date: '21 nov 2025' },
  { number: 'Ep. 1', title: 'Les racines géopolitiques du conflit Ukraine-Russie', date: '30 oct 2025' },
];

const authorArticles = [
  { author: 'Antoine TENA', title: 'Géopolitique du conflit Ukraine-Russie', link: '#' },
  { author: 'Nathan BARRACHIN', title: 'Guide pratique du fact-checking', link: '#' },
  { author: 'Pavel TROFYMOV', title: "OSINT et vérification d'images", link: '#' },
];

const cta = {
  title: "Vous avez une information à vérifier ?",
  description: "Contactez notre équipe de fact-checking pour contribuer à la lutte contre la désinformation",
  button: 'Nous contacter',
};
</script>

<style scoped>
.podcast-page {
  background: #ffffff;
  min-height: 100vh;
}

.podcast-content {
  padding: 60px 20px;
}

.content-grid {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 320px;
  gap: 40px;
}

.main-content {
  display: flex;
  flex-direction: column;
  gap: 50px;
}

.sidebar {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

@media (max-width: 1200px) {
  .content-grid { grid-template-columns: 1fr; }
}

@media (max-width: 480px) {
  .podcast-content { padding: 32px 16px; }
}
</style>
