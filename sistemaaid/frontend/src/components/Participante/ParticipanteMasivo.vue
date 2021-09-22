<template>
  <div class="col-md-12 nav-separator pt-1">
    <div class="card card-container mt-0 form-card">
      <h3 class="primary--text mx-auto mb-6 mt-0">Registrar nuevos participantes</h3>
      <v-spacer></v-spacer>

      <div class="section">
          <div class="container">

              <form
               @submit.prevent="enviarCSV"
               enctype="multipart/form-data">

                <div class="field">
                    <label for="file" class="label">Subir archivo</label>

                    <input type="file"
                    ref="file"
                    @change="seleccionarCSV">
                </div>

              <div class="field">
                  <button class="button is-info">Enviar</button>
              </div>

            </form>

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
            file: ""
        }
    },
    computed: {
      computedDateFormatted () {
        return this.formatDate(this.date)
      }
    },
    methods: {

        seleccionarCSV(){
            this.file = this.$refs.file.files[0]
        },

        async enviarCSV(){
            const formData = new FormData();
            formData.append('file', this.file)

            axios.post('http://localhost:8000/api/v1/participantes/leer', formData,{
              headers: {
                'Content-Type': 'multipart/form-data'
              }
            }).then((response) => {
                    swal("Participantes creados satisfactoriamente", "", "success")
                })
                .catch((err) => {
                    swal("No se ha podido cargar el archivo", "", "error")
                })
            
        },
    },
    created(){

    }
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>