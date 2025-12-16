import { computed, ref } from 'vue';

export type LiveEntryType = 'article' | 'video';

export interface LiveEntry {
  type: LiveEntryType;
  title: string;
  link: string;
  source?: string;
  summary?: string;
  image?: string | null;
  published?: string;
  publishedTime?: number;
  archived_at?: string;
}

const toTimestamp = (value: unknown): number => {
  if (value === null || value === undefined) return 0;
  if (typeof value === 'number') return value;

  const num = Number(value);
  if (!Number.isNaN(num) && `${value}`.length <= 13) return num;

  const d = new Date(String(value));
  return Number.isNaN(+d) ? 0 : d.getTime();
};

const stripHtml = (text?: string): string => {
  if (!text) return '';
  return text.replace(/<[^>]+>/g, '').trim();
};

const getImageUrl = (a: any): string | null => {
  if (!a) return null;
  const cands: any[] = [
    a.image, a.img, a.thumbnail, a.thumb, a.cover, a.picture, a.og_image,
    a.enclosure?.url, a.media?.url, a.media?.thumbnail, a.media?.content?.url,
    Array.isArray(a.images) ? a.images[0] : null,
  ].filter(Boolean);

  for (const c of cands) {
    const url = typeof c === 'string' ? c : (typeof c?.url === 'string' ? c.url : null);
    if (!url) continue;
    if (/\.(jpg|jpeg|png|webp|gif)(\?|#|$)/i.test(url) || /^data:image\//.test(url)) return url;
  }

  const html = a.content || a.summary || a.description || '';
  if (typeof html === 'string') {
    const m = html.match(/<img[^>]+src=["']([^"']+)["']/i);
    if (m?.[1]) return m[1];
  }
  return null;
};

const normalizeArticle = (raw: any): LiveEntry | null => {
  if (!raw) return null;
  const title = (raw.title || '').toString().trim();
  const link = (raw.link || raw.url || '').toString().trim();
  if (!title || !link) return null;

  const published = raw.published || raw.pubDate || raw.date || raw.updated || raw.published_at;
  const publishedTime = raw.publishedTime ?? toTimestamp(published);
  const summary = stripHtml(raw.summary || raw.description || '');
  const source = raw.source?.name || raw.source || raw.site || raw.feed || raw.publisher;

  return {
    type: 'article',
    title,
    link,
    source: source || undefined,
    summary: summary || undefined,
    image: getImageUrl(raw),
    published: published || undefined,
    publishedTime: publishedTime || undefined,
    archived_at: raw.archived_at,
  };
};

const normalizeVideo = (raw: any): LiveEntry | null => {
  if (!raw) return null;
  const title = (raw.title || '').toString().trim();
  const link = (raw.link || '').toString().trim();
  if (!title || !link) return null;

  const published = raw.published || raw.publishedAt;
  const publishedTime = raw.publishedTime ?? toTimestamp(published);
  const summary = stripHtml(raw.summary || raw.description || '');
  const source = raw.channel || raw.source;
  const image = raw.thumbnail || raw.image || getImageUrl(raw);

  // Formater published pour l'affichage (comme les articles)
  let publishedFormatted = published;
  if (publishedTime) {
    try {
      const d = new Date(publishedTime);
      if (!isNaN(+d)) {
        publishedFormatted = d.toLocaleString(undefined, {
          day: "2-digit",
          month: "short",
          hour: "2-digit",
          minute: "2-digit",
        });
      }
    } catch {}
  }

  return {
    type: 'video',
    title,
    link,
    source: source || undefined,
    summary: summary || undefined,
    image: image || null,
    published: publishedFormatted || undefined,
    publishedTime: publishedTime || undefined,
    archived_at: raw.archived_at,
  };
};

export function useArchiveFeed() {
  const items = ref<LiveEntry[]>([]);
  const loading = ref(false);
  const error = ref<string | null>(null);

  const load = async () => {
    loading.value = true;
    error.value = null;

    try {
      const res = await fetch('/archive.json');
      if (!res.ok) throw new Error(`Erreur ${res.status}`);

      const data = await res.json();
      const rawArticles = Array.isArray(data) ? [] : (data?.articles ?? []);
      const rawVideos = Array.isArray(data) ? [] : (data?.videos ?? []);

      const seen = new Set<string>();
      const normalized: LiveEntry[] = [];

      for (const a of rawArticles) {
        const n = normalizeArticle(a);
        if (!n) continue;
        if (seen.has(n.link)) continue;
        seen.add(n.link);
        normalized.push(n);
      }

      for (const v of rawVideos) {
        const n = normalizeVideo(v);
        if (!n) continue;
        if (seen.has(n.link)) continue;
        seen.add(n.link);
        normalized.push(n);
      }

      normalized.sort((a, b) => (b.publishedTime || 0) - (a.publishedTime || 0));
      items.value = normalized;
      
      const articlesCount = normalized.filter(it => it.type === 'article').length;
      const videosCount = normalized.filter(it => it.type === 'video').length;
      console.log(`✅ Archive chargée: ${articlesCount} articles, ${videosCount} vidéos (total: ${normalized.length})`);
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Erreur de chargement de l\'archive';
      console.error('❌ Erreur chargement archive.json:', err);
    } finally {
      loading.value = false;
    }
  };

  const articles = computed(() => items.value.filter(it => it.type === 'article'));
  const videos = computed(() => items.value.filter(it => it.type === 'video'));

  return { items, articles, videos, loading, error, load };
}
