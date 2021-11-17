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

            <v-stepper-step step="5">
            Flujo de ejecución
            </v-stepper-step>
            
          </v-stepper-header>

         <v-stepper-items>
            <v-stepper-content step="1" >
              <FichaTecnica></FichaTecnica>
            </v-stepper-content>
            <v-stepper-content step="2" >
              <MuestraPonderada :tamanoMuestral="fichaTecnica.totalMuestra"></MuestraPonderada>
            </v-stepper-content>
            <v-stepper-content step="3" >
              <h3>Proximamente</h3>
            </v-stepper-content>
            <v-stepper-content step="4" >
              <h3>Proximamente</h3>
            </v-stepper-content>
            <v-stepper-content step="5" >
              <h3>Proximamente</h3>
            </v-stepper-content>
          </v-stepper-items> 
        </v-stepper>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

import FichaTecnica from "../../components/estudios/FichaTecnica.vue";
import MuestraPonderada from "../../components/estudios/MuestraPonderada.vue";
import { EventBus } from "../../main.js";
import swal from 'sweetalert'
import Repository from "../../services/repositories/repositoryFactory";
const EstudiosRepository = Repository.get("Estudios");
const MuestraPonderadaRepository = Repository.get("MuestraPonderada");
const EdicionesRepository = Repository.get("Ediciones");

export default {
  data: () => ({
    pasoActual: 1,
    fichaTecnica: [],
    muestra: [],
    idEdicion: 0
  }),
  components: {
    FichaTecnica,
    MuestraPonderada
  },

  created() {
    EventBus.$on("pasoSiguiente", (data) => { 
        if (this.pasoActual == 1 ) {
          this.fichaTecnica = data
        }
        if (this.pasoActual == 2){
          this.muestra = data
        }
        this.pasoActual += 1; 
    }),

    EventBus.$on("pasoAnterior", () => {
        this.pasoActual -= 1;  
    }),

    EventBus.$on("registrar", (data) => {
        this.muestra = data
        this.insertarEstudio(this.fichaTecnica)
    })
  },

  methods:{
    async insertarEstudio(data){
      try{
        var estudio = await EstudiosRepository.agregar(data);
        data.estudio = estudio.id
        var response = await EdicionesRepository.agregar(data);
        this.idEdicion = response.id
        swal("El estudio ha sido agregado satisfactoriamente", "", "success")
        this.insertarMuestra(this.muestra);  
      }
      catch(err){
        console.log(err)
        swal("El estudio no pudo ser agregado", "", "error")
      }
    },
    async insertarMuestra(data){
      try{
        await MuestraPonderadaRepository.insertarMuestra(data, this.idEdicion);
        swal("La muestra ha sido agregada satisfactoriamente", "", "success")
      }
      catch(err){
        console.log(err)
        swal("La muestra no pudo ser agregada", "", "error")
      }
    }

  }
};
</script>


<style>
@import "../../styles/main.css";
</style>