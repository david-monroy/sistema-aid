<template>
  <v-container fluid elevation="0" class="nav-separator">
    <Loading :show=activeLoading />
    <v-row no-gutters justify="center">
      <h3 class="primary--text mx-auto mb-6 mt-0 md=8">Preprocesamiento</h3>
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
                                label="Sube el archivo que deseas limpiar"
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
            activeLoading: false
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
                this.respuesta= await IaRepository.preprocesamiento(formData);
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
        
    },
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>