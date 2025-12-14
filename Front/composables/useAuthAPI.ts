import { ref } from 'vue';

const API_BASE = 'http://127.0.0.1:8000/api/accounts';

export const useAuthAPI = () => {
  const loading = ref(false);
  const error = ref('');
  const user = ref(null);
  const accessToken = ref('');
  const refreshToken = ref('');

  const setTokens = (access: string, refresh: string) => {
    accessToken.value = access;
    refreshToken.value = refresh;
    if (process.client) {
      localStorage.setItem('access_token', access);
      localStorage.setItem('refresh_token', refresh);
    }
  };

  const loadTokensFromStorage = () => {
    if (process.client) {
      accessToken.value = localStorage.getItem('access_token') || '';
      refreshToken.value = localStorage.getItem('refresh_token') || '';
    }
  };

  const clearTokens = () => {
    accessToken.value = '';
    refreshToken.value = '';
    user.value = null;
    if (process.client) {
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      localStorage.removeItem('auth_logged_in');
      localStorage.removeItem('auth_remember');
    }
  };

  const signup = async (email: string, username: string, password: string, firstName = '', lastName = '') => {
    loading.value = true;
    error.value = '';
    try {
      const response = await fetch(`${API_BASE}/signup/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, username, password, password_confirm: password, first_name: firstName, last_name: lastName }),
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.email?.[0] || data.password?.[0] || 'Signup failed');
      setTokens(data.access, data.refresh);
      user.value = data.user;
      return data;
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Signup error';
      throw err;
    } finally {
      loading.value = false;
    }
  };

  const login = async (email: string, password: string, rememberMe = false) => {
    loading.value = true;
    error.value = '';
    try {
      const response = await fetch(`${API_BASE}/login/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password, remember_me: rememberMe }),
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.error || 'Login failed');
      setTokens(data.access, data.refresh);
      user.value = data.user;
      if (process.client) {
        localStorage.setItem('auth_logged_in', '1');
        localStorage.setItem('auth_remember', rememberMe ? '1' : '0');
      }
      return data;
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Login error';
      throw err;
    } finally {
      loading.value = false;
    }
  };

  const logout = async () => {
    loading.value = true;
    try {
      await fetch(`${API_BASE}/logout/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${accessToken.value}`,
        },
        body: JSON.stringify({ refresh: refreshToken.value }),
      });
    } finally {
      clearTokens();
      loading.value = false;
    }
  };

  const passwordReset = async (email: string) => {
    loading.value = true;
    error.value = '';
    try {
      const response = await fetch(`${API_BASE}/password_reset/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email }),
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.error || 'Password reset failed');
      return data;
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Password reset error';
      throw err;
    } finally {
      loading.value = false;
    }
  };

  const passwordResetConfirm = async (token: string, newPassword: string) => {
    loading.value = true;
    error.value = '';
    try {
      const response = await fetch(`${API_BASE}/password_reset_confirm/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ token, new_password: newPassword, new_password_confirm: newPassword }),
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.error || 'Password reset confirm failed');
      return data;
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Password reset confirm error';
      throw err;
    } finally {
      loading.value = false;
    }
  };

  const me = async () => {
    if (!accessToken.value) loadTokensFromStorage();
    if (!accessToken.value) return null;
    try {
      const response = await fetch(`${API_BASE}/me/`, {
        headers: { 'Authorization': `Bearer ${accessToken.value}` },
      });
      if (response.ok) {
        const data = await response.json();
        user.value = data;
        return data;
      }
    } catch (err) {
      console.error('Me fetch error:', err);
    }
    return null;
  };

  const updateProfile = async (username: string, email: string, firstName = '', lastName = '') => {
    if (!accessToken.value) loadTokensFromStorage();
    loading.value = true;
    error.value = '';
    try {
      const response = await fetch(`${API_BASE}/update_profile/`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${accessToken.value}`,
        },
        body: JSON.stringify({ username, email, first_name: firstName, last_name: lastName }),
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.email?.[0] || data.username?.[0] || 'Profile update failed');
      user.value = data;
      return data;
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Profile update error';
      throw err;
    } finally {
      loading.value = false;
    }
  };

  const changePassword = async (oldPassword: string, newPassword: string) => {
    if (!accessToken.value) loadTokensFromStorage();
    loading.value = true;
    error.value = '';
    try {
      const response = await fetch(`${API_BASE}/change_password/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${accessToken.value}`,
        },
        body: JSON.stringify({ 
          old_password: oldPassword, 
          new_password: newPassword,
          new_password_confirm: newPassword 
        }),
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.old_password?.[0] || data.new_password?.[0] || 'Password change failed');
      return data;
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Password change error';
      throw err;
    } finally {
      loading.value = false;
    }
  };

  return {
    loading,
    error,
    user,
    accessToken,
    refreshToken,
    signup,
    login,
    logout,
    passwordReset,
    passwordResetConfirm,
    me,
    updateProfile,
    changePassword,
    setTokens,
    loadTokensFromStorage,
    clearTokens,
  };
};
