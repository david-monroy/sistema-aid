<template>
  <v-row align="center" class="list px-3 mx-auto nav-separator container">
      <div class="crud-buttons mx-auto">
          <v-btn color="accent2" class="mx-4" @click="goRoute('participantes/agregar')">Agregar participante</v-btn>
          <v-btn color="accent2" class="mx-4">Edición masiva</v-btn>
      </div>
    <v-col cols="12" sm="12" class="mt-4">
      <v-card class="mx-auto p-3" tile>
        <v-card-title> <span class="primary--text">Participantes</span>
          <v-spacer></v-spacer>
          <v-text-field
            v-model="search"
            append-icon="fa-search"
            label="Buscar"
            single-line
            hide-details
          ></v-text-field>
        </v-card-title>
        <v-data-table
          :headers="headers"
          :items="participantes"
          :hide-default-footer="false"
          :items-per-page="5"
          :search="search"
        >

          <template v-slot:[`item.actions`]="{ item }">
            <v-tooltip
                top 
                style="display: inline"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-icon small v-bind="attrs" v-on="on"
                class="mr-2">fa-pen</v-icon>
              </template>
              <span>Editar</span>
            </v-tooltip>

            <v-tooltip
                top 
                style="display: inline"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-icon small v-bind="attrs" v-on="on">fa-trash</v-icon>
              </template>
              <span>Eliminar</span>
            </v-tooltip>
          </template>
        </v-data-table>

      </v-card>
    </v-col>

    
    
  </v-row>
</template>

<script>
import axios from 'axios';
export default {
name: "ParticipantesView",

  data() {
        return {
            search: '',
            headers: [
            { text: 'ID', value: 'id' },
            {
                text: 'Nombre',
                align: 'start',
                value: 'nombre',
            },
            { text: 'Cédula', value: 'cedula' },
            { text: 'Género', value: 'genero' },
            { text: 'Fecha de nacimiento', value: 'fechaNacimiento' },
            { text: 'Edad', value: 'edad' },
            { text: 'Tlf. Principal', value: 'telfPrincipal' },
            { text: 'Tlf. Secundario', value: 'telfSecundario' },
            { text: 'Acciones', value: 'actions', sortable: false },
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

        goRoute(route) {
            this.$router.push("/" + route);
        },
    },

    mounted(){
        this.getParticipantes()
    }
}
</script>

<style>
@import "../../styles/main.css";
</style>