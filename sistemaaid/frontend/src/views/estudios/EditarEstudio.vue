<template>
  <v-container fluid elevation="0" class="nav-separator">
    <v-row no-gutters justify="center">
      <v-col cols="12" md="8" align="center">
        <h3 class="primary--text mx-auto mb-6 mt-0 md=8">
          Editar estudio {{ estudioAEditar.nombre }}
        </h3>
        <v-stepper v-model="pasoActual">
          <v-stepper-header class="third accent-1">
            <v-stepper-step step="1" :complete="pasoActual > 1">
              Ficha Técnica
            </v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step step="2" :complete="pasoActual > 2">
              Ediciones
            </v-stepper-step>

            <v-divider></v-divider>

          </v-stepper-header>

          <v-stepper-items>
            <v-stepper-content step="1">
              <FichaTecnicaEditar :form="estudioAEditar"></FichaTecnicaEditar>
            </v-stepper-content>
            <v-stepper-content step="2">
              <Ediciones :ediciones="ediciones" :tipo="tipo"></Ediciones>
            </v-stepper-content>
          </v-stepper-items>
        </v-stepper>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import MetodologiaEditar from "../../components/estudios/editar/Metodologia.vue";
import FichaTecnicaEditar from "../../components/estudios/editar/FichaTecnica.vue";
import Ediciones from "../../components/estudios/editar/Ediciones.vue";
import MuestraPonderada from "../../components/estudios/MuestraPonderada.vue";
import Instrumento from "../../components/estudios/Instrumento.vue";
import { EventBus } from "../../main.js";
import swal from "sweetalert";
import Repository from "../../services/repositories/repositoryFactory";

const EstudiosRepository = Repository.get("Estudios");
const EdicionesRepository = Repository.get("Ediciones");
const MuestraPonderadaRepository = Repository.get("MuestraPonderada");
const MetodologiaRepository = Repository.get("Metodologia");
const PreguntasRepository = Repository.get("Preguntas");

export default {
  data: () => ({
    pasoActual: 1,
    fichaTecnica: [],
    muestra: [],
    idEdicion: 0,
    tipo: null,
    estudioAEditar: null,
  }),
  components: {
    FichaTecnicaEditar,
    MuestraPonderada,
    MetodologiaEditar,
    Instrumento,
    Ediciones,
  },

  created() {
    EventBus.$on("pasoSiguienteEdicion", (data) => {
      if (this.pasoActual == 1) {
        this.fichaTecnica = data;
      }
      if (this.pasoActual == 2) {
        this.ediciones = data;
        this.actualizarEstudio(this.fichaTecnica);
      }
      if (this.pasoActual == 3) {
        this.metodologia = data;
      }
      if (this.pasoActual == 4) {
        this.instrumento = data;
      }
      this.pasoActual += 1;
    }),
      EventBus.$on("pasoAnterior", () => {
        this.pasoActual -= 1;
      }),
      EventBus.$on("actualizar-estudio", (data) => {
        this.actualizarEstudio(this.fichaTecnica);
      });
  },

  methods: {
    async actualizarEstudio(data) {
      try {
        var estudio = await EstudiosRepository.actualizar(
          this.estudioAEditar.id,
          data
        );
        for (let index = 0; index < this.ediciones.length; index++) {
          const edicion = this.ediciones[index];
          console.log(edicion)
          let editarEdicion = await EdicionesRepository.actualizar(
            edicion.id,
            edicion
          );

          let editarMetodologia = await MetodologiaRepository.actualizar(
          edicion.metodologia.id,
          edicion.metodologia
        );
        }

        swal(
          "El estudio ha sido actualizado satisfactoriamente",
          "",
          "success"
        );
        this.$router.push("/estudios");
      } catch (error) {
        console.log(err);
        swal("El estudio no pudo ser actualizado" + err, "", "error");
      }
    },

    async getEstudio(id) {
      this.estudioAEditar = await EstudiosRepository.consultarEstudio(id);
      this.ediciones = await EstudiosRepository.obtenerEdiciones(id);
      this.getMetodologias(this.ediciones)
    },
    async getMetodologias(ediciones){
      for (let index = 0; index < ediciones.length; index++) {
        const edicion = ediciones[index];
        let metodologia = await MetodologiaRepository.buscarMetodologia(edicion.id);
        edicion.metodologia = metodologia
      }
    },
  },
  mounted() {
    this.getEstudio(this.$route.params.id);
  },
};
</script>


<style>
@import "../../styles/main.css";
</style>