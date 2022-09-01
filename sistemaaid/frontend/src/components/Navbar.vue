<template>
  <div id="navbar">
      <nav class="navbar navbar-expand primary">
        <div class="container container-navbar">
            <a href="/">
                <img class="navbar-logo"
                src="../assets/logo_AID_light.png"
                />
            </a>

          <div class="navbar-list">
            <li class="nav-item" v-if="permisos('backend | estudio | Can view estudio') != false">
            <router-link to="/estudios" class="nav-link" >Estudios</router-link>
            </li>
            <li class="nav-item" v-if="permisos('backend | participante | Can view participante') != false">
                <router-link to="/participantes" class="nav-link">Participantes</router-link>
            </li>
            <li class="nav-item" v-if="permisos('auth | user | reportes') != false">
                <router-link to="/reportes" class="nav-link">Reportes</router-link>
            </li>
            <li class="nav-item" v-if="permisos('auth | user | configuracion') != false">
                <router-link to="/configuracion" class="nav-link">Configuración</router-link>
            </li>

            <li class="nav-item">
                <a class="nav-link">
                  {{activeUser()}}
                <v-icon color="white" @click="cerrarSesion()">fas fa-sign-out-alt</v-icon>
                </a>
            </li>
          </div>
          
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "navbar",
  data: () => ({
  }),

  methods:{
   activeUser() {
      return this.$store.getters["users/getUser"].username;
    },
  
  permisos(permiso) {
      var permisos = this.$store.getters["users/getPermisos"];
      if (permisos.includes(permiso))
        return true;
      else 
        return false;
  },
     cerrarSesion() {
      this.$store.dispatch("users/cerrarSesion", this.form);
      this.$router.push("/login");
    }
  }

}
</script>

<style>
@import "../styles/components/navbar.css";
</style>