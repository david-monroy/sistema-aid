<template>
  <v-row align="center" class="list px-3 mx-auto nav-separator container">
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
          
          :headers="headersLista"
          :items="listasDeCodigo"
          :hide-default-footer="false"
          :items-per-page="5"
          :search="search"
        >
            <template v-slot:[`item.actions`]="{ item }">
                <v-icon small v-bind="attrs" v-on="on"
                @click="seleccionar(item.id)" class="mr-2">far fa-arrow-alt-circle-right</v-icon>
            </template>
        </v-data-table>

      </v-card>
    </v-col>
    <v-col cols="6" sm="6" class="mt-4">
      <v-card class="mx-auto p-3 mb-0" tile>
        <div v-if="categorias.length<1">
          Selecciona una lista de códigos para ver sus categorías.
        </div>
        <div v-else>
          <v-card-title><span class="secondary--text">{{ actualListaDeCodigo }}</span></v-card-title>
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
                                    v-model="form.codigo"
                                    label="Código"
                                    required
                                ></v-text-field>
                            </div>
                        </v-col>
                        <v-col md="10" cols="12" class="py-0">
                            <div class="form-group">
                                <v-text-field
                                    v-model="form.descripcion"
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
          </template>

          <template v-slot:[`item.actions`]="{ item }">
            <v-tooltip
                top 
                style="display: inline"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-icon small v-bind="attrs" v-on="on"
                @click="editarCategoria(item.id, item.codigo, item.descripcion)" class="mr-2">fa-pen</v-icon>
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
            { text: 'Nombre', value: 'nombre' },
            { text: 'Descripción', value: 'descripcion' },
            { text: 'Seleccionar', value: 'actions', sortable: false, align:'center'},
            ],
             headersCategoria: [
            { text: 'Código', value: 'codigo' },
            { text: 'Descripción', value: 'descripcion' },
            { text: 'Acciones', value: 'actions', sortable: false, align:'center'},
            ],
            listasDeCodigo: [],
            listaCodigo:"",
            categorias: [],
            actualListaDeCodigo: null,
            modalEliminar: false,
            modalEditar: false,
            categoriaAEliminar: "",
            categoriaAEliminarCodigo: "",
            form: {
              id: null,
              codigo: null,
              descripcion: null,
              fechaUltimaModificacion: null,
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
            if (ls.id == id) this.actualListaDeCodigo = ls.nombre
          });
          this.categorias = await ListaCodigoRepository.obtenerCategorias(id)
        },
        mostrarEliminar(categoriaID, categoriaCodigo){
          this.modalEliminar = true;
          this.categoriaAEliminar = categoriaID;
          this.categoriaAEliminarCodigo = categoriaCodigo;
        },

        cerrarEliminar(){
          this.modalEliminar = false;
        },

        async eliminarCategoria(){
          try{
            await ListaCodigoRepository.eliminarCategoria(this.categoriaAEliminar)
            // location.href = '/participantes'
            swal("Categoría eliminada", "", "success")
            location.reload()
          }
          catch(err){
            console.log(err)
            swal("La categoría no pudo ser eliminada", "", "error")
          }
        },

        editarCategoria(id, codigo, descripcion){
          console.log(this.date)
          this.form = {
            id: id,
            codigo: codigo,
            descripcion: descripcion,
            listaCodigo: 1
          }
          this.modalEditar = true
        },

        async guardarCambios(){
          try{
            await ListaCodigoRepository.editarCategoria(this.form.id, this.form)
            swal("Categoría editada exitosamente", "", "success")
            location.reload()
          }
          catch(err){
            console.log(err)
            swal("La categoría no pudo ser editada", "", "error")
          }
        }
    },

    mounted(){
        this.getListasDeCodigo();
    }
}
</script>

<style>
@import "../../../styles/main.css";
</style>