import { ref } from 'vue';

interface RateLimitConfig {
  maxAttempts: number;
  windowMs: number; // en millisecondes
  lockoutMs?: number; // durée de blocage en ms (optionnel)
}

export const useRateLimit = (config: RateLimitConfig) => {
  const attempts = ref(0);
  const lastAttemptTime = ref<number | null>(null);
  const isLockedOut = ref(false);
  const lockoutRemainingSeconds = ref(0);
  let lockoutTimer: any = null;

  const checkLimit = (): boolean => {
    const now = Date.now();
    
    // Si on est bloqué, on retourne false
    if (isLockedOut.value) {
      return false;
    }

    // Réinitialiser si la fenêtre de temps est dépassée
    if (lastAttemptTime.value && now - lastAttemptTime.value > config.windowMs) {
      attempts.value = 0;
      lastAttemptTime.value = null;
    }

    // Incrémenter les tentatives
    attempts.value++;
    lastAttemptTime.value = now;

    // Vérifier si limite atteinte
    if (attempts.value >= config.maxAttempts) {
      isLockedOut.value = true;
      
      // Mettre en place le blocage si configuré
      if (config.lockoutMs) {
        startLockout();
      }
      
      return false;
    }

    return true;
  };

  const startLockout = () => {
    if (lockoutTimer) clearInterval(lockoutTimer);
    
    const lockoutMs = config.lockoutMs || 300000; // 5 min par défaut
    const endTime = Date.now() + lockoutMs;

    lockoutTimer = setInterval(() => {
      const remaining = Math.ceil((endTime - Date.now()) / 1000);
      lockoutRemainingSeconds.value = Math.max(0, remaining);
      
      if (remaining <= 0) {
        clearInterval(lockoutTimer);
        isLockedOut.value = false;
        attempts.value = 0;
        lastAttemptTime.value = null;
      }
    }, 100);
  };

  const reset = () => {
    attempts.value = 0;
    lastAttemptTime.value = null;
    isLockedOut.value = false;
    lockoutRemainingSeconds.value = 0;
    if (lockoutTimer) clearInterval(lockoutTimer);
  };

  const getAttemptsRemaining = (): number => {
    return Math.max(0, config.maxAttempts - attempts.value);
  };

  return {
    checkLimit,
    reset,
    isLockedOut,
    lockoutRemainingSeconds,
    attempts,
    getAttemptsRemaining
  };
};
