<template>
  <div class="home">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-content">
        <!-- Hero content will go here -->
      </div>
    </section>

    <!-- Featured Articles Section -->
    <section class="featured">
      <div class="section-container">
        <h2 class="section-title">À la une</h2>
        <div class="featured-grid">
          <!-- Featured articles will go here -->
        </div>
      </div>
    </section>

    <!-- Latest News Section -->
    <section class="latest-news">
      <div class="section-container">
        <h2 class="section-title">Dernières actualités</h2>
        <div class="news-grid">
          <!-- Latest news articles will go here -->
        </div>
      </div>
    </section>

    <!-- Live Section -->
    <section class="live-section">
      <div class="section-container">
        <h2 class="section-title">En direct</h2>
        <div class="live-content">
          <!-- Live content will go here -->
        </div>
      </div>
    </section>

    <!-- Topics Section -->
    <section class="topics">
      <div class="section-container">
        <h2 class="section-title">Thèmes</h2>
        <div class="topics-grid">
          <!-- Topics will go here -->
        </div>
      </div>
    </section>

    <!-- Newsletter Section -->
    <section class="newsletter">
      <div class="section-container">
        <div class="newsletter-content">
          <!-- Newsletter signup will go here -->
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">

</script>

<style scoped>
.home {
  background: #ffffff;
  min-height: 100vh;
  padding-bottom: 60px;
}

/* Hero Section */
.hero {
  width: 100%;
  min-height: 500px;
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
}

.hero-content {
  max-width: 1200px;
  width: 100%;
  text-align: center;
}

/* Section Container */
.section-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Section Title */
.section-title {
  margin: 0;
  font-size: 28px;
  font-weight: 700;
  color: #2f0538;
  margin-bottom: 32px;
  padding-top: 48px;
}

/* Featured Section */
.featured {
  background: #ffffff;
}

.featured-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  min-height: 300px;
}

/* Latest News Section */
.latest-news {
  background: #ffffff;
}

.news-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  min-height: 400px;
}

/* Live Section */
.live-section {
  background: #f5f5f5;
  padding-bottom: 48px;
}

.live-content {
  min-height: 350px;
  background: #ffffff;
  border-radius: 10px;
  padding: 24px;
}

/* Topics Section */
.topics {
  background: #ffffff;
}

.topics-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  min-height: 250px;
}

/* Newsletter Section */
.newsletter {
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  padding: 60px 20px;
  margin-top: 48px;
}

.newsletter-content {
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
  min-height: 200px;
}

/* Responsive */
@media (max-width: 1100px) {
  .featured-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .news-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .topics-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 680px) {
  .hero {
    min-height: 350px;
    padding: 30px 16px;
  }

  .section-title {
    font-size: 22px;
    padding-top: 32px;
    margin-bottom: 24px;
  }

  .featured-grid,
  .news-grid {
    grid-template-columns: 1fr;
    gap: 16px;
  }

  .topics-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .section-container {
    padding: 0 16px;
  }

  .newsletter {
    padding: 40px 16px;
  }
}

@media (max-width: 480px) {
  .hero {
    min-height: 280px;
  }

  .section-title {
    font-size: 18px;
    padding-top: 24px;
  }

  .topics-grid {
    grid-template-columns: 1fr;
  }
}
</style>
