<template>
  <v-container>
    <v-row
      align="center"
      class="list px-3 mx-auto nav-separator container mt-12"
      style="display: flex; justify-content: center"
    >
      <v-col cols="12" sm="6" class="mt-4">
        Seleccione una o dos ediciones del estudio
        <b>{{ estudio.nombre }}</b> para comparar sus resultados
        <v-select
          v-model="presentacion[0].ediciones"
          :items="ediciones"
          item-text="codigo"
          item-value="id"
          chips
          label="Ediciones"
          v-on:input="limiteOpciones"
          multiple
          outlined
          class="mt-2"
        ></v-select>
      </v-col>
    </v-row>
    <v-row align="center" style="display: flex; justify-content: center">
      <v-btn
        :small="$vuetify.breakpoint.smAndDown"
        class="primary"
        @click="getPreguntas()"
        :disable="!valid"
      >
        <p class="mt-3 hidden-sm-and-down">Obtener preguntas</p>
      </v-btn>
    </v-row>
    <div
      class="card-container mt-5 form-card pregunta-card"
      v-for="diapositiva in presentacion"
    >
      <v-form ref="registerForm" v-model="valid" lazy-validation>
        <v-row class="justify-center" v-if="!esUltimo(diapositiva.id) || presentacion.length<2">
          <h4>Diapositiva {{ diapositiva.id }}</h4>
        </v-row>
        <v-row class="justify-center" v-else>
          <h4>Diapositiva {{ diapositiva.id }}</h4>
          <v-icon
            @click="eliminarDiapositiva(diapositiva.id)"
            size="20"
            color="error"
            class="ml-2 mb-2"
            >fa-trash</v-icon
          >
        </v-row>
        <v-row>
          <v-col cols="4">
            <v-combobox
              dense
              outlined
              label="Seleccione la pregunta a graficar"
              v-model="diapositiva.pregunta"
              :items="preguntas"
              item-text="etiqueta"
              item-value="id"
            ></v-combobox>
          </v-col>
          <v-col cols="4">
            <v-select
              v-model="diapositiva.tipoGrafico"
              :items="tiposGrafico"
              item-text="nombre"
              item-value="id"
              label="Tipo de gráfico"
            ></v-select>
            <!-- <GraficoComponente
              :chartID="diapositiva.id"
              :tipoGrafico="diapositiva.tipoGrafico"
            ></GraficoComponente> -->
          </v-col>
          <v-col cols="4">
            <v-textarea
              outlined
              name="input-7-4"
              v-model="diapositiva.texto"
              label="Texto de la diapositiva"
            ></v-textarea>
          </v-col>
        </v-row>
      </v-form>
    </div>
    <v-row align="center" style="display: flex; justify-content: center">
      <v-btn
        :small="$vuetify.breakpoint.smAndDown"
        class="primary my-2"
        @click="agregarDiapositiva()"
        :disable="!valid"
      >
        <p class="mt-3 hidden-sm-and-down">Agregar diapositiva</p>
      </v-btn>
    </v-row>
    <v-row align="center" style="display: flex; justify-content: center">
      <v-btn
        :small="$vuetify.breakpoint.smAndDown"
        class="primary"
        @click="crearPresentacion()"
        :disable="!valid"
      >
        <p class="mt-3 hidden-sm-and-down">Crear presentación</p>
      </v-btn>
    </v-row>
  </v-container>
</template>

<script>
import Chart from "chart.js";
import GraficoComponente from "../../components/reportes/Grafico.vue";
import Repository from "../../services/repositories/repositoryFactory";
const EstudiosRepository = Repository.get("Estudios");
const PreguntasRepository = Repository.get("Preguntas");
const EdicionesRepository = Repository.get("Ediciones");
export default {
  name: "Graficos",
  components: { GraficoComponente },

  data() {
    return {
      estudio_id: null,
      ediciones: [],
      tiposGrafico: [
        { id: "pie", nombre: "Torta" },
        { id: "bar", nombre: "Barras" },
      ],
      estudio: null,
      presentacion: [],
      preguntas : [],
      chartID: 0
    };
  },
  methods: {
    async getEdiciones(id) {
      this.ediciones = await EstudiosRepository.obtenerEdiciones(id);
    },
    limiteOpciones(e) {
      if(e.length > 2) {
        e.pop()
      }
    },
    async getEstudio(id){
      let estudios = await EstudiosRepository.consultar();
      estudios.forEach((est) => {
        if (est.id == id) {
          this.estudio = est;
        }
      });
    },
    agregarDiapositiva(){
      this.chartID = this.chartID + 1
      let diapositiva = {
          tipoGrafico: 'pie',
          texto: null,
          ediciones: null,
          pregunta: null,
          id: this.chartID
      }
      this.presentacion.push(diapositiva)
    },
    eliminarDiapositiva(){
      this.presentacion.pop()
    },
    esUltimo(id){
      let ultimoId = this.presentacion[this.presentacion.length-1].id;  
      if (id == ultimoId) return true
      else return false
    },
    async getPreguntas(){
      if (this.presentacion[0].ediciones.length <= 0){
        swal("", "Debe seleccionar una edición primero", "warning")
      }
      else { 
        this.preguntas = await PreguntasRepository.obtenerPreguntas(this.presentacion[0].ediciones);
      }
      
    },
    async crearPresentacion(){
        console.log(this.presentacion)
        let presentacion = await EdicionesRepository.crearPresentacion(this.presentacion);
        console.log(presentacion)
      }
  },
  mounted() {
    this.estudio_id = this.$route.params.id;
    this.getEstudio(this.estudio_id);
    this.getEdiciones(this.estudio_id);
    this.agregarDiapositiva()
  },
};
</script>

<style>
@import "../../styles/main.css";
.pregunta-card {
  border: black solid 1px;
  padding: 3%;
  margin: 20px 0px;
}
</style>