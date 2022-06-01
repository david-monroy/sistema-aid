<template>
  <div class="col-md-12 pt-1">
    <div class="card-container mt-0 form-card">
        <v-row class="pb-0 mb-0 form-row mt-4" >
            <v-col md="12" cols="12" class="py-0">
                <strong>Antecedentes del estudio: </strong> 
                <span>{{edicion.estudio.antecedentes}}</span>
            </v-col>
        </v-row>  
        <v-row class="pb-0 mb-0 form-row mt-4" >
            <v-col md="12" cols="12" class="py-0">
                <strong>Objetivo del negocio/organización: </strong> 
                <span>{{edicion.estudio.objetivoNegocio}}</span>
            </v-col>
        </v-row>   
        <v-row class="pb-0 mb-0 form-row mt-4" >
            <v-col md="12" cols="12" class="py-0">
                <strong>Población objetivo: </strong> 
                <span>{{edicion.estudio.poblacionObjetivo}}</span>
            </v-col>
        </v-row> 
        <v-row class="pb-0 mb-0 form-row mt-4" >
            <v-col md="6" cols="12" class="py-0">
                <strong>Período: </strong> 
                <span>{{edicion.periodo}}</span>
            </v-col>
            <v-col md="6" cols="12" class="py-0">
                <strong>Tamaño muestral: </strong> 
                <span>{{edicion.tamanoMuestral}}</span>
            </v-col>
        </v-row>  
        <v-row class="pb-0 mb-0 form-row mt-4" >
            <v-col md="6" cols="12" class="py-0">
                <strong>Fecha inicio: </strong> 
                <span>{{edicion.fechaInicio}}</span>
            </v-col>
            <v-col md="6" cols="12" class="py-0">
                <strong>Fecha fin: </strong> 
                <span>{{edicion.fechaFin}}</span>
            </v-col>
        </v-row>    
    </div>
</div>
</template>


<script>
import Repository from "../../services/repositories/repositoryFactory";
const EdicionesRepository = Repository.get("Ediciones");
export default {
  data: () => ({
      edicion:[]
  }),
  props:{
      id: Number,
  },
  mounted(){
      this.getEdicion();
  },
  methods:{
      async getEdicion(){
        this.edicion = await EdicionesRepository.consultarPorId(this.id);    
      }
  }
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>