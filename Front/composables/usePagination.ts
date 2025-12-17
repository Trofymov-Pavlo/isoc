import { computed, ref, type Ref } from 'vue';

export function usePagination<T>(items: Ref<T[]>) {
  const currentPage = ref(1);
  const itemsPerPage = ref(20);

  const totalPages = computed(() => Math.ceil(items.value.length / itemsPerPage.value));

  const paginatedItems = computed(() => {
    const start = (currentPage.value - 1) * itemsPerPage.value;
    const end = start + itemsPerPage.value;
    return items.value.slice(start, end);
  });

  const setItemsPerPage = (count: number) => {
    itemsPerPage.value = count;
    currentPage.value = 1; // Reset to first page
  };

  const nextPage = () => {
    if (currentPage.value < totalPages.value) {
      currentPage.value++;
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  const prevPage = () => {
    if (currentPage.value > 1) {
      currentPage.value--;
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  const goToPage = (page: number) => {
    if (page >= 1 && page <= totalPages.value) {
      currentPage.value = page;
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  const visiblePages = computed(() => {
    const total = totalPages.value;
    const current = currentPage.value;
    const pages: (number | string)[] = [];

    if (total <= 7) {
      // Show all pages if 7 or less
      for (let i = 1; i <= total; i++) {
        pages.push(i);
      }
    } else {
      // Always show first page
      pages.push(1);

      if (current > 3) {
        pages.push('...');
      }

      // Show pages around current
      const start = Math.max(2, current - 1);
      const end = Math.min(total - 1, current + 1);

      for (let i = start; i <= end; i++) {
        pages.push(i);
      }

      if (current < total - 2) {
        pages.push('...');
      }

      // Always show last page
      pages.push(total);
    }

    return pages;
  });

  return {
    currentPage,
    itemsPerPage,
    totalPages,
    paginatedItems,
    setItemsPerPage,
    nextPage,
    prevPage,
    goToPage,
    visiblePages,
  };
}
