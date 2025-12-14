<template>
  <section class="podcast-section">
    <div class="section-container">
      <h2 class="section-title">Podcast</h2>
      <div class="podcast-card">
        <div class="podcast-image">
          <!-- Podcast cover will go here -->
        </div>
        <div class="podcast-content">
          <span class="podcast-badge">Nouveau</span>
          <h3 class="podcast-title">La Guerre de l'Information</h3>
          <p class="podcast-desc">Décryptez les stratégies d'influence, la désinformation et la bataille informationnelle du conflit Ukraine-Russie. Avec nos experts en géopolitique et communication.</p>
          <div class="podcast-meta">
            <span class="podcast-duration">45 min</span>
            <span class="podcast-date">Il y a 2h</span>
          </div>
          <button class="podcast-play-btn">
            <span class="play-icon">▶</span>
            Écouter l'épisode
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
</script>

<style scoped>
.podcast-section {
  padding: 24px 20px;
  background: #ffffff;
}

.section-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.section-title {
  margin: 0;
  font-size: 28px;
  font-weight: 700;
  color: #2f0538;
  margin-bottom: 32px;
  padding-top: 24px;
}

.section-title::before {
  content: "";
  display: inline-block;
  vertical-align: middle;
  width: 6px;
  height: 28px;
  background: linear-gradient(180deg, #2f0538, #4b2faa);
  margin-right: 12px;
  border-radius: 3px;
}

.podcast-card {
  background: #fff;
  border-radius: 12px;
  padding: 32px;
  display: grid;
  grid-template-columns: 250px 1fr;
  gap: 32px;
  align-items: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
}

.podcast-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

.podcast-image {
  width: 250px;
  height: 250px;
  background: linear-gradient(135deg, #2f0538, #4b2faa);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 14px;
}

.podcast-content {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.podcast-badge {
  display: inline-block;
  background: #ff6b6b;
  color: #fff;
  padding: 6px 12px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  width: fit-content;
}

.podcast-title {
  margin: 0;
  font-size: 24px;
  font-weight: 700;
  color: #1a1a1a;
  line-height: 1.3;
}

.podcast-desc {
  margin: 0;
  font-size: 15px;
  line-height: 1.6;
  color: #555;
}

.podcast-meta {
  display: flex;
  gap: 20px;
  font-size: 13px;
  color: #999;
  font-weight: 500;
}

.podcast-play-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: linear-gradient(135deg, #2f0538, #4b2faa);
  color: #fff;
  border: none;
  padding: 14px 28px;
  border-radius: 8px;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s ease;
  width: fit-content;
  box-shadow: 0 4px 12px rgba(47, 5, 56, 0.3);
}

.podcast-play-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(47, 5, 56, 0.4);
}

.play-icon {
  font-size: 14px;
}

@media (max-width: 1100px) {
  .podcast-card {
    grid-template-columns: 1fr;
    text-align: center;
  }

  .podcast-image {
    margin: 0 auto;
  }

  .podcast-badge {
    margin: 0 auto;
  }

  .podcast-play-btn {
    margin: 0 auto;
  }
}

@media (max-width: 680px) {
  .section-title {
    font-size: 22px;
  }

  .podcast-card {
    padding: 24px;
  }

  .podcast-image {
    width: 200px;
    height: 200px;
  }

  .podcast-title {
    font-size: 20px;
  }

  .podcast-desc {
    font-size: 14px;
  }
}

@media (max-width: 480px) {
  .section-title {
    font-size: 18px;
    padding-top: 24px;
  }

  .podcast-image {
    width: 150px;
    height: 150px;
  }

  .podcast-title {
    font-size: 18px;
  }
}
</style>
