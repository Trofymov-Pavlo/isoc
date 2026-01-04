<template>
  <main class="liked-page">
    <!-- Login prompt if not authenticated -->
    <div v-if="!isAuthenticated" class="auth-prompt">
      <div class="auth-card">
        <svg class="auth-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
          <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
          <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
        </svg>
        <h2>Connectez-vous pour accéder à vos favoris</h2>
        <p>Créez un compte ou connectez-vous pour sauvegarder et organiser vos articles préférés.</p>
        <NuxtLink to="/connexion" class="auth-btn">Se connecter</NuxtLink>
      </div>
    </div>

    <section v-else class="liked-wrapper">
      <!-- Header -->
      <div class="liked-header">
        <h1>Mes favoris</h1>
        <p class="count">{{ likedItems.length }} article{{ likedItems.length > 1 ? 's' : '' }}</p>
      </div>

      <!-- Loading state -->
      <div v-if="loading" class="loading-state">Chargement de vos favoris…</div>

      <!-- Content -->
      <div v-else-if="likedItems.length > 0" class="liked-content">
        <LiveArticlesGrid :articles="displayedItems" />
      </div>

      <!-- Empty state -->
      <div v-else class="empty-state">
        <span class="empty-icon">❤️</span>
        <p class="empty-text">Aucun article dans vos favoris.</p>
        <p class="empty-hint">Commencez à liker des articles pour les retrouver ici !</p>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { useAuthState } from '~/composables/useAuthState';
import LiveArticlesGrid from '~/components/in-live/LiveArticlesGrid.vue';
import { useSavedMedia } from '~/composables/useSavedMedia';

const { isAuthenticated } = useAuthState();
const { 
  likedItems, 
  loading,
  getSavedItems,
  initialize
} = useSavedMedia();

const archiveByLink = ref<Record<string, { image?: string; published?: string }>>({});

const formatSavedDate = (dateString: string): string => {
  try {
    const date = new Date(dateString);
    if (Number.isNaN(date.getTime())) return dateString;
    return date.toLocaleDateString('fr-FR', { day: 'numeric', month: 'short', year: 'numeric' });
  } catch {
    return dateString;
  }
};
const displayedItems = computed(() => {
  return likedItems.value.map(item => ({
    link: item.link,
    title: item.title,
    source: item.source,
    image: item.thumbnail || archiveByLink.value[item.link]?.image,
    summary: '',
    type: item.media_type === 'article' || item.media_type === 'live' ? 'article' : 'video',
    published: item.published_date || archiveByLink.value[item.link]?.published || item.saved_at,
  }));
});

const loadArchiveIndex = async () => {
  try {
    const res = await fetch('/archive.json');
    if (!res.ok) return;
    const data = await res.json();

    const rawArticles: any[] = Array.isArray(data) ? data : (data?.articles ?? []);
    const rawVideos: any[] = Array.isArray(data) ? [] : (data?.videos ?? []);

    const idx: Record<string, { image?: string; published?: string }> = {};

    for (const a of rawArticles) {
      const link = (a?.link || a?.url || '').toString();
      if (!link) continue;
      const image = (a?.image || a?.img || a?.thumbnail || a?.thumb || a?.og_image || a?.picture || a?.cover) as string | undefined;
      const published = (a?.published || a?.pubDate || a?.date || a?.updated || a?.published_at) as string | undefined;
      if (image || published) idx[link] = { image, published };
    }

    for (const v of rawVideos) {
      const link = (v?.link || '').toString();
      if (!link) continue;
      const image = (v?.thumbnail || v?.image) as string | undefined;
      const published = (v?.published || v?.date || v?.publishedAt) as string | undefined;
      if (image || published) idx[link] = { image, published };
    }

    archiveByLink.value = idx;
  } catch {
    // ignore
  }
};

onMounted(async () => {
  await initialize();
  await getSavedItems();
  await loadArchiveIndex();
});

</script>

<style scoped>
.liked-page {
  min-height: 100vh;
  background: #fff;
}

.auth-prompt {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 24px;
  background: #fff;
}

.auth-card {
  background: white;
  border-radius: 16px;
  padding: 48px;
  max-width: 500px;
  text-align: center;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
}

.auth-icon {
  width: 64px;
  height: 64px;
  margin: 0 auto 24px;
  color: #7b5ce0;
}

.auth-card h2 {
  margin: 0 0 16px;
  font-size: 28px;
  font-weight: 700;
  color: #1a1a1a;
}

.auth-card p {
  margin: 0 0 32px;
  font-size: 16px;
  color: #666;
  line-height: 1.6;
}

.auth-btn {
  display: inline-block;
  padding: 12px 32px;
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  color: white;
  border-radius: 10px;
  text-decoration: none;
  font-weight: 600;
  font-size: 14px;
  transition: all 0.2s ease;
}

.auth-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(47, 5, 56, 0.3);
}

.liked-wrapper {
  max-width: 1400px;
  margin: 0 auto;
  padding: 48px calc(2vw) 60px;
}

.liked-header {
  margin-bottom: 40px;
}

.liked-header h1 {
  margin: 0 0 8px;
  font-size: 32px;
  font-weight: 700;
  color: #1a1a1a;
}

.liked-header .count {
  margin: 0;
  font-size: 14px;
  color: #999;
}

.liked-content {
  margin-bottom: 60px;
}

.loading-state {
  text-align: center;
  padding: 60px 20px;
  color: #666;
  font-size: 16px;
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

  .liked-header h1 {
    font-size: 24px;
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
