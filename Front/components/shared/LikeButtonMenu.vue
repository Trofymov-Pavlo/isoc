<template>
  <div class="like-menu-container">
    <button
      class="like-btn"
      type="button"
      @click.stop="onHeartClick"
      :title="isAnySaved ? 'Gérer' : 'Enregistrer'"
      :class="{ active: isAnySaved }"
    >
      <svg
        class="icon"
        viewBox="0 0 24 24"
        :fill="isAnySaved ? 'currentColor' : 'none'"
        stroke="currentColor"
        stroke-width="2"
      >
        <path
          d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"
        ></path>
      </svg>
    </button>

    <!-- Vertical action bar (opens when heart is already pink) -->
    <Transition name="menu">
      <div v-if="menuOpen" class="action-bar" @click.stop>
        <button
          class="action-btn"
          type="button"
          :class="{ active: isSaved('liked') }"
          :title="isSaved('liked') ? 'Retirer des likés' : 'Ajouter aux likés'"
          @click="toggleCategory('liked')"
        >
          <svg
            class="action-icon"
            viewBox="0 0 24 24"
            :fill="isSaved('liked') ? 'currentColor' : 'none'"
            stroke="currentColor"
            stroke-width="2"
          >
            <path
              d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"
            ></path>
          </svg>
        </button>

        <button
          class="action-btn"
          type="button"
          :class="{ active: isSaved('watch_later') }"
          :title="isSaved('watch_later') ? 'Retirer de à lire plus tard' : 'Ajouter à lire plus tard'"
          @click="toggleCategory('watch_later')"
        >
          <svg class="action-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"></circle>
            <polyline points="12 6 12 12 16 14"></polyline>
          </svg>
        </button>

        <div v-if="userCategories.length > 0" class="action-divider"></div>

        <button
          v-for="cat in userCategories"
          :key="cat.id"
          class="action-btn"
          type="button"
          :class="{ active: isSaved(cat.name) }"
          :title="cat.name"
          @click="toggleCategory(cat.name)"
        >
          <span class="action-emoji">{{ cat.icon }}</span>
        </button>

        <div class="action-divider"></div>

        <button class="action-btn add" type="button" title="Nouvelle catégorie" @click="createCategoryFromPrompt">
          <svg class="action-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="12" y1="5" x2="12" y2="19"></line>
            <line x1="5" y1="12" x2="19" y2="12"></line>
          </svg>
        </button>
      </div>
    </Transition>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, onUnmounted, ref, watch } from 'vue';
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
const { toggleSave, isSaved: checkSaved, userCategories, getUserCategories, createCategory, initialize, isInitialized } =
  useSavedMedia();

const menuOpen = ref(false);

watch(
  () => isAuthenticated.value,
  async (authed) => {
    if (!authed) {
      menuOpen.value = false;
      return;
    }
    if (!isInitialized.value) {
      await initialize();
    }
  },
  { immediate: true }
);

const isSaved = (category: string) => {
  if (!isAuthenticated.value) return false;
  return checkSaved(props.link, category);
};

const isAnySaved = computed(() => {
  if (!isAuthenticated.value) return false;
  const categories = ['liked', 'watch_later', ...userCategories.value.map((c) => c.name)];
  return categories.some((cat) => checkSaved(props.link, cat));
});

const closeMenu = () => {
  menuOpen.value = false;
};

const openMenu = async () => {
  if (!isAuthenticated.value) {
    navigateTo('/connexion');
    return;
  }
  await getUserCategories();
  menuOpen.value = true;
};

const toggleCategory = async (category: string) => {
  await toggleSave({
    link: props.link,
    title: props.title || 'Sans titre',
    source: props.source,
    media_type: props.mediaType,
    thumbnail: props.thumbnail,
    published_date: props.publishedDate,
    category,
  });
};

const onHeartClick = async () => {
  if (!isAuthenticated.value) {
    navigateTo('/connexion');
    return;
  }

  // Grey heart -> like directly (pink)
  if (!isAnySaved.value) {
    await toggleCategory('liked');
    return;
  }

  // Pink heart -> open/close action bar
  if (menuOpen.value) closeMenu();
  else await openMenu();
};

const createCategoryFromPrompt = async () => {
  if (!isAuthenticated.value) {
    navigateTo('/connexion');
    return;
  }

  const name = window.prompt('Nom de la nouvelle catégorie :');
  if (!name || !name.trim()) return;

  const created = await createCategory(name.trim());
  if (created) {
    await getUserCategories();
  }
};

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
  display: inline-flex;
  align-items: center;
}

.like-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 6px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
  color: #ccc;
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

/* Vertical action bar centered on the heart icon (Y-centered) */
.action-bar {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(28px, -50%) scale(1);
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 10px;
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 999px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
  z-index: 1000;
}

.action-btn {
  width: 36px;
  height: 36px;
  border-radius: 999px;
  border: none;
  background: white;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
  color: #666;
}

.action-btn:hover {
  background: #f5f5f5;
}

.action-btn.active {
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  color: white;
}

.action-icon {
  width: 18px;
  height: 18px;
}

.action-emoji {
  font-size: 16px;
  line-height: 1;
}

.action-divider {
  width: 100%;
  height: 1px;
  background: #e9e9e9;
}

.action-btn.add {
  color: #7b5ce0;
}

/* Transition */
.menu-enter-active,
.menu-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}

.menu-enter-from,
.menu-leave-to {
  opacity: 0;
  transform: translate(28px, -50%) scale(0.96);
}
</style>
