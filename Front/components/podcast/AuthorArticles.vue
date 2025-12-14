<template>
  <div class="sidebar-box articles-box">
    <h3 class="sidebar-title">Articles des animateurs</h3>
    <div class="author-articles">
      <div v-for="author in authors" :key="author.title" class="author-section">
        <span class="author-name">{{ author.author }}</span>
        <a :href="author.link" class="article-link">{{ author.title }}</a>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface AuthorArticle { author: string; title: string; link: string }
const props = defineProps<{ authors: AuthorArticle[] }>();
</script>

<style scoped>
.sidebar-box { background: #f9f9f9; padding: 24px; border-radius: 12px; border: 1px solid #f0f0f0; }
.sidebar-title { font-size: 16px; font-weight: 700; color: #1a1a1a; margin: 0 0 12px; }
.author-articles { display: flex; flex-direction: column; gap: 16px; }
.author-section { padding: 12px; background: #fff; border-radius: 6px; border: 1px solid #e5e5e5; }
.author-name { font-size: 11px; font-weight: 700; color: #7b5ce0; text-transform: uppercase; display: block; margin-bottom: 6px; }
.article-link { color: #1a1a1a; text-decoration: none; font-size: 13px; font-weight: 600; line-height: 1.4; transition: all 0.22s ease; display: block; }
.article-link:hover { color: #7b5ce0; }
</style>
