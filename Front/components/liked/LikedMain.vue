<template>
  <main class="liked-page">
    <section class="liked-wrapper">
      <!-- Tabs for categories -->
      <div class="tabs-container">
        <button
          class="tab"
          :class="{ active: activeTab === 'all' }"
          @click="activeTab = 'all'"
        >
          📑 Tous ({{ savedItems.length }})
        </button>
        <button
          class="tab"
          :class="{ active: activeTab === 'liked' }"
          @click="activeTab = 'liked'"
        >
          ❤️ Likés ({{ likedItems.length }})
        </button>
        <button
          class="tab"
          :class="{ active: activeTab === 'watch_later' }"
          @click="activeTab = 'watch_later'"
        >
          ⏰ À lire plus tard ({{ watchLaterItems.length }})
        </button>
        <button
          v-for="cat in userCategories"
          :key="cat.id"
          class="tab"
          :class="{ active: activeTab === cat.name }"
          @click="activeTab = cat.name"
        >
          {{ cat.icon }} {{ cat.name }} ({{ getCategoryItems(cat.name).length }})
        </button>
        <button class="tab tab-add" @click="showCreateModal = true">
          + Nouvelle catégorie
        </button>
      </div>

      <!-- Loading state -->
      <div v-if="loading" class="loading-state">Chargement de vos médias enregistrés…</div>

      <!-- Content -->
      <div class="liked-content" v-else-if="displayedItems.length">
        <LiveArticlesGrid :articles="displayedItems" />
      </div>

      <!-- Empty state -->
      <div class="empty-state" v-else>
        <span class="empty-icon">📌</span>
        <p class="empty-text">Aucun média dans cette catégorie.</p>
        <p class="empty-hint">Commencez à enregistrer des articles pour les retrouver ici !</p>
      </div>
    </section>

    <!-- Create category modal -->
    <div v-if="showCreateModal" class="modal-overlay" @click.self="showCreateModal = false">
      <div class="modal-card">
        <h3>Créer une nouvelle catégorie</h3>
        <div class="form-group">
          <label>Nom de la catégorie</label>
          <input v-model="newCategoryName" type="text" placeholder="Ex: À lire demain" maxlength="50" />
        </div>
        <div class="form-group">
          <label>Icône (emoji)</label>
          <input v-model="newCategoryIcon" type="text" placeholder="Ex: 📚" maxlength="2" />
        </div>
        <div class="form-group">
          <label>Couleur</label>
          <input v-model="newCategoryColor" type="color" />
        </div>
        <div class="modal-actions">
          <button class="btn-secondary" @click="cancelCreate">Annuler</button>
          <button class="btn-primary" @click="handleCreateCategory" :disabled="!newCategoryName">Créer</button>
        </div>
        <p v-if="createError" class="error">{{ createError }}</p>
      </div>
    </div>
  </main>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';

import LiveArticlesGrid from '~/components/in-live/LiveArticlesGrid.vue';
import { useSavedMedia } from '~/composables/useSavedMedia';

const { 
  savedItems, 
  userCategories, 
  loading, 
  likedItems, 
  watchLaterItems, 
  getCategoryItems, 
  getUserCategories,
  getSavedItems,
  createCategory 
} = useSavedMedia();

const activeTab = ref<string>('all');
const showCreateModal = ref(false);
const newCategoryName = ref('');
const newCategoryIcon = ref('📌');
const newCategoryColor = ref('#2f0538');
const createError = ref('');

const displayedItems = computed(() => {
  let items = [];
  
  if (activeTab.value === 'all') {
    items = savedItems.value;
  } else if (activeTab.value === 'liked') {
    items = likedItems.value;
  } else if (activeTab.value === 'watch_later') {
    items = watchLaterItems.value;
  } else {
    // Custom category
    items = getCategoryItems(activeTab.value);
  }
  
  // Format items to match LiveArticlesGrid interface
  return items.map(item => ({
    link: item.link,
    title: item.title,
    source: item.source,
    image: item.thumbnail,
    summary: '',
    type: item.media_type === 'article' || item.media_type === 'live' ? 'article' : 'video',
    published: item.saved_at,
  }));
});

onMounted(async () => {
  await Promise.all([
    getSavedItems(),
    getUserCategories(),
  ]);
});

const cancelCreate = () => {
  showCreateModal.value = false;
  newCategoryName.value = '';
  newCategoryIcon.value = '📌';
  newCategoryColor.value = '#2f0538';
  createError.value = '';
};

const handleCreateCategory = async () => {
  if (!newCategoryName.value.trim()) {
    createError.value = 'Le nom est requis';
    return;
  }
  
  createError.value = '';
  const result = await createCategory(
    newCategoryName.value.trim(),
    newCategoryColor.value,
    newCategoryIcon.value
  );
  
  if (result) {
    cancelCreate();
  } else {
    createError.value = 'Impossible de créer la catégorie';
  }
};
</script>

<style scoped>
.liked-page {
  min-height: 100vh;
  background: #fff;
}

.liked-wrapper {
  max-width: 1400px;
  margin: 0 auto;
  padding: 48px calc(2vw) 60px;
}

.tabs-container {
  display: flex;
  gap: 8px;
  margin-bottom: 32px;
  flex-wrap: wrap;
}

.tab {
  padding: 12px 20px;
  border: 1px solid #e0e0e0;
  background: #fff;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  color: #666;
}

.tab:hover {
  background: #f8f8f8;
  border-color: #ccc;
}

.tab.active {
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  color: #fff;
  border-color: #2f0538;
}

.tab-add {
  background: #f0f0f0;
  border-style: dashed;
  color: #7b5ce0;
}

.tab-add:hover {
  background: #e8e8e8;
  border-color: #7b5ce0;
}

.liked-content {
  margin-bottom: 60px;
}

.loading-state {
  text-align: center;
  padding: 60px 20px;
  color: #666;
  font-size: 16px;
}

.empty-state {
  text-align: center;
  padding: 80px 20px;
}

.empty-icon {
  font-size: 64px;
  display: block;
  margin-bottom: 16px;
  opacity: 0.5;
}

.empty-text {
  font-size: 18px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0 0 8px;
}

.empty-hint {
  font-size: 16px;
  color: #999;
  margin: 0;
}

/* Modal */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-card {
  background: #fff;
  border-radius: 16px;
  padding: 32px;
  max-width: 500px;
  width: 90%;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.modal-card h3 {
  margin: 0 0 24px 0;
  font-size: 24px;
  color: #1a1a1a;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  font-size: 14px;
  color: #333;
}

.form-group input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 14px;
  font-family: inherit;
}

.form-group input:focus {
  outline: none;
  border-color: #7b5ce0;
  box-shadow: 0 0 0 3px rgba(123, 92, 224, 0.1);
}

.modal-actions {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
  margin-top: 24px;
}

.btn-primary,
.btn-secondary {
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  border: none;
  font-size: 14px;
}

.btn-primary {
  background: linear-gradient(135deg, #2f0538 0%, #4b2faa 100%);
  color: #fff;
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(47, 5, 56, 0.3);
}

.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-secondary {
  background: #f0f0f0;
  color: #666;
}

.btn-secondary:hover {
  background: #e0e0e0;
}

.error {
  color: #e74c3c;
  font-size: 13px;
  margin: 12px 0 0 0;
}

@media (max-width: 768px) {
  .liked-wrapper {
    padding: 32px calc(2vw) 40px;
  }

  .tabs-container {
    gap: 6px;
  }

  .tab {
    padding: 10px 16px;
    font-size: 13px;
  }

  .empty-state {
    padding: 60px 20px;
  }

  .empty-text {
    font-size: 16px;
  }

  .empty-hint {
    font-size: 14px;
  }

  .modal-card {
    padding: 24px;
  }
}
</style>
