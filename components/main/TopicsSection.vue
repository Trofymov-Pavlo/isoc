<template>
  <section class="topics">
    <div class="section-container">
      <h2 class="section-title">Thèmes</h2>
      <div class="topics-grid">
        <a href="#" class="topic-card" v-for="topic in ['Militaire', 'Politique', 'Humanitaire', 'Économie']" :key="topic">
          <span class="topic-name">{{ topic }}</span>
        </a>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
</script>

<style scoped>
.topics {
  padding: 48px 20px;
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
  padding-top: 48px;
}

.topics-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}

.topic-card {
  background: linear-gradient(135deg, rgba(123, 92, 224, 0.1), rgba(75, 47, 170, 0.1));
  border: 1px solid rgba(123, 92, 224, 0.2);
  padding: 24px;
  border-radius: 10px;
  text-align: center;
  text-decoration: none;
  color: #2f0538;
  font-weight: 600;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100px;
}

.topic-card:hover {
  background: linear-gradient(135deg, rgba(123, 92, 224, 0.2), rgba(75, 47, 170, 0.2));
  border-color: rgba(123, 92, 224, 0.4);
  transform: translateY(-4px);
}

.topic-name {
  font-size: 16px;
}

@media (max-width: 1100px) {
  .topics-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 680px) {
  .section-title {
    font-size: 22px;
  }

  .topics-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .section-title {
    font-size: 18px;
    padding-top: 24px;
  }

  .topics-grid {
    grid-template-columns: 1fr;
  }
}
</style>
