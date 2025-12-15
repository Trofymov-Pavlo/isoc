<template>
  <main class="podcast-page">
    <PageHero
      title="La Guerre de l'information"
      subtitle="Analyse approfondie des enjeux informationnels du conflit Ukraine-Russie"
      badge="Podcast AXIOM"
      badge-icon="🎙️"
    />

    <div class="podcast-wrapper">
      <div class="podcast-meta-bar">
        <div class="hosts-info">
          <span class="host-label">Présenté par</span>
          <div class="hosts-list">
            <span v-for="(host, i) in hero.hosts" :key="host" class="host">
              {{ host }}<span v-if="i < hero.hosts.length - 1" class="separator">•</span>
            </span>
          </div>
        </div>
        <div class="play-info">
          <span class="duration">{{ hero.duration }}</span>
          <span class="date">{{ hero.date }}</span>
        </div>
      </div>

      <div class="play-button-row">
        <button class="play-button" @click="togglePlayback">
          <span class="play-icon" v-if="!isPlaying">▶</span>
          <span class="pause-icon" v-else>⏸</span>
        </button>
        <span class="play-label">{{ isPlaying ? 'Écouter le podcast' : 'Lancer la lecture' }}</span>
      </div>

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
    </div>
  </main>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import PageHero from '~/components/shared/PageHero.vue';
import AuthorArticles from '~/components/podcast/AuthorArticles.vue';
import CtaSection from '~/components/podcast/CtaSection.vue';
import EpisodeSummary from '~/components/podcast/EpisodeSummary.vue';
import HostsSection from '~/components/podcast/HostsSection.vue';
import KeyPointsSection from '~/components/podcast/KeyPointsSection.vue';
import NewsletterSection from '~/components/podcast/NewsletterSection.vue';
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
  min-height: 100vh;
  background: #fff;
}

.podcast-wrapper {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 calc(2vw);
}

.podcast-meta-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 32px 0 24px;
  border-bottom: 1px solid #f0f0f0;
  max-width: 900px;
  margin: 0 auto;
}

.hosts-info {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.host-label {
  font-size: 12px;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-weight: 600;
}

.hosts-list {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.host {
  font-size: 14px;
  font-weight: 600;
  color: #2f0538;
}

.separator {
  margin: 0 4px;
  color: #ddd;
}

.play-info {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 2px;
}

.duration {
  font-size: 14px;
  font-weight: 600;
  color: #1a1a1a;
}

.date {
  font-size: 13px;
  color: #999;
}

.play-button-row {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 16px;
  padding: 32px 0;
}

.play-button {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  border: none;
  color: #fff;
  font-size: 24px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(47, 5, 56, 0.3);
}

.play-button:hover {
  transform: scale(1.1);
  box-shadow: 0 6px 20px rgba(47, 5, 56, 0.4);
}

.play-icon,
.pause-icon {
  margin-left: 3px;
}

.play-label {
  font-size: 16px;
  font-weight: 600;
  color: #2f0538;
}

.podcast-content {
  padding: 32px 0;
}

.content-grid {
  display: grid;
  grid-template-columns: 1fr 360px;
  gap: 48px;
}

@media (max-width: 1100px) {
  .content-grid {
    grid-template-columns: 1fr;
  }
  
  .sidebar {
    order: -1;
  }
}

@media (max-width: 680px) {
  .podcast-meta-bar {
    flex-direction: column;
    align-items: flex-start;
    gap: 16px;
  }
  
  .play-info {
    align-items: flex-start;
  }
}
</style>
