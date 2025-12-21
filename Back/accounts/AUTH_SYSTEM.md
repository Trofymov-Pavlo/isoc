# Système d'Authentification AXIOME

## 📋 Vue d'ensemble

Le système d'authentification d'AXIOME est construit avec Django REST Framework et utilise des JSON Web Tokens (JWT) pour l'authentification sécurisée entre le frontend Nuxt et le backend Django.

## 🏗️ Architecture

### Structure des dossiers

```
Back/accounts/
├── api_urls.py          # Routes API des comptes (/api/accounts/)
├── urls.py              # Configuration URL racine du projet Django
├── settings.py          # Configuration Django (ex-isoc_auth)
├── wsgi.py              # Point d'entrée WSGI
├── asgi.py              # Point d'entrée ASGI
├── models.py            # Modèle User personnalisé
├── serializers.py       # Sérialiseurs REST pour les endpoints
├── views.py             # ViewSet avec actions signup/login/logout
├── throttles.py         # Rate limiting (anti-spam)
└── migrations/          # Migrations de base de données
```

### Flux d'authentification

```
Frontend (Nuxt)                Backend (Django)
     │                              │
     ├─ signup() ──────────────────>│
     │  (email, username, pwd)      │
     │                              ├─ Validation
     │                              ├─ Création User
     │                              ├─ Génération JWT (access + refresh)
     │<─────────── {user, tokens} ──┤
     │                              │
     ├─ login() ───────────────────>│
     │  (email, password)            │
     │                              ├─ Vérification
     │                              ├─ Génération JWT
     │<─────────── {user, tokens} ──┤
     │                              │
     ├─ API calls ─────────────────>│
     │  Authorization: Bearer token  │
     │                              ├─ Validation JWT
     │<───────────── response ───────┤
     │                              │
     ├─ logout() ──────────────────>│
     │  (refresh_token)              │
     │                              ├─ Blacklist token
     │<───────────── success ────────┤
```

## 🔑 Endpoints API

Base URL: `http://localhost:8000/api/accounts/`

### 1. Inscription

**POST** `/signup/`

```json
{
  "email": "user@example.com",
  "username": "john_doe",
  "password": "SecurePass123",
  "password_confirm": "SecurePass123",
  "first_name": "John",
  "last_name": "Doe"
}
```

**Réponse (201 Created):**
```json
{
  "user": {
    "id": 1,
    "email": "user@example.com",
    "username": "john_doe",
    "first_name": "John",
    "last_name": "Doe"
  },
  "access": "eyJ0eXAiOiJKV1QiLCJhb...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhb..."
}
```

**Rate limit:** 3 tentatives / heure, blocage 30 min

### 2. Connexion

**POST** `/login/`

```json
{
  "email": "user@example.com",
  "password": "SecurePass123",
  "remember_me": true
}
```

**Réponse (200 OK):**
```json
{
  "user": { ... },
  "access": "eyJ0eXAiOiJKV1QiLCJhb...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhb...",
  "remember_me": true
}
```

**Rate limit:** 5 tentatives / minute, blocage 5 min

### 3. Déconnexion

**POST** `/logout/`

Headers: `Authorization: Bearer <access_token>`

```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhb..."
}
```

**Réponse (200 OK):**
```json
{
  "message": "Logged out successfully"
}
```

### 4. Réinitialisation mot de passe

**POST** `/password_reset/`

```json
{
  "email": "user@example.com"
}
```

**Rate limit:** 3 tentatives / heure

### 5. Profil utilisateur

**GET** `/profile/`

Headers: `Authorization: Bearer <access_token>`

**Réponse (200 OK):**
```json
{
  "id": 1,
  "email": "user@example.com",
  "username": "john_doe",
  "first_name": "John",
  "last_name": "Doe",
  "liked_articles": [...],
  "liked_videos": [...]
}
```

**PUT** `/profile/`

Mise à jour du profil (nom, prénom, etc.)

**POST** `/change_password/`

Changement de mot de passe pour utilisateur connecté

## 🔒 Sécurité

### JWT Tokens

- **Access Token:** Expire après 15 minutes, utilisé pour authentifier les requêtes API
- **Refresh Token:** Expire après 7 jours, utilisé pour renouveler l'access token
- Algorithme: HS256 (HMAC-SHA256)
- Secret: `DJANGO_SECRET_KEY` (variable d'environnement)

### Rate Limiting

Implémenté via `throttles.py` pour prévenir les attaques par force brute:

| Endpoint | Limite | Fenêtre | Blocage |
|----------|--------|---------|---------|
| Signup | 3 | 1h | 30 min |
| Login | 5 | 1 min | 5 min |
| Password Reset | 3 | 1h | - |

### CORS

Configuration dans `settings.py`:
- Origins autorisés: `http://localhost:3000`, `http://127.0.0.1:3000`
- Credentials: activés
- Variable d'environnement: `CORS_ALLOWED_ORIGINS`

### CSRF

Protection CSRF désactivée pour l'API REST (JWT suffit).
Trusted origins: identiques aux CORS origins.

## 🚀 Démarrage

### Backend

```bash
cd Back
python manage.py migrate         # Appliquer les migrations
python manage.py runserver 8000  # Démarrer sur port 8000
```

### Frontend (Nuxt)

```bash
cd Front
npm install
npm run dev  # Port 3000
```

## 🔧 Configuration

### Variables d'environnement (Backend)

Créer un fichier `.env` dans `Back/`:

```env
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### Frontend (Nuxt)

Configuration dans `Front/nuxt.config.ts`:

```typescript
runtimeConfig: {
  public: {
    apiBase: 'http://localhost:8000/api/accounts',
    // ...
  }
}
```

## 📱 Frontend - Composables

### useAuthAPI()

Gère les appels API d'authentification:
- `signup(email, username, password, firstName, lastName)`
- `login(email, password, rememberMe)`
- `logout()`
- `getProfile()`
- `updateProfile(data)`
- `changePassword(oldPassword, newPassword)`

### useAuthState()

Gère l'état d'authentification côté client:
- `isAuthenticated` (reactive)
- `setAuth(logged, remember)`
- `checkAuth()` - vérifie les tokens localement
- `clearAuth()` - nettoie l'état

### useRateLimit()

Gère le rate limiting côté client (protection supplémentaire):
- Stockage localStorage
- Compteur de tentatives
- Lockout temporaire
- Reset automatique après expiration

## 🐛 Dépannage

### NetworkError lors de la connexion

**Cause:** Le frontend tente de contacter le backend sur le mauvais port.

**Solution:** Vérifier que Django tourne sur port 8000:
```bash
python manage.py runserver 8000
```

### CORS errors

**Cause:** Origin du frontend non autorisé.

**Solution:** Ajouter l'origin dans `CORS_ALLOWED_ORIGINS` (settings.py ou .env)

### Token expired

**Cause:** Access token expiré (15 min).

**Solution:** Implémenter le refresh automatique dans `useAuthAPI`:
```typescript
const refreshAccessToken = async () => {
  const response = await fetch(`${API_BASE}/token/refresh/`, {
    method: 'POST',
    body: JSON.stringify({ refresh: refreshToken.value })
  });
  // ...
};
```

## 📊 Modèle User personnalisé

```python
class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    liked_articles = models.JSONField(default=list)
    liked_videos = models.JSONField(default=list)
    remember_me = models.BooleanField(default=False)
    password_reset_token = models.CharField(max_length=255, blank=True)
    
    USERNAME_FIELD = 'email'  # Connexion par email
    REQUIRED_FIELDS = ['username']
```

## 🔄 Migrations

Appliquer les migrations après modification du modèle:

```bash
python manage.py makemigrations accounts
python manage.py migrate
```

## 📝 Notes

- Le système utilise `djangorestframework-simplejwt` pour la gestion des JWT
- Les tokens de refresh peuvent être blacklistés après déconnexion
- Le champ `remember_me` est stocké mais pas encore utilisé pour ajuster l'expiration des tokens (à implémenter)
- En production, configurer un vrai SECRET_KEY et désactiver DEBUG
