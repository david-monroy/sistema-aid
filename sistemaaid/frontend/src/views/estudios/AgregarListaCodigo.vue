<template>
<div class="col-md-12 nav-separator pt-1">
    <div class="card card-container mt-0 form-card">
      <h3 class="primary--text mx-auto mb-6 mt-0">Registrar nuevo participante</h3>
      <v-spacer></v-spacer>
      <v-form
        ref="registerForm"
        v-model="valid"
        lazy-validation
      >
    <v-row class="pb-0 mb-0 form-row" >
        <v-col md="10" cols="10" class="py-0">
            <div class="form-group">
                <v-file-input
                        v-model="file"
                        truncate-length="15"
                        label="Carga el archivo con la lista de código"
                ></v-file-input>
            </div>
        </v-col>
        <v-col md="2" cols="2" align="end">
            <v-btn
                    :small="$vuetify.breakpoint.smAndDown"
                    class="primary"
                    @click="cargarListaCodigo()"
                    :disable=!valid
            >
            <p class="mt-3 hidden-sm-and-down">Cargar</p>
            <v-icon>mdi-chevron-right</v-icon>
            </v-btn>
        </v-col>
    </v-row>
      </v-form>
        <div>
            <p> A continuación puede cargar la lista de códgio desde un archivo .csv.</p>
            <p> El archivo debe estar como se muestra a acontinuación</p>
            <img
                src="../../assets/tablademuestraponderada.png"
            />  
        </div>
    </div>
</div>
</template>



<script>
import swal from 'sweetalert'
import Repository from "../../services/repositories/repositoryFactory";
const ListaCodigoRepository = Repository.get("ListaCodigo");

export default {
    data(){
        return {
            file: "",
            valid:true
        }
    },
    props: {
        tamanoMuestral: String,
        tipo:String
    },
    methods: {
        async cargarListaCodigo(){
            const formData = new FormData();
            formData.append('file', this.file)
            try{
                await ListaCodigoRepository.cargarListaCodigo(formData);
            }
            catch(err){
                console.log(err)
                swal("No se pudo procesar la muestra", "", "error")
            } 
        },
        goRoute(route) {
            this.$router.push("/" + route);
        },
    },
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>