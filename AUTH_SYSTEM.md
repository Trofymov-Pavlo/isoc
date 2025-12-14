# Système d'Authentification ISOC

## Vue d'ensemble

Système d'authentification complet avec Django + DRF (JWT) + Nuxt 4.

### Architecture

- **Backend**: Django 6.0 + Django REST Framework + JWT (Simple JWT)
- **Frontend**: Nuxt 4 avec état auth global partagé via localStorage
- **Database**: SQLite (dev) / PostgreSQL (prod ready)

## Backend Django

### Installation

```bash
cd Back
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # Optional, admin créé par défaut
python manage.py runserver 8000
```

### Endpoints API

#### Signup
```
POST /api/accounts/signup/
{
  "email": "user@example.com",
  "username": "john_doe",
  "password": "secure_password_123",
  "password_confirm": "secure_password_123",
  "first_name": "John",
  "last_name": "Doe"
}

Response (201):
{
  "user": { "id": 1, "email": "user@example.com", ... },
  "access": "JWT_ACCESS_TOKEN",
  "refresh": "JWT_REFRESH_TOKEN"
}
```

#### Login
```
POST /api/accounts/login/
{
  "email": "user@example.com",
  "password": "secure_password_123",
  "remember_me": true
}

Response (200):
{
  "user": { ... },
  "access": "JWT_ACCESS_TOKEN",
  "refresh": "JWT_REFRESH_TOKEN",
  "remember_me": true
}
```

#### Logout
```
POST /api/accounts/logout/
Headers: Authorization: Bearer {access_token}
Body: { "refresh": "JWT_REFRESH_TOKEN" }

Response (200):
{ "message": "Logged out successfully" }
```

#### Get Current User
```
GET /api/accounts/me/
Headers: Authorization: Bearer {access_token}

Response (200):
{ "id": 1, "email": "user@example.com", "username": "john_doe", ... }
```

#### Password Reset
```
POST /api/accounts/password_reset/
{
  "email": "user@example.com"
}

Response (200):
{
  "message": "Password reset link sent to email",
  "token": "RESET_TOKEN"
}
```

#### Password Reset Confirm
```
POST /api/accounts/password_reset_confirm/
{
  "token": "RESET_TOKEN",
  "new_password": "new_password_123",
  "new_password_confirm": "new_password_123"
}

Response (200):
{ "message": "Password reset successfully" }
```

### Modèle de Données

**CustomUser (extends Django AbstractUser)**
- `email` (unique)
- `username`
- `password_hash` (SHA-256)
- `first_name`, `last_name`
- `remember_me` (boolean)
- `password_reset_token` (string, nullable)

## Frontend Nuxt

### Installation & Lancement

```bash
cd Front
npm install
npm run dev  # Localhost 3000
```

### Composables

#### `useAuthAPI()`
Client API pour communiquer avec le backend Django.

```typescript
import { useAuthAPI } from '~/composables/useAuthAPI';

const { 
  signup,           // (email, username, password, firstName, lastName) => Promise
  login,            // (email, password, rememberMe) => Promise
  logout,           // () => Promise
  passwordReset,    // (email) => Promise
  passwordResetConfirm,  // (token, newPassword) => Promise
  me,               // () => Promise (get current user)
  loading,          // ref<boolean>
  error,            // ref<string>
  user,             // ref<User | null>
  accessToken,      // ref<string>
  refreshToken      // ref<string>
} = useAuthAPI();
```

#### `useAuthState()`
État d'authentification global (localStorage persisté).

```typescript
import { useAuthState } from '~/composables/useAuthState';

const {
  isAuthenticated,  // ref<boolean>
  rememberMe,       // ref<boolean>
  setAuth          // (value: boolean, remember?: boolean) => void
} = useAuthState();
```

### Pages d'Authentification

- `/connexion` - Login
- `/signup` - Création de compte
- `/support` - Mot de passe oublié (réinitialisation)

### Flux de Connexion

1. User remplit le formulaire de login (`/connexion`)
2. Frontend appelle `useAuthAPI.login(email, password, rememberMe)`
3. Backend valide et retourne les tokens JWT
4. Frontend stocke tokens + `rememberMe` dans localStorage
5. Frontend met à jour `useAuthState().setAuth(true, rememberMe)`
6. Bouton "Compte" du sub-header change de "Compte" → "Mon compte"
7. User est redirigé vers `/`

### Flux de Création de Compte

1. User remplit le formulaire de signup (`/signup`)
2. Frontend appelle `useAuthAPI.signup(...)`
3. Backend crée le compte et retourne les tokens
4. Même flux que login
5. User redirigé vers `/`

### Réinitialisation de Mot de Passe

1. User clique "Mot de passe oublié ?" sur `/connexion` → va à `/support`
2. Rentre son email
3. Backend génère un token et le retourne (IRL: envoi par email)
4. User utilise le token pour réinitialiser son mot de passe
5. Peut alors se reconnecter

## Features Implémentées

✅ **Signup** - Création de compte avec validation  
✅ **Login** - JWT authentication  
✅ **Remember Me** - Persiste la connexion via localStorage  
✅ **Logout** - Invalidation des tokens  
✅ **Password Reset** - Flow complet de réinitialisation  
✅ **JWT Tokens** - Access + Refresh tokens  
✅ **CORS** - Frontend ↔ Backend communication  
✅ **Validation** - Email, password, username sur backend et frontend  
✅ **UI State** - Navigation reflect état d'auth (bouton "Compte")  
✅ **Auto-import** - Composables et composants Nuxt auto-importés  

## Variables d'Environnement (Optional)

### Backend (.env ou settings.py)
```
DJANGO_SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,localhost:3000
DATABASE_URL=sqlite:///db.sqlite3
JWT_ALGORITHM=HS256
ACCESS_TOKEN_LIFETIME=3600  # 1 hour
REFRESH_TOKEN_LIFETIME=604800  # 7 days
```

### Frontend (.env ou nuxt.config.ts)
```
NUXT_PUBLIC_API_BASE=http://127.0.0.1:8000
```

## Tests

### Backend API Tests
```bash
cd Back
python test_auth_api.sh
# ou run Python test script
```

### Frontend
```bash
cd Front
npm run build  # Vérifier la compilation
npm run dev    # Tester manuellement
```

## Déploiement (Roadmap)

- [ ] PostgreSQL au lieu de SQLite
- [ ] Refresh token rotation
- [ ] Email verification
- [ ] Google OAuth intégration
- [ ] Rate limiting
- [ ] 2FA
- [ ] Token blacklist
- [ ] Better error handling

## Troubleshooting

### CORS Error
→ Vérifier que `CORS_ALLOWED_ORIGINS` dans `Back/isoc_auth/settings.py` inclut localhost:3000

### Token Expired
→ Utiliser le `refresh_token` pour générer un nouveau `access_token` (endpoint à implémenter)

### API Not Responding
→ Vérifier que Django runserver est actif : `python manage.py runserver 8000`

---

**Créé le**: 14 Décembre 2025  
**Branche**: feature/connexion  
**Status**: MVP Fonctionnel ✅
