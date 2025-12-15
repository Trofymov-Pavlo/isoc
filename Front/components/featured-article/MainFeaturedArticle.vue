<template>
  <main class="featured-article-page">
    <ArticleHero />

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
              <li><strong>Amplification de narratifs</strong> — Promotion sélective</li>
              <li><strong>Astroturfing</strong> — Mouvements artificiels</li>
              <li><strong>Désinformation coordonnée</strong></li>
              <li><strong>Contournement de modération</strong></li>
            </ul>
          </ArticleSection>

          <ArticleSection id="social-media">
            <template #title>Rôle des réseaux sociaux : Telegram, X et autres</template>
            <p>Les plateformes jouent un rôle central dans la diffusion et la manipulation des perceptions.</p>
          </ArticleSection>

          <ArticleSection id="deepfakes">
            <template #title>Deepfakes et technologie de désinformation</template>
            <p>Les deepfakes représentent une menace émergente dans la guerre informationnelle.</p>
          </ArticleSection>

          <ArticleSection id="osint">
            <template #title>OSINT, Fact-checking et lutte contre la désinformation</template>
            <p>L'OSINT et le fact-checking jouent un rôle crucial.</p>
          </ArticleSection>

          <ArticleSection id="impact">
            <template #title>Impact sur les perceptions et l'opinion publique</template>
            <p>La guerre informationnelle impacte directement la perception du conflit par le public.</p>
          </ArticleSection>

          <ArticleSection id="conclusion">
            <template #title>Conclusion</template>
            <p>Une approche critique et vérifiée est essentielle pour naviguer ce paysage informatif.</p>
          </ArticleSection>

          <RelatedGrid />
        </div>
      </div>
    </article>
  </main>
</template>

<script setup lang="ts">
import ArticleHero from './ArticleHero.vue'
import TableOfContents from './TableOfContents.vue'
import ArticleSection from './sections/ArticleSection.vue'
import RelatedGrid from './RelatedGrid.vue'
</script>

<style scoped>
.featured-article-page {
  max-width: 1100px;
  margin: 2rem auto;
  padding: 1rem;
  background: #ffffff;
}
.article-image-section { display: flex; justify-content: center; margin: 1rem 0; }
.featured-image { max-width: 240px; filter: drop-shadow(0 4px 12px rgba(0,0,0,0.08)); }
.content-container { display: grid; grid-template-columns: 280px 1fr; gap: 2rem; }
.main-content { min-width: 0; }

/* Harmonize with site visuals */
.section-title { font-size: 22px; color: #2f0538; margin: 0 0 12px; }
article p { color: #4a4a55; line-height: 1.6; }
ul { padding-left: 18px; }
</style>
