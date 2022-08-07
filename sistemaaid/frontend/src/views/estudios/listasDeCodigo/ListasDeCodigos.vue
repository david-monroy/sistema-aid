<template>
  <v-row align="center" class="list px-3 mx-auto nav-separator container" style="display: flex; align-items: flex-start">
    <v-col cols="6" sm="6" class="mt-4">
      <v-card class="mx-auto p-3" tile>
        <v-card-title> <span class="primary--text">Listas de Código</span>
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
          sort-by='nombre'
          :headers="headersLista"
          :items="listasDeCodigo"
          :hide-default-footer="false"
          :items-per-page="5"
          :search="search"
        >
        <template v-slot:top>
          <v-dialog v-model="modalEliminarLista" max-width="700px">
                <v-card>
                  <v-card-title class="body-1 mx-auto text-center">¿Seguro que desea eliminar la lista {{listaAEliminarNombre}}?</v-card-title>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn class="secondary--text" text @click="modalEliminarLista=false">Cancelar</v-btn>
                    <v-btn color="blue darken-1" text @click="eliminarLista()">Sí, eliminar</v-btn>
                    <v-spacer></v-spacer>
                  </v-card-actions>
                </v-card>
              </v-dialog>

              <v-dialog v-model="modalEditarLista" max-width="700px">
                <v-card>
                  <v-card-title class="body-1 mx-auto text-center">Editar lista de código</v-card-title>
                  <v-form
                    ref="form"
                    v-model="valid"
                    lazy-validation
                  >
                      <v-row class="form-row px-6 mx-0 mt-2" >
                        <v-col md="6" cols="12" class="py-0">
                            <div class="form-group">
                                <v-text-field
                                    v-model="formEditarLista.nombre"
                                    label="Nombre"
                                    required
                                ></v-text-field>
                            </div>
                        </v-col>
                        <v-col md="6" cols="12" class="py-0">
                            <div class="form-group">
                                <v-text-field
                                    v-model="formEditarLista.descripcion"
                                    label="Descripción"
                                    required
                                ></v-text-field>
                            </div>
                        </v-col>
                      </v-row>
                  </v-form>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn class="error--text" text @click="modalEditarLista=false">Cancelar</v-btn>
                    <v-btn color="success" text @click="guardarCambiosLista()">Guardar Cambios</v-btn>
                    <v-spacer></v-spacer>
                  </v-card-actions>
                </v-card>
              </v-dialog>
        </template>
            <template v-slot:[`item.categorias`]="{ item }">
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
                @click="editarLista(item.id, item.nombre, item.descripcion)" class="mr-2">fa-pen</v-icon>
              </template>
              <span>Editar</span>
            </v-tooltip>

            <v-tooltip
                top 
                style="display: inline"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-icon small v-bind="attrs" v-on="on"
                @click="mostrarEliminarLista(item.id, item.nombre)" class="red--text">fa-trash</v-icon>
              </template>
              <span>Eliminar</span>
            </v-tooltip>
          </template>
        </v-data-table>
        <v-row class="d-flex" style="justify-content: center">
          <v-btn color="accent2" class="mx-4 my-6" @click="goRoute('estudios/agregarListaCodigo')">Agregar lista de código</v-btn>
        </v-row>
      </v-card>
    </v-col>
    <v-col cols="6" sm="6" class="mt-4">
      <v-card class="mx-auto p-3 mb-0" tile>
        <div v-if="!listaCodigo.id">
          Selecciona una lista de códigos para ver sus categorías.
        </div>
        <div v-else>
          <v-card-title><span class="secondary--text">{{ listaCodigo.nombre }}</span></v-card-title>
        <v-card-title> <span class="primary--text">Categorías</span>
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
          :headers="headersCategoria"
          :items="categorias"
          :hide-default-footer="false"
          :items-per-page="5"
          :search="search"
          sort-by='codigo'
        >

        <template v-slot:top>
              <v-dialog v-model="modalEliminar" max-width="700px">
                <v-card>
                  <v-card-title class="body-1 mx-auto text-center">¿Seguro que desea eliminar la categoría {{categoriaAEliminarCodigo}}?</v-card-title>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn class="secondary--text" text @click="modalEliminar=false">Cancelar</v-btn>
                    <v-btn color="blue darken-1" text @click="eliminarCategoria()">Sí, eliminar</v-btn>
                    <v-spacer></v-spacer>
                  </v-card-actions>
                </v-card>
              </v-dialog>

              <v-dialog v-model="modalEditar" max-width="700px">
                <v-card>
                  <v-card-title class="body-1 mx-auto text-center">Editar categoría</v-card-title>
                  <v-form
                    ref="form"
                    v-model="valid"
                    lazy-validation
                  >
                      <v-row class="form-row px-6 mx-0 mt-2" >
                        <v-col md="2" cols="12" class="py-0">
                            <div class="form-group">
                                <v-text-field
                                    v-model="formEditar.codigo"
                                    label="Código"
                                    required
                                ></v-text-field>
                            </div>
                        </v-col>
                        <v-col md="10" cols="12" class="py-0">
                            <div class="form-group">
                                <v-text-field
                                    v-model="formEditar.descripcion"
                                    label="Descripción"
                                    required
                                ></v-text-field>
                            </div>
                        </v-col>
                      </v-row>
                  </v-form>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn class="error--text" text @click="modalEditar=false">Cancelar</v-btn>
                    <v-btn color="success" text @click="guardarCambios()">Guardar Cambios</v-btn>
                    <v-spacer></v-spacer>
                  </v-card-actions>
                </v-card>
              </v-dialog>

              <v-dialog v-model="modalAgregar" max-width="700px">
                <v-card>
                  <v-card-title class="body-1 mx-auto text-center"><span>Agregar categoría a <b class="secondary--text"> {{ listaCodigo.nombre}}</b></span></v-card-title>
                  <v-form
                    ref="formAgregar"
                    v-model="validAgregar"
                    lazy-validation
                  >
                      <v-row class="form-row px-6 mx-0 mt-2" >
                        <v-col md="2" cols="12" class="py-0">
                            <div class="form-group">
                                <v-text-field
                                    v-model="formAgregar.codigo"
                                    label="Código"
                                    required
                                ></v-text-field>
                            </div>
                        </v-col>
                        <v-col md="10" cols="12" class="py-0">
                            <div class="form-group">
                                <v-text-field
                                    v-model="formAgregar.descripcion"
                                    label="Descripción"
                                    required
                                ></v-text-field>
                            </div>
                        </v-col>
                      </v-row>
                  </v-form>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn class="error--text" text @click="modalAgregar=false">Cancelar</v-btn>
                    <v-btn color="success" text @click="agregarCategoria()">Agregar</v-btn>
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
                @click="editarCategoria(item.id, item.codigo, item.descripcion, item.listaCodigo_id)" class="mr-2">fa-pen</v-icon>
              </template>
              <span>Editar</span>
            </v-tooltip>

            <v-tooltip
                top 
                style="display: inline"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-icon small v-bind="attrs" v-on="on"
                @click="mostrarEliminar(item.id, item.codigo)" class="red--text">fa-trash</v-icon>
              </template>
              <span>Eliminar</span>
            </v-tooltip>
          </template>
        </v-data-table>
        <v-row class="d-flex" style="justify-content: center">
          <v-btn color="accent2" class="mx-4 my-6" @click="modalAgregar = true">Agregar categoria</v-btn>
        </v-row>
        </div>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import swal from 'sweetalert'
import Repository from "../../../services/repositories/repositoryFactory";
const ListaCodigoRepository = Repository.get("ListaCodigo");
export default {
  data() {
        return {
            search: '',
            headersLista: [
            { text: 'ID', value: 'id' }, 
            { text: 'Nombre', value: 'nombre' },
            { text: 'Descripción', value: 'descripcion' },
            { text: 'Ver categorías', value: 'categorias', sortable: false, align:'center'},
            { text: 'Acciones', value: 'actions', sortable: false, align:'center'},
            ],
             headersCategoria: [
            { text: 'Código', value: 'codigo' },
            { text: 'Descripción', value: 'descripcion' },
            { text: 'Acciones', value: 'actions', sortable: false, align:'center'},
            ],
            listasDeCodigo: [],
            listaCodigo: {
              id: null,
              nombre: null,
            },
            categorias: [],
            actualListaDeCodigo: null,
            modalEliminar: false,
            modalEditar: false,
            modalEliminarLista: false,
            modalEditarLista: false,
            modalAgregar: false,
            listaCodigoSeleccionada: null,
            listaAEliminar: '',
            listaAEliminarNombre: "",
            categoriaAEliminar: "",
            categoriaAEliminarCodigo: "",
            formEditar: {
              id: null,
              codigo: null,
              descripcion: null,
              listaCodigo: null,
            },
            formEditarLista: {
              id: null,
              nombre: null,
              descripcion: null,
            },
            formAgregar: {
              id: null,
              codigo: null,
              descripcion: null,
              listaCodigo: null,
            },
            date: new Date().toISOString().substr(0, 10),
        }
    },
    computed: {

    },
    methods: {
        async getListasDeCodigo(){
            try{
                this.listasDeCodigo = await ListaCodigoRepository.consultar();
            }
            catch(err){
                console.log(err)
                swal("No se pudo obtener las listas de código", "", "error")
            }
        },
        async seleccionar(id){
          this.listasDeCodigo.forEach(ls => {
            if (ls.id == id) {
              this.listaCodigo = ls
            }
          });
          this.listaCodigoSeleccionada = id
          this.categorias = await ListaCodigoRepository.obtenerCategorias(id)
        },
        mostrarEliminar(categoriaID, categoriaCodigo){
          this.modalEliminar = true;
          this.categoriaAEliminar = categoriaID;
          this.categoriaAEliminarCodigo = categoriaCodigo;
        },
        mostrarEliminarLista(id, nombre){
          this.modalEliminarLista = true;
          this.listaAEliminar = id;
          this.listaAEliminarNombre = nombre;
        },

        cerrarEliminar(){
          this.modalEliminar = false;
          this.modalEliminarLista = false;
        },

        async eliminarCategoria(){
          try{
            await ListaCodigoRepository.eliminarCategoria(this.categoriaAEliminar)
            // location.href = '/participantes'
            swal("Categoría eliminada", "", "success")
            this.seleccionar(this.listaCodigoSeleccionada)
            this.modalEliminar = false
          }
          catch(err){
            console.log(err)
            swal("La categoría no pudo ser eliminada", "", "error")
          }
        },

        async eliminarLista(){
          try{
            await ListaCodigoRepository.eliminar(this.listaAEliminar)
            // location.href = '/participantes'
            swal("Lista de códigos eliminada", "", "success")
            this.modalEliminarLista = false
            this.getListasDeCodigo()
            this.categorias = []
          }
          catch(err){
            console.log(err)
            swal("La lista no pudo ser eliminada", "", "error")
          }
        },

        editarCategoria(id, codigo, descripcion, listaCodigo){
          this.formEditar = {
            id: id,
            codigo: codigo,
            descripcion: descripcion,
            listaCodigo: listaCodigo
          }
          this.modalEditar = true
        },

        editarLista(id, nombre, descripcion){
          this.formEditarLista = {
            id: id,
            nombre: nombre,
            descripcion: descripcion,
          }
          this.modalEditarLista = true
        },

        async guardarCambios(){
          try{
            await ListaCodigoRepository.editarCategoria(this.formEditar.id, this.formEditar)
            swal("Categoría editada exitosamente", "", "success")
            this.seleccionar(this.listaCodigoSeleccionada)
            this.modalEditar = false
          }
          catch(err){
            console.log(err)
            swal("La categoría no pudo ser editada", "", "error")
          }
        },
        async guardarCambiosLista(){
          try{
            await ListaCodigoRepository.editar(this.formEditarLista.id, this.formEditarLista)
            swal("Lista editada exitosamente", "", "success")
            this.modalEditarLista = false
          }
          catch(err){
            console.log(err)
            swal("La lista no pudo ser editada", "", "error")
          }
        },

        async agregarCategoria(){
          this.formAgregar.listaCodigo = this.listaCodigo.id
          
          try{
            await ListaCodigoRepository.crearCategoria(this.formAgregar)
            this.seleccionar(this.listaCodigoSeleccionada)
            swal("Categoría creada exitosamente", "", "success")
            this.modalAgregar = false
            this.formAgregar.id = null
            this.formAgregar.codigo = null
            this.formAgregar.descripcion = null
            this.formAgregar.listaCodigo = null
          }
          catch(err){
            console.log(err)
            swal("El código de la categoría ya existe", "", "error")
          }
        },
        goRoute(route) {
            this.$router.push("/" + route);
        },
    },

    mounted(){
        this.getListasDeCodigo();
    }
}
</script>

<style>
@import "../../../styles/main.css";
</style>