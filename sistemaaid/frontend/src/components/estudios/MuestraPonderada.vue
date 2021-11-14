<template>
  <div class="col-md-12 pt-1">
    <div class="card-container mt-0 form-card">
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
                        label="Carga el archivo con la distribución de la población"
                    ></v-file-input>
                </div>
            </v-col>
            <v-col md="2" cols="2" align="end">
                <v-btn
                    :small="$vuetify.breakpoint.smAndDown"
                    class="primary"
                    @click="cargarCSV()"
                    :disable=!valid
                >
                    <p class="mt-3 hidden-sm-and-down">Cargar</p>
                    <v-icon>mdi-chevron-right</v-icon>
                </v-btn>
            </v-col>
        </v-row>
            <div v-if="muestraPonderada.length > 0">
                <v-data-table
                :headers="getHeaders()"
                :items="muestraPonderada"
                hide-default-footer
                :items-per-page="-1"
                class="elevation-1"
                >
                </v-data-table>
            </div>
        <v-row class="mt-2">
            <v-col align="begin">
                <v-btn
                    :small="$vuetify.breakpoint.smAndDown"
                    class="primary"
                    @click="paso1()"
                    :disable=!valid
                >
                <p class="mt-3 hidden-sm-and-down">Atrás</p>
                    <v-icon>mdi-chevron-right</v-icon>
                </v-btn>
            </v-col>
            <v-col align="center">
                <v-btn
                    text
                    :small="$vuetify.breakpoint.smAndDown"
                    class="red--text"
                    @click="goRoute('estudios')">Cancelar
                </v-btn>
            </v-col>
            <v-col align="end">
                <v-btn
                    :small="$vuetify.breakpoint.smAndDown"
                    class="primary"
                    @click="cargarCSV()"
                    :disable=!valid
                >
                    <p class="mt-3 hidden-sm-and-down">Siguiente</p>
                    <v-icon>mdi-chevron-right</v-icon>
                </v-btn>
            </v-col>
        </v-row>
      </v-form>
    </div>

   
</div>
</template>



<script>
import swal from 'sweetalert'
import Repository from "../../services/repositories/repositoryFactory";
const MuestraPonderadaRepository = Repository.get("MuestraPonderada");

export default {
    data(){
        return {
            file: "",
            valid:true,
            muestraPonderada: [],
        }
    },
    methods: {
        async cargarCSV(){
            const formData = new FormData();
            formData.append('file', this.file)
            try{
                this.muestraPonderada = await MuestraPonderadaRepository.cargarMuestra(formData);
                console.log (this.muestraPonderada)  
            }
            catch(err){
                console.log(err)
                swal("No se pudo procesar la muestra", "", "error")
            } 
        },
        getHeaders(){
            var headers = []
            for (var key in this.muestraPonderada[0]){      
                var head = {
                   text: key, 
                   value: key
                }
                headers.push(head)
            }
            return headers
        },
        paso1() {
            let validatedForm = this.$refs.registerForm.validate();

            if (validatedForm){
                if (this.form.fechaInicio > this.form.fechaFin){
                    swal("La fecha fin del estudio debe ser mayor a la fecha de inicio", "", "error")
                }
                else {
                    EventBus.$emit("paso2",this.form)
                }
            }   
        },  
        paso3() {
            let validatedForm = this.$refs.registerForm.validate();

            if (validatedForm){
                if (this.form.fechaInicio > this.form.fechaFin){
                    swal("La fecha fin del estudio debe ser mayor a la fecha de inicio", "", "error")
                }
                else {
                    EventBus.$emit("paso2",this.form)
                }
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