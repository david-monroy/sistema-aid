import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import '@fortawesome/fontawesome-free/css/all.css' // Ensure you are using css-loader


Vue.use(Vuetify)

export default new Vuetify({
  icons: {
    iconfont: 'fa',
  },
  theme: {
    themes: {
      light: {
        primary: "#163172",
        secondary: "#1E56A0",
        light: "#F6F6F6",
        accent1: "#D6E4F0",
        accent2: "#F3ECD3",
        dark: "#30343D",
        success: "#21BF73",
        error: "#FD5E53"
      }
    }
  }
  
})