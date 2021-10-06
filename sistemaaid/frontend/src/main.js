// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
<<<<<<< HEAD
import VueTheMask from 'vue-the-mask'
=======
import store from "./store";
>>>>>>> aid-us1

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import vuetify from './plugins/vuetify'

import vuetify from './plugins/vuetify'

Vue.config.productionTip = false
Vue.use(BootstrapVue, VueTheMask)

export const EventBus = new Vue();

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  vuetify,
  template: '<App/>'
})
