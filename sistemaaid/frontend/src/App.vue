<template>
  <v-app>

    <v-main>
      <navbar id="navbar" style="z-index: 100; position: fixed; width: 100%"></navbar>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import Navbar from "./components/Navbar.vue";
export default {
  name: 'App',
  components: { Navbar },
  data: () => ({
    //
  }),
};
</script>
