// Test rapide de la structure des données pour le frontend
const fs = require('fs');
const path = require('path');

const archivePath = path.join(__dirname, 'Front/public/archive.json');
const data = JSON.parse(fs.readFileSync(archivePath, 'utf-8'));

const now = Date.now();
const twentyFourHoursAgo = now - (24 * 60 * 60 * 1000);

const articles = data.articles || [];
const videos = data.videos || [];

const recentArticles = articles.filter(a => (a.publishedTime || 0) >= twentyFourHoursAgo);
const recentVideos = videos.filter(v => (v.publishedTime || 0) >= twentyFourHoursAgo);

console.log('\n��� Statistiques archive.json:');
console.log(`  Articles totaux: ${articles.length}`);
console.log(`  Articles <24h: ${recentArticles.length}`);
console.log(`  Vidéos totales: ${videos.length}`);
console.log(`  Vidéos <24h: ${recentVideos.length}`);

if (recentVideos.length > 0) {
  console.log('\n��� Exemples de vidéos récentes:');
  recentVideos.slice(0, 3).forEach(v => {
    console.log(`  - ${v.channel}: ${v.title.substring(0, 60)}`);
    console.log(`    publishedTime: ${v.publishedTime} (${new Date(v.publishedTime).toISOString()})`);
  });
} else {
  console.log('\n⚠️  Aucune vidéo récente (<24h) trouvée!');
}

console.log('\n✅ Test terminé\n');
