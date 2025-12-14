<template>
  <div class="videos-grid" v-if="videos.length">
    <article v-for="(video, i) in videos" :key="i" class="video-card">
      <a :href="video.link" target="_blank" rel="noopener" class="video-thumbnail">
        <div class="video-placeholder-small">
          <span class="play-icon-small">▶</span>
        </div>
        <div class="video-overlay"></div>
      </a>
      <div class="video-content">
        <span class="video-source">{{ video.source }}</span>
        <h3 class="video-title">
          <a :href="video.link" target="_blank" rel="noopener">{{ video.title }}</a>
        </h3>
        <p class="video-description">{{ video.description }}</p>
        <time class="video-time">{{ video.date }}</time>
      </div>
    </article>
  </div>
</template>

<script setup lang="ts">
interface VideoItem { id:number; title:string; description:string; source:string; date:string; link:string }
const props = defineProps<{ videos: VideoItem[] }>();
</script>

<style scoped>
.videos-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:24px; }
.video-card { background:#fff; border-radius:10px; overflow:hidden; box-shadow:0 2px 8px rgba(0,0,0,.06); transition:all .3s ease; cursor:pointer; }
.video-card:hover { transform: translateY(-6px); box-shadow:0 8px 24px rgba(0,0,0,.12); }
.video-thumbnail { display:block; position:relative; text-decoration:none; }
.video-placeholder-small { width:100%; aspect-ratio:16/9; background: linear-gradient(135deg, #2f0538, #4b2faa); display:flex; align-items:center; justify-content:center; transition:all .3s ease; }
.play-icon-small { font-size:42px; color:rgba(255,255,255,.7); transition:all .3s ease; }
.video-card:hover .play-icon-small { font-size:48px; color:#fff; }
.video-overlay { position:absolute; inset:0; background:rgba(0,0,0,0); transition:background .3s ease; }
.video-card:hover .video-overlay { background:rgba(0,0,0,.1); }
.video-content { padding:20px; display:flex; flex-direction:column; gap:10px; }
.video-source { color:#7b5ce0; font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:.5px; }
.video-title { margin:0; font-size:16px; font-weight:700; line-height:1.4; color:#1a1a1a; }
.video-title a { color:inherit; text-decoration:none; transition:color .2s ease; }
.video-title a:hover { color:#7b5ce0; }
.video-description { margin:0; font-size:13px; line-height:1.5; color:#666; }
.video-time { font-size:12px; color:#999; }
@media (max-width: 1100px){ .videos-grid{ grid-template-columns:repeat(2,1fr) } }
@media (max-width: 680px){ .videos-grid{ grid-template-columns:1fr } }
</style>
