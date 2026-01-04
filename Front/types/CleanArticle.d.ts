export type CleanArticle = {
  title: string;
  link: string;
  image?: string | null;
  source?: string;
  channel?: string; // Add for type consistency with videos
  published?: string;
  publishedTime?: number;
  summary?: string;
  type?: string; // Add for search results
};

type Raw = Record<string, any>;