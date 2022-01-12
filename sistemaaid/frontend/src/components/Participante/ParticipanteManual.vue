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
                        v-model="form.correo"
                        label="Correo electrónico"
                        required
                        :rules='[rules.emailRules]'
                    ></v-text-field>
                </div>
            </v-col>
            <v-col md="4" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.correoUcab"
                        label="Correo UCAB"
                    ></v-text-field>
                </div>
            </v-col>
          </v-row>
        <v-row class="pb-0 mb-0 form-row" >
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
            <v-col md="4" cols="12" class="py-0">
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
            <v-col md="4" cols="12" class="py-0">
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
                <div class="form-group">
                    <v-select
                        v-model="form.estado_id"
                        :items="estados"
                        item-text="nombre"
                        item-value="id"
                        label="Estado"
                        ></v-select>
                </div>
            </v-col>
            <v-col md="4" cols="12" class="py-0">
                <div class="form-group">
                    <v-select
                        v-model="form.municipio_id"
                        :items="municipios()"
                        item-text="nombre"
                        item-value="id"
                        label="Municipio"
                        ></v-select>
                </div>
            </v-col>  
            <v-col md="4" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.lugar"
                        label="Dirección"
                    ></v-text-field>
                </div>
            </v-col>
          </v-row>

          <v-expansion-panels class="my-6">
            <v-expansion-panel>
            <v-expansion-panel-header>
                Información académica (opcional)
            </v-expansion-panel-header>
            <v-expansion-panel-content>
                <v-row class="pb-0 mb-0 form-row" >
                    <v-col cols="12" class="py-0">
                        <v-autocomplete
                        v-model="form.colegio_id"
                        :items="colegios"
                        label="Colegio"
                        item-text="nombre"
                        item-value="id"
                        ></v-autocomplete>
                    </v-col>
                </v-row>
                <v-row class="pb-0 mb-0 form-row">

                    <v-col md="4" cols="12" class="py-0">
                        <v-select
                        v-model="form.sede_id"
                        :items="sedes"
                        item-text="nombre"
                        item-value="id"
                        label="Sede UCAB"
                        ></v-select>
                    </v-col>

                    <v-col md="4" cols="12" class="py-0">
                        <v-autocomplete
                        v-model="form.carrera_id"
                        :items="carreras"
                        label="Carrera"
                        item-text="nombre"
                        item-value="id"
                        ></v-autocomplete>
                    </v-col>

                    <v-col md="4" cols="12" class="py-0">
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

            <v-expansion-panel>
            <v-expansion-panel-header>
                Redes sociales (opcional)
            </v-expansion-panel-header>
            <v-expansion-panel-content>
                <v-row class="pb-0 mb-0 form-row d-flex" style="justify-content: space-around">
                    <v-col md="2" cols="12" class="py-0">
                        <v-text-field
                        v-model="form.instagram"
                        label="Instagram"
                        ></v-text-field>
                    </v-col>
                    <v-col md="2" cols="12" class="py-0">
                        <v-text-field
                        v-model="form.twitter"
                        label="Twitter"
                        ></v-text-field>
                    </v-col>
                    <v-col md="2" cols="12" class="py-0">
                        <v-text-field
                        v-model="form.facebook"
                        label="Facebook"
                        ></v-text-field>
                    </v-col>
                    <v-col md="2" cols="12" class="py-0">
                        <v-text-field
                        v-model="form.linkedin"
                        label="Linkedin"
                        ></v-text-field>
                    </v-col>
                    <v-col md="2" cols="12" class="py-0">
                        <v-text-field
                        v-model="form.tiktok"
                        label="Tik Tok"
                        ></v-text-field>
                    </v-col>
                </v-row>
            </v-expansion-panel-content>
            </v-expansion-panel>
        </v-expansion-panels>

            <v-btn @click="registrarParticipante"
                :disabled="!valid"
                class="btn success btn-block w-50 my-2 mx-auto  d-none d-sm-flex">
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
import swal from 'sweetalert';
import Repository from "../../services/repositories/repositoryFactory";
const ParticipantesRepository = Repository.get("Participantes");
const ParticipanteCarrerasRepository = Repository.get("ParticipanteCarreras");
const SedesRepository = Repository.get("Sedes");
const CarrerasRepository = Repository.get("Carreras");
const ColegiosRepository = Repository.get("Colegios");
const LugaresRepository = Repository.get("Lugares");
export default {
    data(){
        return {
            valid: false,
            estados: [],
            municipios_todos: [],
            form: {
                nombre: '',
                genero: '',
                cedula: '',
                fechaNacimiento: null,
                correo: '',
                correoUcab: null,
                telfPrincipal: '',
                telfSecundario: null,
                carrera_id: null,
                sede_id: null,
                colegio_id: null,
                participante_id: null,
                estado_id: null,
                municipio_id: null,
                lugar: '',
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
                
            },
            informacion_academica: []
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
        async registrarParticipante() {
            let validatedForm = this.$refs.registerForm.validate();
            this.form.fechaNacimiento = this.fechaNacimiento;

            if (validatedForm){
                if (this.edad_calculada < 11) {
                    swal("El participante debe ser mayor de 11 años", "", "error") 
                } else {
                    try{
                        let res = await ParticipantesRepository.agregar(this.form);
                        this.form.participante_id = res.id;
                        if (this.form.carrera_id && this.form.sede_id) {
                            this.registrarParticipanteCarrera()
                        }
                        swal("Participante creado satisfactoriamente", "", "success")
                    }
                    catch(err){
                        console.log(err)
                        swal("El participante no pudo ser creado", "", "error")
                    }
                }
            }
        },

        async registrarParticipanteCarrera() {
            try{
                await ParticipanteCarrerasRepository.agregar(this.form);
            }
            catch(err){
                console.log(err)
                swal("El participante no pudo ser creado", "", "error")
            }
        },

        municipios() {
            let id = this.form.estado_id;
            let array = [];
            this.municipios_todos.forEach(mun => {
                if (mun.fk_lugar_id == id) {
                    array.push(mun)
                }
            });
            return array
        },

        async getCarreras(){
            this.carreras = await CarrerasRepository.obtener();
        },
        async getSedes(){
            this.sedes = await SedesRepository.obtener();
        },
        async getColegios(){
            this.colegios = await ColegiosRepository.obtener();
        },
        async getEstados(){
            this.estados = await LugaresRepository.obtenerEstados();
            this.municipios_todos = await LugaresRepository.obtenerMunicipios();
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
        this.getEstados();
    }
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>