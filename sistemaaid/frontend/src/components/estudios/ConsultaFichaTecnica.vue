<template>
  <div class="col-md-12 pt-1">
    <div class="card-container mt-0 form-card">
        <v-row class="pb-0 mb-0 form-row mt-4" >
            <v-col md="12" cols="12" class="py-0 info-text" v-if='edicion.estudio.antecedentes'>
                <strong>Antecedentes del estudio: </strong> 
                <span>{{edicion.estudio.antecedentes}}</span>
            </v-col>
        </v-row>  
        <v-row class="pb-0 mb-0 form-row mt-4" >
            <v-col md="12" cols="12" class="py-0 info-text" v-if='edicion.estudio.objetivoNegocio'>
                <strong>Objetivo del negocio/organización: </strong> 
                <span>{{edicion.estudio.objetivoNegocio}}</span>
            </v-col>
        </v-row>   
        <v-row class="pb-0 mb-0 form-row mt-4" >
            <v-col md="12" cols="12" class="py-0 info-text" v-if='edicion.estudio.poblacionObjetivo'>
                <strong>Población objetivo: </strong> 
                <span>{{edicion.estudio.poblacionObjetivo}}</span>
            </v-col>
        </v-row> 
        <v-row class="pb-0 mb-0 form-row mt-4" >
            <v-col md="3" cols="12" class="py-0 info-text" v-if='edicion.periodo'>
                <strong>Período: </strong> 
                <span>{{edicion.periodo}}</span>
            </v-col>
            <v-col md="3" cols="12" class="py-0 info-text" v-if='edicion.totalMuestra'>
                <strong>Tamaño muestral: </strong> 
                <span>{{edicion.totalMuestra}}</span>
            </v-col>
            <v-col md="3" cols="12" class="py-0 info-text" v-if='edicion.fechaInicio'>
                <strong>Fecha inicio: </strong> 
                <span>{{edicion.fechaInicio}}</span>
            </v-col>
            <v-col md="3" cols="12" class="py-0 info-text" v-if='edicion.fechaFin'>
                <strong>Fecha fin: </strong> 
                <span>{{edicion.fechaFin}}</span>
            </v-col>
        </v-row> 
        <v-row class="pb-0 mb-0 form-row mt-4" v-if='metodologia'>
            <strong class="primary--text">METODOLOGÍA: </strong> 
        </v-row>
        <v-row class="pb-0 mb-0 form-row mt-4" >
            <v-col md="3" cols="12" class="py-0 info-text" v-if='metodologia.modalidadCuantitativa' >
                <strong>Cualitativa: </strong> 
                <span>{{metodologia.descripcionCualitativa}}</span>
            </v-col>
            <v-col md="3" cols="12" class="py-0 info-text" v-if='metodologia.modalidadCualitativa'>
                <strong>Modalidad: </strong> 
                <span>{{metodologia.modalidadCualitativa}}</span>
            </v-col>
            <v-col md="3" cols="12" class="py-0 info-text" v-if='metodologia.descripcionCuantitativa'>
                <strong>Cuantitativa: </strong> 
                <span>{{metodologia.descripcionCuantitativa}}</span>
            </v-col>
            <v-col md="3" cols="12" class="py-0 info-text" v-if='metodologia.modalidadCuantitativa'>
                <strong>Modalidad: </strong> 
                <span>{{metodologia.modalidadCuantitativa}}</span>
            </v-col>
        </v-row> 
    </div>
</div>
</template>


<script>
import Repository from "../../services/repositories/repositoryFactory";
const MetodologiaRepository = Repository.get("Metodologia");
export default {
  data: () => ({
    metodologia: {}
  }),
  props:{
      edicion: {},
  },
  mounted(){
    this.getMetodologia(this.edicion.id)
  },
  methods:{
    async getMetodologia(id){
        this.metodologia = await MetodologiaRepository.buscarMetodologia(id)

    }
  }
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>