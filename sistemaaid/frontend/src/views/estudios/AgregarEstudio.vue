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
              <MuestraPonderada :tamanoMuestral="fichaTecnica.totalMuestra" :tipo="tipo"></MuestraPonderada>
            </v-stepper-content>
            <v-stepper-content step="3" >
              <Metodologia :tipo="tipo"></Metodologia>
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

import Metodologia from "../../components/estudios/Metodologia.vue"
import FichaTecnica from "../../components/estudios/FichaTecnica.vue";
import MuestraPonderada from "../../components/estudios/MuestraPonderada.vue";
import { EventBus } from "../../main.js";
import swal from 'sweetalert'
import Repository from "../../services/repositories/repositoryFactory";
const EstudiosRepository = Repository.get("Estudios");
const EdicionesRepository = Repository.get("Ediciones");
const MuestraPonderadaRepository = Repository.get("MuestraPonderada");
const MetodologiaRepository = Repository.get("Metodologia")

export default {
  data: () => ({
    pasoActual: 1,
    fichaTecnica: [],
    muestra: [],
    idEdicion: 0,
    tipo: null
  }),
  components: {
    FichaTecnica,
    MuestraPonderada,
    Metodologia
  },

  created() {
    EventBus.$on("pasoSiguiente", (data) => { 
        if (this.pasoActual == 1 ) {
          this.fichaTecnica = data
          this.tipo = "Estudio"
        }
        if (this.pasoActual == 2){
          this.muestra = data
        }
        if (this.pasoActual == 3){
          this.metodologia = data
        }
        this.pasoActual += 1; 
    }),

    EventBus.$on("pasoAnterior", () => {
        this.pasoActual -= 1;  
    }),

    EventBus.$on("registrar-estudio", (data) => {
        this.muestra = data
        this.insertarEstudio(this.fichaTecnica)
    })
  },

  methods:{
    async insertarEstudio(data){
      try{
        var estudio = await EstudiosRepository.agregar(data);
        data.estudio_id = estudio.id
        var response = await EdicionesRepository.agregar(data);
        this.idEdicion = response.id  
        this.metodologia.edicionId = response.id
        if (this.muestra) await MuestraPonderadaRepository.insertarMuestra(this.muestra, this.idEdicion);
        if (this.metodologia) await MetodologiaRepository.insertarMetodologia (this.metodologia)
        swal("El estudio ha sido agregado satisfactoriamente", "", "success")
      }
      catch(err){
        console.log(err)
        swal("El estudio no pudo ser agregado", "", "error")
      }
    }

  }
};
</script>


<style>
@import "../../styles/main.css";
</style>