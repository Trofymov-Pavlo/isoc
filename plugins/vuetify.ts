// plugins/vuetify.ts
import { defineNuxtPlugin } from 'nuxt/app'
import { createVuetify } from 'vuetify'
import { aliases, mdi } from 'vuetify/iconsets/mdi'

export default defineNuxtPlugin(nuxtApp => {
  const vuetify = createVuetify({
    icons: {
      defaultSet: 'mdi',
      aliases,
      sets: { mdi }
    },
    theme: {
      defaultTheme: 'light',
      themes: {
        light: {
          dark: false,
          colors: {
            primary: '#4F46E5',
            secondary: '#14B8A6',
            surface: '#FFFFFF',
            background: '#FAFAFA'
          }
        }
      }
    }
  })
  nuxtApp.vueApp.use(vuetify)
})
