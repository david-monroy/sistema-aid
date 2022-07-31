<template>
  <div class="col-md-12 pt-1">
    <div class="card-container mt-0 form-card">
      <v-row>
        <Boton titulo="Cargar encuestas" 
        :route=route
        permiso="backend | encuesta | Can add encuesta"></Boton>
        <Boton v-if="encuestas.length > 0" titulo="Codificar respuestas" 
          :route=route  
          permiso="backend | encuesta | Can add encuesta"></Boton>
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
import AgregarEncuestas from "../../components/estudios/AgregarEncuestas.vue"
const EdicionesRepository = Repository.get("Ediciones");
export default {
  data: () => ({
    encuestas: [],
    route: ""
  }),
  props:{
      edicion: {},
  },
  components: {
    DataTable,
    AgregarEncuestas,
    Boton
    },
  beforeMount(){
    this.getEncuestas(this.edicion.id);
    this.route = "ediciones/AgregarEncuestas/" + this.edicion.id;
  },
  methods:{
    async getEncuestas(id){
        this.encuestas = await EdicionesRepository.obtenerEncuestas(id)
    },
  }
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>