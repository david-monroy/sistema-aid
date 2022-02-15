<template>
  <v-row align="center" class="list px-3 mx-auto nav-separator container">
    

    <!-- BOTONES -->
    <div class="crud-buttons mx-auto">
      <v-btn color="accent2" class="mx-4" @click="goRoute('estudios/agregar')">Agregar estudio</v-btn>
      <v-btn color="accent1" class="mx-4" @click="buscador = true">Filtrar</v-btn>
    </div>

    <!-- TABLA -->
    <v-col cols="12" sm="12" class="mt-4">
      <v-card class="mx-auto p-3" tile>
        <v-card-title> <span class="primary--text">Estudios con sus ediciones</span>
          <v-spacer></v-spacer>
        </v-card-title>
        <v-data-table
          :headers="headers"
          :items="ediciones"
          :hide-default-footer="false"
          :items-per-page="5"
          :search="search"
        >
          <template v-slot:top>
              <v-dialog v-model="popupEliminar" max-width="700px">
                <v-card>
                  <v-card-title class="body-1 mx-auto text-center">¿Seguro que desea eliminar el estudio?</v-card-title>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn class="secondary--text" text @click="popupEliminar = false">Cancelar</v-btn>
                    <v-btn color="blue darken-1" text @click="eliminarParticipante()">Sí, eliminar</v-btn>
                    <v-spacer></v-spacer>
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
                @click="editarEdicion(item.id)" class="mr-2">fa-pen</v-icon>
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
              <span>Información</span>
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
    <div class="crud-buttons mx-auto mt-4">
      <v-btn color="secondary" class="mx-4" @click="exportarCSV(csvData)">Exportar a CSV</v-btn>
    </div>
  </v-row>
</template>

<script>
import swal from 'sweetalert';
import Repository from "../../services/repositories/repositoryFactory";
const EdicionRepository = Repository.get("Ediciones");
export default {
  data: () => ({
            valid: false,
            buscador: false,
            search: '',
            headers: [
            {
                text: 'Código del Estudio',
                align: 'start',
                value: 'estudio[1]',
            },
            {text: 'Nombre del estudio',value: 'estudio[0]'},
            { text: 'Edición', value: 'codigo' },
            { text: 'Inicio', value: 'fechaInicio' },
            { text: 'Fin ', value: 'fechaFin' },
            { text: 'Período', value: 'periodo' },
            { text: 'Acciones', value: 'actions', sortable: false },
            ],
            ediciones: [],
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
              actualEstado: "Provicional",
              actualMunicipio: "Provicional",
              lugar: {
                estado: 'Provicional',
                municipio: 'Provicional',
              }
            },
            lista_consultada: [],
            participantes_origen: []
        }),
    methods: {
        async getEdiciones(){
          try{
            this.ediciones = await EdicionRepository.consultar();
          }
          catch(err){
            console.log(err)
            swal("No se pudo obtener las ediciones", "", "error")
          } 
        },

        mostrarEliminar(participanteID, participanteNombre){
          this.popupEliminar = true;
          this.participanteAEliminar = participanteID;
          this.participanteAEliminarNombre = participanteNombre;
        },

        async eliminarParticipante(){
          try{
            await EdicionesRepository.eliminar(this.participanteAEliminar)
            location.href = '/ediciones'
          }
          catch(err){
            console.log(err)
            swal("El participante no pudo ser eliminado", "", "error")
          }
        },

        async filtrar(){
          try{
            this.ediciones = await ParticipantesRepository.filtrar(this.form);
          }
          catch(err){
            console.log(err)
            swal("La consulta no pudo ser realizada", "", "error")
          }
        },

        exportarCSV(arrData){
          let csvContent = "data:text/csv;charset=utf-8,";
          csvContent += [
            Object.keys(arrData[0]).join(";"),
            ...arrData.map(item => Object.values(item).join(";"))
          ]
            .join("\n")
            .replace(/(^\[)|(\]$)/gm, "");

          const data = encodeURI(csvContent);
          const link = document.createElement("a");
          link.setAttribute("href", data);
          link.setAttribute("download", "estudios.csv");
          link.click();
        },

        async limpiar(){
          this.$refs.registerForm.reset();
          this.ediciones = [];
          this.getEdiciones();
        },

        goRoute(route) {
            this.$router.push("/" + route);
        },
    },

    mounted(){
        this.getEdiciones();
    }
}
</script>

<style>
@import "../../styles/main.css";
</style>