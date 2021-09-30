<template>
  <v-container fluid elevation="0" class="nav-separator">
    <v-row no-gutters justify="center">
      <v-col cols="12" md="8" align="center">
        <h3 class="primary--text mx-auto mb-6 mt-0 md=8">Agregar un nuevo estudio</h3>
        <v-stepper v-model="pasoActual">
          <v-stepper-header class="third accent-1">
            <v-stepper-step step="1"
            :complete="pasoActual>1">
            Ficha Técnica
            </v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step step="2"
            :complete="pasoActual>2">
            Muestra
            </v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step step="3"
            :complete="pasoActual>3">
            Metodología
            </v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step step="4"
            :complete="pasoActual>4">
            Instrumento
            </v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step step="5"
            >
            Flujo de ejecución
            </v-stepper-step>
            
          </v-stepper-header>

         <v-stepper-items>
            <v-stepper-content step="1">
              <FichaTecnica></FichaTecnica>
            </v-stepper-content>

            <v-stepper-content step="2">
              <FichaTecnica></FichaTecnica>
            </v-stepper-content>
          </v-stepper-items> 
        </v-stepper>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

import FichaTecnica from "../../components/estudios/FichaTecnica.vue";
import { EventBus } from "../../main.js";
import axios from 'axios'
import swal from 'sweetalert'
export default {
  data: () => ({
    pasoActual: 1
  }),
  components: {
    FichaTecnica
  },

  created() {
    EventBus.$on("ficha-tecnica", (data) => {
        this.insertarEstudio(data);  
    })
  },

  methods:{
    async insertarEstudio(data){
      const estudio_path = 'http://localhost:8000/api/v1/estudios/'
      await axios.post(estudio_path, data).then((response) => {
          data.estudio = response.data.id;
          this.insertarEdicion(data)
        })
        .catch((err) => {
          console.log(err)
          swal("El código del estudio está duplicado", "", "error")
        })
    },
    async insertarEdicion(data){
      const edicion_path = 'http://localhost:8000/api/v1/ediciones/'
      await axios.post(edicion_path, data).then((response) => {
          swal("Estudio creado satisfactoriamente", "", "success")
          this.pasoActual = 2; 
        })
        .catch((err) => {
          console.log(err)
          swal("Estudio no pudo ser creado", "", "error")
        })
    }

  }
};
</script>


<style>
@import "../../styles/main.css";
</style>