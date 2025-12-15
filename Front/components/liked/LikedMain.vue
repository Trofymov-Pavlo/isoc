<template>
  <main class="liked-page">
    <PageHero
      title="Articles likés"
      subtitle="Retrouvez tous les articles que vous avez sauvegardés"
      badge="Mes favoris"
      badge-icon="❤️"
    />

    <section class="liked-wrapper">
      <div class="liked-content" v-if="items.length">
        <div class="grid">
          <article v-for="it in items" :key="it.id" class="item">
            <h3 class="title">{{ it.title }}</h3>
            <p class="meta">{{ it.source }} — {{ it.date }}</p>
          </article>
        </div>
      </div>
      <div class="empty-state" v-else>
        <span class="empty-icon">📌</span>
        <p class="empty-text">Aucun article liké pour le moment.</p>
        <p class="empty-hint">Commencez à liker des articles pour les retrouver ici !</p>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
import PageHero from '~/components/shared/PageHero.vue';

const items: Array<{ id:number; title:string; source:string; date:string; }> = []
</script>

<style scoped>
.liked-page {
  min-height: 100vh;
  background: #fff;
}

.liked-wrapper {
  max-width: 1400px;
  margin: 0 auto;
  padding: 48px calc(2vw) 60px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 24px;
}

.item {
  background: #fff;
  border: 1px solid #e5e5e5;
  border-radius: 12px;
  padding: 24px;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.item:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  border-color: #d0d0d0;
}

.title {
  margin: 0 0 12px;
  font-size: 16px;
  font-weight: 700;
  color: #1a1a1a;
  line-height: 1.4;
}

.meta {
  margin: 0;
  font-size: 13px;
  color: #999;
}

.empty-state {
  text-align: center;
  padding: 80px 20px;
}

.empty-icon {
  font-size: 64px;
  display: block;
  margin-bottom: 16px;
  opacity: 0.5;
}

.empty-text {
  font-size: 18px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0 0 8px;
}

.empty-hint {
  font-size: 14px;
  color: #999;
  margin: 0;
}

@media (max-width: 968px) {
  .grid {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  }
}
</style>

