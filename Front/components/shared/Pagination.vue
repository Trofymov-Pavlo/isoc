<template>
  <div class="pagination-controls">
    <!-- Items per page selector -->
    <div class="items-per-page">
      <span class="label">Afficher :</span>
      <button
        v-for="count in [10, 20, 50, 100]"
        :key="count"
        :class="['page-size-btn', { active: itemsPerPage === count }]"
        @click="onItemsPerPageChange(count)"
      >
        {{ count }}
      </button>
    </div>

    <!-- Page navigation -->
    <div v-if="totalPages > 1" class="page-navigation">
      <button
        class="nav-btn"
        :disabled="currentPage === 1"
        @click="onPrevPage"
      >
        Précédent
      </button>

      <button
        v-for="(page, index) in visiblePages"
        :key="index"
        :class="['page-btn', { active: page === currentPage, ellipsis: page === '...' }]"
        :disabled="page === '...'"
        @click="typeof page === 'number' && onGoToPage(page)"
      >
        {{ page }}
      </button>

      <button
        class="nav-btn"
        :disabled="currentPage === totalPages"
        @click="onNextPage"
      >
        Suivant
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  currentPage: number;
  totalPages: number;
  itemsPerPage: number;
  visiblePages: (number | string)[];
}>();

const emit = defineEmits<{
  (e: 'update:itemsPerPage', value: number): void;
  (e: 'next'): void;
  (e: 'prev'): void;
  (e: 'goTo', page: number): void;
}>();

const onItemsPerPageChange = (count: number) => emit('update:itemsPerPage', count);
const onNextPage = () => emit('next');
const onPrevPage = () => emit('prev');
const onGoToPage = (page: number) => emit('goTo', page);
</script>

<style scoped>
.pagination-controls {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 32px 0;
  gap: 24px;
  flex-wrap: wrap;
}

.items-per-page {
  display: flex;
  align-items: center;
  gap: 8px;
}

.label {
  font-size: 14px;
  color: #666;
  font-weight: 500;
}

.page-size-btn {
  padding: 6px 12px;
  border: 1px solid #ddd;
  background: #f8f8f8;
  color: #666;
  border-radius: 6px;
  cursor: pointer;
  font-size: 13px;
  font-weight: 500;
  transition: all 0.2s ease;
}

.page-size-btn:hover {
  background: #fff;
  border-color: #2f0538;
  color: #2f0538;
}

.page-size-btn.active {
  background: #2f0538;
  color: white;
  border-color: #2f0538;
}

.page-navigation {
  display: flex;
  align-items: center;
  gap: 6px;
}

.nav-btn,
.page-btn {
  padding: 8px 14px;
  border: 1px solid #ddd;
  background: #f8f8f8;
  color: #666;
  border-radius: 6px;
  cursor: pointer;
  font-size: 13px;
  font-weight: 500;
  transition: all 0.2s ease;
  min-width: 40px;
}

.nav-btn:hover:not(:disabled),
.page-btn:hover:not(:disabled):not(.ellipsis) {
  background: #fff;
  border-color: #2f0538;
  color: #2f0538;
}

.page-btn.active {
  background: #2f0538;
  color: white;
  border-color: #2f0538;
}

.page-btn.ellipsis {
  cursor: default;
  border-color: transparent;
  background: transparent;
}

.nav-btn:disabled,
.page-btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

@media (max-width: 680px) {
  .pagination-controls {
    flex-direction: column;
    align-items: stretch;
  }

  .items-per-page {
    justify-content: center;
  }

  .page-navigation {
    justify-content: center;
    flex-wrap: wrap;
  }
}
</style>
