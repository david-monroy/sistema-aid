<template>
  <div class="col-md-12 pt-1">
    <div class="card-container mt-0 form-card">
      <div v-if="instrumento.length > 0">
        <v-row >
          <v-btn
                    :small="$vuetify.breakpoint.smAndDown"
                    class="primary"
                    @click="exportarExcel()"
                >Exportar</v-btn>
        </v-row>
        
            <DataTable :items="instrumento"></DataTable>    
        </div>
        <div v-else>
            <p> Cargar instrumento</p>    
        </div>
    </div>
</div>
</template>

<script>
import Repository from "../../services/repositories/repositoryFactory";
import DataTable from "../../components/comunes/DataTable.vue"
const PreguntasRepository = Repository.get("Preguntas");
import exportFromJSON from "export-from-json";
export default {
  data: () => ({
    instrumento: [],
  }),
  props:{
      edicion: {},
  },
  components: {
    DataTable
    },
  beforeMount(){
    this.getInstrumento(this.edicion.id)
  },
  methods:{
    async getInstrumento(id){
        this.instrumento = await PreguntasRepository.obtenerInstrumento(id);
    },
    async exportarExcel() {

      await PreguntasRepository.dataEntry(this.edicion.id);
      
    },
  }
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>