<template>
  <div class="col-md-12 pt-1">
    <div class="card-container mt-0 form-card">
        <div v-if="encuestas.length > 0">
            <DataTable :items="encuestas"></DataTable>    
        </div>
        <div v-else>
            <p> Cargar encuestas</p>    
        </div>
    </div>
</div>
</template>

<script>
import Repository from "../../services/repositories/repositoryFactory";
import DataTable from "../../components/comunes/DataTable.vue"
const EdicionesRepository = Repository.get("Ediciones");
export default {
  data: () => ({
    encuestas: []
  }),
  props:{
      edicion: {},
  },
  components: {
    DataTable
    },
  beforeMount(){
    this.getEncuestas(this.edicion.id)
  },
  methods:{
    async getEncuestas(id){
        this.encuestas = await EdicionesRepository.obtenerEncuestas(id)
        console.log(this.encuestas)
    },
  }
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>