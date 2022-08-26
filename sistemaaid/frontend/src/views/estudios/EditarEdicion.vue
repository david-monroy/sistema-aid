<template>
  <v-container fluid elevation="0" class="nav-separator">
    <v-row no-gutters justify="start">
      <h3 class="primary--text mx-auto mb-6 mt-0 md=8">
        {{ edicion.estudio.nombre }} - {{ edicion.codigo }}
      </h3>
    </v-row>
    <v-expansion-panels class="px-12">
      <v-expansion-panel>
        <v-expansion-panel-header>
          <template v-slot:default>
            <v-row no-gutters class="panels-title"> Información General </v-row>
          </template>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-row class="pb-0 mb-0 form-row">
            <v-col md="6" cols="12" class="py-0">
              <div class="form-group">
                <v-tooltip left>
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="edicion.periodo"
                      label="Período"
                      v-bind="attrs"
                      v-on="on"
                      dense
                      type="number"
                    ></v-text-field>
                  </template>
                  <span>Período académico de la UCAB</span>
                </v-tooltip>
              </div>
            </v-col>

            <v-col md="6" cols="12" class="py-0">
              <div class="form-group">
                <v-tooltip right>
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="edicion.totalMuestra"
                      label="Tamaño muestral * "
                      required
                      type="number"
                      :rules="[rules.required, rules.muestra]"
                      v-bind="attrs"
                      v-on="on"
                      dense
                    ></v-text-field>
                  </template>
                  <span>Cantidad de personas a encuestar</span>
                </v-tooltip>
              </div>
            </v-col>
          </v-row>

          <v-row class="pb-0 mb-0 form-row">
            <v-col md="6" cols="12" class="py-0">
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
                    v-model="edicion.fechaInicio"
                    label="Fecha inicio *"
                    hint="AAAA-MM-DD"
                    persistent-hint
                    prepend-icon="fa-calendar"
                    v-bind="attrs"
                    v-on="on"
                    required
                    dense
                    :rules="[rules.required]"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="edicion.fechaInicio"
                  no-title
                  color="primary"
                  @input="menu1 = false"
                  @change="actualizarFecha()"
                ></v-date-picker>
              </v-menu>
            </v-col>

            <v-col md="6" cols="12" class="py-0">
              <v-menu
                ref="menu2"
                v-model="menu2"
                :close-on-content-click="false"
                transition="scale-transition"
                offset-y
                max-width="290px"
                min-width="auto"
                dense
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="edicion.fechaFin"
                    label="Fecha Fin"
                    hint="AAAA-MM-DD"
                    persistent-hint
                    prepend-icon="fa-calendar"
                    v-bind="attrs"
                    @blur="date = parseDate(dateFormatted)"
                    v-on="on"
                    required
                    dense
                    :rules="[rules.required]"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="edicion.fechaFin"
                  no-title
                  color="primary"
                  :min="edicion.fechaInicio"
                  @input="menu2 = false"
                ></v-date-picker>
              </v-menu>
            </v-col>
          </v-row>
        </v-expansion-panel-content>
      </v-expansion-panel>
      <v-expansion-panel>
        <v-expansion-panel-header>
          <template v-slot:default>
            <v-row no-gutters class="panels-title"> Muestra Ponderada </v-row>
          </template>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <ConsultarMuestraPonderada
            :edicion="edicion"
          ></ConsultarMuestraPonderada>
        </v-expansion-panel-content>
      </v-expansion-panel>
      <v-expansion-panel>
        <v-expansion-panel-header>
          <template v-slot:default>
            <v-row no-gutters class="panels-title"> Instrumento </v-row>
          </template>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <ConsultarInstrumento :edicion="edicion"></ConsultarInstrumento>
        </v-expansion-panel-content>
      </v-expansion-panel>
      <v-expansion-panel>
        <v-expansion-panel-header>
          <template v-slot:default>
            <v-row no-gutters class="panels-title"> Encuestas </v-row>
          </template>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <ConsultarEncuestas :edicion="edicion"></ConsultarEncuestas>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
    <v-col align="center">
            <v-btn
              :small="$vuetify.breakpoint.smAndDown"
              class="success"
              @click="actualizarEdicion()"
              :disable="!valid"
            >
              <p class="mt-3 hidden-sm-and-down">Actualizar</p>
            </v-btn>
          </v-col>
  </v-container>
</template>


<script>
import swal from "sweetalert";
import Repository from "../../services/repositories/repositoryFactory";
import ConsultarFichaTecnica from "../../components/estudios/ConsultaFichaTecnica.vue";
import ConsultarMuestraPonderada from "../../components/estudios/ConsultarMuestraPonderada.vue";
import ConsultarInstrumento from "../../components/estudios/ConsultarInstrumento.vue";
import ConsultarEncuestas from "../../components/estudios/ConsultarEncuestas.vue";

import { EventBus } from "../../main.js";
const EdicionRepository = Repository.get("Ediciones");

export default {
  data() {
    return {
      file: "",
      valid: true,
      respuesta: [],
      idEdicion: null,
      edicion: {},
      valid: true,
      muestraPonderada: [],
      date: new Date().toISOString().substr(0, 10),
      dateFormatted: this.formatDate(new Date().toISOString().substr(0, 10)),
      menu1: false,
      menu2: false,
      rules: ({} = {
        required: (value) =>
          (!!value && value !== "" && value !== undefined) ||
          "Este campo es requerido",
        muestra: (value) =>
          (!!value && value > 0) || "La muestra debe ser mayor a 0",
        textos: (value) => value.length <= 280 || "El texto es demasiado largo",
        poblacion: (value) =>
          value.length <= 50 || "El texto es demasiado largo",
      }),
    };
  },
  components: {
    ConsultarFichaTecnica,
    ConsultarMuestraPonderada,
    ConsultarInstrumento,
    ConsultarEncuestas,
  },
  computed: {
    computedDateFormatted() {
      return this.formatDate(this.date);
    },
  },
  beforeMount() {
    this.buscarEdicion(this.$route.params.id);
  },
   watch: {
    date() {
      this.fechaFin = this.formatDate(this.date);
    },
  },
  methods: {
    async actualizarEdicion(){
        try {
            let payload = {
            id: this.edicion.id,
            codigo: this.edicion.codigo,
            fechaInicio: this.edicion.fechaInicio,
            fechaFin: this.edicion.fechaFin,
            periodo: this.edicion.periodo,
            vinculada: this.edicion.vinculada,
            totalMuestra: this.edicion.totalMuestra,
            estudio_id: this.edicion.estudio.id
        }
            let editarEdicion = await EdicionRepository.actualizar(
            payload.id,
            payload
          );
        
        console.log(payload)
          swal(
          "La edición ha sido actualizada satisfactoriamente",
          "",
          "success"
        );
        this.$router.push("/estudios");
        } catch (error) {
            swal("No se pudo actualizar la edicion", "", "error");
        }
      
    },
    async cargarExcel() {
      const formData = new FormData();
      formData.append("file", this.file);
      try {
        this.respuesta = await EdicionRepository.cargarEncuestas(
          formData,
          edicion.id
        );
      } catch (err) {
        console.log(err);
        swal("No se pudo procesar la muestra", "", "error");
      }
    },
    formatDate(date) {
      if (!date) return null;
      const [year, month, day] = date.split("-");
      return `${year}-${month}-${day}`;
    },
    parseDate(date) {
      if (!date) return null;
      const [month, day, year] = date.split("/");
      return `${year}-${month.padStart(2, "0")}-${day.padStart(2, "0")}`;
    },
    actualizarFecha() {
      this.form.fechaFin = "";
    },

    async buscarEdicion(id) {
      try {
        this.edicion = await EdicionRepository.buscarEdicion(id);
      } catch (err) {
        console.log(err);
        swal("No se pudo procesar la muestra", "", "error");
      }
    },
  },
};
</script>

<style>
@import "../../styles/main.css";
</style>