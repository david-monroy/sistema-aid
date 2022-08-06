<template>
<v-btn :small="$vuetify.breakpoint.smAndDown"
       v-if="permisos(permiso) != false"
       class="primary ml-2 mb-2"
       @click="goRoute(route)"
       :disable=!valid>
       <p class="mt-3 hidden-sm-and-down">{{titulo}}</p>
</v-btn>
</template>

<script>
export default {
  name: "Boton",
  props: {
    titulo: String,
    route: String,
    permiso: String
  },
  methods: {
    goRoute(route) {
      this.$router.push("/" + route);
    },
    permisos(permiso) {
      var permisos = this.$store.getters["users/getPermisos"];
      if (permisos.includes(permiso))
        return true;
      else 
        return false;
    }
  },
  data: () => ({}),
};
</script>

<style>
@import "../../styles/components/dashboard.css";
@import "../../styles/main.css";
</style>