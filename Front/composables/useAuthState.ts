import { onMounted, watchEffect } from 'vue';

export const useAuthState = () => {
  const isAuthenticated = useState<boolean>('auth/loggedIn', () => {
    // Initialiser depuis le localStorage côté client
    if (process.server) return false;
    const storedAuth = localStorage.getItem('auth_logged_in');
    return storedAuth === '1';
  });
  
  const rememberMe = useState<boolean>('auth/remember', () => {
    // Initialiser depuis le localStorage côté client
    if (process.server) return false;
    const storedRemember = localStorage.getItem('auth_remember');
    return storedRemember === '1';
  });

  const loadFromStorage = () => {
    if (process.server) return;
    const storedAuth = localStorage.getItem('auth_logged_in');
    const storedRemember = localStorage.getItem('auth_remember');
    if (storedAuth === '1') {
      isAuthenticated.value = true;
    } else {
      isAuthenticated.value = false;
    }
    if (storedRemember === '1') {
      rememberMe.value = true;
    } else {
      rememberMe.value = false;
    }
  };

  const persist = () => {
    if (process.server) return;
    localStorage.setItem('auth_logged_in', isAuthenticated.value ? '1' : '0');
    localStorage.setItem('auth_remember', rememberMe.value ? '1' : '0');
  };

  const setAuth = (value: boolean, remember = false) => {
    isAuthenticated.value = value;
    rememberMe.value = remember;
    persist();
  };

  onMounted(() => {
    loadFromStorage();
  });

  // Surveiller les changements et persister automatiquement
  watchEffect(() => {
    persist();
  });

  return { isAuthenticated, rememberMe, setAuth, loadFromStorage };
};
