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
                        label="Carga el archivo con la distribución de la población (Opcional)"
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
                <h4 class="mb-3">El tamaño muestral es: {{tamanoMuestral}}</h4>
                <v-data-table
                :headers="getHeaders()"
                :items="muestraPonderada"
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
                    @click="pasoSiguiente()"
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
const MuestraPonderadaRepository = Repository.get("MuestraPonderada");

export default {
    data(){
        return {
            file: "",
            valid:true,
            muestraPonderada: [],
        }
    },
    props: {
        tamanoMuestral: String,
        tipo:String
    },
    methods: {
        async cargarCSV(){
            const formData = new FormData();
            formData.append('file', this.file)
            try{
                this.muestraPonderada = await MuestraPonderadaRepository.cargarMuestra(formData, this.tamanoMuestral);
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
    },
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>