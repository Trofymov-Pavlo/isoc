const stripHtml = (text) => text ? text.replace(/<[^>]+>/g, '').trim() : '';
const toTimestamp = (value) => {
  if (!value) return 0;
  if (typeof value === 'number') return value;
  const d = new Date(String(value));
  return isNaN(+d) ? 0 : d.getTime();
};

const normalizeVideo = (raw) => {
  if (!raw) return null;
  const title = (raw.title || '').toString().trim();
  const link = (raw.link || '').toString().trim();
  if (!title || !link) return null;

  const published = raw.published || raw.publishedAt;
  const publishedTime = raw.publishedTime ?? toTimestamp(published);
  const summary = stripHtml(raw.summary || raw.description || '');
  const source = raw.channel || raw.source;
  const image = raw.thumbnail || raw.image;

  console.log('Input video:', { title: title.substring(0, 30), thumbnail: raw.thumbnail, image: raw.image });
  console.log('Computed image:', image);

  return {
    type: 'video',
    title,
    link,
    source,
    summary,
    image: image || null,
    published,
    publishedTime,
  };
};

// Test avec une vidéo de l'archive
import fs from 'fs';
const data = JSON.parse(fs.readFileSync('Front/public/archive.json', 'utf-8'));
const testVideo = data.videos[0];

console.log('\n=== Test normalizeVideo ===\n');
const result = normalizeVideo(testVideo);
console.log('\nResult:', JSON.stringify(result, null, 2));
