# Vérification du Système de Médias Enregistrés

## ✅ Complété

### Backend
- [x] Django app `saved_media` créée avec modèles SavedMedia et UserCategory
- [x] Endpoints API: toggle, list, by_category, top, is_saved, categories CRUD
- [x] Authentification JWT requise sur tous les endpoints
- [x] Migrations créées et appliquées
- [x] `django_config/` dossier créé pour config du projet
- [x] URLs correctement routées (`/api/saved-media/...`)

### Frontend
- [x] Composable `useSavedMedia.ts` créée avec tous les appels API
- [x] `LikeButton.vue` refactorisé pour utiliser backend API
- [x] `VideosGrid.vue` mise à jour avec props pour LikeButton
- [x] `LiveArticlesGrid.vue` mise à jour avec props pour LikeButton
- [x] `ProfilMain.vue` affiche top 3 depuis backend
- [x] `LikedMain.vue` affiche tous les médias depuis backend
- [x] `layouts/default.vue` a les imports des composants
- [x] Route `/api/saved-media/` correctly configured in Django

## 🧪 À Tester

### Workflow Utilisateur
1. [ ] Créer compte et se connecter
2. [ ] Aller sur page `/articles` (ou `/video` ou `/en-direct`)
3. [ ] Cliquer sur ❤️ vide d'un article/vidéo
4. [ ] Vérifier que ❤️ devient plein
5. [ ] Aller sur `/liked` et vérifier que l'item apparaît
6. [ ] Aller sur `/mon-compte` et vérifier que le top 3 affiche l'item
7. [ ] Se déconnecter
8. [ ] Se reconnecter
9. [ ] Aller sur `/liked` - l'item doit toujours être là ✅ (persiste!)
10. [ ] Cliquer sur ❤️ plein pour le supprimer
11. [ ] Aller sur `/liked` - l'item ne doit plus être là
12. [ ] Aller sur `/mon-compte` - le section "Médias enregistrés" doit être vide

### Navigation
- [ ] Les boutons de navigation (Accueil, En Direct, Vidéos, Articles) fonctionnent
- [ ] Le bouton "Liked" ❤️ dans le header pointe vers `/liked`
- [ ] Le lien "Voir tout" dans mon-compte pointe vers `/liked`

## 📋 Structure Backend

```
Back/
├── django_config/          # Config du projet Django
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── __init__.py
├── accounts/               # App d'authentification
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── ...
├── saved_media/            # App de médias enregistrés
│   ├── models.py          (SavedMedia, UserCategory)
│   ├── views.py           (SavedMediaViewSet, UserCategoryViewSet)
│   ├── serializers.py
│   ├── urls.py
│   ├── admin.py
│   ├── apps.py
│   └── migrations/
├── manage.py
└── db.sqlite3
```

## 🔌 Endpoints API

- `GET /api/saved-media/` - Liste tous les médias sauvegardés
- `POST /api/saved-media/toggle/` - Ajoute ou supprime un média
- `GET /api/saved-media/by_category/?category=liked` - Filtre par catégorie
- `GET /api/saved-media/top/?limit=3` - Top N items
- `GET /api/saved-media/is_saved/?link=...` - Vérifie si sauvegardé
- `GET /api/saved-media/categories/` - Liste des catégories custom
- `POST /api/saved-media/categories/` - Crée une catégorie
- `DELETE /api/saved-media/categories/{id}/` - Supprime une catégorie
