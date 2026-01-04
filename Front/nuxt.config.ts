// nuxt.config.ts
import { defineNuxtConfig } from 'nuxt/config'

export default defineNuxtConfig({
  compatibilityDate: '2025-12-14',
  devtools: { enabled: process.env.NODE_ENV === 'development' },

  nitro: {
    experimental: {
      websocket: false
    }
  },

  runtimeConfig: {
    public: {
      // Backend API URLs - configurable par environment
      apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://localhost:8000/api/accounts',
      apiDonations: process.env.NUXT_PUBLIC_API_DONATIONS || 'http://localhost:8000/api/donations',
      apiScraper: process.env.NUXT_PUBLIC_SCRAPER_BASE || 'http://localhost:8000',
      // Feature flags
      enableScraperIntegration: process.env.NUXT_PUBLIC_ENABLE_SCRAPER === 'true',
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
