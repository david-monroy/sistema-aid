<template>
  <div class="col-md-12 pt-1">
    <div class="card-container mt-0 form-card">
      <v-form
        ref="registerForm"
        v-model="valid"
        lazy-validation
      >
        <v-row class="pb-0 mb-0 mt-2 form-row" >
            <v-col md="8" cols="8" class="py-0">
                <div class="form-group">
                    <v-textarea
                    v-model="form.descripcionCualitativa"
                    dense
                    label="Describa como aplicará la parte cualitativa del estudio"
                    :rules='[rules.textos]'
                    auto-grow
                    counter
                    rows="2"
                    ></v-textarea>
                </div>
            </v-col>
            <v-col md="4" cols="4" class="py-0">
                <v-select
                v-model="form.modalidadCualitativa"
                :items="modalidades"
                label="Modalidad"
                ></v-select>
            </v-col>
        </v-row>
        <v-row class="pb-0 mb-0 form-row" >
            <v-col md="8" cols="8" class="py-0">
                <div class="form-group">
                    <v-textarea
                    v-model="form.descripcionCuantitativa"
                    dense
                    label="Describa como aplicará la parte cuantitativa del estudio"
                    :rules='[rules.textos]'
                    auto-grow
                    counter
                    rows="2"
                    ></v-textarea>
                </div>
            </v-col>
            <v-col md="4" cols="4" class="py-0">
                <v-select
                v-model="form.modalidadCuantitativa"
                :items="modalidades"
                label="Modalidad"
                ></v-select>
            </v-col>
        </v-row>
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

export default {
    data(){
        return {
            valid:true,
            modalidades: ['Presencial autoadministrado', 'Presencial cara a cara', 'Online(autoadministrado)'],
            rules: {} = {
                textos: (value) => 
                (value.length <= 280) || "El texto es demasiado largo"
            },
            form: {
                descripcionCualitativa: '',
                modalidadCualitativa: '',
                descripcionCuantitativa:'', 
                modalidadCuantitativa:'',
                edicionId:''
            },
        }
    },
    props: {
        tipo:String
    },
    methods: {
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
                EventBus.$emit("pasoSiguiente",this.form)
            }
            else {
                EventBus.$emit("pasoSiguienteEdi",this.form)
            }
        }, 
        goRoute(route) {
            this.$router.push("/" + route);
        },
        async insertarInfo(){
            if (this.tipo == "Estudio"){
                 EventBus.$emit("registrar-estudio",this.form)
            }
            else {
                 EventBus.$emit("registrar-edicion",this.form)
            }
           
        },
    },
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>