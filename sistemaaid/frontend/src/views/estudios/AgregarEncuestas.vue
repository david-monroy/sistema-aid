<template>
  <v-container fluid elevation="0" class="nav-separator">
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
                                label="Carga el archivo con la distribución de la población (Opcional)"
                            ></v-file-input>
                        </div>
                    </v-col>
                    <v-col md="2" cols="2" align="end">
                <v-btn
                    :small="$vuetify.breakpoint.smAndDown"
                    class="primary"
                    @click="cargarExcel()"
                    :disable=!valid
                >
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
import { EventBus } from "../../main.js";
const EdicionRepository = Repository.get("Ediciones");

export default {
    data(){
        return {
            file: "",
            valid:true,
            respuesta: [],
        }
    },
    methods: {
        async cargarExcel(){
            const formData = new FormData();
            formData.append('file', this.file)
            try{
                this.respuesta = await EdicionRepository.cargarEncuestas(formData);
            }
            catch(err){
                console.log(err)
                swal("No se pudo procesar la muestra", "", "error")
            } 
        }    
    },
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>