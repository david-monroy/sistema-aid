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
              <li class="nav-item">
            <router-link to="/estudios" class="nav-link">Estudios</router-link>
            </li>
            <li class="nav-item">
                <router-link to="/participantes" class="nav-link">Participantes</router-link>
            </li>
            <li class="nav-item">
                <router-link to="#" class="nav-link">Reportes</router-link>
            </li>
            <li class="nav-item">
                <router-link to="#" class="nav-link">Configuración</router-link>
            </li>

            <li class="nav-item">
                <a class="nav-link">
                <v-icon>fas fa-sign-out-alt</v-icon>   Cerrar sesión
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

}
</script>

<style>
@import "../styles/components/navbar.css";
</style>