<template>
  <section class="topnews">
    <div class="row">
      <article
        v-for="(it, i) in top4"
        :key="(it.link || it.title) + i"
        class="item"
      >
        <a v-if="it.image" :href="it.link" target="_blank" rel="noopener" class="thumb">
          <img :src="it.image" :alt="it.title" loading="lazy" />
        </a>

        <div class="meta">
          <p v-if="it.source" class="source">{{ it.source }}</p>
          <a :href="it.link" target="_blank" rel="noopener" class="title">{{ it.title }}</a>
        </div>
      </article>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed, onMounted } from "vue";
import { useArticles } from "@/composables/useArticles";

const { all, load } = useArticles({
  apiBase: "http://127.0.0.1:5000",
  query: "ukraine",
  hours: 24,
  meta: 1,
});

const top4 = computed(() => 
  all.value.filter(a => a.image).slice(0, 4)
);

onMounted(() => {
  load();
  setInterval(load, 5 * 60 * 1000);
});
</script>



<style scoped lang="css">
.topnews {
  background: #fff;
  border-top: 1px solid #eee;
  border-bottom: 1px solid #eee;
  padding: 8px 8px;
}

.row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
  align-items: flex-start;
}

.item {
  display: grid;
  grid-template-columns: 55px 1fr; /* image carrée */
  gap: 8px;
  min-height: 40px;
}

/* IMAGE CARRÉE */
.thumb img {
  width: 55px;
  height: 55px;        /* HAUTEUR = LARGEUR */
  object-fit: cover;   /* coupe pour avoir un carré propre */
  border-radius: 4px;
  display: block;
}

.meta {
  display: grid;
  gap: 2px;
}

/* très petit, comme Mediapart */
.source {
  margin: 0;
  color: #a00;
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .25px;
  line-height: 1.1;
}

.title {
  color: #111;
  text-decoration: none;
  font-weight: 700;
  font-size: 11px;   /* compact */
  line-height: 1.25;
}

.title:hover {
  text-decoration: underline;
}

@media (max-width: 1000px) {
  .row {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 600px) {
  .row {
    grid-template-columns: 1fr;
  }
.item {
  display: grid;
  grid-template-columns: 55px 1fr;
  gap: 8px;
  min-height: 40px;
  align-items: center;     
}

  .thumb img {
    width: 50px;
    height: 50px;
  }
  .title {
    font-size: 12px;
  }
  .source {
    font-size: 9.5px;
  }
}

</style>    