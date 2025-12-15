<template>
  <main class="featured-article-page">
    <PageHero
      title="La guerre de l'information"
      subtitle="Stratégies d'influence et perceptions du conflit Ukraine-Russie"
      badge="Article en vedette"
      badge-icon="📰"
    />

    <div class="article-wrapper">
      <div class="article-meta-bar">
        <div class="author-info">
          <span class="author-avatar">AT</span>
          <div class="author-details">
            <span class="author-name">Antoine TENA</span>
            <span class="publish-date">14 décembre 2025</span>
          </div>
        </div>
        <div class="reading-time">
          <span class="icon">⏱️</span>
          <span>12 min de lecture</span>
        </div>
      </div>

      <section class="article-image-section">
        <img src="@/assets/logoIsoc.png" alt="Guerre de l'information" class="featured-image" />
      </section>

      <article class="article-content">
        <div class="content-container">
          <TableOfContents />

          <div class="main-content">
            <ArticleSection id="introduction">
              <template #title>Introduction</template>
              <p>
                Le conflit Ukraine-Russie ne se joue pas uniquement sur le terrain militaire. Une bataille informationnelle tout aussi cruciale se déploie sur les réseaux sociaux, les médias traditionnels et les plateformes numériques.
              </p>
              <p>
                Cet article explore comment les acteurs du conflit utilisent les technologies modernes pour contrôler le récit et influencer l'opinion publique.
              </p>
            </ArticleSection>

            <ArticleSection id="strategies">
              <template #title>Stratégies d'influence et campagnes informationnelles</template>
              <ul>
                <li><strong>Amplification de narratifs</strong> — Promotion sélective de certains récits pour orienter la perception publique</li>
                <li><strong>Astroturfing</strong> — Création de mouvements artificiels pour simuler un soutien populaire</li>
                <li><strong>Désinformation coordonnée</strong> — Diffusion synchronisée de fausses informations à travers multiples canaux</li>
                <li><strong>Contournement de modération</strong> — Techniques pour échapper aux systèmes de détection automatique</li>
              </ul>
            </ArticleSection>

            <ArticleSection id="social-media">
              <template #title>Rôle des réseaux sociaux : Telegram, X et autres</template>
              <p>
                Les plateformes de réseaux sociaux jouent un rôle central dans la diffusion et la manipulation des perceptions du conflit. Telegram, X (anciennement Twitter), Facebook et d'autres plateformes servent de vecteurs principaux pour la propagation d'informations, qu'elles soient vérifiées ou non.
              </p>
              <p>
                Ces plateformes permettent une diffusion rapide et massive, mais aussi une fragmentation de l'information qui rend difficile la distinction entre sources fiables et désinformation.
              </p>
            </ArticleSection>

            <ArticleSection id="deepfakes">
              <template #title>Deepfakes et technologie de désinformation</template>
              <p>
                Les deepfakes représentent une menace émergente dans la guerre informationnelle. Ces vidéos et audios manipulés par intelligence artificielle peuvent créer des contenus hyperréalistes difficiles à distinguer de la réalité.
              </p>
              <p>
                Dans le contexte du conflit Ukraine-Russie, les deepfakes ont été utilisés pour créer de fausses déclarations de dirigeants, simuler des événements qui ne se sont jamais produits, et semer la confusion dans le public.
              </p>
            </ArticleSection>

            <ArticleSection id="osint">
              <template #title>OSINT, Fact-checking et lutte contre la désinformation</template>
              <p>
                L'OSINT (Open Source Intelligence) et le fact-checking jouent un rôle crucial dans la lutte contre la désinformation. Des organisations indépendantes et des journalistes utilisent des outils d'analyse open-source pour vérifier les informations circulant sur le conflit.
              </p>
              <p>
                Ces techniques permettent de géolocaliser des vidéos, vérifier l'authenticité d'images, et croiser des sources pour établir les faits avec précision.
              </p>
            </ArticleSection>

            <ArticleSection id="impact">
              <template #title>Impact sur les perceptions et l'opinion publique</template>
              <p>
                La guerre informationnelle impacte directement la perception du conflit par le public mondial. Les campagnes de désinformation réussissent souvent à polariser les opinions, créer de la confusion, et éroder la confiance dans les institutions médiatiques traditionnelles.
              </p>
              <p>
                Cette manipulation de l'opinion publique a des conséquences réelles sur le soutien politique, les décisions diplomatiques, et même sur les actions militaires menées par les différents acteurs du conflit.
              </p>
            </ArticleSection>

            <ArticleSection id="conclusion">
              <template #title>Conclusion</template>
              <p>
                La guerre de l'information est devenue un élément indissociable des conflits modernes. Dans le cas de l'Ukraine-Russie, elle illustre comment les technologies numériques peuvent être utilisées comme armes de guerre psychologique.
              </p>
              <p>
                Une approche critique et vérifiée de l'information est essentielle pour naviguer ce paysage informatif complexe et éviter d'être manipulé par les différentes forces en présence.
              </p>
            </ArticleSection>

            <RelatedGrid />
          </div>
        </div>
      </article>
    </div>
  </main>
</template>

<script setup lang="ts">
import PageHero from '~/components/shared/PageHero.vue'
import TableOfContents from './TableOfContents.vue'
import ArticleSection from './sections/ArticleSection.vue'
import RelatedGrid from './RelatedGrid.vue'
</script>

<style scoped>
.featured-article-page {
  min-height: 100vh;
  background: #ffffff;
  padding-bottom: 60px;
}

.article-wrapper {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 calc(2vw);
}

.article-meta-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 32px 0 24px;
  border-bottom: 1px solid #f0f0f0;
  max-width: 900px;
  margin: 0 auto;
}

.author-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.author-avatar {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #ff6b6b 0%, #ff8e53 100%);
  color: #fff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 16px;
}

.author-details {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.author-name {
  font-weight: 600;
  font-size: 14px;
  color: #1a1a1a;
}

.publish-date {
  font-size: 13px;
  color: #999;
}

.reading-time {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 14px;
  color: #666;
}

.icon {
  font-size: 18px;
}

.article-image-section {
  display: flex;
  justify-content: center;
  margin: 40px 0;
}

.featured-image {
  max-width: 280px;
  filter: drop-shadow(0 4px 16px rgba(47, 5, 56, 0.15));
  transition: transform 0.3s ease;
}

.featured-image:hover {
  transform: scale(1.05);
}

.article-content {
  max-width: 1200px;
  margin: 0 auto;
}

.content-container {
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: 48px;
  align-items: start;
}

.main-content {
  min-width: 0;
  max-width: 800px;
}

@media (max-width: 968px) {
  .content-container {
    grid-template-columns: 1fr;
    gap: 0;
  }
  
  .article-image-section {
    margin: 24px 0;
  }
  
  .featured-image {
    max-width: 200px;
  }
  
  .article-meta-bar {
    flex-direction: column;
    align-items: flex-start;
    gap: 16px;
  }
}
</style>
