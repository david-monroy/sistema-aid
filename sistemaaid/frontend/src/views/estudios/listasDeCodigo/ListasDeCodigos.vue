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
        </v-data-table>

      </v-card>
    </v-col>
    <v-col cols="6" sm="6" class="mt-4">
      <v-card class="mx-auto p-3" tile>
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
        </v-data-table>

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
            ],
             headersCategoria: [
            { text: 'Código', value: 'codigo' },
            { text: 'Descripción', value: 'descripcion' },
            ],
            listasDeCodigo: [],
            listaCodigo:""
        }
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

        async getCategorias(){
            try{
                this.categorias = await ListaCodigoRepository.obtenerCategorias(1);
            }
            catch(err){
                console.log(err)
                swal("No se pudo obtener las listas de código", "", "error")
            }
        },

   
    },

    mounted(){
        this.getListasDeCodigo();
        this.getCategorias();
    }
}
</script>

<style>
@import "../../../styles/main.css";
</style>