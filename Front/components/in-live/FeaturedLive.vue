<template>
  <article class="featured-article" v-if="article">
    <a
      v-if="article.image"
      :href="article.link"
      target="_blank"
      rel="noopener"
      class="featured-image"
      :class="{ 'video-thumbnail': article.type === 'video' }"
    >
      <img :src="article.image" :alt="article.title" loading="lazy" />
      <div v-if="article.type === 'video'" class="video-overlay">
        <span class="play-icon">▶</span>
      </div>
      <div class="featured-overlay"></div>
      <LikeButton
        :link="article.link"
        :title="article.title"
        :source="article.source || 'En direct'"
        :media-type="article.type === 'video' ? 'video' : 'article'"
        :thumbnail="article.image"
        :published-date="article.published"
      />
    </a>
    <div v-else class="featured-image placeholder">
      <span class="placeholder-icon">📰</span>
      <LikeButton
        :link="article.link"
        :title="article.title"
        :source="article.source || 'En direct'"
        :media-type="article.type === 'video' ? 'video' : 'article'"
        :thumbnail="article.image"
        :published-date="article.published"
      />
    </div>

    <div class="featured-content">
      <p v-if="article.source" class="featured-source">{{ article.source }}</p>
      <h2 class="featured-title">
        <a :href="article.link" target="_blank" rel="noopener">{{ article.title }}</a>
      </h2>
      <p v-if="article.summary" class="featured-summary">
        {{ article.summary }}
      </p>
      <div class="featured-footer">
        <time v-if="article.published" class="featured-time">
          {{ formatTime(article.published) }}
        </time>
        <div class="footer-actions">
          <a :href="article.link" target="_blank" rel="noopener" class="read-link">
            Lire l'article complet →
          </a>
        </div>
      </div>
    </div>
  </article>
</template>

<script setup lang="ts">
import LikeButton from '~/components/shared/LikeButton.vue';

interface Article {
  title: string;
  link: string;
  summary?: string;
  image?: string;
  source?: string;
  published?: string;
  type?: 'article' | 'video';
}

const props = defineProps<{ article: Article }>();

const formatTime = (dateString?: string): string => {
  if (!dateString) return '';

  try {
    if (/jan|fév|mar|avr|mai|jui|aoû|sep|oct|nov|déc/i.test(dateString)) {
      return dateString;
    }

    const date = new Date(dateString);
    if (isNaN(date.getTime())) return dateString;

    return date.toLocaleDateString('fr-FR', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
    });
  } catch {
    return dateString;
  }
};

// TODO(liked-vertical-bar): Consider adding a persistent vertical action bar
// on heart-click (heart, watch later, categories, plus) to match requested UX.
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
  height: 720px;
  overflow: hidden;
  background: #f5f5f5;
  display: block;
}

.featured-image.video-thumbnail .video-overlay {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(47, 5, 56, 0.3);
  transition: all 0.3s ease;
}

.featured-article:hover .video-overlay {
  background: rgba(47, 5, 56, 0.4);
}

.play-icon {
  font-size: 64px;
  color: rgba(255, 255, 255, 0.9);
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  transition: all 0.3s ease;
}

.featured-article:hover .play-icon {
  font-size: 72px;
  color: #fff;
}

.featured-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.featured-article:hover .featured-image img {
  transform: scale(1.05);
}

.featured-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to right, rgba(0, 0, 0, 0.1), transparent);
  pointer-events: none;
}

.featured-image.placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #f5f5f5 0%, #fafafa 100%);
}

.featured-content {
  padding: 40px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  justify-content: center;
}

.featured-meta {
  display: flex;
  align-items: center;
  gap: 12px;
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
  line-height: 1.3;
  color: #1a1a1a;
}

.featured-title a {
  color: inherit;
  text-decoration: none;
  transition: color 0.22s ease;
}

.featured-title a:hover {
  color: #7b5ce0;
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
  margin-top: 8px;
  padding-top: 16px;
  border-top: 1px solid #f0f0f0;
}

.footer-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.featured-time {
  font-size: 13px;
  color: #999;
  font-weight: 500;
}

.read-link {
  font-size: 13px;
  font-weight: 600;
  color: #7b5ce0;
  text-decoration: none;
  transition: all 0.22s ease;
  padding: 4px 8px;
  border-radius: 4px;
}

.read-link:hover {
  background: rgba(123, 92, 224, 0.1);
  color: #6a4dc7;
}

@media (max-width: 1100px) {
  .featured-article {
    grid-template-columns: 1fr;
  }

  .featured-image {
    height: 340px;
  }
}

@media (max-width: 680px) {
  .featured-article {
    grid-template-columns: 1fr;
    margin-bottom: 32px;
  }

  .featured-image {
    height: 280px;
  }

  .featured-content {
    padding: 24px;
    gap: 12px;
  }

  .featured-title {
    font-size: 24px;
  }

  .featured-summary {
    font-size: 14px;
  }
}
</style>
