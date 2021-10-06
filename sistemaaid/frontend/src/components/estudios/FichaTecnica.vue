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
                        label="Código "
                        required
                        :rules='[rules.required]'
                    ></v-text-field>
                </div>
            </v-col>
            <v-col md="10" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.nombre"
                        label="Nombre del Estudio"
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
                        label="Objetivo del negocio"
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
                        label="Objetivo de la Organización"
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
                        label="Población objetivo"
                        required
                        :rules='[rules.required]'
                    ></v-text-field>
                </div>
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

export default {
    data(){
        return {
            form: {
                codigo: '',
                nombre: '',
                poblacionObjetivo:'', 
                antecedentes:'', 
                objetivoNegocio :'',
                objetivoOrganizacion:''
            },
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