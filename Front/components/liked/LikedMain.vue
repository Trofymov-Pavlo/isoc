<template>
  <main class="liked-page">
    <PageHero
      title="Articles likés"
      subtitle="Retrouvez tous les articles que vous avez sauvegardés"
      badge="Mes favoris"
      badge-icon="❤️"
    />

    <section class="liked-wrapper">
      <div class="liked-content" v-if="displayedItems.length">
        <LiveArticlesGrid :articles="displayedItems" />
      </div>
      <div class="empty-state" v-else>
        <span class="empty-icon">📌</span>
        <p class="empty-text">Aucun article liké pour le moment.</p>
        <p class="empty-hint">Commencez à liker des articles pour les retrouver ici !</p>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
import { computed, onMounted } from 'vue';
import PageHero from '~/components/shared/PageHero.vue';
import LiveArticlesGrid from '~/components/in-live/LiveArticlesGrid.vue';
import { useLiked } from '~/composables/useLiked';
import { useArticles } from '~/composables/useArticles';
import { useVideos } from '~/composables/useVideos';

const { likedItems, loadLiked } = useLiked();
const { all: articles, load: loadArticles } = useArticles({ hours: 0 });
const { videos, fetchVideos } = useVideos();

const displayedItems = computed(() => {
  const allItems = [
    ...articles.value.map(a => ({ ...a, type: 'article' })),
    ...videos.value.map(v => ({ ...v, type: 'video', source: v.channel, title: v.title, link: v.link, image: v.thumbnail, published: v.published })),
  ];
  return allItems.filter(item => likedItems.value.has(item.link));
});

onMounted(() => {
  loadLiked();
  loadArticles();
  fetchVideos({ hours: 0, limit: 1000 });
});
</script>

<style scoped>
.liked-page {
  min-height: 100vh;
  background: #fff;
}

.liked-wrapper {
  max-width: 1400px;
  margin: 0 auto;
  padding: 48px calc(2vw) 60px;
}

.liked-content {
  margin-bottom: 60px;
}

.empty-state {
  text-align: center;
  padding: 80px 20px;
}

.empty-icon {
  font-size: 64px;
  display: block;
  margin-bottom: 16px;
  opacity: 0.5;
}

.empty-text {
  font-size: 18px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0 0 8px;
}

.empty-hint {
  font-size: 16px;
  color: #999;
  margin: 0;
}

@media (max-width: 768px) {
  .liked-wrapper {
    padding: 32px calc(2vw) 40px;
  }

  .empty-state {
    padding: 60px 20px;
  }

  .empty-text {
    font-size: 16px;
  }

  .empty-hint {
    font-size: 14px;
  }
}
</style>

