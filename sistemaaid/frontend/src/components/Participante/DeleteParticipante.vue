<template>
  <div class="container">
      <div class="row">
          <div class="col">
              <h3>¿Estás seguro que deseas este participante?</h3>
              <p>Nombre: {{ this.element.name }} </p>
              <p>Apellido: {{ this.element.lastname }} </p>
          </div>
      </div>
      
      <div class="row">
      <div class="col">
          <b-button v-on:click="deleteParticipante"
          variant="danger">
            Eliminar
          </b-button>
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
            id: this.$route.params.id,
            element: {
                name: '',
                lastname: ''
            }
        }
    },
    methods: {
        getParticipante(){
            const path = `http://localhost:8000/api/v1/participantes/${this.id}/`

            axios.get(path).then((response) => {
                this.element.name = response.data.name
                this.element.lastname = response.data.lastname
            })
            .catch((err) => {
                console.log(err)
            })
        },
        deleteParticipante(){
            const path = `http://localhost:8000/api/v1/participantes/${this.id}/`

            axios.delete(path).then((res) => {
                location.href = '/participantes'
            })
            .catch((err) => {
                swal('No es posible eliminar el libro', '', 'error')
            })
        }
    },
    created(){
        this.getParticipante()
    }
}
</script>

<style>

</style>