/**
 * Composable for managing saved media (liked, watch later, custom categories)
 * Syncs with backend API with global reactive state
 */

import { ref, computed } from 'vue';
import { useAuthState } from './useAuthState';

export interface SavedMediaItem {
  id: number;
  link: string;
  title: string;
  source: string;
  media_type: 'article' | 'video' | 'live';
  category: 'liked' | 'watch_later' | string;
  thumbnail?: string;
  saved_at: string;
}

export interface UserCategory {
  id: number;
  name: string;
  color: string;
  icon: string;
  created_at: string;
}

// Global state shared across all instances
const savedItems = ref<SavedMediaItem[]>([]);
const userCategories = ref<UserCategory[]>([]);
const loading = ref(false);
const error = ref<string | null>(null);
const isInitialized = ref(false);

export const useSavedMedia = () => {
  const { isAuthenticated } = useAuthState();
  const isServer = typeof window === 'undefined';
  
  const API_BASE = 'http://localhost:8000/api/saved-media';

  const getToken = (): string | null => {
    if (isServer) return null;
    try {
      return localStorage.getItem('access_token');
    } catch {
      return null;
    }
  };

  const getHeaders = () => {
    const token = getToken();
    return {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    };
  };

  /**
   * Make API call with proper error handling
   */
  const apiCall = async (endpoint: string, method = 'GET', body?: any) => {
    try {
      if (isServer) {
        throw new Error('Saved media API cannot be called during SSR');
      }

      const options: RequestInit = {
        method,
        headers: getHeaders(),
      };

      if (body && method !== 'GET') {
        options.body = JSON.stringify(body);
      }

      const response = await fetch(`${API_BASE}${endpoint}`, options);

      if (!response.ok) {
        if (response.status === 401) {
          // Token expired or invalid
          try {
            localStorage.removeItem('access_token');
            localStorage.removeItem('refresh_token');
          } catch {
            // ignore
          }
          throw new Error('Authentication expired. Please login again.');
        }
        throw new Error(`API error: ${response.status}`);
      }

      return await response.json();
    } catch (err) {
      console.error('API Error:', err);
      throw err;
    }
  };

  /**
   * Initialize: load saved items and categories
   */
  const initialize = async () => {
    if (isInitialized.value || !isAuthenticated.value || !getToken()) return;
    
    try {
      isInitialized.value = true;
      await Promise.all([
        getSavedItems(),
        getUserCategories(),
      ]);
    } catch (err) {
      console.error('Failed to initialize saved media:', err);
      isInitialized.value = false;
    }
  };

  /**
   * Toggle save status for a media item
   */
  const toggleSave = async (payload: {
    link: string;
    title: string;
    source: string;
    media_type: 'article' | 'video' | 'live';
    category?: string;
    thumbnail?: string;
  }) => {
    if (!getToken()) return { saved: false };
    
    try {
      loading.value = true;
      error.value = null;
      const response = await apiCall('/toggle/', 'POST', payload);
      
      // Update local state immediately for instant UI feedback
      if (response.saved) {
        // Item was added - refresh to get the full item with ID
        await getSavedItems();
      } else {
        // Item was removed - remove from local state
        const category = payload.category || 'liked';
        savedItems.value = savedItems.value.filter(
          item => !(item.link === payload.link && item.category === category)
        );
      }
      
      return response;
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to toggle save';
      return { saved: false };
    } finally {
      loading.value = false;
    }
  };

  /**
   * Get all saved items
   */
  const getSavedItems = async () => {
    if (!getToken()) return [];
    
    try {
      loading.value = true;
      error.value = null;
      const response = await apiCall('/');
      if (Array.isArray(response)) {
        savedItems.value = response;
        return response;
      }
      return [];
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to fetch saved items';
      return [];
    } finally {
      loading.value = false;
    }
  };

  /**
   * Get saved items by category
   */
  const getSavedByCategory = async (category: string) => {
    if (!getToken()) return [];
    
    try {
      const response = await apiCall(`/by_category/?category=${category}`);
      return Array.isArray(response) ? response : [];
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to fetch category items';
      return [];
    }
  };

  /**
   * Get top N saved items (for dashboard)
   */
  const getTopSaved = async (limit = 3, category = 'liked') => {
    if (!getToken()) return [];
    
    try {
      const response = await apiCall(`/top/?limit=${limit}&category=${category}`);
      return Array.isArray(response) ? response : [];
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to fetch top items';
      return [];
    }
  };

  /**
   * Check if a specific media is saved (uses local cache)
   */
  const isSaved = (link: string, category = 'liked') => {
    return savedItems.value.some(item => item.link === link && item.category === category);
  };

  /**
   * Get all user custom categories
   */
  const getUserCategories = async () => {
    if (!getToken()) return [];
    
    try {
      const response = await apiCall('/categories/');
      if (Array.isArray(response)) {
        userCategories.value = response;
        return response;
      }
      return [];
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to fetch categories';
      return [];
    }
  };

  /**
   * Create a new custom category
   */
  const createCategory = async (name: string, color = '#2f0538', icon = '❤️') => {
    if (!getToken()) return null;
    
    try {
      const response = await apiCall('/categories/', 'POST', {
        name,
        color,
        icon,
      });
      if (response) {
        await getUserCategories();
      }
      return response;
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to create category';
      return null;
    }
  };

  /**
   * Delete a custom category
   */
  const deleteCategory = async (categoryId: number) => {
    if (!getToken()) return false;
    
    try {
      await apiCall(`/categories/${categoryId}/`, 'DELETE');
      await getUserCategories();
      // Also refresh saved items as items in deleted category may have been removed
      await getSavedItems();
      return true;
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to delete category';
      return false;
    }
  };

  /**
   * Computed property to get liked items
   */
  const likedItems = computed(() => {
    return savedItems.value.filter(item => item.category === 'liked');
  });

  /**
   * Computed property to get watch later items
   */
  const watchLaterItems = computed(() => {
    return savedItems.value.filter(item => item.category === 'watch_later');
  });

  /**
   * Get items for a specific custom category
   */
  const getCategoryItems = (category: string) => {
    return savedItems.value.filter(item => item.category === category);
  };

  return {
    // State
    savedItems,
    userCategories,
    loading,
    error,
    isInitialized,
    
    // Methods
    initialize,
    toggleSave,
    getSavedItems,
    getSavedByCategory,
    getTopSaved,
    getUserCategories,
    createCategory,
    deleteCategory,
    
    // Computed/helpers
    isSaved,
    likedItems,
    watchLaterItems,
    getCategoryItems,
  };
};
