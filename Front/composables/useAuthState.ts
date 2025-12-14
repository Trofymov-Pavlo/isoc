import { onMounted } from 'vue';

export const useAuthState = () => {
  const isAuthenticated = useState<boolean>('auth/loggedIn', () => false);
  const rememberMe = useState<boolean>('auth/remember', () => false);

  const loadFromStorage = () => {
    if (process.server) return;
    const storedAuth = localStorage.getItem('auth_logged_in');
    const storedRemember = localStorage.getItem('auth_remember');
    if (storedAuth === '1') {
      isAuthenticated.value = true;
    }
    if (storedRemember === '1') {
      rememberMe.value = true;
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

  return { isAuthenticated, rememberMe, setAuth };
};
