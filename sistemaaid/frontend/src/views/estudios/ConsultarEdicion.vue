<template>
<v-container fluid elevation="0" class="nav-separator">
    <v-row no-gutters justify="start">
      <h3 class="primary--text mx-auto mb-6 mt-0 md=8">{{edicion.estudio.nombre}} - {{edicion.codigo}}</h3>
    </v-row>
  <v-expansion-panels>
    <v-expansion-panel>
      <v-expansion-panel-header>
        <template v-slot:default>
          <v-row no-gutters class="panels-title">
              Información General
          </v-row>
        </template>
      </v-expansion-panel-header>
      <v-expansion-panel-content>
            <ConsultarFichaTecnica :edicion="edicion"></ConsultarFichaTecnica>  
      </v-expansion-panel-content>
    </v-expansion-panel>
    <v-expansion-panel>
      <v-expansion-panel-header>
        <template v-slot:default>
          <v-row no-gutters class="panels-title">
              Muestra Ponderada
          </v-row>
        </template>
      </v-expansion-panel-header>
      <v-expansion-panel-content>
          <ConsultarMuestraPonderada :edicion="edicion"></ConsultarMuestraPonderada>
      </v-expansion-panel-content>
    </v-expansion-panel>
    <v-expansion-panel>
      <v-expansion-panel-header>
        <template v-slot:default>
          <v-row no-gutters class="panels-title">
              Instrumento
          </v-row>
        </template>
      </v-expansion-panel-header>
      <v-expansion-panel-content>
            <ConsultarInstrumento :edicion="edicion"></ConsultarInstrumento>
      </v-expansion-panel-content>
    </v-expansion-panel>
    <v-expansion-panel>
      <v-expansion-panel-header>
        <template v-slot:default>
          <v-row no-gutters class="panels-title">
              Encuestas
          </v-row>
        </template>
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        <ConsultarEncuestas :edicion="edicion"></ConsultarEncuestas>
      </v-expansion-panel-content>
    </v-expansion-panel>

  </v-expansion-panels>
</v-container>
</template>


<script>
import swal from 'sweetalert'
import Repository from "../../services/repositories/repositoryFactory";
import ConsultarFichaTecnica from "../../components/estudios/ConsultaFichaTecnica.vue";
import ConsultarMuestraPonderada from "../../components/estudios/ConsultarMuestraPonderada.vue";
import ConsultarInstrumento from "../../components/estudios/ConsultarInstrumento.vue";
import ConsultarEncuestas from "../../components/estudios/ConsultarEncuestas.vue";

import { EventBus } from "../../main.js";
const EdicionRepository = Repository.get("Ediciones");

export default {
    data(){
        return {
            file: "",
            valid:true,
            respuesta: [],
            idEdicion: null,
            edicion: {}
        }
    },
    components: {
    ConsultarFichaTecnica,
    ConsultarMuestraPonderada,
    ConsultarInstrumento,
    ConsultarEncuestas
    },
    beforeMount(){
        this.buscarEdicion(this.$route.params.id);
    },
    methods: {
        async cargarExcel(){
            const formData = new FormData();
            formData.append('file', this.file)
            try{
                this.respuesta = await EdicionRepository.cargarEncuestas(formData,edicion.id);
            }
            catch(err){
                console.log(err)
                swal("No se pudo procesar la muestra", "", "error")
            } 
        },
        
        async buscarEdicion(id){
            try{
                this.edicion = await EdicionRepository.buscarEdicion(id);

            }
            catch(err){
                console.log(err)
                swal("No se pudo procesar la muestra", "", "error")
            } 
        }
    },
}
</script>

<style>
@import "../../styles/main.css";
</style>