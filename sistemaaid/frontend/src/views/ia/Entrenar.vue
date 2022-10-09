<template>
  <v-container fluid elevation="0" class="nav-separator">
    <Loading :show=activeLoading />
    <v-row no-gutters justify="center">
      <h3 class="primary--text mx-auto mb-6 mt-0 md=8">Reentrenar modelo</h3>
    </v-row>
    <v-row
      align="center"
      class="list px-3 mx-auto nav-separator container mt-12"
      style="display: flex; justify-content: center"
    >
      <v-col cols="12" sm="6" class="mt-4">
        Seleccione el modelo a entrenar
        <v-select
          v-model="listaCodigoSelect"
          :items="listasDeCodigo"
          item-text="nombre"
          item-value="id"
          chips
          label="Modelos"
          outlined
          class="mt-2"
        ></v-select>
      </v-col>
    </v-row>
    <v-row no-gutters justify="center">
      <v-col cols="12" md="8" align="center">
        <div class="card-container mt-0 form-card">
            <v-form
                ref="registerForm"
                v-model="valid"
                lazy-validation>
                <v-row class="pb-0 mb-0 form-row" >
                    <v-col md="10" cols="10" class="py-0">
                        <div class="form-group">
                            <v-file-input
                                v-model="file"
                                truncate-length="15"
                                label="Sube el archivo con los registros para entrenar"
                            ></v-file-input>
                        </div>
                    </v-col>
                    <v-col md="2" cols="2" align="end">
                <v-btn
                    :small="$vuetify.breakpoint.smAndDown"
                    class="primary"
                    @click="cargarExcel()"
                    :disable=!valid>
                    <p class="mt-3 hidden-sm-and-down">Cargar</p>
                    <v-icon>mdi-chevron-right</v-icon>
                </v-btn>
            </v-col>
                </v-row>
            </v-form>
        </div> 
      </v-col>
    </v-row>
  </v-container>
</template>



<script>
import swal from 'sweetalert'
import Repository from "../../services/repositories/repositoryFactory";
import Loading from "../../components/comunes/Loading.vue"
import { EventBus } from "../../main.js";
const EdicionRepository = Repository.get("Ediciones");
const ListaCodigoRepository = Repository.get("ListaCodigo");
import exportFromJSON from "export-from-json";
const IaRepository = Repository.get("IA");

export default {
    data(){
        return {
            file: "",
            valid:true,
            respuesta: [],
            idEdicion: null,
            edicion: {},
            activeLoading: false,
            listaCodigoSelect: true,
            listasDeCodigo: []
        }
    },
     mounted(){
        this.username = this.$store.getters["users/getUser"].username;
    },
    components: {
        Loading
    },
    methods: {
        async cargarExcel(){
            const formData = new FormData();
            formData.append('file', this.file)
            try{
                this.activeLoading = true;
                this.respuesta= await IaRepository.entrenar(formData, this.listaCodigoSelect);
                this.activeLoading = false 
                if (this.respuesta.status == 200 ){
                    swal("", this.respuesta.detail, "success");
                }
            }
            catch(err){
                this.activeLoading = false
                swal("Error", this.respuesta.error[0], "error")
            } 
        },
        async getListasDeCodigo(){
            try{
                this.listasDeCodigo = await ListaCodigoRepository.consultar();
            }
            catch(err){
                console.log(err)
                swal("No se pudo obtener las listas de código", "", "error")
            }
        },
        
    },
    mounted(){
        this.getListasDeCodigo();
    }
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>