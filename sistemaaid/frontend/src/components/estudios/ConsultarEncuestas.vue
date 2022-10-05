<template>
  <div class="col-md-12 pt-1">
    <div class="card-container mt-0 form-card">
      <Loading :show=activeLoading />
      <v-row>
        <Boton titulo="Cargar encuestas" 
        :route=route
        permiso="backend | encuesta | Can add encuesta"></Boton>
        <Boton v-if="encuestas.length > 0" titulo="Codificar respuestas" 
          :route=route  
          permiso="backend | encuesta | Can add encuesta"></Boton>
        </v-row>
      <v-row>
      <v-text-field
      label="ID encuesta a consultar"
      v-model="encuestaId"
    ></v-text-field>
    <v-btn
                    :small="$vuetify.breakpoint.smAndDown"
                    class="primary"
                    @click="getEncuestas()"
                >Consultar</v-btn>
      </v-row>
      <v-row v-if="encuestas.length > 0">
        <DataTable :items="encuestas"></DataTable>  
      </v-row>
    </div>
  </div>
</template>

<script>
import Repository from "../../services/repositories/repositoryFactory";
import DataTable from "../../components/comunes/DataTable.vue"
import Boton from "../../components/comunes/Boton.vue"
const EdicionesRepository = Repository.get("Ediciones");
import exportFromJSON from "export-from-json";
import Loading from "../../components/comunes/Loading.vue"
export default {
  data: () => ({
    encuestas: [],
    route: "",
    activeLoading: false,
    encuestaId: ""
  }),
  props:{
      edicion: {},
  },
  components: {
    DataTable,
    Boton,
    Loading
    },
  beforeMount(){
    this.route = "ediciones/AgregarEncuestas/" + this.edicion.id;
  },
  methods:{
    async getEncuestas(){
        this.activeLoading=true;
        this.encuestas = await EdicionesRepository.obtenerEncuestas(this.encuestaId)
        this.activeLoading=false;
    },
     exportarExcel() {
      const data = this.instrumento;
      const fileName = "instrumento";
      const exportType = exportFromJSON.types.xls;

      exportFromJSON({ data, fileName, exportType });
    },
  }
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>