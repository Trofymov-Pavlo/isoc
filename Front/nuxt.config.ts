// nuxt.config.ts
import { defineNuxtConfig } from 'nuxt/config'

export default defineNuxtConfig({
  compatibilityDate: '2025-12-14',
  devtools: { enabled: true },

  runtimeConfig: {
    public: {
      apiBase: process.env.API_BASE || '/api/accounts'
    }
  },

  css: [
    'vuetify/styles',
    '@/assets/styles/main.scss',
    '@mdi/font/css/materialdesignicons.css'
  ],

  components: [{ path: '@/components', pathPrefix: true }],
  typescript: { strict: true },

  build: {
    transpile: ['vuetify']
  },

  vite: {
    ssr: { noExternal: ['vuetify'] },
    define: { 'process.env.DEBUG': false },
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: '@use "@/assets/styles/vuetify.settings.scss" as *;'
        }
      }
    },
    logLevel: 'warn'
  }
})
