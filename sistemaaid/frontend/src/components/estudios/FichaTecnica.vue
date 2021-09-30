<template>
  <div class="col-md-12 pt-1">
    <div class="card-container mt-0 form-card">
      <v-form
        ref="registerForm"
        v-model="valid"
        lazy-validation
      >
        <v-row class="pb-0 mb-0 form-row" >
            <v-col md="2" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.codigo"
                        label="Código *"
                        required
                        :rules='[rules.required]'
                    ></v-text-field>
                </div>
            </v-col>
            <v-col md="10" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.nombre"
                        label="Nombre del Estudio *"
                        required
                        :rules='[rules.required]'
                    ></v-text-field>
                </div>
            </v-col>
        </v-row>

        <v-row class="pb-0 mb-0 form-row" >
            <v-col md="12" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.antecendentes"
                        label="Antecedentes del estudio"
                    ></v-text-field>
                </div>
            </v-col>
        </v-row>

        <v-row class="pb-0 mb-0 form-row" >
            <v-col md="12" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.objetivoNegocio"
                        label="Objetivo del negocio *"
                        required
                        :rules='[rules.required]'
                    ></v-text-field>
                </div>
            </v-col>
        </v-row>

        <v-row class="pb-0 mb-0 form-row" >
            <v-col md="12" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.objetivoOrganizacion"
                        label="Objetivo de la Organización *"
                        required
                        :rules='[rules.required]'
                    ></v-text-field>
                </div>
            </v-col>
        </v-row>

        <v-row class="pb-0 mb-0 form-row" >
            <v-col md="12" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.poblacionObjetivo"
                        label="Población objetivo *"
                        required
                        :rules='[rules.required]'
                    ></v-text-field>
                </div>
            </v-col>
        </v-row>

        <v-row class="pb-0 mb-0 form-row" >
            <v-col md="6" cols="12" class="py-0">
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

            <v-col md="6" cols="12" class="py-0">
                <div class="form-group">
                    <v-tooltip right>
                        <template v-slot:activator="{ on, attrs }">
                            <v-text-field
                            v-model="form.totalMuestra"
                            label="Total de la muestra"
                            required
                            :rules='[rules.required]'
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
            <v-col md="6" cols="12" class="py-0">
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
                    ></v-date-picker>
                </v-menu>
            </v-col>

            <v-col md="6" cols="12" class="py-0">
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
                        @input="menu1 = false"
                    ></v-date-picker>
                </v-menu>
            </v-col>
        </v-row>

        
        <v-row>
            <v-col align="begin"></v-col>
            <v-col align="center">
                <v-btn
                    text
                    :small="$vuetify.breakpoint.smAndDown"
                    class="red--text"
                    @click="goRoute('HomeUser')">Cancelar
                </v-btn>
            </v-col>
            <v-col align="end">
                <v-btn
                    :small="$vuetify.breakpoint.smAndDown"
                    class="primary"
                    @click="ComponentsInformation()"
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

export default {
    data(){
        return {
            form: {
                codigo: '',
                nombre: '',
                poblacionObjetivo:'', 
                antecedentes:'', 
                objetivoNegocio :'',
                objetivoOrganizacion:'',
                periodo:'',
                fechaInicio: moment().format("YYYY-MM-DD"),
                fechaFin:'',
                idEstudio:'',
                vinculada: true,
                totalMuestra: 1000
            },
            menu1:false,
            menu2:false,
            rules: {} = {
                required: (value) =>
                (!!value && value !== "" && value !== undefined) || "Este campo es requerido",
            }
        }
    },
    computed: {},
    methods: {
        
        ComponentsInformation() {
            let validatedForm = this.$refs.registerForm.validate();

            if (validatedForm){
                EventBus.$emit("ficha-tecnica",this.form)
            }
                
        },  
    },
    mounted(){}
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>