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
            <v-col md="6" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.nombre"
                        label="Nombre y apellido"
                        required
                        :rules='[rules.required]'
                    ></v-text-field>
                </div>
            </v-col>
            <v-col md="6" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.cedula"
                        label="Cédula"
                        name="cedula"
                        required
                        :rules='[rules.required]'
                    ></v-text-field>
                </div>
            </v-col>
          </v-row>

          <v-row class="pb-0 mb-0 form-row" >
            <v-col md="6" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.correo"
                        label="Correo electrónico"
                        required
                        :rules='[rules.emailRules]'
                    ></v-text-field>
                </div>
            </v-col>
            <v-col md="6" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.correoUcab"
                        label="Correo UCAB"
                    ></v-text-field>
                </div>
            </v-col>
          </v-row>
        <v-row class="pb-0 mb-0 form-row" >
            <v-col md="6" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.telfPrincipal"
                        type="number"
                        label="Teléfono primario"
                        required
                        :rules='[rules.required, rules.PhoneRules]'
                    ></v-text-field>
                </div>
            </v-col>
            <v-col md="6" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.telfSecundario"
                        label="Teléfono secundario"
                        type='number'
                    ></v-text-field>
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
                                v-model="date"
                                label="Fecha"
                                hint="AAAA-MM-DD"
                                persistent-hint
                                prepend-icon="fa-calendar"
                                v-bind="attrs"
                                @blur="date = parseDate(dateFormatted)"
                                v-on="on"
                            ></v-text-field>
                        </template>
                        <v-date-picker
                            v-model="date"
                            no-title
                            max="2010-01-01"
                            color="primary"
                            @input="menu1 = false"
                        ></v-date-picker>
                    </v-menu>
                </v-col>
                <v-col md="4" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="edad_calculada"
                        label="Edad"
                        required
                        readonly
                    ></v-text-field>
                </div>
            </v-col>

              
            <v-col md="4" cols="12" class="py-0">
                <div class="form-group" style="display: flex; justify-content: center; width: 100%">
                    <v-select
                        v-model="form.genero"
                        :items="generos"
                        item-text="nombre"
                        item-value="id"
                        label="Género"
                        ></v-select>
                </div>
            </v-col>
          </v-row>

          <v-expansion-panels class="my-6">
            <v-expansion-panel>
            <v-expansion-panel-header>
                Estudios (opcional)
            </v-expansion-panel-header>
            <v-expansion-panel-content>
                <v-row class="pb-0 mb-0 form-row" >
                    <v-col md="6" cols="12" class="py-0">
                        <v-autocomplete
                        v-model="form.colegio"
                        :items="colegios"
                        label="Colegio"
                        item-text="nombre"
                        item-value="id"
                        ></v-autocomplete>
                    </v-col>

                    <v-col md="6" cols="12" class="py-0">
                        <v-select
                        v-model="form.sede"
                        :items="sedes"
                        item-text="nombre"
                        item-value="id"
                        label="Sede"
                        ></v-select>
                    </v-col>

                </v-row>

                <v-row class="pb-0 mb-0 form-row" >

                    <v-col md="6" cols="12" class="py-0">
                        <v-autocomplete
                        v-model="form.carrera"
                        :items="carreras"
                        label="Carrera"
                        item-text="nombre"
                        item-value="id"
                        ></v-autocomplete>
                    </v-col>

                    <v-col md="6" cols="12" class="py-0">
                        <v-select
                        v-model="form.semestre"
                        :items="semestres"
                        item-text="nombre"
                        item-value="id"
                        label="Semestre"
                        ></v-select>
                    </v-col>

                </v-row>
            </v-expansion-panel-content>
            </v-expansion-panel>
        </v-expansion-panels>

            <v-btn @click="registrarParticipante"
                :disabled="!valid"
                class="btn secondary btn-block w-50 my-2 mx-auto  d-none d-sm-flex">
                Registrar
            </v-btn>
            <v-btn @click="goRoute(back)"
                class="btn-block accent1 w-25 mx-auto  mb-0 d-none d-sm-flex">
                Regresar
            </v-btn>
      </v-form>
    </div>

  </div>
</template>


<script>
import axios from 'axios'
import swal from 'sweetalert'

export default {
    data(){
        return {
            form: {
                nombre: '',
                genero: '',
                cedula: '',
                fechaNacimiento: null,
                edad: null,
                correo: '',
                correoUcab: '',
                telfPrincipal: '',
                telfSecundario: null,
                carrera: null,
                sede: null,
                colegio: null,
                participante: null
            },
            date: new Date().toISOString().substr(0, 10),
            dateFormatted: this.formatDate(new Date().toISOString().substr(0, 10)),
            menu1: false,
            back:'participantes',
            carreras: [],
            sedes: [],
            colegios: [],
            generos: [
                { nombre: 'Masculino', id: 'M'},
                { nombre: 'Femenino', id: 'F'},
                { nombre: 'Otro', id: 'O'}
            ],
            semestres: [
                { nombre: 'Egresado', id: 11},
                { nombre: '1ro', id: 1},
                { nombre: '2do', id: 2},
                { nombre: '3ro', id: 3},
                { nombre: '4to', id: 4},
                { nombre: '5to', id: 5},
                { nombre: '6to', id: 6},
                { nombre: '7mo', id: 7},
                { nombre: '8vo', id: 8},
                { nombre: '9no', id: 9},
                { nombre: '10mo', id: 10},
            ],
            rules: {} = {
                required: (value) =>
                (!!value && value !== "" && value !== undefined) || "Este campo es requerido",
                cedulaRules: 
                (v) => (v && v.length >= 6) || "Número de cédula inválido",
                emailRules: 
                (v) => /.+@.+\..+/.test(v) || "Dirección de correo inválida",
                emailUcabRules: 
                (v) => /.+@.+\..+\..+\../.test(v) || "Dirección de correo UCAB inválida",
                PhoneRules: 
                (v) => (v && v.length == 11) || "Número de teléfono debe tener 11 dígitos",
                
            }
        }
    },
    computed: {
      computedDateFormatted () {
        return this.formatDate(this.date)
      },

      edad_calculada(){
        var hoy = new Date();
        var fecha_nac = new Date(this.date);
        var edad = hoy.getFullYear() - fecha_nac.getFullYear();
        var m = hoy.getMonth() - fecha_nac.getMonth();

        if (m < 0 || (m === 0 && hoy.getDate() < fecha_nac.getDate())) {
            edad--;
        }

        return edad;
      }
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
        async registrarParticipante() {

            let validatedForm = this.$refs.registerForm.validate();
            this.form.fechaNacimiento = this.fechaNacimiento;
            this.form.edad = this.edad_calculada;
            const participante_path = 'http://localhost:8000/api/v1/participantes/'

            if (validatedForm){

                if (this.form.edad < 11) {
                    swal("El participante debe ser mayor de 11 años", "", "error") 
                } else {
                    
                await axios.post(participante_path, this.form).then((response) => {
                    this.form.participante = response.data.id

                    if (this.form.carrera && this.form.sede) {
                        this.registrarParticipanteCarrera()
                    }
                    swal("Participante creado satisfactoriamente", "", "success")
                })
                .catch((err) => {
                    console.log(err)
                    swal("Participante no pudo ser creado", "", "error")
                })
                //this.$refs.registerForm.reset();
                }
            }
                
        },

        async registrarParticipanteCarrera() {
            const participantecarrera_path = 'http://localhost:8000/api/v1/participantecarreras/'
            await axios.post(participantecarrera_path, this.form).then((response) => {})
                .catch((err) => {
                    console.log(err)
                    swal("Participante no pudo ser creado", "", "error")
                })
        },

        getCarreras(){
            const path = 'http://localhost:8000/api/v1/carreras/'
            axios.get(path).then((response) => {
                this.carreras = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        },
        getSedes(){
            const path = 'http://localhost:8000/api/v1/sedes/'
            axios.get(path).then((response) => {
                this.sedes = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        },
        getColegios(){
            const path = 'http://localhost:8000/api/v1/colegios/'
            axios.get(path).then((response) => {
                this.colegios = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        },
    },
    watch: {
      date () {
        this.fechaNacimiento = this.formatDate(this.date)
      },
    },
    mounted(){
        this.getCarreras();
        this.getSedes();
        this.getColegios();
    }
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>