// /src/composables/useArticles.ts 
import { ref } from "vue";
import type { CleanArticle, Raw } from "~/types/CleanArticle";


function getImageUrl(a: Raw): string | null {
  const cands: any[] = [
    a.image, a.img, a.thumbnail, a.thumb, a.cover, a.picture, a.og_image,
    a.enclosure?.url, a.media?.url, a.media?.thumbnail, a.media?.content?.url,
    Array.isArray(a.images) ? a.images[0] : null,
  ].filter(Boolean);

  for (const c of cands) {
    const url = typeof c === "string" ? c : (typeof c?.url === "string" ? c.url : null);
    if (!url) continue;
    if (/\.(jpg|jpeg|png|webp|gif)(\?|#|$)/i.test(url) || /^data:image\//.test(url)) return url;
  }

  const html = a.content || a.summary || a.description || "";
  if (typeof html === "string") {
    const m = html.match(/<img[^>]+src=["']([^"']+)["']/i);
    if (m?.[1]) return m[1];
  }
  return null;
}

function normalize(a: Raw): CleanArticle | null {
  if (!a) return null;
  const title = (a.title || "").toString().trim();
  const link = (a.link || a.url || "").toString().trim();
  if (!title || !link) return null;

  const image = getImageUrl(a);
  const source = a.source?.name || a.source || a.site || a.feed || a.publisher || undefined;

  let published: string | undefined;
  let publishedTime: number | undefined;
  const rawDate = a.published || a.pubDate || a.date || a.updated;
  if (rawDate) {
    const d = new Date(rawDate);
    if (!isNaN(+d)) {
      published = d.toLocaleString(undefined, {
        day: "2-digit",
        month: "short",
        hour: "2-digit",
        minute: "2-digit",
      });
      publishedTime = d.getTime();
    }
  }

  const summary = (a.summary || a.description || "").toString().replace(/<[^>]+>/g, "").trim();

  return { title, link, image, source, published, publishedTime, summary };
}

export function useArticles(opts?: {
  apiBase?: string; query?: string; hours?: number; meta?: number;
}) {
  const query = ref(opts?.query ?? "");
  const hours = ref(opts?.hours ?? 48);
  const meta = ref(opts?.meta ?? 1);

  const loading = ref(false);
  const error = ref<string | null>(null);
  const all = ref<CleanArticle[]>([]);

  async function load() {
    loading.value = true; error.value = null;

    // Charge directement depuis archive.json local
    try {
      const res = await fetch('/archive.json');
      if (!res.ok) throw new Error(`Erreur ${res.status}`);
      
      const data = await res.json();
      const listArch: Raw[] = Array.isArray(data) ? data : (data?.articles ?? []);
      
      const seen = new Set<string>();
      const cleaned: CleanArticle[] = [];
      
      for (const it of listArch) {
        const n = normalize(it);
        if (!n) continue;
        if (seen.has(n.link)) continue;
        seen.add(n.link);
        cleaned.push(n);
      }
      
      // Tri par date décroissante (plus récent d'abord)
      cleaned.sort((a, b) => (b.publishedTime || 0) - (a.publishedTime || 0));
      
      all.value = cleaned;
    } catch (e) {
      console.error('Erreur chargement archive.json:', e);
      error.value = "Erreur de chargement des articles.";
    } finally {
      loading.value = false;
    }
  }

  return { query, hours, meta, loading, error, all, load };
}
