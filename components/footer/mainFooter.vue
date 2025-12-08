<template>
  <footer class="bg-slate-950 border-t border-slate-800 py-12">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid md:grid-cols-3 gap-8 mb-8">
        <div>
          <h3 class="text-white font-bold text-lg mb-4">À propos</h3>
          <p class="text-slate-400 text-sm">
            Projet académique ISOC531 analysant l'impact des technologies numériques dans le conflit ukrainien.
          </p>
        </div>
        <div>
          <h3 class="text-white font-bold text-lg mb-4">Navigation</h3>
          <ul class="space-y-2 text-sm">
            <li><NuxtLink to="/" class="text-slate-400 hover:text-blue-400 transition-colors">Accueil</NuxtLink></li>
            <li><NuxtLink to="/enDirect" class="text-slate-400 hover:text-blue-400 transition-colors">En Direct</NuxtLink></li>
            <li><NuxtLink to="/inLivePage" class="text-slate-400 hover:text-blue-400 transition-colors">Live</NuxtLink></li>
          </ul>
        </div>
        <div>
          <h3 class="text-white font-bold text-lg mb-4">Contact</h3>
          <p class="text-slate-400 text-sm mb-2">Université - ISOC531</p>
          <p class="text-slate-400 text-sm">Janvier 2025</p>
        </div>
      </div>
      <div class="border-t border-slate-800 pt-8 text-center text-slate-500 text-sm">
        © {{ yearRange }} - Projet ISOC531. Toutes les sources sont dûment citées.
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
const yearRange = `2024-${new Date().getFullYear()}`
</script>
