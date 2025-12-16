// ~/composables/useTheme.ts
import { ref, watch, onMounted } from 'vue';

type Theme = 'light' | 'dark';

const isDark = ref<boolean>(false);

export function useTheme() {
  // Load theme from localStorage on mount
  const initTheme = () => {
    if (process.client) {
      const saved = localStorage.getItem('theme');
      if (saved) {
        isDark.value = saved === 'dark';
      } else {
        // Check system preference
        isDark.value = window.matchMedia('(prefers-color-scheme: dark)').matches;
      }
      applyTheme();
    }
  };

  // Apply theme to document
  const applyTheme = () => {
    if (process.client) {
      const html = document.documentElement;
      if (isDark.value) {
        html.classList.add('dark-mode');
        html.style.colorScheme = 'dark';
      } else {
        html.classList.remove('dark-mode');
        html.style.colorScheme = 'light';
      }
      localStorage.setItem('theme', isDark.value ? 'dark' : 'light');
    }
  };

  // Toggle theme
  const toggleTheme = () => {
    isDark.value = !isDark.value;
    applyTheme();
  };

  // Watch for changes
  watch(isDark, () => {
    applyTheme();
  });

  // Initialize on mount
  onMounted(() => {
    initTheme();
  });

  return {
    isDark,
    toggleTheme,
    initTheme,
  };
}
