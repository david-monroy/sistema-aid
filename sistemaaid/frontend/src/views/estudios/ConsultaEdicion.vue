<template>
  <v-container fluid elevation="0" class="nav-separator">
    <v-row no-gutters justify="center">
        <h3 style="text-align:left"> Estudio-Edicion {{edicion.codigo}}</h3>
        <v-expansion-panels>
            <v-expansion-panel>
                <v-expansion-panel-header>
                  Información general
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <ConsultaFichaTecnica :id="id"></ConsultaFichaTecnica>
                </v-expansion-panel-content>
            </v-expansion-panel>
                   
            <v-expansion-panel>
                <v-expansion-panel-header>
                    Prueba 2
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    Contenido 2
                </v-expansion-panel-content>
            </v-expansion-panel>
        </v-expansion-panels>
    </v-row>
  </v-container>
</template>

<script>
import swal from 'sweetalert'
import Repository from "../../services/repositories/repositoryFactory";
import ConsultaFichaTecnica from "../../components/estudios/ConsultaFichaTecnica.vue"

export default {
  data: () => ({
      id: ""
  }),
  components:{
      ConsultaFichaTecnica
  },
  mounted() {
    this.id = this.$route.params.id;
  },

  methods:{
  }
};
</script>

<style>
@import "../../styles/main.css";
</style>