<template>
  <v-row align="center" class="list px-3 mx-auto nav-separator container">
      <div class="crud-buttons mx-auto">
          <v-btn color="accent2" class="mx-4" @click="goRoute('participantes/agregar')">Agregar participante</v-btn>
          <v-btn color="accent2" class="mx-4" @click="goRoute('participantes/editar/masivo')">Edición masiva</v-btn>
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

          <template v-slot:top>
              <v-dialog v-model="popupEliminar" max-width="700px">
                <v-card>
                  <v-card-title class="body-1 mx-auto text-center">¿Seguro que desea eliminar a {{participanteAEliminarNombre}}?</v-card-title>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn class="secondary--text" text @click="cerrarEliminar">Cancelar</v-btn>
                    <v-btn color="blue darken-1" text @click="eliminarParticipante()">Sí, eliminar</v-btn>
                    <v-spacer></v-spacer>
                  </v-card-actions>
                </v-card>
              </v-dialog>

          <v-dialog v-model="modalEstudios" max-width="950px">
                <v-card class="project-dialog">
                  <v-card-title class="headline grey lighten-2">
                    {{actualParticipanteEstudios.nombre}} ({{actualParticipanteEstudios.genero}})
                  </v-card-title>

                  <v-card-text class="my-2  pb-0" style="display: flex; justify-content: space-between">
                    <div>
                          <strong>Cédula: </strong> <p>{{actualParticipanteEstudios.cedula}}</p>
                      </div>
                      <div>
                          <strong>Correo: </strong> <p>{{actualParticipanteEstudios.correo}}</p>
                      </div>
                      <div v-if="actualParticipanteEstudios.correoUcab">
                          <strong>Correo UCAB: </strong> <p>{{actualParticipanteEstudios.correoUcab}}</p>
                      </div>
                      <div v-else>
                          <strong>Correo UCAB: </strong> <p class='text-center'>-</p>
                      </div>
                      
                      <div>
                          <strong>Fecha de nacimiento: </strong> <p>{{actualParticipanteEstudios.fechaNacimiento}}</p>
                      </div>
                      <div>
                          <strong>Tlf. Principal: </strong> <p>{{actualParticipanteEstudios.telfPrincipal}}</p>
                      </div>
                      <div v-if="actualParticipanteEstudios.telfSecundario">
                          <strong>Tlf. Secundario: </strong> <p>{{actualParticipanteEstudios.telfSecundario}}</p>
                      </div>
                      <div v-else>
                          <strong>Tlf. Secundario: </strong> <p class='text-center'>-</p>
                      </div>
                    
                  </v-card-text>

                  <v-expansion-panels focusable class="px-5 mb-2">
                    <v-expansion-panel>
                        <v-expansion-panel-header>Estudios</v-expansion-panel-header>
                        <v-expansion-panel-content>
                            <v-simple-table max-height="240px">
                                <template v-slot:default>
                                <thead >
                                    <tr>
                                      <th class="text-center">
                                        Sede
                                    </th>
                                    <th class="text-center">
                                        Participante
                                    </th>
                                    <th class="text-center">
                                        Carrera
                                    </th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr
                                    v-for="(par_car,p) in actualParticipanteCarreras"
                                    :key="p"
                                    >
                                    <td class="text-center">{{ par_car.sede }}</td>
                                    <td class="text-center">{{ par_car.carrera }}</td>
                                    <td class="text-center">{{ par_car.semestre }}</td>
                                    </tr>
                                </tbody>
                                </template>
                            </v-simple-table>
                        </v-expansion-panel-content>
                    </v-expansion-panel>
                </v-expansion-panels>

                  <v-card-actions>
                    <v-btn
                      color="primary"
                      text
                      @click="modalEstudios = false"
                    >
                      Cerrar
                    </v-btn>
                  </v-card-actions>
                  </v-card>
              </v-dialog>

          </template>

          <template v-slot:[`item.actions`]="{ item }">
            <v-tooltip
                top 
                style="display: inline"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-icon small v-bind="attrs" v-on="on"
                @click="editarParticipante(item.id)" class="mr-2">fa-pen</v-icon>
              </template>
              <span>Editar</span>
            </v-tooltip>

            <v-tooltip
                top 
                style="display: inline"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-icon small v-bind="attrs" v-on="on"
                @click="abrirEstudios(item.id)" class="mr-2 secondary--text">fa-info-circle</v-icon>
              </template>
              <span>Estudios</span>
            </v-tooltip>

            <v-tooltip
                top 
                style="display: inline"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-icon small v-bind="attrs" v-on="on"
                @click="mostrarEliminar(item.id, item.nombre)" class="red--text">fa-trash</v-icon>
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
            { text: 'Correo electrónico', value: 'correo' },
            { text: 'Tlf. Principal', value: 'telfPrincipal' },
            { text: 'Tlf. Secundario', value: 'telfSecundario' },
            { text: 'Acciones', value: 'actions', sortable: false },
            ],
            participantes: [],

            popupEliminar: false,
            participanteAEliminar: "",
            participanteAEliminarNombre: "",
            modalEstudios: false,
            actualParticipanteEstudios: {
              nombre: 'Provicional',
              cedula: 'Provicional',
              correo: 'Provicional',
              correoUcab: 'Provicional',
              telfPrincipal: 'Provicional',
              telfSecundario: 'Provicional',
              fechaNacimiento: 'Provicional',
              genero: 'Provicional',
            },
            participante_carreras: null,
            actualParticipanteCarreras: []
        }
    },
    computed: {
      
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
        getParticipanteCarreras(){
            const path = 'http://localhost:8000/api/v1/participantecarreras/'
            axios.get(path).then((response) => {
                this.participante_carreras = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        },

        mostrarEliminar(participanteID, participanteNombre){
          this.popupEliminar = true;
          this.participanteAEliminar = participanteID;
          this.participanteAEliminarNombre = participanteNombre;
        },

        cerrarEliminar(){
          this.popupEliminar = false;
        },

        eliminarParticipante(){
            const path = `http://localhost:8000/api/v1/participantes/${this.participanteAEliminar}/`

            axios.delete(path).then((res) => {
                location.href = '/participantes'
            })
            .catch((err) => {
                swal('No es posible eliminar el libro', '', 'error')
            })
        },

        editarParticipante(id){
          this.goRoute(`participantes/${id}/editar`);
        },

        setParticipanteCarreras(id){
          this.participante_carreras.forEach(p => {
              if (p.participante == id){
                  this.actualParticipanteCarreras.push(p);
              }
          });
      },

        abrirEstudios(userID){
          this.modalEstudios = true;
          this.participanteEstudios = userID;
          this.participantes.forEach(par => {
            if (par.id == this.participanteEstudios){
              this.actualParticipanteEstudios = par;
            }
          });
          this.setParticipanteCarreras(userID);
        },
        

        goRoute(route) {
            this.$router.push("/" + route);
        },
    },

    mounted(){
        this.getParticipantes();
        this.getParticipanteCarreras();
    }
}
</script>

<style>
@import "../../styles/main.css";
</style>