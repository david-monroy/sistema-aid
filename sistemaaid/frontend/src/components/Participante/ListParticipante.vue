<template>
  <div class="container">
      <div class="row">
          <div class="col text-left">
              <div>
                  <h2>Listado de participantes</h2>
                  <b-button
                  size="sm"
                  :to="{ name: 'NewParticipante' }"
                  variant="primary">
                    
                    Nuevo participante
                  </b-button>
              </div>
              
              <br>

              <div class="col-md-12">
                  <b-table striped hover
                   :items="participantes"
                   :fields="fields">

                    <template
                    v-slot:cell(action)="row">
                        <b-button size="sm"
                        variant="primary"
                        :to="{ name: 'EditParticipante', params: { id: row.item.id } }"
                        >
                            Editar
                        </b-button>

                        <b-button size="sm"
                        variant="danger"
                        :to="{ name: 'DeleteParticipante', params: { id: row.item.id } }"
                        >
                            Eliminar
                        </b-button>
                    </template>

                  </b-table>
              </div>
          </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            fields: [
                { key: 'nombre', label: 'Nombre' },
                { key: 'cedula', label: 'Cédula' },
                { key: 'action', label: '' },
            ],
            participantes: []
        }
    },
    methods: {

        getParticipantes(){
            const path = 'http://localhost:8000/api/v1/participantes/'
            axios.get(path).then((response) => {
                this.participantes = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        },
    },

    created(){
        this.getParticipantes()
    }


}
</script>

<style>

</style>