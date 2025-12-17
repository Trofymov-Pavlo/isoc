<template>
  <button
    class="like-btn"
    :class="{ liked: isLiked }"
    @click="onClick"
    :title="isLiked ? 'Retirer des favoris' : 'Ajouter aux favoris'"
    :aria-pressed="isLiked"
  >
    <svg class="icon" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
    </svg>
  </button>
</template>

<script setup lang="ts">
defineProps<{
  isLiked: boolean;
}>();

const emit = defineEmits<{
  (e: 'toggle'): void;
}>();

const onClick = () => {
  emit('toggle');
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

.like-btn:hover {
  color: #ff9fb3;
  transform: scale(1.15);
}

.like-btn.liked {
  color: #ff6b95;
}

.like-btn.liked:hover {
  transform: scale(1.2);
}

.icon {
  width: 20px;
  height: 20px;
}
</style>
