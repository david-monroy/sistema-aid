<template>
  <div class="col-md-12 nav-separator pt-1">
    <div class="card card-container mt-0 form-card">
      <h3 class="primary--text mx-auto mb-6 mt-0">Editar participante</h3>
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

              
            <v-col md="6" cols="12" class="py-0">
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
            <v-expansion-panel v-for="(pc, i) in participante_carreras_actual" :key="i">
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
                        :return-object="false"
                        ></v-autocomplete>
                    </v-col>

                    <v-col md="6" cols="12" class="py-0">
                        <v-select
                        v-model="pc.sede"
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
                        v-model="pc.carrera"
                        :items="carreras"
                        label="Carrera"
                        item-text="nombre"
                        item-value="id"
                        :return-object="false"
                        ></v-autocomplete>
                    </v-col>

                    <v-col md="6" cols="12" class="py-0">
                        <v-select
                        v-model="pc.semestre"
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

            <v-btn @click="guardarCambios(participanteID)"
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
                correo: null,
                correoUcab: null,
                telfPrincipal: '',
                telfSecundario: null,
            },
            date: new Date().toISOString().substr(0, 10),
            dateFormatted: this.formatDate(new Date().toISOString().substr(0, 10)),
            menu1: false,
            back:'participantes',
            participanteID: null,
            carreras: [],
            participante_carreras: [],
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
      participante_carreras_actual(){
          let arreglo_pc = []
          this.participante_carreras.forEach(p => {
              if (p.participante == this.participanteID){
                  arreglo_pc.push(p)
              }
          });
          return arreglo_pc;
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

        async guardarCambios(id) {

            let validatedForm = this.$refs.registerForm.validate();
            this.form.fechaNacimiento = this.dateFormatted;
            const participante_path = `http://localhost:8000/api/v1/participantes/${id}/`

                if (validatedForm){

                    if (this.edad_calculada < 11) {
                        swal("El participante debe ser mayor de 11 años", "", "error") 
                    } else {

                        axios.put(participante_path, this.form).then((response) => {
                            this.participanteID = response.data.id

                            if (this.participante_carreras_actual) {
                                this.actualizarParticipanteCarrera()
                            }
                            
                            swal("Participante actualizado satisfactoriamente", "", "success")
                        })
                        .catch((err) => {
                            console.log(err)
                        })
                    }
                }
            },

            actualizarParticipanteCarrera() {
                
                this.participante_carreras_actual.forEach(pc => {
                    let id = pc.id
                    const participantecarrera_path = `http://localhost:8000/api/v1/participantecarreras/${id}/`

                    axios.put(participantecarrera_path, pc).then((response) => {})
                    .catch((err) => {
                        console.log(err)
                    })
                });

                location.reload()
            },

            getParticipante(id){
            const path = `http://localhost:8000/api/v1/participantes/${id}/`
            this.participanteID = id;
            axios.get(path).then((response) => {
                this.form.nombre = response.data.nombre
                this.form.genero = response.data.genero
                this.form.cedula = response.data.cedula
                this.form.correo = response.data.correo
                this.form.correoUcab = response.data.correoUcab
                this.form.fechaNacimiento = response.data.fechaNacimiento
                this.form.telfPrincipal = response.data.telfPrincipal
                this.form.telfSecundario = response.data.telfSecundario
                this.form.colegio = response.data.colegio
                this.date = response.data.fechaNacimiento
            })
            .catch((err) => {
                console.log(err)
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
        getParticipanteCarreras(){
            const path = 'http://localhost:8000/api/v1/participantecarreras/'
            axios.get(path).then((response) => {
                this.participante_carreras = response.data
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
        this.dateFormatted = this.formatDate(this.date)
      },
    },
    mounted(){
        this.getParticipante(this.$route.params.id);
        this.getCarreras();
        this.getSedes();
        this.getColegios();
        this.getParticipanteCarreras();
    }
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>