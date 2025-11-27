<template>
  <div class="article-page">
    <article class="article-container">
      <header class="article-header">
        <h1 class="article-title">{{ article.title }}</h1>
        <div class="article-meta">
          <span class="author">Par {{ article.author }}</span>
          <span class="date">{{ article.date }}</span>
          <span class="location">{{ article.location }}</span>
        </div>
      </header>

      <img :src="article.image" alt="" class="article-hero" />

      <div class="article-body">
        <p class="lead-text">{{ article.excerpt }}</p>
        
        <div v-html="article.content" class="article-text"></div>
      </div>

      <footer class="article-footer">
        <div class="share">Partager cet article</div>
      </footer>
    </article>
  </div>
</template>

<script setup>
const article = {
  id: 1,
  title: "Titre principal — Crise et perspectives",
  excerpt: "Un aperçu approfondi des événements marquants du jour, analysés par la rédaction.",
  author: "Jean Dupont",
  date: "27 novembre 2025 à 14h45",
  location: "Paris",
  image: "https://cdn.pixabay.com/photo/2020/02/12/05/16/dog-cartoon-4841703_1280.jpg",
  content: "<p>test1</p>"
}
</script>

<style scoped>
.article-page { display:grid; /* left gap | main column | sidebar */ grid-template-columns: 800px; gap:28px; max-width:1280px; margin:0 auto; padding:20px }

.article-container { background:var(--paper); padding:24px; width:100% }

.article-header { margin-bottom:24px }
.article-title { font-family: 'Merriweather', Georgia, serif; font-size:44px; line-height:1.15; margin:0 0 12px 0 }
.article-meta { display:flex; gap:16px; color:var(--muted); font-size:13px; flex-wrap:wrap }
.article-meta span { display:flex; align-items:center }
.article-meta span::after { content:"•"; margin-left:16px }
.article-meta span:last-child::after { content:"" }

.article-hero { width:750px; height:400px; margin:24px 0; display:block }

.article-body { line-height:1.7 }
.lead-text { font-size:18px; font-weight:600; color:#222; margin-bottom:16px }

.article-text { color:#333 }
.article-text p { margin-bottom:16px }
.article-text p:first-letter { font-weight:600 }

.article-footer { margin-top:32px; padding-top:16px; border-top:1px solid var(--rule) }
.share { color:var(--muted); font-size:13px }

.article-sidebar { padding:24px 0 }
.sidebar-box { background:var(--paper); padding:14px; border:1px solid var(--rule) }
.sidebar-box h3 { margin:0 0 12px 0 }
.sidebar-box ul { list-style:none; padding:0; margin:0 }
.sidebar-box li { margin-bottom:8px }
.sidebar-box a { color:#0b6b88; text-decoration:none; font-size:14px }
.sidebar-box a:hover { text-decoration:underline }

@media (max-width: 768px) {
  .article-page { grid-template-columns: 1fr; gap:16px }
  .article-title { font-size:28px }
}
</style>
