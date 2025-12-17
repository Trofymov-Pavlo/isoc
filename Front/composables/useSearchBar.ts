import { ref } from 'vue';

export interface UseSearchBar {
  query: ReturnType<typeof ref<string>>;
  setQuery: (val: string) => void;
  clear: () => void;
  onEnter: () => void;
}

export function useSearchBar(onEnter?: () => void): UseSearchBar {
  const query = ref('');

  function setQuery(val: string) {
    query.value = val;
  }

  function clear() {
    query.value = '';
    if (onEnter) onEnter();
  }

  function onEnterHandler() {
    if (onEnter) onEnter();
  }

  return { query, setQuery, clear, onEnter: onEnterHandler };
}
