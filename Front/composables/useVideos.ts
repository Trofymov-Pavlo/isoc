// useVideos.ts
import { ref, computed } from 'vue';

export interface Video {
  channel: string;
  title: string;
  link: string;
  published: string;
  publishedTime: number;
  thumbnail?: string;
  summary?: string;
  type: string;
  archived_at?: string;
}

export const useVideos = () => {
  const videos = ref<Video[]>([]);
  const loading = ref(false);
  const error = ref<string | null>(null);

  const fetchVideos = async (options?: {
    hours?: number;
    channel?: string;
    limit?: number;
  }) => {
    loading.value = true;
    error.value = null;

    // Charge directement depuis archive.json local
    try {
      const res = await fetch('/archive.json');
      if (!res.ok) throw new Error(`Erreur ${res.status}`);
      
      const data = await res.json();
      const listVideos: Video[] = Array.isArray(data) ? data : (data?.videos ?? []);
      
      // Tri par date décroissante (plus récent d'abord)
      listVideos.sort((a, b) => (b.publishedTime || 0) - (a.publishedTime || 0));
      
      videos.value = listVideos;
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Erreur chargement vidéos';
      console.error('Erreur chargement archive.json:', err);
    } finally {
      loading.value = false;
    }
  };

  const getChannels = computed(() => {
    const channels = new Set(videos.value.map(v => v.channel));
    return Array.from(channels).sort();
  });

  const filterByChannel = (channel: string) => {
    return videos.value.filter(v => v.channel === channel);
  };

  const filterByQuery = (query: string) => {
    const q = query.toLowerCase();
    return videos.value.filter(v =>
      v.title.toLowerCase().includes(q) ||
      (v.summary && v.summary.toLowerCase().includes(q)) ||
      v.channel.toLowerCase().includes(q)
    );
  };

  const formatDate = (isoDate: string | number): string => {
    try {
      const date = typeof isoDate === 'string'
        ? new Date(isoDate)
        : new Date(isoDate);

      const now = new Date();
      const diffMs = now.getTime() - date.getTime();
      const diffHours = Math.floor(diffMs / (1000 * 60 * 60));
      const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));

      if (diffHours < 1) return 'À l\'instant';
      if (diffHours < 24) return `Il y a ${diffHours}h`;
      if (diffDays < 7) return `Il y a ${diffDays}j`;

      return date.toLocaleDateString('fr-FR', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
      });
    } catch {
      return 'Date inconnue';
    }
  };

  const getYoutubeVideoId = (url: string): string | null => {
    try {
      if (url.includes('youtube.com/watch?v=')) {
        return url.split('v=')[1].split('&')[0];
      } else if (url.includes('youtu.be/')) {
        return url.split('youtu.be/')[1].split('?')[0];
      }
    } catch {
      return null;
    }
    return null;
  };

  return {
    videos,
    loading,
    error,
    fetchVideos,
    getChannels,
    filterByChannel,
    filterByQuery,
    formatDate,
    getYoutubeVideoId,
  };
};
