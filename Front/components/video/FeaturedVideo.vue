<template>
  <article class="featured-article" v-if="video">
    <div class="featured-image video-player">
      <div class="video-placeholder">
        <span class="play-icon">▶</span>
      </div>
      <div class="featured-overlay"></div>
    </div>

    <div class="featured-content">
      <p v-if="video.source" class="featured-source">{{ video.source }}</p>
      <h2 class="featured-title">
        <a :href="video.link" target="_blank" rel="noopener">{{ video.title }}</a>
      </h2>
      <p v-if="video.description" class="featured-summary">
        {{ video.description }}
      </p>
      <div class="featured-footer">
        <time v-if="video.date" class="featured-time">
          {{ video.date }}
        </time>
        <a :href="video.link" target="_blank" rel="noopener" class="read-link">
          Regarder la vidéo →
        </a>
      </div>
    </div>
  </article>
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

const props = defineProps<{ video: VideoItem }>();
</script>

<style scoped>
.featured-article {
  background: #ffffff;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid #e5e5e5;
  margin-bottom: 48px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
}

.featured-article:hover {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  border-color: #d0d0d0;
}

.featured-image {
  position: relative;
  width: 100%;
  height: 400px;
  overflow: hidden;
  background: #f5f5f5;
  display: block;
}

.featured-image.video-player {
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  display: flex;
  align-items: center;
  justify-content: center;
}

.video-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.play-icon {
  font-size: 72px;
  color: rgba(255, 255, 255, 0.8);
  transition: all 0.3s ease;
}

.video-placeholder:hover .play-icon {
  color: #fff;
  transform: scale(1.2);
}

.featured-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to right, rgba(0, 0, 0, 0.1), transparent);
  pointer-events: none;
}

.featured-content {
  padding: 40px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  justify-content: center;
}

.featured-source {
  margin: 0;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.6px;
  color: #ff6b6b;
}

.featured-title {
  margin: 0;
  font-size: 32px;
  font-weight: 700;
  line-height: 1.2;
  color: #1a1a1a;
}

.featured-title a {
  color: inherit;
  text-decoration: none;
  transition: color 0.2s ease;
}

.featured-title a:hover {
  color: #2f0538;
}

.featured-summary {
  margin: 0;
  font-size: 16px;
  line-height: 1.6;
  color: #555;
}

.featured-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding-top: 8px;
  border-top: 1px solid #f0f0f0;
}

.featured-time {
  font-size: 13px;
  color: #999;
  font-weight: 500;
}

.read-link {
  color: #2f0538;
  text-decoration: none;
  font-weight: 600;
  font-size: 14px;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 4px;
}

.read-link:hover {
  color: #ff6b6b;
  gap: 8px;
}

@media (max-width: 1100px) {
  .featured-article {
    grid-template-columns: 1fr;
  }
  
  .featured-image {
    height: 300px;
  }
}

@media (max-width: 680px) {
  .featured-title {
    font-size: 24px;
  }
  
  .featured-content {
    padding: 24px;
  }
  
  .featured-footer {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }
}
</style>
