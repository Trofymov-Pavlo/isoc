<template>
  <section class="hero">
    <div class="hero-text">
      <p class="hero-category">
        {{ category }}
      </p>

      <h1 class="hero-title">
        {{ title }}
      </h1>

      <p class="hero-chapo">
        {{ chapo }}
      </p>

      <p class="hero-author">
        par {{ author }}
      </p>
    </div>

    <div class="hero-image">
      <img :src="image" alt="" />
      <p v-if="imageCredit" class="hero-credit">
        © {{ imageCredit }}
      </p>
    </div>
  </section>
</template>

<script setup lang="ts">
defineProps<{
  category: string
  title: string
  chapo: string
  author: string
  image: string
  imageCredit?: string
}>()
</script>

<style scoped lang="scss">
.hero {
  display: grid;
  grid-template-columns: 2fr 1.5fr;
  gap: 32px;
  align-items: start;
  padding: 24px 0;
  border-top: 1px solid #eee;
}

.hero-text {
  max-width: 650px;
}

.hero-category {
  font-size: 14px;
  font-weight: 700;
  text-transform: none;
  margin-bottom: 8px;
}

.hero-title {
  font-family: "Playfair Display", serif;
  font-size: 40px;
  line-height: 1.05;
  margin: 0 0 16px;
}

.hero-chapo {
  font-size: 16px;
  line-height: 1.6;
  color: #555;
  margin-bottom: 12px;
}

.hero-author {
  font-size: 14px;
  color: #777;
}

.hero-image {
  text-align: right;
}

.hero-image img {
  max-width: 100%;
  height: auto;
  display: block;
  margin-left: auto;
}

.hero-credit {
  font-size: 12px;
  color: #777;
  margin-top: 4px;
}
  
/* responsive */
@media (max-width: 900px) {
  .hero {
    grid-template-columns: 1fr;
  }

  .hero-image {
    text-align: left;
  }

  .hero-title {
    font-size: 30px;
  }
}
</style>
    