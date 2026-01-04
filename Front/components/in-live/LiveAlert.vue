<template>
  <div class="alert alert-error">
    <span class="alert-icon">⚠️</span>
    <span>{{ message }}</span>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{ message: string }>();
</script>

<style scoped>
.alert {
  max-width: 1200px;
  margin: 0 auto 24px;
  padding: 14px 18px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 14px;
}

.alert-error {
  background: rgba(255, 107, 107, 0.1);
  border: 1px solid rgba(255, 107, 107, 0.3);
  color: #d32f2f;
}

.alert-icon {
  font-size: 18px;
  flex-shrink: 0;
}
</style>
