# Accounts Module

Module d'authentification et de gestion des utilisateurs pour Axiome.

## 📁 Structure

```
accounts/
├── README.md              # Ce fichier
├── AUTH_SYSTEM.md         # Documentation complète du système
│
├── django_urls.py         # URLs principales Django (projet)
├── urls.py                # URLs de l'app accounts (API)
├── views.py               # Endpoints API (ViewSet)
├── models.py              # Modèle utilisateur personnalisé
├── serializers.py         # Sérialiseurs pour validation des données
├── throttles.py           # Rate limiting (anti-spam)
├── admin.py               # Configuration interface admin Django
├── apps.py                # Configuration de l'app Django
│
├── settings.py            # Configuration Django du projet
├── wsgi.py                # Point d'entrée WSGI
└── asgi.py                # Point d'entrée ASGI
```

## 🎯 Responsabilités par fichier

### Core Application

- **`models.py`** : Modèle `CustomUser` avec authentification par email
- **`serializers.py`** : Validation des données d'entrée/sortie de l'API
- **`views.py`** : Logique des endpoints (signup, login, logout, profile, etc.)
- **`urls.py`** : Routes API de l'app (`/api/accounts/`)
- **`throttles.py`** : Limitation du taux de requêtes par IP

### Configuration

- **`settings.py`** : Configuration Django (DB, CORS, JWT, apps installées)
- **`django_urls.py`** : Routing principal du projet Django
- **`wsgi.py`** / **`asgi.py`** : Serveurs de déploiement
- **`apps.py`** : Configuration de l'app Django
- **`admin.py`** : Interface d'administration Django

## 🔗 Flux de données

```
Request → django_urls.py → urls.py → views.py → serializers.py → models.py
                                          ↓
                                     throttles.py (rate limit)
```

## 📝 Points clés

1. **Authentification par email** : Le champ `email` est utilisé comme identifiant principal
2. **JWT Tokens** : Utilise `djangorestframework-simplejwt` pour les tokens d'accès/refresh
3. **Rate Limiting** : Protection contre le bruteforce sur signup/login/password reset
4. **Séparation des URLs** :
   - `django_urls.py` : configuration projet (admin + api)
   - `urls.py` : routes spécifiques à l'app accounts

## 🚀 Démarrage rapide

```bash
# Migrations
python manage.py makemigrations accounts
python manage.py migrate

# Créer un superuser
python manage.py createsuperuser

# Lancer le serveur
python manage.py runserver 8000
```

## 📚 Documentation

Voir [AUTH_SYSTEM.md](AUTH_SYSTEM.md) pour la documentation complète incluant:
- Architecture détaillée
- Documentation des endpoints
- Guide de sécurité
- Configuration JWT
- Exemples d'utilisation
