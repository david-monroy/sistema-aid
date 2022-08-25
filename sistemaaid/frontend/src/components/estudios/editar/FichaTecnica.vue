<template>
  <div class="col-md-12 pt-1">
    <div class="card-container mt-0 form-card">
      <v-form
        ref="registerForm"
        v-model="valid"
        lazy-validation
      >
        <v-row class="pb-0 mb-0 form-row mt-4" >
            <v-col md="2" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.codigo"
                        label="Código *"
                        required
                        disabled
                        dense
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
                        dense
                        :rules='[rules.required]'
                    ></v-text-field>
                </div>
            </v-col>
        </v-row>

        <v-row class="pb-0 mb-0 form-row" >
            <v-col md="12" cols="12" class="py-0">
                <div class="form-group">
                    <v-textarea
                    v-model="form.antecedentes"
                    dense
                    label="Antecedentes del estudio"
                    :rules='[rules.textos]'
                    auto-grow
                    counter
                    rows="2"
                    ></v-textarea>
                </div>
            </v-col>
        </v-row>

        <v-row class="pb-0 mb-0 form-row" >
            <v-col md="12" cols="12" class="py-0">
                <div class="form-group">
                    <v-textarea
                    v-model="form.objetivoNegocio"
                    dense
                    label="Objetivo del negocio/organización *"
                    :rules='[rules.required, rules.textos]'
                    counter
                    auto-grow
                    rows="2"
                    ></v-textarea>
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
                        dense
                        :rules='[rules.required, rules.poblacion]'
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
import { EventBus } from "../../../main.js";
import moment from "moment";
import swal from 'sweetalert';
import Repository from "../../../services/repositories/repositoryFactory";
const EstudiosRepository = Repository.get("Estudios");

export default {
    data(){
        return {
            date: new Date().toISOString().substr(0, 10),
            dateFormatted: this.formatDate(new Date().toISOString().substr(0, 10)),
            menu1:false,
            menu2:false,
            valid: true,
            rules: {} = {
                required: (value) =>
                (!!value && value !== "" && value !== undefined) || "Este campo es requerido",
                muestra: (value) =>
                (!!value && value > 0) || "La muestra debe ser mayor a 0",
                textos: (value) => 
                (value.length <= 280) || "El texto es demasiado largo",
                poblacion: (value) => 
                (value.length <= 50) || "El texto es demasiado largo",

            }
        }
    },
    props: {
        form: Object
    },
    computed: {
        computedDateFormatted () {
        return this.formatDate(this.date)
      },
    },
    methods: {
        formatDate (date) {
            if (!date) return null
            const [year, month, day] = date.split('-')
            return `${year}-${month}-${day}`
        },
        parseDate (date) {
            if (!date) return null
            const [month, day, year] = date.split('/')
            return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
        },
        async pasoSiguiente() {
            let validatedForm = this.$refs.registerForm.validate();
            if (validatedForm){
                EventBus.$emit("pasoSiguienteEdicion", this.form)
            }   
        },  
        actualizarFecha(){
            this.form.fechaFin = ''
        },
        goRoute(route) {
            this.$router.push("/" + route);
        },
    },
    watch: {
      date () {
        this.fechaFin = this.formatDate(this.date)
      },

    },
}
</script>

<style>
@import "../../../styles/main.css";
@import "../../../styles/components/participantes.css";
</style>