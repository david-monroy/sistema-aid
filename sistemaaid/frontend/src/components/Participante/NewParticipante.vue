<template>
  <div class="container">
      <div class="row">
          <div class="col text-left">
              <h2>Nuevo participante</h2>
          </div>
      </div>

      <div class="row">
          <div class="col">
              <div class="card">
                  <div class="card-body">
                      <form @submit="onSubmit">
                          <div class="form-group row">
                              <label for="nombre"
                              class="col-sm-2 col-form-label">
                                  Nombre
                              </label>
                              <div class="col-sm-6">
                                  <input
                                  type="text"
                                  placeholder="Nombre"
                                  name="nombre"
                                  class="form-control"
                                  v-model.trim="form.nombre"
                                  >
                              </div>
                          </div>

                          <div class="form-group row">
                              <label for="genero"
                              class="col-sm-2 col-form-label">
                                  Género
                              </label>
                              <div class="col-sm-6">
                                  <input
                                  type="text"
                                  placeholder="Género"
                                  name="genero"
                                  class="form-control"
                                  v-model.trim="form.genero"
                                  >
                              </div>
                          </div>

                          <div class="form-group row">
                              <label for="cedula"
                              class="col-sm-2 col-form-label">
                                  Cédula
                              </label>
                              <div class="col-sm-6">
                                  <input
                                  type="text"
                                  placeholder="Cédula"
                                  name="cedula"
                                  class="form-control"
                                  v-model.trim="form.cedula"
                                  >
                              </div>
                          </div>

                          <div class="form-group row">
                              <label for="fechaNacimiento"
                              class="col-sm-2 col-form-label">
                                  Fecha de nacimiento
                              </label>
                              <div class="col-sm-6">
                                  <input
                                  type="date"
                                  placeholder="Fecha de nacimiento"
                                  name="fechaNacimiento"
                                  class="form-control"
                                  v-model.trim="form.fechaNacimiento"
                                  >
                              </div>
                          </div>

                          <div class="form-group row">
                              <label for="edad"
                              class="col-sm-2 col-form-label">
                                  Edad
                              </label>
                              <div class="col-sm-6">
                                  <input
                                  type="number"
                                  placeholder="Edad"
                                  name="edad"
                                  class="form-control"
                                  v-model.trim="form.edad"
                                  >
                              </div>
                          </div>

                          <div class="form-group row">
                              <label for="telfPrincipal"
                              class="col-sm-2 col-form-label">
                                  Teléfono principal
                              </label>
                              <div class="col-sm-6">
                                  <input
                                  type="text"
                                  placeholder="Teléfono Principal"
                                  name="telfPrincipal"
                                  class="form-control"
                                  v-model.trim="form.telfPrincipal"
                                  >
                              </div>
                          </div>

                          <div class="form-group row">
                              <label for="telfSecundario"
                              class="col-sm-2 col-form-label">
                                  Teléfono secundario
                              </label>
                              <div class="col-sm-6">
                                  <input
                                  type="text"
                                  placeholder="Teléfono secundario"
                                  name="telfSecundario"
                                  class="form-control"
                                  v-model.trim="form.telfSecundario"
                                  >
                              </div>
                          </div>

                          <div class="rows">
                              <div class="col text-left">
                                  <b-button type="submit"
                                  variant="primary">
                                    Crear
                                  </b-button>
                                  <b-button type="submit"
                                  class="btn-large-space"
                                  :to="{ name: 'ListParticipante' }"
                                  >
                                    Cancelar
                                  </b-button>
                              </div>
                          </div>

                      </form>
                  </div>
              </div>
          </div>
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
            }
        }
    },
    methods: {
        onSubmit(evt){
            evt.preventDefault()

            const path = 'http://localhost:8000/api/v1/participantes/'

            axios.post(path, this.form).then((response) => {
                this.form.nombre = response.data.nombre
                this.form.genero = response.data.genero
                this.form.cedula = response.data.cedula
                this.form.fechaNacimiento = response.data.fechaNacimiento
                this.form.edad = response.data.edad
                this.form.telfPrincipal = response.data.telfPrincipal
                this.form.telfSecundario = response.data.telfSecundario
                
                swal("Participante creado satisfactoriamente", "", "success")
            })
            .catch((err) => {
                swal("El participante no ha sido creado", "", "error")
            })
        },
    },
    created(){

    }
}
</script>

<style>

</style>