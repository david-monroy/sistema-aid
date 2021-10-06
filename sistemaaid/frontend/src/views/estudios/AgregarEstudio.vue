<template>
  <v-container fluid elevation="0" class="nav-separator">
    <v-row no-gutters justify="center">
      <v-col cols="12" md="8" align="center">
        <v-stepper>
          <v-stepper-header class="third accent-1">
            <v-stepper-step step="1">
            Ficha Técnica
            </v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step step="2">
            Muestra
            </v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step step="3">
            Metodología
            </v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step step="4">
            Instrumento
            </v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step step="5">
            Flujo de ejecución
            </v-stepper-step>
            
          </v-stepper-header>

         <v-stepper-items>
            <v-stepper-content step="1">
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
import Repository from "../../services/repositories/repositoryFactory";
const EstudiosRepository = Repository.get("Estudios");

export default {
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
      try{
        await EstudiosRepository.agregar(data);
        swal("Participante creado satisfactoriamente", "", "success")
      }
      catch(err){
        console.log(err)
          swal("Participante no pudo ser creado", "", "error")
      }
    }
  }
};
</script>


<style>
@import "../../styles/main.css";
</style>