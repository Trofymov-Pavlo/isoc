export type CleanArticle = {
  title: string;
  link: string;
  image?: string | null;
  source?: string;
  published?: string;
  publishedTime?: number;
  summary?: string;
};

type Raw = Record<string, any>;