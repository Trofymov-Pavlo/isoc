/**
 * Composable for managing saved media (liked, watch later, custom categories)
 * Syncs with backend API instead of localStorage
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
  created_at: string;
}

export const useSavedMedia = () => {
  // Auth state is used only for “logged-in” semantics; tokens are stored in localStorage.
  // IMPORTANT: this composable can be imported during SSR, so never touch localStorage on server.
  useAuthState();

  const isServer = typeof window === 'undefined';
  
  const savedItems = ref<SavedMediaItem[]>([]);
  const userCategories = ref<UserCategory[]>([]);
  const loading = ref(false);
  const error = ref<string | null>(null);

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
    if (!getToken()) return false;
    
    try {
      loading.value = true;
      error.value = null;
      const response = await apiCall('/toggle/', 'POST', payload);
      // Refresh saved items after toggle
      if (response) {
        await getSavedItems();
      }
      return response;
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to toggle save';
      return null;
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
  const getTopSaved = async (limit = 3) => {
    if (!getToken()) return [];
    
    try {
      const response = await apiCall(`/top/?limit=${limit}`);
      return Array.isArray(response) ? response : [];
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to fetch top items';
      return [];
    }
  };

  /**
   * Check if a specific media is saved
   */
  const checkSaved = async (link: string) => {
    if (!getToken()) return false;
    
    try {
      const response = await apiCall(`/is_saved/?link=${encodeURIComponent(link)}`);
      return response?.saved || false;
    } catch (err) {
      return false;
    }
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
  const createCategory = async (name: string, color = '#FF69B4') => {
    if (!getToken()) return null;
    
    try {
      const response = await apiCall('/categories/', 'POST', {
        name,
        color,
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
      return true;
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to delete category';
      return false;
    }
  };

  /**
   * Computed property to check if a link is saved
   */
  const isSaved = (link: string) => {
    return savedItems.value.some(item => item.link === link);
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

  return {
    // State
    savedItems,
    userCategories,
    loading,
    error,
    
    // Methods
    toggleSave,
    getSavedItems,
    getSavedByCategory,
    getTopSaved,
    checkSaved,
    getUserCategories,
    createCategory,
    deleteCategory,
    
    // Computed
    isSaved,
    likedItems,
    watchLaterItems,
  };
};
