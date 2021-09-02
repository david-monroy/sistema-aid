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
                    ></v-text-field>
                </div>
            </v-col>
          </v-row>

          <v-row class="pb-0 mb-0 form-row" >
            <v-col md="6" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.telfPrincipal"
                        label="Teléfono primario"
                        required
                    ></v-text-field>
                </div>
            </v-col>
            <v-col md="6" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.telfSecundario"
                        label="Teléfono secundario"
                        required
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
                                v-model="dateFormatted"
                                label="Fecha"
                                hint="MM/DD/AAAA"
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
                            @input="menu1 = false"
                        ></v-date-picker>
                    </v-menu>
                </v-col>
                <v-col md="6" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.edad"
                        label="Edad"
                        required
                        type="number"
                    ></v-text-field>
                </div>
            </v-col>
          </v-row>

          <div style="display: flex; justify-content: center; width: 100%">
            <label for="genero" class="text-center mx-auto">Género:</label>
          </div>
          <v-row class="pb-0 mb-0 form-row mx-auto" style="display: flex; justify-content: center; width: 100%">
              
            <v-col md="" cols="12" class="py-0">
                <div class="form-group" style="display: flex; justify-content: center; width: 100%">
                    <v-radio-group
                    v-model="form.genero"
                    row
                    >
                    <v-radio
                        label="Masculino"
                        value="M"
                    ></v-radio>
                    <v-radio
                        label="Femenino"
                        value="F"
                    ></v-radio>
                    <v-radio
                        label="Otro"
                        value="O"
                    ></v-radio>
                    </v-radio-group>
                </div>
            </v-col>
          </v-row>

            <v-btn @click="guardarCambios(participanteID)"
                :disabled="!valid"
                class="btn secondary btn-block w-50 my-2 mx-auto  d-none d-sm-flex">
                Guardar cambios
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
                telfPrincipal: '',
                telfSecundario: null,
            },
            date: new Date().toISOString().substr(0, 10),
            dateFormatted: this.formatDate(new Date().toISOString().substr(0, 10)),
            menu1: false,
            back:'participantes',
            participanteID: null,
        }
    },
    computed: {
      computedDateFormatted () {
        return this.formatDate(this.date)
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
        guardarCambios(id) {

            let validatedForm = this.$refs.registerForm.validate();
            this.form.fechaNacimiento = this.dateFormatted;

                if (validatedForm){
                    const path = `http://localhost:8000/api/v1/participantes/${id}/`

                    axios.put(path, this.form).then((response) => {
                        this.participanteID = response.data.id
                        this.form.nombre = response.data.nombre
                        this.form.genero = response.data.genero
                        this.form.cedula = response.data.cedula
                        this.form.fechaNacimiento = response.data.fechaNacimiento
                        this.form.edad = response.data.edad
                        this.form.telfPrincipal = response.data.telfPrincipal
                        this.form.telfSecundario = response.data.telfSecundario
                        
                        swal("Participante actualizado satisfactoriamente", "", "success")
                    })
                    .catch((err) => {
                        console.log(err)
                    })
                    this.reset();
                }
            },
            getParticipante(id){
            const path = `http://localhost:8000/api/v1/participantes/${id}/`
            this.participanteID = id;
            axios.get(path).then((response) => {
                this.form.nombre = response.data.nombre
                this.form.genero = response.data.genero
                this.form.cedula = response.data.cedula
                this.form.fechaNacimiento = response.data.fechaNacimiento
                this.form.edad = response.data.edad
                this.form.telfPrincipal = response.data.telfPrincipal
                this.form.telfSecundario = response.data.telfSecundario
                this.date = response.data.fechaNacimiento
            })
            .catch((err) => {
                console.log(err)
            })
        }
    },
    watch: {
      date () {
        this.dateFormatted = this.formatDate(this.date)
      },
    },
    mounted(){
        this.getParticipante(this.$route.params.id);
    }
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>