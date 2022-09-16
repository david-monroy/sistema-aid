<template>
  <v-row align="center" class="list px-3 mx-auto nav-separator container">
    <v-navigation-drawer
      class="pt-12"
      v-model="buscador"
      absolute
      width="400px"
      temporary
      right
    >
      <v-form ref="registerForm" v-model="valid" lazy-validation class="mt-12">
        <div class="form-group">
          <v-text-field
            class="px-8 my-0 py-0"
            v-model="form.nombre"
            label="Nombre y apellido"
          ></v-text-field>
        </div>
        <div class="form-group">
          <v-select
            v-model="form.genero"
            :items="generos"
            item-text="nombre"
            item-value="id"
            label="Género"
            class="px-8 my-0 py-0"
          ></v-select>
        </div>
        <div class="form-group">
          <v-select
            v-model="form.estado"
            :items="estados"
            item-text="nombre"
            item-value="id"
            label="Estado"
            class="px-8 my-0 py-0"
          ></v-select>
        </div>
        <div class="form-group">
          <v-select
            v-model="form.municipio"
            :items="municipios()"
            item-text="nombre"
            item-value="id"
            label="Municipio"
            class="px-8 my-0 py-0"
          ></v-select>
        </div>
        <div class="form-group">
          <v-select
            v-model="form.sede"
            :items="sedes"
            item-text="nombre"
            item-value="id"
            label="Sede"
            class="px-8 my-0 py-0"
          ></v-select>
        </div>
        <div class="form-group">
          <v-autocomplete
            v-model="form.colegio"
            :items="colegios"
            label="Colegio"
            item-text="nombre"
            item-value="id"
            class="px-8 my-0 py-0"
          ></v-autocomplete>
        </div>
        <div class="form-group">
          <v-autocomplete
            v-model="form.carrera"
            :items="carreras"
            label="Carrera"
            item-text="nombre"
            item-value="id"
            class="px-8 my-0 py-0"
          ></v-autocomplete>
        </div>
        <div class="form-group">
          <v-select
            v-model="form.semestre"
            :items="semestres"
            item-text="nombre"
            item-value="id"
            label="Semestre"
            class="px-8 my-0 py-0"
          ></v-select>
        </div>
        <v-btn
          @click="filtrar()"
          :disabled="!valid"
          class="btn secondary btn-block w-50 my-2 mx-auto d-none d-sm-flex"
        >
          Buscar
        </v-btn>
        <v-btn
          @click="limpiar()"
          :disabled="!valid"
          class="btn accent1 btn-block w-50 my-2 mx-auto d-none d-sm-flex"
        >
          Limpiar
        </v-btn>
      </v-form>
    </v-navigation-drawer>

    <!-- BOTONES -->
    <div class="crud-buttons mx-auto">
      <v-btn
        color="accent2"
        class="mx-4"
        @click="goRoute('participantes/agregar')"
        >Agregar participante</v-btn
      >
      <v-btn
        color="accent2"
        class="mx-4"
        @click="goRoute('participantes/masivo')"
        >Cargar excel</v-btn
      >
      <v-btn color="accent1" class="mx-4" @click="buscador = true"
        >Filtrar</v-btn
      >
    </div>

    <!-- TABLA -->
    <v-col cols="12" sm="12" class="mt-4">
      <v-card class="mx-auto p-3" tile>
        <v-card-title>
          <span class="primary--text">Participantes</span>
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
                <v-card-title class="body-1 mx-auto text-center"
                  >¿Seguro que desea eliminar a
                  {{ participanteAEliminarNombre }}?</v-card-title
                >
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    class="secondary--text"
                    text
                    @click="popupEliminar = false"
                    >Cancelar</v-btn
                  >
                  <v-btn
                    color="blue darken-1"
                    text
                    @click="eliminarParticipante()"
                    >Sí, eliminar</v-btn
                  >
                  <v-spacer></v-spacer>
                </v-card-actions>
              </v-card>
            </v-dialog>

            <v-dialog v-model="modalEstudios" max-width="950px">
              <v-card class="project-dialog">
                <v-card-title class="headline grey lighten-2">
                  {{ actualParticipanteEstudios.nombre }} ({{
                    actualParticipanteEstudios.genero
                  }})
                </v-card-title>

                <v-card-text class="my-2 pb-0">
                  <v-row>
                    <v-col class="md-4">
                      <div>
                        <strong>Cédula: </strong>
                        <p>{{ actualParticipanteEstudios.cedula }}</p>
                      </div>
                    </v-col>
                    <v-col class="md-4">
                      <div>
                        <strong>Correo: </strong>
                        <p>{{ actualParticipanteEstudios.correo }}</p>
                      </div>
                    </v-col>
                    <v-col class="md-4">
                      <div v-if="actualParticipanteEstudios.correoUcab">
                        <strong>Correo UCAB: </strong>
                        <p>{{ actualParticipanteEstudios.correoUcab }}</p>
                      </div>
                      <div v-else>
                        <strong>Correo UCAB: </strong>
                        <p class="text-center">-</p>
                      </div>
                    </v-col>
                  </v-row>

                  <v-row>
                    <v-col class="md-4">
                      <div>
                        <strong>Fecha de nacimiento: </strong>
                        <p>{{ actualParticipanteEstudios.fechaNacimiento }}</p>
                      </div>
                    </v-col>
                    <v-col class="md-4">
                      <div>
                        <strong>Tlf. Principal: </strong>
                        <p>{{ actualParticipanteEstudios.telfPrincipal }}</p>
                      </div>
                    </v-col>
                    <v-col class="md-4">
                      <div v-if="actualParticipanteEstudios.telfSecundario">
                        <strong>Tlf. Secundario: </strong>
                        <p>{{ actualParticipanteEstudios.telfSecundario }}</p>
                      </div>
                      <div v-else>
                        <strong>Tlf. Secundario: </strong>
                        <p class="text-center">-</p>
                      </div>
                    </v-col>
                  </v-row>
                </v-card-text>

                <v-expansion-panels focusable class="px-5 mb-2">
                  <v-expansion-panel v-if="encuestas">
                    <v-expansion-panel-header
                      >Estudios que ha participado</v-expansion-panel-header
                    >
                    <v-expansion-panel-content>
                      <v-row class="pb-0 mb-0 form-row mt-2">
                        <v-col md="4" cols="12" class="py-0">
                          <v-menu
                            ref="menu1"
                            v-model="menu1"
                            :close-on-content-click="false"
                            transition="scale-transition"
                            offset-y
                            max-width="290px"
                            min-width="auto"
                          >
                            <template v-slot:activator="{ on, attrs }">
                              <v-text-field
                                v-model="fechaInicio"
                                label="Fecha inicio *"
                                hint="AAAA-MM-DD"
                                persistent-hint
                                prepend-icon="fa-calendar"
                                v-bind="attrs"
                                v-on="on"
                                required
                              ></v-text-field>
                            </template>
                            <v-date-picker
                              v-model="fechaInicio"
                              no-title
                              color="primary"
                              @input="menu1 = false"
                              @change="actualizarFecha()"
                            ></v-date-picker>
                          </v-menu>
                        </v-col>
                        <v-col md="4" cols="12" class="py-0">
                          <v-menu
                            ref="menu2"
                            v-model="menu2"
                            :close-on-content-click="false"
                            transition="scale-transition"
                            offset-y
                            max-width="290px"
                            min-width="auto"
                          >
                            <template v-slot:activator="{ on, attrs }">
                              <v-text-field
                                v-model="fechaFin"
                                label="Fecha estimada fin *"
                                hint="AAAA-MM-DD"
                                persistent-hint
                                prepend-icon="fa-calendar"
                                v-bind="attrs"
                                v-on="on"
                                required
                              ></v-text-field>
                            </template>
                            <v-date-picker
                              v-model="fechaFin"
                              no-title
                              color="primary"
                              :min="fechaInicio"
                              @input="menu2 = false"
                            ></v-date-picker>
                          </v-menu>
                        </v-col>
                        <v-col>
                          <v-btn
                            color="secondary"
                            class="mx-4"
                            @click="filtrarPorFechas()"
                          >
                            Filtrar por fechas
                          </v-btn>
                        </v-col>
                      </v-row>
                      <v-simple-table max-height="240px">
                        <template v-slot:default>
                          <thead>
                            <tr>
                              <th class="text-center">Código</th>
                              <th class="text-center">Nombre</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr v-for="encuesta in encuestas" key="id">
                              <td class="text-center">{{ encuesta.codigo }}</td>
                              <td class="text-center">{{ encuesta.nombre }}</td>
                            </tr>
                          </tbody>
                        </template>
                      </v-simple-table>
                    </v-expansion-panel-content>
                  </v-expansion-panel>

                  <v-expansion-panel
                    v-if="
                      actualParticipanteEstudios.estado ||
                      actualParticipanteEstudios.municipio ||
                      actualParticipanteEstudios.direccion
                    "
                  >
                    <v-expansion-panel-header
                      >Ubicación</v-expansion-panel-header
                    >
                    <v-expansion-panel-content>
                      <v-simple-table max-height="240px">
                        <template v-slot:default>
                          <thead>
                            <tr>
                              <th
                                class="text-center"
                                v-if="actualParticipanteEstudios.estado"
                              >
                                Estado
                              </th>
                              <th
                                class="text-center"
                                v-if="actualParticipanteEstudios.municipio"
                              >
                                Municipio
                              </th>
                              <th
                                class="text-center"
                                v-if="actualParticipanteEstudios.direccion"
                              >
                                Dirección
                              </th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td
                                v-if="actualParticipanteEstudios.estado"
                                class="text-center"
                              >
                                {{ actualParticipanteEstudios.estado }}
                              </td>
                              <td
                                v-if="actualParticipanteEstudios.municipio"
                                class="text-center"
                              >
                                {{ actualParticipanteEstudios.municipio }}
                              </td>
                              <td
                                v-if="actualParticipanteEstudios.direccion"
                                class="text-center"
                              >
                                {{ actualParticipanteEstudios.direccion }}
                              </td>
                            </tr>
                          </tbody>
                        </template>
                      </v-simple-table>
                    </v-expansion-panel-content>
                  </v-expansion-panel>

                  <v-expansion-panel
                    v-if="actualParticipanteCarreras.length > 0"
                  >
                    <v-expansion-panel-header
                      >Información académica</v-expansion-panel-header
                    >
                    <v-expansion-panel-content>
                      <v-simple-table max-height="240px">
                        <template v-slot:default>
                          <thead>
                            <tr>
                              <th
                                class="text-center"
                                v-if="actualParticipanteCarreras[0].colegio"
                              >
                                Colegio
                              </th>
                              <th
                                class="text-center"
                                v-if="actualParticipanteCarreras[0].sede"
                              >
                                Sede
                              </th>
                              <th
                                class="text-center"
                                v-if="actualParticipanteCarreras[0].carrera"
                              >
                                Carrera
                              </th>
                              <th
                                class="text-center"
                                v-if="actualParticipanteCarreras[0].semestre"
                              >
                                Semestre
                              </th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td
                                class="text-center"
                                v-if="actualParticipanteCarreras[0].colegio"
                              >
                                {{ actualParticipanteCarreras[0].colegio }}
                              </td>
                              <td
                                class="text-center"
                                v-if="actualParticipanteCarreras[0].sede"
                              >
                                {{ actualParticipanteCarreras[0].sede.nombre }}
                              </td>
                              <td
                                class="text-center"
                                v-if="actualParticipanteCarreras[0].carrera"
                              >
                                {{
                                  actualParticipanteCarreras[0].carrera.nombre
                                }}
                              </td>
                              <td
                                class="text-center"
                                v-if="actualParticipanteCarreras[0].semestre"
                              >
                                {{ actualParticipanteCarreras[0].semestre }}
                              </td>
                            </tr>
                          </tbody>
                        </template>
                      </v-simple-table>
                    </v-expansion-panel-content>
                  </v-expansion-panel>

                  <v-expansion-panel
                    v-if="
                      actualParticipanteEstudios.instagram ||
                      actualParticipanteEstudios.twitter ||
                      actualParticipanteEstudios.facebook ||
                      actualParticipanteEstudios.linkedin ||
                      actualParticipanteEstudios.tiktok
                    "
                  >
                    <v-expansion-panel-header
                      >Redes Sociales</v-expansion-panel-header
                    >
                    <v-expansion-panel-content>
                      <v-simple-table max-height="240px">
                        <template v-slot:default>
                          <thead>
                            <tr>
                              <th
                                class="text-center"
                                v-if="actualParticipanteEstudios.instagram"
                              >
                                <v-icon>fab fa-instagram</v-icon>
                              </th>
                              <th
                                class="text-center"
                                v-if="actualParticipanteEstudios.twitter"
                              >
                                <v-icon>fab fa-twitter</v-icon>
                              </th>
                              <th
                                class="text-center"
                                v-if="actualParticipanteEstudios.facebook"
                              >
                                <v-icon>fab fa-facebook</v-icon>
                              </th>
                              <th
                                class="text-center"
                                v-if="actualParticipanteEstudios.linkedin"
                              >
                                <v-icon>fab fa-linkedin</v-icon>
                              </th>
                              <th
                                class="text-center"
                                v-if="actualParticipanteEstudios.tiktok"
                              >
                                <v-icon>fab fa-tiktok</v-icon>
                              </th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td
                                v-if="actualParticipanteEstudios.instagram"
                                class="text-center"
                              >
                                {{ actualParticipanteEstudios.instagram }}
                              </td>
                              <td
                                v-if="actualParticipanteEstudios.twitter"
                                class="text-center"
                              >
                                {{ actualParticipanteEstudios.twitter }}
                              </td>
                              <td
                                v-if="actualParticipanteEstudios.facebook"
                                class="text-center"
                              >
                                {{ actualParticipanteEstudios.facebook }}
                              </td>
                              <td
                                v-if="actualParticipanteEstudios.linkedin"
                                class="text-center"
                              >
                                {{ actualParticipanteEstudios.linkedin }}
                              </td>
                              <td
                                v-if="actualParticipanteEstudios.tiktok"
                                class="text-center"
                              >
                                {{ actualParticipanteEstudios.tiktok }}
                              </td>
                            </tr>
                          </tbody>
                        </template>
                      </v-simple-table>
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                </v-expansion-panels>

                <v-card-actions>
                  <v-btn color="primary" text @click="modalEstudios = false">
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
                  @click="editarParticipante(item.id)"
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
                  @click="abrirEstudios(item.id)"
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
                  @click="mostrarEliminar(item.id, item.nombre)"
                  class="red--text"
                  >fa-trash</v-icon
                >
              </template>
              <span>Eliminar</span>
            </v-tooltip>
          </template>
        </v-data-table>
      </v-card>
    </v-col>
    <v-div style="display: flex; flex-direction: column" class="mx-auto mt-4">
      <div class="crud-buttons mx-auto mt-4">
        <v-btn color="secondary" class="mx-4" @click="exportarCSV(csvData)">
          Exportar a excel
        </v-btn>
      </div>
      <div class="crud-buttons mx-auto mt-4">
        <v-btn
          @click="goRoute('inicio')"
          class="btn-block accent1 mx-auto mb-0 d-none d-sm-flex"
        >
          Regresar
        </v-btn>
      </div>
    </v-div>
  </v-row>
</template>

<script>
import swal from "sweetalert";
import moment from "moment";
import Repository from "../../services/repositories/repositoryFactory";
const LugaresRepository = Repository.get("Lugares");
const ParticipantesRepository = Repository.get("Participantes");
const ParticipanteCarrerasRepository = Repository.get("ParticipanteCarreras");
const SedesRepository = Repository.get("Sedes");
const CarrerasRepository = Repository.get("Carreras");
const ColegiosRepository = Repository.get("Colegios");
export default {
  name: "ParticipantesView",
  data() {
    return {
      valid: false,
      buscador: false,
      search: "",
      headers: [
        {
          text: "Nombre",
          align: "start",
          value: "nombre",
        },
        { text: "Cédula", value: "cedula" },
        { text: "Género", value: "genero" },
        { text: "Correo electrónico", value: "correo" },
        { text: "Estado", value: "estado" },
        { text: "Tlf. Principal", value: "telfPrincipal" },
        { text: "Acciones", value: "actions", sortable: false },
      ],
      participantes: [],
      popupEliminar: false,
      participanteAEliminar: "",
      participanteAEliminarNombre: "",
      modalEstudios: false,
      actualParticipanteEstudios: {
        nombre: "Provicional",
        cedula: "Provicional",
        correo: "Provicional",
        correoUcab: "Provicional",
        telfPrincipal: "Provicional",
        telfSecundario: "Provicional",
        fechaNacimiento: "Provicional",
        genero: "Provicional",
        actualEstado: "Provicional",
        actualMunicipio: "Provicional",
        lugar: {
          estado: "Provicional",
          municipio: "Provicional",
        },
      },
      participante_carreras: null,
      actualParticipanteCarreras: [],
      form: {
        nombre: null,
        cedula: null,
        genero: null,
        sede: null,
        colegio: null,
        semestre: null,
        carrera: null,
        estado: null,
        municipio: null,
      },
      carreras: [],
      sedes: [],
      colegios: [],
      generos: [
        { nombre: "Masculino", id: "M" },
        { nombre: "Femenino", id: "F" },
        { nombre: "Otro", id: "O" },
      ],
      semestres: [
        { nombre: "Egresado", id: 11 },
        { nombre: "1ro", id: 1 },
        { nombre: "2do", id: 2 },
        { nombre: "3ro", id: 3 },
        { nombre: "4to", id: 4 },
        { nombre: "5to", id: 5 },
        { nombre: "6to", id: 6 },
        { nombre: "7mo", id: 7 },
        { nombre: "8vo", id: 8 },
        { nombre: "9no", id: 9 },
        { nombre: "10mo", id: 10 },
      ],
      lista_consultada: [],
      participantes_origen: [],
      estados: [],
      municipios_todos: [],
      encuestas: [],
      menu1: false,
      menu2: false,
      fechaInicio: moment().format("YYYY-MM-DD"),
      fechaFin: moment().format("YYYY-MM-DD"),
      usuarioAFiltrar: null
    };
  },
  computed: {
    participanteDetalleCarreras() {
      this.actualParticipanteCarreras.forEach((par_car) => {
        this.carreras.forEach((carrera) => {
          if (par_car.carrera == carrera.id) par_car.carrera = carrera.nombre;
        });
      });
    },
    csvData() {
      return this.participantes.map((item) => ({
        ...item,
        colegio: item.colegio.nombre || null,
      }));
    },
  },
  methods: {
    async getParticipantes() {
      this.participantes_origen = await ParticipantesRepository.obtener();
      let estado;
      let municipio;
      let lugar_id;
      let colegio;
      this.participantes_origen.forEach((par) => {
        estado = null;
        municipio = null;
        colegio = null;
        lugar_id = 0;
        if (par.lugar) lugar_id = par.lugar.id;
        if (par.colegio) colegio = par.colegio.nombre;
        this.estados.forEach((e) => {
          if (e.id == lugar_id) {
            estado = e.nombre;
          }
        });
        this.municipios_todos.forEach((m) => {
          if (m.id == lugar_id) {
            municipio = m.nombre;
            this.estados.forEach((e) => {
              if (m.fk_lugar_id == e.id) {
                estado = e.nombre;
              }
            });
          }
        });
        this.participantes.push({
          id: par.id,
          nombre: par.nombre,
          cedula: par.cedula,
          correo: par.correo,
          correoUcab: par.correoUcab,
          telfPrincipal: par.telfPrincipal,
          telfSecundario: par.telfSecundario,
          fechaNacimiento: par.fechaNacimiento,
          genero: par.genero,
          colegio: colegio,
          estado: estado,
          municipio: municipio,
          direccion: par.direccion,
          instagram: par.instagram,
          twitter: par.twitter,
          facebook: par.facebook,
          linkedin: par.linkedin,
          tiktok: par.tiktok,
        });
      });
    },
    async getParticipanteCarreras() {
      this.participante_carreras =
        await ParticipanteCarrerasRepository.obtener();
    },
    async getLugares() {
      this.estados = await LugaresRepository.obtenerEstados();
      this.municipios_todos = await LugaresRepository.obtenerMunicipios();
      this.getParticipantes();
    },
    municipios() {
      let id = this.form.estado;
      let array = [];
      this.municipios_todos.forEach((mun) => {
        if (mun.fk_lugar_id == id) {
          array.push(mun);
        }
      });
      return array;
    },
    mostrarEliminar(participanteID, participanteNombre) {
      this.popupEliminar = true;
      this.participanteAEliminar = participanteID;
      this.participanteAEliminarNombre = participanteNombre;
    },
    async eliminarParticipante() {
      try {
        await ParticipantesRepository.eliminar(this.participanteAEliminar);
        location.href = "/participantes";
      } catch (err) {
        console.log(err);
        swal("El participante no pudo ser eliminado", "", "error");
      }
    },
    editarParticipante(id) {
      this.goRoute(`participantes/${id}/editar`);
    },
    setParticipanteCarreras(id) {
      let par_car = {};
      let existe = false;
      this.participante_carreras.forEach((p) => {
        if (p.participante.id == id) {
          this.participantes.forEach((par) => {
            if (par.id == id) {
              p.colegio = par.colegio;
            }
          });
          this.actualParticipanteCarreras.push(p);
          existe = true;
        }
      });
      if (!existe) {
        this.participantes.forEach((par) => {
          if (par.id == id) {
            if (par.colegio) {
              par_car.colegio = par.colegio;
              this.actualParticipanteCarreras.push(par_car);
            }
          }
        });
      }
    },

    async abrirEstudios(userID) {
      this.actualParticipanteCarreras.splice(
        0,
        this.actualParticipanteCarreras.length
      );
      this.modalEstudios = true;
      this.participanteEstudios = userID;
      this.participantes.forEach((par) => {
        if (par.id == this.participanteEstudios) {
          this.actualParticipanteEstudios = par;
        }
      });
      this.usuarioAFiltrar = userID
      this.setParticipanteCarreras(userID);
      this.encuestas = await ParticipantesRepository.obtenerEncuestas(userID);
      
      console.log(this.encuestas);
    },

    async filtrarPorFechas(){
      let fechas = {
        fechaInicio: this.fechaInicio,
        fechaFin: this.fechaFin
      }
      this.encuestas = await ParticipantesRepository.obtenerEncuestasPorFechas(this.usuarioAFiltrar, fechas);
    },

    async filtrar() {
      try {
        this.participantes_origen = await ParticipantesRepository.filtrar(
          this.form
        );
        this.participantes = [];
        let estado;
        let municipio;
        let lugar_id;
        this.participantes_origen.forEach((par) => {
          (estado = null), (municipio = null), console.log(par);
          lugar_id = par.lugar_id;
          this.estados.forEach((e) => {
            if (e.id == lugar_id) {
              estado = e.nombre;
            }
          });
          this.municipios_todos.forEach((m) => {
            if (m.id == lugar_id) {
              municipio = m.nombre;
              this.estados.forEach((e) => {
                if (m.fk_lugar_id == e.id) {
                  estado = e.nombre;
                }
              });
            }
          });
          this.participantes.push({
            id: par.id,
            nombre: par.nombre,
            cedula: par.cedula,
            correo: par.correo,
            correoUcab: par.correoUcab,
            telfPrincipal: par.telfPrincipal,
            telfSecundario: par.telfSecundario,
            fechaNacimiento: par.fechaNacimiento,
            genero: par.genero,
            colegio: par.colegio_id,
            estado: estado,
            municipio: municipio,
            direccion: par.direccion,
            instagram: par.instagram,
            twitter: par.twitter,
            facebook: par.facebook,
            linkedin: par.linkedin,
            tiktok: par.tiktok,
          });
        });
      } catch (err) {
        console.log(err);
        swal("La consulta no pudo ser realizada", "", "error");
      }
    },

    exportarCSV(arrData) {
      let csvContent = "data:text/csv;charset=utf-8,";

      csvContent += [
        Object.keys(arrData[0]).join(";"),
        ...arrData.map((item) => Object.values(item).join(";")),
      ]
        .join("\n")
        .replace(/(^\[)|(\]$)/gm, "");

      const data = encodeURI(csvContent);
      const link = document.createElement("a");
      link.setAttribute("href", data);
      link.setAttribute("download", "participantes.csv");
      link.click();
      console.log(arrData);
    },

    async limpiar() {
      this.$refs.registerForm.reset();
      this.participantes = [];
      this.getParticipantes();
    },

    async getCarreras() {
      this.carreras = await CarrerasRepository.obtener();
    },
    async getSedes() {
      this.sedes = await SedesRepository.obtener();
    },
    async getColegios() {
      this.colegios = await ColegiosRepository.obtener();
    },

    goRoute(route) {
      this.$router.push("/" + route);
    },
  },

  mounted() {
    this.getLugares();
    this.getParticipanteCarreras();
    this.getCarreras();
    this.getSedes();
    this.getColegios();
  },
};
</script>

<style>
@import "../../styles/main.css";
</style>