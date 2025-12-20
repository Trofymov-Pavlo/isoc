<template>
  <button
    class="like-btn"
    :class="{ liked: isLiked }"
    @click="onClick"
    :title="isLiked ? 'Retirer des favoris' : 'Ajouter aux favoris'"
    :aria-pressed="isLiked"
    :disabled="isLoading"
  >
    <svg class="icon" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
    </svg>
  </button>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { useAuthState } from '~/composables/useAuthState';
import { useSavedMedia } from '~/composables/useSavedMedia';

interface Props {
  link: string;
  title?: string;
  source?: string;
  mediaType: 'article' | 'video' | 'live';
  thumbnail?: string;
  category?: string;
}

const props = withDefaults(defineProps<Props>(), {
  category: 'liked',
  source: 'AXIOM',
});

const emit = defineEmits<{
  (e: 'toggle', saved: boolean): void;
}>();

const { isLoggedIn } = useAuthState();
const { toggleSave, isSaved, loading } = useSavedMedia();

const localSaved = ref(false);
const isLoading = ref(false);

// On mount, check if item is already saved
const isLiked = computed(() => {
  if (!isLoggedIn.value) {
    return localSaved.value;
  }
  return isSaved(props.link);
});

const onClick = async () => {
  if (!isLoggedIn.value) {
    // Fallback to localStorage for non-authenticated users
    localSaved.value = !localSaved.value;
    emit('toggle', localSaved.value);
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
      category: props.category,
    });
    emit('toggle', !isLiked.value);
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped>
.like-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
  color: #ccc;
}

.like-btn:hover:not(:disabled) {
  color: #ff9fb3;
  transform: scale(1.15);
}

.like-btn.liked {
  color: #ff6b95;
}

.like-btn.liked:hover:not(:disabled) {
  transform: scale(1.2);
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
