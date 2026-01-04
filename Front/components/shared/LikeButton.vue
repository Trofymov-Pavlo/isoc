<template>
  <button
    v-if="isAuthenticated"
    class="like-btn"
    :class="{ liked: isLiked }"
    @click.prevent.stop="onClick"
    :title="isLiked ? 'Retirer des favoris' : 'Ajouter aux favoris'"
    :aria-pressed="isLiked"
    :disabled="isLoading"
  >
    <svg class="icon" viewBox="0 0 24 24" :fill="isLiked ? 'currentColor' : 'none'" stroke="currentColor" stroke-width="2">
      <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
    </svg>
  </button>
</template>

<script setup lang="ts">
import { ref, computed, watch, onMounted } from 'vue';
import { useAuthState } from '~/composables/useAuthState';
import { useSavedMedia } from '~/composables/useSavedMedia';

interface Props {
  link: string;
  title?: string;
  source?: string;
  mediaType: 'article' | 'video' | 'live';
  thumbnail?: string;
  publishedDate?: string;
}

const props = withDefaults(defineProps<Props>(), {
  source: 'AXIOM',
});

const { isAuthenticated } = useAuthState();
const { toggleSave, isSaved, initialize, isInitialized } = useSavedMedia();

const isLoading = ref(false);

// Initialize when user is authenticated
watch(
  () => isAuthenticated.value,
  async (authed) => {
    if (authed && !isInitialized.value) {
      await initialize();
    }
  },
  { immediate: true }
);

// Check if item is saved using the global cache
const isLiked = computed(() => {
  if (!isAuthenticated.value) return false;
  return isSaved(props.link);
});

const onClick = async () => {
  if (!isAuthenticated.value) {
    navigateTo('/connexion');
    return;
  }

  isLoading.value = true;
  try {
    await toggleSave({
      link: props.link,
      title: props.title || 'Sans titre',
      source: props.source,
      media_type: props.mediaType,
      thumbnail: props.thumbnail,
      published_date: props.publishedDate,
    });
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped>
.like-btn {
  position: absolute;
  top: 12px;
  right: 12px;
  background: rgba(255, 255, 255, 0.95);
  border: none;
  cursor: pointer;
  padding: 8px;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
  color: #dee2e6;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  backdrop-filter: blur(8px);
  z-index: 10;
}

.like-btn:hover:not(:disabled) {
  background: white;
  color: #ff6b95;
  transform: scale(1.1);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.like-btn.liked {
  color: #ff6b95;
}

.like-btn.liked:hover:not(:disabled) {
  transform: scale(1.15);
}

.like-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.icon {
  width: 20px;
  height: 20px;
}
</style>
