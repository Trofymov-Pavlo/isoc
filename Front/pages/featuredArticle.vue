<template>
  <MainFeaturedArticle />
</template>

<script setup lang="ts">
import MainFeaturedArticle from "~/components/featuredArticle/MainFeaturedArticle.vue";
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.featured-article-page {
  background: #ffffff;
  min-height: 100vh;
}

/* Hero Section */
.article-hero {
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  color: #fff;
  padding: 60px 20px;
}

.hero-container {
  max-width: 900px;
  margin: 0 auto;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.15);
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  margin-bottom: 20px;
}

.badge-icon {
  font-size: 14px;
}

.article-title {
  font-size: 48px;
  font-weight: 800;
  line-height: 1.2;
  margin-bottom: 16px;
  letter-spacing: -0.5px;
}

.article-subtitle {
  font-size: 18px;
  opacity: 0.95;
  margin-bottom: 32px;
  line-height: 1.6;
}

.article-meta {
  display: flex;
  align-items: center;
  gap: 32px;
  padding-top: 24px;
  border-top: 1px solid rgba(255, 255, 255, 0.2);
}

.author-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.author-avatar {
  width: 44px;
  height: 44px;
  background: rgba(255, 255, 255, 0.25);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 14px;
}

.author-details {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.author-name {
  font-weight: 600;
}

.publish-date {
  font-size: 13px;
  opacity: 0.9;
}

.reading-time {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  opacity: 0.9;
}

/* Featured Image */
.article-image-section {
  max-width: 100%;
  height: 500px;
  overflow: hidden;
  background: #f5f5f5;
}

.featured-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Article Content */
.article-content {
  padding: 60px 20px;
}

.content-container {
  max-width: 900px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 250px 1fr;
  gap: 40px;
}

/* Table of Contents */
.table-of-contents {
  position: sticky;
  top: 80px;
  height: fit-content;
}

.toc-title {
  margin: 0 0 16px;
  font-size: 14px;
  font-weight: 700;
  text-transform: uppercase;
  color: #2f0538;
  letter-spacing: 0.5px;
}

.toc-nav {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.toc-link {
  color: #666;
  text-decoration: none;
  font-size: 13px;
  line-height: 1.6;
  padding: 6px 0;
  border-left: 2px solid transparent;
  padding-left: 12px;
  transition: all 0.22s ease;
}

.toc-link:hover {
  color: #2f0538;
  border-left-color: #7b5ce0;
  padding-left: 16px;
}

/* Main Content */
.main-content {
  display: flex;
  flex-direction: column;
  gap: 40px;
}

.article-section {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.section-title {
  font-size: 32px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0;
  line-height: 1.2;
}

.section-text {
  font-size: 16px;
  line-height: 1.8;
  color: #555;
  margin: 0;
}

.section-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.section-list li {
  font-size: 16px;
  line-height: 1.7;
  color: #555;
  padding-left: 24px;
  position: relative;
}

.section-list li:before {
  content: "→";
  position: absolute;
  left: 0;
  color: #7b5ce0;
  font-weight: 700;
}

/* Content Boxes */
.content-box {
  padding: 24px;
  border-radius: 10px;
  background: #f9f9f9;
  border-left: 4px solid #7b5ce0;
}

.highlight-box {
  background: linear-gradient(135deg, rgba(123, 92, 224, 0.05), rgba(123, 92, 224, 0.02));
}

.warning-box {
  border-left-color: #ff9800;
  background: rgba(255, 152, 0, 0.05);
}

.info-box {
  border-left-color: #2196f3;
  background: rgba(33, 150, 243, 0.05);
}

.box-title {
  font-size: 16px;
  font-weight: 700;
  color: #2f0538;
  margin: 0 0 12px;
}

.box-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.box-list li {
  font-size: 14px;
  line-height: 1.6;
  color: #555;
}

/* Platforms Grid */
.platforms-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin: 20px 0;
}

.platform-card {
  background: #f9f9f9;
  padding: 24px;
  border-radius: 10px;
  text-align: center;
  border: 2px solid #f0f0f0;
  transition: all 0.3s ease;
}

.platform-card:hover {
  border-color: #7b5ce0;
  box-shadow: 0 4px 12px rgba(123, 92, 224, 0.1);
}

.platform-icon {
  font-size: 36px;
  margin-bottom: 12px;
}

.platform-name {
  font-size: 16px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 8px;
}

.platform-desc {
  font-size: 13px;
  color: #666;
  line-height: 1.5;
  margin: 0;
}

/* Share Section */
.share-section {
  padding: 32px 0;
  border-top: 1px solid #e5e5e5;
  border-bottom: 1px solid #e5e5e5;
  margin-top: 40px;
}

.share-title {
  font-size: 16px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 16px;
}

.share-buttons {
  display: flex;
  align-items: center;
  gap: 12px;
}

.share-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  font-size: 12px;
  transition: all 0.22s ease;
}

.share-btn.twitter {
  background: #000;
  color: #fff;
}

.share-btn.twitter:hover {
  background: #222;
}

.share-btn.facebook {
  background: #1877f2;
  color: #fff;
}

.share-btn.facebook:hover {
  background: #166fe5;
}

.share-btn.linkedin {
  background: #0a66c2;
  color: #fff;
}

.share-btn.linkedin:hover {
  background: #095195;
}

.share-btn.telegram {
  background: #0088cc;
  color: #fff;
}

.share-btn.telegram:hover {
  background: #0077aa;
}

/* Related Articles */
.related-section {
  background: #f9f9f9;
  padding: 60px 20px;
  margin-top: 60px;
}

.section-container {
  max-width: 900px;
  margin: 0 auto;
}

.related-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-top: 32px;
}

.related-card {
  background: #fff;
  padding: 24px;
  border-radius: 10px;
  border: 1px solid #e5e5e5;
  transition: all 0.3s ease;
}

.related-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
}

.related-image {
  font-size: 36px;
  margin-bottom: 16px;
}

.related-title {
  font-size: 16px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 12px;
  line-height: 1.4;
}

.related-desc {
  font-size: 13px;
  color: #666;
  line-height: 1.5;
  margin: 0;
}

/* Newsletter */
.newsletter-section {
  padding: 60px 20px;
}

.newsletter-box {
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  color: #fff;
  padding: 48px;
  border-radius: 12px;
  text-align: center;
  max-width: 600px;
  margin: 0 auto;
}

.newsletter-title {
  font-size: 28px;
  font-weight: 700;
  margin: 0 0 12px;
}

.newsletter-desc {
  font-size: 16px;
  opacity: 0.9;
  margin: 0 0 24px;
}

.newsletter-form {
  display: flex;
  gap: 12px;
}

.newsletter-input {
  flex: 1;
  padding: 12px 16px;
  border: none;
  border-radius: 8px;
  font-size: 14px;
}

.newsletter-input::placeholder {
  color: #999;
}

.newsletter-btn {
  padding: 12px 24px;
  background: #7b5ce0;
  color: #fff;
  border: none;
  border-radius: 8px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s ease;
  white-space: nowrap;
}

.newsletter-btn:hover {
  background: #6a4dc7;
  transform: translateY(-2px);
}

/* Responsive */
@media (max-width: 1200px) {
  .content-container {
    grid-template-columns: 1fr;
  }

  .table-of-contents {
    position: static;
    margin-bottom: 40px;
  }

  .toc-nav {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
  }
}

@media (max-width: 768px) {
  .article-title {
    font-size: 32px;
  }

  .article-meta {
    flex-direction: column;
    align-items: flex-start;
    gap: 16px;
  }

  .section-title {
    font-size: 24px;
  }

  .platforms-grid {
    grid-template-columns: 1fr;
  }

  .related-grid {
    grid-template-columns: 1fr;
  }

  .toc-nav {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .article-hero {
    padding: 40px 16px;
  }

  .article-title {
    font-size: 24px;
  }

  .article-subtitle {
    font-size: 14px;
  }

  .article-image-section {
    height: 250px;
  }

  .article-content {
    padding: 32px 16px;
  }

  .section-title {
    font-size: 20px;
  }

  .section-text {
    font-size: 14px;
  }

  .newsletter-form {
    flex-direction: column;
  }
}
</style>
