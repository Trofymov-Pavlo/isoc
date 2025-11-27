<template>
  <div class="ticker">
    <div class="ticker-inner" :class="{ loading: pending }">
      <template v-if="pending">
        <span>Chargement...</span>
      </template>

      <template v-else-if="error">
        <span class="error">Erreur de chargement</span>
      </template>

      <template v-else>
        <div class="ticker-content">
          <div
            class="tick-item"
            v-for="(item, i) in data"
            :key="i"
          >
            <a :href="item.link" target="_blank" rel="noopener">
              {{ item.title }}
            </a>
          </div>

          <!-- duplication pour boucle infinie -->
          <div
            class="tick-item"
            v-for="(item, i) in data"
            :key="'dup-' + i"
          >
            <a :href="item.link" target="_blank" rel="noopener">
              {{ item.title }}
            </a>
          </div>
        </div>
      </template>
    </div>
  </div>
</template>

<script setup lang="ts">
const { data, pending, error } = await useAsyncData("articles", () =>
  $fetch("http://127.0.0.1:5000/articles", {
    query: {
      q: "ukraine",
      page: 1
    }
  })
);
</script>

<style scoped>
.ticker {
  background: #0f5f72;
  color: white;
  overflow: hidden;
  white-space: nowrap;
  padding: 8px 0;
  font-size: 14px;
}

.ticker-inner {
  display: flex;
  align-items: center;
  overflow: hidden;
}

.ticker-content {
  display: inline-flex;
  gap: 40px;
  padding-left: 100%;
  animation: scroll-left 50s linear infinite;
}

.tick-item a {
  color: white;
  text-decoration: none;
}

.tick-item a:hover {
  text-decoration: underline;
}

.loading {
  opacity: 0.5;
}

@keyframes scroll-left {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
</style>
