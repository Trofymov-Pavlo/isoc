import { ref, computed } from 'vue';

export function useLiked() {
  const likedItems = ref<Set<string>>(new Set());

  // Load from localStorage
  const loadLiked = () => {
    if (typeof localStorage !== 'undefined') {
      const stored = localStorage.getItem('AXIOM_LIKED_ITEMS');
      if (stored) {
        try {
          likedItems.value = new Set(JSON.parse(stored));
        } catch {
          likedItems.value = new Set();
        }
      }
    }
  };

  // Save to localStorage
  const saveLiked = () => {
    if (typeof localStorage !== 'undefined') {
      localStorage.setItem('AXIOM_LIKED_ITEMS', JSON.stringify(Array.from(likedItems.value)));
    }
  };

  // Toggle like
  const toggleLike = (link: string) => {
    if (likedItems.value.has(link)) {
      likedItems.value.delete(link);
    } else {
      likedItems.value.add(link);
    }
    saveLiked();
  };

  // Check if item is liked
  const isLiked = computed(() => (link: string) => likedItems.value.has(link));

  // Get all liked items (need to load articles/videos separately)
  const likedCount = computed(() => likedItems.value.size);

  return {
    likedItems,
    loadLiked,
    toggleLike,
    isLiked,
    likedCount,
  };
}
