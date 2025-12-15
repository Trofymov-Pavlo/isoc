<template>
  <div class="articles-grid" v-if="videos.length">
    <article
      v-for="(video, i) in videos"
      :key="video.id || i"
      class="article-card"
    >
      <a
        :href="video.link"
        target="_blank"
        rel="noopener"
        class="article-image video-thumbnail"
      >
        <div class="video-placeholder-small">
          <span class="play-icon-small">▶</span>
        </div>
        <div class="image-overlay"></div>
      </a>

      <div class="article-content">
        <p v-if="video.source" class="article-source">{{ video.source }}</p>
        <h2 class="article-title">
          <a :href="video.link" target="_blank" rel="noopener">{{ video.title }}</a>
        </h2>
        <p v-if="video.description" class="article-summary">
          {{ truncate(video.description, 120) }}
        </p>
        <div class="article-footer">
          <time v-if="video.date" class="article-time">
            {{ video.date }}
          </time>
          <a :href="video.link" target="_blank" rel="noopener" class="read-link">
            Regarder →
          </a>
        </div>
      </div>
    </article>
  </div>
</template>

<script setup lang="ts">
interface VideoItem { 
  id: number; 
  title: string; 
  description: string; 
  source: string; 
  date: string; 
  link: string;
}

const props = defineProps<{ videos: VideoItem[] }>();

const truncate = (text: string, max: number): string => {
  if (!text) return '';
  if (text.length <= max) return text;
  return text.substring(0, max).trim() + '...';
};
</script>

<style scoped>
.articles-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.article-card {
  background: #ffffff;
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid #e5e5e5;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
}

.article-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  border-color: #d0d0d0;
}

.article-image {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 9;
  overflow: hidden;
  background: #f5f5f5;
  display: block;
}

.article-image.video-thumbnail {
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
}

.video-placeholder-small {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.play-icon-small {
  font-size: 42px;
  color: rgba(255, 255, 255, 0.7);
  transition: all 0.3s ease;
}

.article-card:hover .play-icon-small {
  font-size: 48px;
  color: #fff;
}

.image-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.1), transparent);
  pointer-events: none;
}

.article-content {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  flex: 1;
}

.article-source {
  margin: 0;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: #ff6b6b;
}

.article-title {
  margin: 0;
  font-size: 16px;
  font-weight: 700;
  line-height: 1.4;
  color: #1a1a1a;
}

.article-title a {
  color: inherit;
  text-decoration: none;
  transition: color 0.2s ease;
}

.article-title a:hover {
  color: #2f0538;
}

.article-summary {
  margin: 0;
  font-size: 13px;
  line-height: 1.5;
  color: #666;
}

.article-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding-top: 8px;
  margin-top: auto;
  border-top: 1px solid #f0f0f0;
}

.article-time {
  font-size: 12px;
  color: #999;
  font-weight: 500;
}

.read-link {
  color: #2f0538;
  text-decoration: none;
  font-weight: 600;
  font-size: 13px;
  transition: all 0.2s ease;
}

.read-link:hover {
  color: #ff6b6b;
}

@media (max-width: 1100px) {
  .articles-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 680px) {
  .articles-grid {
    grid-template-columns: 1fr;
  }
}
</style>
