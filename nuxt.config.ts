// nuxt.config.ts
import { defineNuxtConfig } from 'nuxt/config'

export default defineNuxtConfig({
  devtools: { enabled: false },
  nitro: { compatibilityDate: '2025-10-19', },

  css: [
    'vuetify/styles',
    '@/assets/styles/main.scss',
    '@mdi/font/css/materialdesignicons.css'
  ],

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
