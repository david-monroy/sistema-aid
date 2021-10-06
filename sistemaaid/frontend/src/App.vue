<template>
  <v-app>

    <v-main>
      <navbar id="navbar" style="z-index: 100; position: fixed; width: 100%" v-if="estaLogueado() == true"></navbar>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import Navbar from "./components/Navbar.vue";
import jwt from "../src/common/jwt.service";
export default {
  name: 'App',
  components: { Navbar },
  data: () => ({
    //
  }),
  methods: {
    estaLogueado() {
      var token = jwt.isTokenValid();
      return token
    },
  },
};
</script>
