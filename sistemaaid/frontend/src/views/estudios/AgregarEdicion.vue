<template>
  <v-container fluid elevation="0" class="nav-separator">
    <Loading :show=activeLoading />
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

            <v-stepper-content step="3">
              <Metodologia :tipo="tipo"></Metodologia>
            </v-stepper-content>

             <v-stepper-content step="4">
              <Instrumento></Instrumento>
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
import Metodologia from "../../components/estudios/Metodologia.vue"
import Loading from "../../components/comunes/Loading.vue"
import Instrumento from '../../components/estudios/Instrumento.vue';
import { EventBus } from "../../main.js";
import swal from 'sweetalert'
import Repository from "../../services/repositories/repositoryFactory";
const EdicionesRepository = Repository.get("Ediciones");
const MuestraPonderadaRepository = Repository.get("MuestraPonderada");
const MetodologiaRepository = Repository.get("Metodologia");
const PreguntasRepository = Repository.get("Preguntas")

export default {
  data: () => ({
    pasoActual: 1,
    fichaTecnica:[],
    muestra:[],
    metodologia:[],
    instrumento:[],
    tipo:"",
    idEdicion:0,
    activeLoading: false
  }),
  components: {
    InformacionGeneral,
    MuestraPonderada,
    Metodologia,
    Instrumento,
    Loading
  },

  created() {
    EventBus.$on("pasoSiguienteEdi", (data) => { 
        if (this.pasoActual == 1 ) {
          this.fichaTecnica = data
          this.tipo = "Edicion"
        }
        if (this.pasoActual == 2){
          this.muestra = data
        }
        if (this.pasoActual == 3){
          this.metodologia = data
        }
        if (this.pasoActual == 4){
          this.instrumento = data
        }
        this.pasoActual += 1; 
    }),

    EventBus.$on("pasoAnteriorEdi", () => {
        this.pasoActual -= 1;  
    }),

    EventBus.$on("registrar-edicion", (data) => {
        this.instrumento = data
        this.insertarEdicion()
    })
  },

  methods:{
    async insertarEdicion(){
      try{ 
        this.activeLoading = true;
        var response = await EdicionesRepository.agregar(this.fichaTecnica);
        this.idEdicion = response.id  
        await MuestraPonderadaRepository.insertarMuestra(this.muestra, this.idEdicion);
        if (this.metodologia != []){
          this.metodologia.edicionId = response.id
          await MetodologiaRepository.insertarMetodologia (this.metodologia);
        }
      
        var resultadoPreguntas= await PreguntasRepository.cargar(this.instrumento, this.idEdicion);

        if (resultadoPreguntas.status == 200){
          this.activeLoading = false;
          swal("", resultadoPreguntas.detail, "success")
          this.$router.push("/estudios");
        }
        else {
          this.activeLoading = false;
          swal("ERROR", resultadoPreguntas.error[0], "error")
        }
          
      }
      catch(err){
        this.activeLoading = false;
        swal("ERROR", err, "error")
      }
    }
  }
};
</script>


<style>
@import "../../styles/main.css";
</style>