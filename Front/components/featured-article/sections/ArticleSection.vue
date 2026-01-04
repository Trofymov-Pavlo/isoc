<template>
  <section class="article-section" :id="id">
    <h2 class="section-title"><slot name="title" /></h2>
    <div class="section-body">
      <slot />
    </div>
  </section>
</template>

<script setup lang="ts">
defineProps<{ id: string }>();
</script>

<style scoped>
.article-section {
  margin: 48px 0;
  padding-bottom: 32px;
  border-bottom: 1px solid #f5f5f5;
}

.article-section:last-of-type {
  border-bottom: none;
}

.section-title {
  font-size: 28px;
  font-weight: 700;
  color: #2f0538;
  margin: 0 0 20px;
  line-height: 1.3;
}

.section-body {
  color: #4a4a55;
  font-size: 16px;
  line-height: 1.75;
}

.section-body :deep(p) {
  margin: 0 0 16px;
}

.section-body :deep(ul) {
  margin: 16px 0;
  padding-left: 24px;
}

.section-body :deep(li) {
  margin: 10px 0;
  color: #4a4a55;
}

.section-body :deep(strong) {
  color: #2f0538;
  font-weight: 600;
}
</style>
