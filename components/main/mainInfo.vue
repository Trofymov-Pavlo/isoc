<template>
  <aside class="mini-sidebar">
    <h3 class="mini-title">À la une</h3>

    <article
      v-for="a in articles"
      :key="a.id"
      class="mini-item"
    >
      <NuxtLink :to="`/article/${a.slug}`" class="mini-link">
        <div v-if="a.image" class="thumb-wrapper">
          <img :src="a.image" alt="" />
        </div>
        <div class="mini-text">
          <p v-if="a.category" class="mini-category">
            {{ a.category }}
          </p>
          <p class="mini-headline">
            {{ a.title }}
          </p>
        </div>
      </NuxtLink>
    </article>
  </aside>
</template>

<script setup lang="ts">
interface Article {
  id: number
  slug: string
  title: string
  category?: string
  image?: string
}

defineProps<{
  articles: Article[]
}>()
</script>

<style scoped lang="scss">
.mini-sidebar {
  width: 260px;
  border-right: 1px solid #eee;
  padding-right: 16px;
}

.mini-title {
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: .08em;
  color: #777;
  margin-bottom: 8px;
}

.mini-item {
  padding: 8px 0;
  border-bottom: 1px solid #f0f0f0;
}

.mini-link {
  display: flex;
  gap: 8px;
  text-decoration: none;
  color: inherit;
}

.thumb-wrapper {
  flex-shrink: 0;
  width: 70px;
  height: 50px;
  overflow: hidden;
}

.thumb-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.mini-text {
  display: flex;
  flex-direction: column;
}

.mini-category {
  font-size: 10px;
  text-transform: uppercase;
  color: #b33;
  margin-bottom: 2px;
}

.mini-headline {
  font-size: 12px;
  line-height: 1.2;
}
</style>
