<template>
  <div class="like-menu-container">
    <button
      class="like-btn"
      @click="toggleMenu"
      :title="'Enregistrer'"
      :class="{ active: isAnySaved }"
    >
      <svg class="icon" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2">
        <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
      </svg>
    </button>

    <!-- Dropdown menu -->
    <Transition name="menu">
      <div v-if="menuOpen" class="like-menu" @click.stop>
        <button
          class="menu-item"
          :class="{ active: isSaved('liked') }"
          @click="toggleCategory('liked')"
        >
          <svg class="menu-icon" viewBox="0 0 24 24" fill="currentColor">
            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
          </svg>
          <span>Likés</span>
        </button>

        <button
          class="menu-item"
          :class="{ active: isSaved('watch_later') }"
          @click="toggleCategory('watch_later')"
        >
          <svg class="menu-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"></circle>
            <polyline points="12 6 12 12 16 14"></polyline>
          </svg>
          <span>À lire plus tard</span>
        </button>

        <div v-if="userCategories.length > 0" class="menu-divider"></div>

        <button
          v-for="cat in userCategories"
          :key="cat.id"
          class="menu-item"
          :class="{ active: isSaved(cat.name) }"
          @click="toggleCategory(cat.name)"
        >
          <span class="menu-icon">{{ cat.icon }}</span>
          <span>{{ cat.name }}</span>
        </button>

        <div class="menu-divider"></div>

        <button class="menu-item menu-add" @click="openCreateModal">
          <svg class="menu-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="12" y1="5" x2="12" y2="19"></line>
            <line x1="5" y1="12" x2="19" y2="12"></line>
          </svg>
          <span>Nouvelle catégorie</span>
        </button>
      </div>
    </Transition>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useAuthState } from '~/composables/useAuthState';
import { useSavedMedia } from '~/composables/useSavedMedia';

interface Props {
  link: string;
  title?: string;
  source?: string;
  mediaType: 'article' | 'video' | 'live';
  thumbnail?: string;
}

const props = withDefaults(defineProps<Props>(), {
  source: 'AXIOM',
});

const emit = defineEmits<{
  (e: 'createCategory'): void;
}>();

const { isAuthenticated } = useAuthState();
const { toggleSave, isSaved: checkSaved, userCategories, getUserCategories } = useSavedMedia();

const menuOpen = ref(false);

onMounted(async () => {
  // Load categories regardless of auth status
  await getUserCategories();
});

const isSaved = (category: string) => {
  if (!isAuthenticated.value) return false;
  return checkSaved(props.link, category);
};

const isAnySaved = computed(() => {
  if (!isAuthenticated.value) return false;
  const categories = ['liked', 'watch_later', ...userCategories.value.map(c => c.name)];
  return categories.some(cat => checkSaved(props.link, cat));
});

const toggleMenu = () => {
  if (!isAuthenticated.value) {
    if (typeof window !== 'undefined') {
      window.location.href = '/connexion';
    }
    return;
  }
  menuOpen.value = !menuOpen.value;
};

const toggleCategory = async (category: string) => {
  await toggleSave({
    link: props.link,
    title: props.title || 'Sans titre',
    source: props.source,
    media_type: props.mediaType,
    thumbnail: props.thumbnail,
    category,
  });
};

const openCreateModal = () => {
  menuOpen.value = false;
  emit('createCategory');
};

// Close menu when clicking outside
const handleClickOutside = (event: MouseEvent) => {
  const target = event.target as HTMLElement;
  if (!target.closest('.like-menu-container')) {
    menuOpen.value = false;
  }
};

onMounted(() => {
  document.addEventListener('click', handleClickOutside);
});

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside);
});
</script>

<style scoped>
.like-menu-container {
  position: relative;
  display: inline-block;
}

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
  position: relative;
}

.like-btn:hover {
  color: #ff9fb3;
  transform: scale(1.15);
}

.like-btn.active {
  color: #ff6b95;
}

.icon {
  width: 20px;
  height: 20px;
}

/* Dropdown menu */
.like-menu {
  position: absolute;
  top: calc(100% + 8px);
  right: 0;
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
  padding: 8px;
  min-width: 220px;
  z-index: 1000;
}

.menu-item {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 12px;
  border: none;
  background: white;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 14px;
  color: #333;
  text-align: left;
}

.menu-item:hover {
  background: #f5f5f5;
}

.menu-item.active {
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  color: white;
}

.menu-item.active .menu-icon {
  color: white;
}

.menu-icon {
  width: 18px;
  height: 18px;
  flex-shrink: 0;
  color: #666;
}

.menu-add {
  color: #7b5ce0;
  font-weight: 600;
}

.menu-add .menu-icon {
  color: #7b5ce0;
}

.menu-divider {
  height: 1px;
  background: #e0e0e0;
  margin: 8px 0;
}

/* Transition */
.menu-enter-active,
.menu-leave-active {
  transition: all 0.2s ease;
}

.menu-enter-from,
.menu-leave-to {
  opacity: 0;
  transform: translateY(-8px);
}
</style>
