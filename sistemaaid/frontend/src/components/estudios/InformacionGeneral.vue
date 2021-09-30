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
                    <v-autocomplete
                        v-model="form.estudio"
                        :items="estudios"
                        label="Estudio al que se le agregará una nueva edición"
                        item-text="nombre"
                        item-value="id"
                    ></v-autocomplete>
                </div>
            </v-col>
        </v-row>

        <v-row class="pb-0 mb-0 form-row" >
            <v-col md="4" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.codigo"
                        label="Código de la edición*"
                        required
                        :rules='[rules.required]'
                    ></v-text-field>
                </div>
            </v-col>

            <v-col md="4" cols="12" class="py-0">
                <div class="form-group">
                    <v-tooltip left>
                    <template v-slot:activator="{ on, attrs }">
                        <v-text-field
                            v-model="form.periodo"
                            label="Periodo"
                            v-bind="attrs"
                            v-on="on"
                        ></v-text-field>
                         </template>
                        <span>Período académico de la UCAB</span>
                    </v-tooltip> 
                </div>
            </v-col>

            <v-col md="4" cols="12" class="py-0">
                <div class="form-group">
                    <v-tooltip right>
                        <template v-slot:activator="{ on, attrs }">
                            <v-text-field
                            v-model="form.totalMuestra"
                            label="Total de la muestra *"
                            required
                            :rules='[rules.required,rules.muestra]'
                            v-bind="attrs"
                            v-on="on"
                            ></v-text-field>
                        </template>
                        <span>Cantidad de personas a encuestar</span>
                    </v-tooltip>
                    
                </div>
            </v-col>
        </v-row>

        <v-row class="pb-0 mb-0 form-row" >
            <v-col md="4" cols="12" class="py-0">
                <v-menu
                    ref="menu1"
                    v-model="menu1"
                    :close-on-content-click="false"
                    transition="scale-transition"
                    offset-y
                    max-width="290px"
                    min-width="auto"
                    >
                    <template v-slot:activator="{ on, attrs }">
                        <v-text-field
                            v-model="form.fechaInicio"
                            label="Fecha inicio *"
                            hint="AAAA-MM-DD"
                            persistent-hint
                            prepend-icon="fa-calendar"
                            v-bind="attrs"
                            v-on="on"
                            required
                            :rules='[rules.required]'
                        ></v-text-field>
                    </template>
                    <v-date-picker
                        v-model="form.fechaInicio"
                        no-title
                        color="primary"
                        @input="menu1 = false"
                        @change="actualizarFecha()"
                    ></v-date-picker>
                </v-menu>
            </v-col>

            <v-col md="4" cols="12" class="py-0">
                <v-menu
                    ref="menu2"
                    v-model="menu2"
                    :close-on-content-click="false"
                    transition="scale-transition"
                    offset-y
                    max-width="290px"
                    min-width="auto"
                    >
                    <template v-slot:activator="{ on, attrs }">
                        <v-text-field
                            v-model="form.fechaFin"
                            label="Fecha estimada fin *"
                            hint="AAAA-MM-DD"
                            persistent-hint
                            prepend-icon="fa-calendar"
                            v-bind="attrs"
                            v-on="on"
                            required
                            :rules='[rules.required]'
                        ></v-text-field>
                    </template>
                    <v-date-picker
                        v-model="form.fechaFin"
                        no-title
                        color="primary"
                        :min="form.fechaInicio"
                        @input="menu2 = false"
                    ></v-date-picker>
                </v-menu>
            </v-col>

            <v-col md="4" cols="12" class="py-0">
                <div class="form-group">
                    <v-checkbox
                        v-model="form.vinculada"
                        label="Vincular esta edición a versiones anteriores a la hora de mostrar reportes"
                    ></v-checkbox>
                </div>
            </v-col>
        </v-row>

        
        <v-row>
            <v-col align="begin">
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
                    @click="enviarDatos()"
                    :disable=!valid
                >
                    <p class="mt-3 hidden-sm-and-down">Muestra</p>
                    <v-icon>mdi-chevron-right</v-icon>
                </v-btn>
            </v-col>
        </v-row>
      </v-form>
    </div>
</div>
</template>


<script>
import { EventBus } from "../../main.js";
import moment from "moment";
import swal from 'sweetalert';
import axios from 'axios'

export default {
    data(){
        return {
            form: {
                codigo: '',
                periodo:'',
                fechaInicio: moment().format("YYYY-MM-DD"),
                fechaFin:'',
                idEstudio:'',
                vinculada: true,
                totalMuestra: '',

            },
            menu1:false,
            menu2:false,
            valid: true,
            estudios:[],
            rules: {} = {
                required: (value) =>
                (!!value && value !== "" && value !== undefined) || "Este campo es requerido",
                muestra: (value) =>
                (!!value && value > 0) || "La muestra debe ser mayor a 0",
            }
        }
    },
    computed: {},
    methods: {
        enviarDatos() {
            let validatedForm = this.$refs.registerForm.validate();

            if (validatedForm){
                if (this.form.fechaInicio > this.form.fechaFin){
                    swal("La fecha fin del estudio debe ser mayor a la fecha de inicio", "", "error")
                }
                else {
                    EventBus.$emit("informacion-general",this.form)
                }
            }
                
        },  
        actualizarFecha(){
            this.form.fechaFin = ''
        },
        goRoute(route) {
            this.$router.push("/" + route);
        },
        getEstudios(){
            const path = 'http://localhost:8000/api/v1/estudios/'
            axios.get(path).then((response) => {
                this.estudios = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        },
    },
    mounted(){
        this.getEstudios();
    }
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>