<template>
  <article class="featured-video">
    <div class="featured-video-player">
      <div class="video-placeholder">
        <span class="play-icon">▶</span>
      </div>
    </div>
    <div class="featured-content">
      <span class="featured-source">{{ video.source }}</span>
      <h2 class="featured-title">{{ video.title }}</h2>
      <p class="featured-summary">{{ video.description }}</p>
      <div class="featured-footer">
        <time class="featured-time">{{ video.date }}</time>
        <a :href="video.link" target="_blank" rel="noopener" class="watch-link">▶ Regarder la vidéo</a>
      </div>
    </div>
  </article>
</template>

<script setup lang="ts">
interface VideoItem { id:number; title:string; description:string; source:string; date:string; link:string }
const props = defineProps<{ video: VideoItem }>();
</script>

<style scoped>
.featured-video { background:#fff; border-radius:12px; overflow:hidden; box-shadow:0 4px 16px rgba(0,0,0,0.08); margin-bottom:48px; display:grid; grid-template-columns:1.5fr 1fr; gap:32px; }
.featured-video-player { position:relative; aspect-ratio:16/9; background: linear-gradient(135deg, #2f0538, #4b2faa); }
.video-placeholder { width:100%; height:100%; display:flex; align-items:center; justify-content:center; cursor:pointer; transition:all .3s ease; }
.play-icon { font-size:72px; color:rgba(255,255,255,.8); transition:all .3s ease; }
.video-placeholder:hover .play-icon { color:#fff; font-size:84px; }
.featured-content { padding:32px 32px 32px 0; display:flex; flex-direction:column; gap:16px; justify-content:center; }
.featured-source { color:#7b5ce0; font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:.8px; }
.featured-title { margin:0; font-size:28px; font-weight:700; line-height:1.3; color:#1a1a1a; }
.featured-summary { margin:0; font-size:15px; line-height:1.6; color:#555; }
.featured-footer { display:flex; align-items:center; justify-content:space-between; gap:16px; margin-top:8px; }
.featured-time { font-size:13px; color:#999; }
.watch-link { display:inline-flex; align-items:center; gap:8px; color:#7b5ce0; text-decoration:none; font-weight:600; font-size:14px; transition:all .3s ease; }
.watch-link:hover { color:#2f0538; gap:12px; }
@media (max-width: 1100px){ .featured-video{ grid-template-columns:1fr } .featured-content{ padding:0 32px 32px } }
@media (max-width: 680px){ .featured-title{ font-size:22px } }
</style>
