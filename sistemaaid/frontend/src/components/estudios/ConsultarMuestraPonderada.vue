<template>
  <div class="col-md-12 pt-1">
    <div class="card-container mt-0 form-card">
        <div v-if="muestraPonderada.length > 0">
            <DataTable :items="muestraPonderada"></DataTable>    
        </div>
        <div v-else>
            <p> Cargar muestra</p>    
        </div>
    </div>
</div>
</template>

<script>
import Repository from "../../services/repositories/repositoryFactory";
import DataTable from "../../components/comunes/DataTable.vue"
const MuestraPonderadaRepository = Repository.get("MuestraPonderada");
export default {
  data: () => ({
    muestraPonderada: []
  }),
  props:{
      edicion: {},
  },
  components: {
    DataTable
    },
  beforeMount(){
    this.getMuestra(this.edicion.id)
  },
  methods:{
    async getMuestra(id){
        this.muestraPonderada = await MuestraPonderadaRepository.obtenerMuestra(id)
    },
  }
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>