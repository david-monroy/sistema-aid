<template>
  <v-container fluid elevation="0" class="nav-separator">
    <v-row no-gutters justify="center">
      <v-col cols="12" md="8" align="center">
        <h3 class="primary--text mx-auto mb-6 mt-0 md=8">Agregar una edición a un estudio existente</h3>
        <v-stepper v-model="pasoActual">
          <v-stepper-header class="third accent-1">
            <v-stepper-step step="1"
            :complete="pasoActual>1">
            Información general
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
              <InformacionGeneral></InformacionGeneral>
            </v-stepper-content>

            <v-stepper-content step="2">
              <MuestraPonderada :tamanoMuestral="fichaTecnica.totalMuestra" :tipo="tipo"></MuestraPonderada>
            </v-stepper-content>
          </v-stepper-items> 
        </v-stepper>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

import InformacionGeneral from "../../components/estudios/InformacionGeneral.vue";
import MuestraPonderada from "../../components/estudios/MuestraPonderada.vue";
import { EventBus } from "../../main.js";
import swal from 'sweetalert'
import Repository from "../../services/repositories/repositoryFactory";
const EdicionesRepository = Repository.get("Ediciones");
const MuestraPonderadaRepository = Repository.get("MuestraPonderada");

export default {
  data: () => ({
    pasoActual: 1,
    fichaTecnica:[],
    muestra:[],
    tipo:"",
    idEdicion:0
  }),
  components: {
    InformacionGeneral,
    MuestraPonderada
  },

  created() {
    EventBus.$on("pasoSiguienteEdi", (tipo,data) => { 
        if (this.pasoActual == 1 ) {
          this.fichaTecnica = data
          this.tipo = tipo
        }
        if (this.pasoActual == 2){
          this.muestra = data
        }
        this.pasoActual += 1; 
    }),

    EventBus.$on("pasoAnteriorEdi", () => {
        this.pasoActual -= 1;  
    }),

    EventBus.$on("registrar-edicion", (data) => {
        this.muestra = data
        this.insertarEdicion(this.fichaTecnica)
    })
  },

  methods:{
    async insertarEdicion(data){
      try{ 
        var response = await EdicionesRepository.agregar(data);
        console.log(response)
        this.idEdicion = response.id
        this.insertarMuestra(this.muestra);  
        swal("El edición ha sido agregada satisfactoriamente", "", "success")
      }
      catch(err){
        console.log(err)
        swal("La edición no se pudo agregar", "", "error")
      }
    },
    async insertarMuestra(data){
      try{
        await MuestraPonderadaRepository.insertarMuestra(data, this.idEdicion);
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