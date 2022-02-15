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
                        label="Carga el archivo con la lista de preguntas"
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
            <div v-if="preguntas.length > 0">
                <v-data-table
                :headers="headers"
                :items="preguntas"
                hide-default-footer
                :items-per-page="-1"
                class="elevation-1"
                >
                </v-data-table>
            </div>
            <div v-else>
                <p> A continuación puede cargar un archivo .csv para obtener la distribución de la población para este estudio.</p>
                <p> Puede guiarse de esta tabla, puede agregar tantas columnas desee.</p>
                <img
                src="../../assets/tablademuestraponderada.png"
                />
                
            </div>
        <v-row class="mt-2">
            <v-col align="begin">
                <v-btn
                    :small="$vuetify.breakpoint.smAndDown"
                    class="primary"
                    @click="pasoAnterior()"
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
                    @click="insertarInfo()"
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
import { EventBus } from "../../main.js";
const PreguntasRepository = Repository.get("Preguntas");

export default {
    data(){
        return {
            file: "",
            valid:true,
            preguntas: [],
            headers: [
            {
                text: 'Código',
                align: 'start',
                value: 'Codigo',
            },
            { text: 'Etiqueta', value: 'Pregunta' },
            { text: 'Tipo', value: 'Tipo' },
            ]
        }
    },
    methods: {
        async cargarCSV(){
            const formData = new FormData();
            formData.append('file', this.file)
            try{
               this.preguntas = await PreguntasRepository.preview(formData);
               console.log(this.preguntas)
            }
            catch(err){
                console.log(err)
                swal("No se pudoieron cargar las preguntas", "", "error")
            } 
        },
        pasoAnterior() {
            if (this.tipo == "Estudio"){
                EventBus.$emit("pasoAnterior",this.form)
            }
            else {
                EventBus.$emit("pasoAnteriorEdi",this.form)
            }

        },  
        pasoSiguiente() {
            if (this.tipo == "Estudio"){
                EventBus.$emit("pasoSiguiente",this.muestraPonderada)
            }
            else {
                EventBus.$emit("pasoSiguienteEdi",this.muestraPonderada)
            }
        }, 
        goRoute(route) {
            this.$router.push("/" + route);
        },
        async insertarInfo(){
            if (this.tipo == "Estudio"){
                 EventBus.$emit("registrar-estudio",this.preguntas)
            }
            else {
                 EventBus.$emit("registrar-edicion",this.preguntas)
            }
           
        },
    },
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>