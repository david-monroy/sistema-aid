<template>
  <v-row align="center" class="list px-3 mx-auto nav-separator container">

    <!-- BOTONES -->
    <div class="crud-buttons mx-auto">
      <v-btn color="accent2" class="mx-4" @click="goRoute('usuarios/agregar')">Agregar usuario</v-btn>
    </div>

    <!-- TABLA -->
    <v-col cols="12" sm="12" class="mt-4">
      <v-card class="mx-auto p-3" tile>
        <v-card-title> <span class="primary--text">Usuarios</span>
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
          :items="usuarios"
          :hide-default-footer="false"
          :items-per-page="5"
          :search="search"
        >
          <template v-slot:top>
              <v-dialog v-model="popupEliminar" max-width="700px">
                <v-card>
                  <v-card-title class="body-1 mx-auto text-center">¿Seguro que desea eliminar a {{usuarioAEliminarNombre}}?</v-card-title>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn class="secondary--text" text @click="popupEliminar = false">Cancelar</v-btn>
                    <v-btn color="blue darken-1" text @click="eliminarUsuario()">Sí, eliminar</v-btn>
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
                @click="editarUsuario(item.id)" class="mr-2">fa-pen</v-icon>
              </template>
              <span>Editar</span>
            </v-tooltip>

            <v-tooltip
                top 
                style="display: inline"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-icon small v-bind="attrs" v-on="on"
                @click="mostrarEliminar(item.id, item.username)" class="red--text">fa-trash</v-icon>
              </template>
              <span>Eliminar</span>
            </v-tooltip>
          </template>
        </v-data-table>
      </v-card>
    </v-col>
    <div style="display: flex; flex-direction: column" class="mx-auto mt-4">
      <div class="crud-buttons mx-auto mt-2">
        <v-btn @click="goRoute('configuracion')"
            class="btn-block accent1 mx-auto  mb-0 d-none d-sm-flex">
            Regresar
        </v-btn>
      </div>
    </div>
  </v-row>
</template>

<script>
import swal from 'sweetalert';
import Repository from "../../services/repositories/repositoryFactory";
const UsuariosRepository = Repository.get("Usuarios");
export default {
name: "UsuariosView",
  data() {
        return {
            valid: false,
            buscador: false,
            search: '',
            headers: [
            { text: 'Usuario', value: 'username' },
            { text: 'Nombre', value: 'first_name' },
            { text: 'Apellido', value: 'last_name' },
            { text: 'Correo electrónico', value: 'email' },
            { text: 'Acciones', value: 'actions', sortable: false },
            ],
            usuarios: [],
            popupEliminar: false,
            usuarioAEliminar: "",
            usuarioAEliminarNombre: "",
            modalEstudios: false,
        }
    },
    computed: {

    },
    methods: {
        async getUsuarios(){
            this.usuarios = await UsuariosRepository.obtener();
        },
        mostrarEliminar(usuarioID, usuarioNombre){
          this.popupEliminar = true;
          this.usuarioAEliminar = usuarioID;
          this.usuarioAEliminarNombre = usuarioNombre;
        },
        async eliminarUsuario(){
          try{
            await UsuariosRepository.eliminar(this.usuarioAEliminar)
            location.href = '/usuarios'
          }
          catch(err){
            console.log(err)
            swal("El usuario no pudo ser eliminado", "", "error")
          }
        },
        editarUsuario(id){
          this.goRoute(`usuarios/${id}/editar`);
        },

        goRoute(route) {
            this.$router.push("/" + route);
        },
    },

    mounted(){
        this.getUsuarios();
    }
}
</script>

<style>
@import "../../styles/main.css";
</style>