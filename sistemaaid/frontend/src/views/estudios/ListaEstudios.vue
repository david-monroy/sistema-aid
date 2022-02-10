<template>
  <v-row align="center" class="list px-3 mx-auto nav-separator container" style="display: flex; align-items: flex-start">
    <v-col cols="6" sm="6" class="mt-4">
      <v-card class="mx-auto p-3" tile>
        <v-card-title> <span class="primary--text">Estudios</span>
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
          sort-by='codigo'
          :headers="headersEstudios"
          :items="estudios"
          :hide-default-footer="false"
          :items-per-page="10"
          :search="search"
        >
            <template v-slot:[`item.ediciones`]="{ item }">
                <v-icon small v-bind="attrs" v-on="on"
                @click="seleccionar(item.id)" class="mr-2">far fa-arrow-alt-circle-right</v-icon>
            </template>
            <template v-slot:[`item.actions`]="{ item }">
            <v-tooltip
                top 
                style="display: inline"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-icon small v-bind="attrs" v-on="on"
                @click="editarEstudio(item)" class="mr-2">fa-pen</v-icon>
              </template>
              <span>Editar</span>
            </v-tooltip>
            </template>
        </v-data-table>
        <v-row class="d-flex" style="justify-content: center">
          <v-btn color="accent2" class="mx-4 my-6" @click="goRoute('estudios/agregarEstudio')">Agregar estudio</v-btn>
        </v-row>
      </v-card>
    </v-col>
    <v-col cols="6" sm="6" class="mt-4">
      <v-card class="mx-auto p-3 mb-0" tile>
        <div v-if="!estudio.id">
          Selecciona un estudio para ver sus ediciones.
        </div>
        <div v-else>
          <v-card-title><span class="secondary--text">{{ estudio.nombre }}</span></v-card-title>
        <v-card-title> <span class="primary--text">Ediciones</span>
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
          :headers="headerEdiciones"
          :items="ediciones"
          :hide-default-footer="false"
          :items-per-page="10"
          :search="search"
          sort-by='codigo'
        >
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
          </template>
        </v-data-table>
        <v-row class="d-flex" style="justify-content: center">
          <v-btn color="accent2" class="mx-4 my-6" @click="goRoute('estudios/agregarEdicion')">Agregar edición</v-btn>
        </v-row>
        </div>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import swal from 'sweetalert'
import Repository from "../../services/repositories/repositoryFactory";
const EstudiosRepository = Repository.get("Estudios");
const EdicionesRepository = Repository.get("Ediciones");
export default {
    data() {
        return {
            search: '',
            headersEstudios: [
            { text: 'Código', value: 'codigo' },
            { text: 'Nombre', value: 'nombre' },
            { text: 'Ediciones', value: 'ediciones', sortable: false, align:'center'},
            { text: 'Acciones', value: 'acciones', sortable: false, align:'center'},
            ],
            headerEdiciones: [
            { text: 'Código', value: 'codigo' },
            { text: 'Fecha Inicio', value: 'fechaInicio' },
            { text: 'Fecha Fin', value: 'fechaFin' },
            { text: 'Período', value: 'periodo' },
            { text: 'Acciones', value: 'actions', sortable: false, align:'center'},
            ],
            estudios: [],
            estudio: {
              id: null,
              nombre: null,
            },
            modalEliminarEstudio: false,
            modalEditarEstudio: false,
            actualEstudio: null,
            estudioSeleccionado: null,
            estudioAEliminar: '',
            estudioAEliminarNombre: "",
            date: new Date().toISOString().substr(0, 10),
        }
    },
    methods: {
        async getEstudios(){
            try{
                this.estudios = await EstudiosRepository.consultar();
            }
            catch(err){
                console.log(err)
                swal("No se pudo obtener los estudios", "", "error")
            }
        },
        async seleccionar(id){
          this.estudios.forEach(est => {
            if (est.id == id) {
              this.estudio = est
            }
          });
          this.estudioSeleccionado = id
          this.ediciones = await EstudiosRepository.obtenerEdiciones(id)
          console.log(id)
        },
        mostrarEliminarEstudio(id, nombre){
          this.modalEliminarEstudio = true;
          this.estudioAEliminar = id;
          this.estudioAEliminarNombre = nombre;
        },
        cerrarEliminar(){
        //   this.modalEliminar = false;
          this.modalEliminarEstudio = false;
        },
        editarEstudio(item){
            console.log(item);
        },
        editarEdicion(item){
            console.log(item);
        },
        async eliminarEstudio(){
          try{
            await EstudiosRepository.eliminar(this.estudioAEliminar)
            // location.href = '/participantes'
            swal("Estudio eliminado", "", "success")
            this.modalEliminarEstudio = false
            this.getEstudios()
            this.ediciones = []
          }
          catch(err){
            console.log(err)
            swal("el estudio no pudo ser eliminado", "", "error")
          }
        },
        goRoute(route) {
            this.$router.push("/" + route);
        },
    },
    mounted(){
        this.getEstudios();
    }
}
</script>

<style>
@import "../../styles/main.css";
</style>