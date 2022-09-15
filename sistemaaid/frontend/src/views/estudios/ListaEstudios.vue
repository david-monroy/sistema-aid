<template>
  <v-row
    align="center"
    class="list px-3 mx-auto nav-separator container"
    style="display: flex; align-items: flex-start"
  >
    <v-col cols="6" sm="6" class="mt-4">
      <v-card class="mx-auto p-3" tile>
        <v-card-title>
          <span class="primary--text">Estudios</span>
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
          sort-by="codigo"
          :headers="headersEstudios"
          :items="estudios"
          :hide-default-footer="false"
          :items-per-page="10"
          :search="search"
        >
          <template v-slot:top>
            <v-dialog v-model="modalEstudio" max-width="650px">
              <v-card class="project-dialog">
                <v-card-title class="headline grey lighten-2">
                  {{ actualEstudio.nombre }}
                </v-card-title>

                <v-card-text class="my-2 pb-0">
                  <v-row>
                    <v-col class="md-6">
                      <div>
                        <strong>Código: </strong>
                        <p>{{ actualEstudio.codigo }}</p>
                      </div>
                    </v-col>
                    <v-col class="md-6">
                      <div>
                        <strong>Nombre: </strong>
                        <p>{{ actualEstudio.nombre }}</p>
                      </div>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col class="md-6">
                      <div>
                        <strong>Población objetivo: </strong>
                        <p>{{ actualEstudio.poblacionObjetivo }}</p>
                      </div>
                    </v-col>
                    <v-col class="md-6">
                      <div v-if="actualEstudio.correoUcab">
                        <strong>Antecedentes: </strong>
                        <p>{{ actualEstudio.antecedentes }}</p>
                      </div>
                      <div v-else>
                        <strong>Antecedentes: </strong>
                        <p class="text-center">-</p>
                      </div>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col class="md-6">
                      <div>
                        <strong>Objetivo de negocio: </strong>
                        <p>{{ actualEstudio.objetivoNegocio }}</p>
                      </div>
                    </v-col>
                  </v-row>
                </v-card-text>

                <v-card-actions>
                  <v-btn color="primary" text @click="modalEstudio = false">
                    Cerrar
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </template>
          <template v-slot:[`item.ediciones`]="{ item }">
            <v-icon
              small
              v-bind="attrs"
              v-on="on"
              @click="seleccionar(item.id)"
              class="mr-2"
              >far fa-arrow-alt-circle-right</v-icon
            >
          </template>
          <template v-slot:[`item.actions`]="{ item }">
            <v-tooltip top style="display: inline">
              <template v-slot:activator="{ on, attrs }">
                <v-icon
                  small
                  v-bind="attrs"
                  v-on="on"
                  @click="editarEstudio(item.id)"
                  class="mr-2"
                  >fa-pen</v-icon
                >
              </template>
              <span>Editar</span>
            </v-tooltip>

            <v-tooltip top style="display: inline">
              <template v-slot:activator="{ on, attrs }">
                <v-icon
                  small
                  v-bind="attrs"
                  v-on="on"
                  @click="mostrarInformacion(item.id)"
                  class="mr-2 secondary--text"
                  >fa-info-circle</v-icon
                >
              </template>
              <span>Información</span>
            </v-tooltip>
          </template>
        </v-data-table>
        <v-row class="d-flex" style="justify-content: center">
          <v-btn
            color="accent2"
            class="mx-4 my-6"
            @click="goRoute('estudios/agregarEstudio')"
            >Agregar estudio</v-btn
          >
        </v-row>
      </v-card>
    </v-col>
    <v-col cols="6" sm="6" class="mt-4">
      <v-card class="mx-auto p-3 mb-0" tile>
        <div v-if="!estudio.id">
          Selecciona un estudio para ver sus ediciones.
        </div>
        <div v-else>
          <v-card-title
            ><span class="secondary--text">{{
              estudio.nombre
            }}</span></v-card-title
          >
          <v-card-title>
            <span class="primary--text">Ediciones</span>
            <v-spacer></v-spacer>
            <v-text-field
              v-model="search2"
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
            :search="search2"
            sort-by="codigo"
          >
            <template v-slot:top>
              <v-dialog v-model="modalEdicion" max-width="650px">
                <v-card class="project-dialog">
                  <v-card-title class="headline grey lighten-2">
                    {{ actualEdicion.nombre }}
                  </v-card-title>

                  <v-card-text class="my-2 pb-0">
                    <v-row>
                      <v-col class="md-6">
                        <div>
                          <strong>Código: </strong>
                          <p>{{ actualEdicion.codigo }}</p>
                        </div>
                      </v-col>
                      <v-col class="md-6">
                        <div>
                          <strong>Estudio: </strong>
                          <p>{{ estudio.nombre }}</p>
                        </div>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col class="md-6">
                        <div>
                          <strong>Fecha de inicio: </strong>
                          <p>{{ actualEdicion.fechaInicio }}</p>
                        </div>
                      </v-col>
                      <v-col class="md-6">
                        <div>
                          <strong>Fecha de fin: </strong>
                          <p>{{ actualEdicion.fechaInicio }}</p>
                        </div>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col class="md-6">
                        <div>
                          <strong>Período: </strong>
                          <p>{{ actualEdicion.periodo }}</p>
                        </div>
                      </v-col>
                      <v-col class="md-6">
                        <div>
                          <strong>Muestra total: </strong>
                          <p>{{ actualEdicion.totalMuestra }}</p>
                        </div>
                      </v-col>
                    </v-row>
                  </v-card-text>

                  <v-card-actions>
                    <v-btn color="primary" text @click="modalEdicion = false">
                      Cerrar
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </template>
            <template v-slot:[`item.actions`]="{ item }">
              <v-tooltip top style="display: inline">
                <template v-slot:activator="{ on, attrs }">
                  <v-icon
                    small
                    v-bind="attrs"
                    v-on="on"
                    @click="editarEdicion(item)"
                    class="mr-2"
                    >fa-pen</v-icon
                  >
                </template>
                <span>Editar</span>
              </v-tooltip>
              <v-tooltip top style="display: inline">
                <template v-slot:activator="{ on, attrs }">
                  <v-icon
                    small
                    v-bind="attrs"
                    v-on="on"
                    @click="mostrarInformacionEdicion(item.id)"
                    class="mr-2 secondary--text"
                    >fa-info-circle</v-icon
                  >
                </template>
                <span>Información</span>
              </v-tooltip>
              <v-tooltip top style="display: inline">
                <template v-slot:activator="{ on, attrs }">
                  <v-icon
                    small
                    v-bind="attrs"
                    v-on="on"
                    @click="CargarEncuestas(item.id)"
                    class="mr-2 secondary--text"
                    >fa-upload</v-icon
                  >
                </template>
                <span>Cargar encuestas</span>
              </v-tooltip>
            </template>
          </v-data-table>
          <v-row class="d-flex" style="justify-content: center">
            <v-btn
              color="accent2"
              class="mx-4 my-6"
              @click="goRoute('estudios/agregarEdicion')"
              >Agregar edición</v-btn
            >
          </v-row>
        </div>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import swal from "sweetalert";
import Repository from "../../services/repositories/repositoryFactory";
const EstudiosRepository = Repository.get("Estudios");
const EdicionesRepository = Repository.get("Ediciones");
export default {
  data() {
    return {
      search: "",
      search2: "",
      headersEstudios: [
        { text: "Código", value: "codigo" },
        { text: "Nombre", value: "nombre" },
        {
          text: "Ediciones",
          value: "ediciones",
          sortable: false,
          align: "center",
        },
        {
          text: "Acciones",
          value: "actions",
          sortable: false,
          align: "center",
        },
      ],
      headerEdiciones: [
        { text: "Código", value: "codigo" },
        { text: "Fecha Inicio", value: "fechaInicio" },
        { text: "Fecha Fin", value: "fechaFin" },
        { text: "Período", value: "periodo" },
        {
          text: "Acciones",
          value: "actions",
          sortable: false,
          align: "center",
        },
      ],
      estudios: [],
      ediciones: [],
      estudio: {
        id: null,
        nombre: null,
      },
      modalEliminarEstudio: false,
      modalEditarEstudio: false,
      modalEstudio: false,
      modalEdicion: false,
      actualEstudio: {
        nombre: null,
        codigo: null,
        poblacionObjetivo: null,
        antecedentes: null,
        objetivoNegocio: null,
      },
      actualEdicion: {
        codigo: null,
        fechaInicio: null,
        fechaFin: null,
        periodo: null,
        totalMuestra: null,
      },
      estudioSeleccionado: null,
      estudioAEliminar: "",
      estudioAEliminarNombre: "",
      date: new Date().toISOString().substr(0, 10),
    };
  },
  methods: {
    async getEstudios() {
      try {
        this.estudios = await EstudiosRepository.consultar();
      } catch (err) {
        console.log(err);
        swal("No se pudo obtener los estudios", "", "error");
      }
    },
    async seleccionar(id) {
      this.estudios.forEach((est) => {
        if (est.id == id) {
          this.estudio = est;
        }
      });
      this.estudioSeleccionado = id;
      this.ediciones = await EstudiosRepository.obtenerEdiciones(id);
    },
    mostrarEliminarEstudio(id, nombre) {
      this.modalEliminarEstudio = true;
      this.estudioAEliminar = id;
      this.estudioAEliminarNombre = nombre;
    },
    cerrarEliminar() {
      this.modalEliminarEstudio = false;
    },
    CargarEncuestas(id) {
      this.$router.push(`/ediciones/AgregarEncuestas/${id}`);
    },
    async editarEstudio(id) {
      let ediciones = await EstudiosRepository.obtenerEdiciones(id);
      let tieneEncuestas = false;
      for (let index = 0; index < ediciones.length; index++) {
        const edicion = ediciones[index];
        let encuestas = await EdicionesRepository.obtenerEncuestas(edicion.id);
        if (encuestas.length > 0) tieneEncuestas = true;
      }
      if (tieneEncuestas)
        swal(
          "No se puede editar un estudio cuyas ediciones ya tienen encuestas",
          "",
          "error"
        );
      else this.goRoute(`estudios/${id}/editar`);
    },
    async editarEdicion(edicion) {
      let encuestas = await EdicionesRepository.obtenerEncuestas(edicion.id);
      if (encuestas.length > 0) {
        swal(
          "No se puede editar un estudio cuyas ediciones ya tienen encuestas",
          "",
          "error"
        );
      } else this.goRoute(`estudios/editarEdicion/${edicion.id}`);
    },
    mostrarInformacion(id) {
      this.modalEstudio = true;
      let estudio = id;
      this.estudios.forEach((est) => {
        if (est.id == estudio) {
          this.actualEstudio = est;
        }
      });
    },
    mostrarInformacionEdicion(id) {
      this.$router.push(`/ediciones/${id}`);
    },
    async eliminarEstudio() {
      try {
        await EstudiosRepository.eliminar(this.estudioAEliminar);
        // location.href = '/participantes'
        swal("Estudio eliminado", "", "success");
        this.modalEliminarEstudio = false;
        this.getEstudios();
        this.ediciones = [];
      } catch (err) {
        console.log(err);
        swal("el estudio no pudo ser eliminado", "", "error");
      }
    },
    goRoute(route) {
      this.$router.push("/" + route);
    },
  },
  mounted() {
    this.getEstudios();
  },
};
</script>

<style>
@import "../../styles/main.css";
</style>