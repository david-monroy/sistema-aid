<template>
  <div class="col-md-12 pt-1">
    <div class="card-container mt-0 form-card">
      <v-form
        ref="registerForm"
        v-model="valid"
        lazy-validation
      >
        <v-row class="pb-0 mb-0 form-row" >
            <v-col md="12" cols="12" class="py-0">
                <div class="form-group">
                    <v-file-input
                        v-model="file"
                        truncate-length="15"
                        label="Carga el archivo con la distribución de la población"
                    ></v-file-input>
                </div>
            </v-col>
        </v-row>
        <v-row>
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

    <div>
        <v-data-table
      :items="muestraPonderada"
      class="elevation-1"
    >
    </v-data-table>
    </div>
</div>
</template>



<script>
import swal from 'sweetalert'
import Repository from "../../services/repositories/repositoryFactory";
import muestraPonderadaRepository from '../../services/repositories/Estudios/muestraPonderada.repository';
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