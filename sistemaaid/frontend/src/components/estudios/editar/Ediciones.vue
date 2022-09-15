<template>
  <div class="col-md-12 pt-1">
    <div class="card-container mt-0 form-card">
      <v-form ref="registerForm" v-model="valid" lazy-validation>
        <v-expansion-panels>
          <v-expansion-panel v-for="edicion in ediciones" key="id">
            <v-expansion-panel-header>
              <template v-slot:default>
                <v-row no-gutters class="panels-title">
                  Edición {{ edicion.codigo }}
                </v-row>
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
              <MetodologiaEditar :edicion="edicion"></MetodologiaEditar>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>

        <v-row class="mt-2">
          <v-col align="begin">
            <v-btn
              :small="$vuetify.breakpoint.smAndDown"
              class="primary"
              @click="pasoAnterior()"
              :disable="!valid"
            >
              <p class="mt-3 hidden-sm-and-down">Atrás</p>
              <v-icon>mdi-chevron-right</v-icon>
            </v-btn>
          </v-col>
          <v-col align="center">
            <v-btn
              text
              :small="$vuetify.breakpoint.smAndDown"
              class="red--text"
              @click="goRoute('estudios')"
              >Cancelar
            </v-btn>
          </v-col>
          <v-col align="end">
            <v-btn
              :small="$vuetify.breakpoint.smAndDown"
              class="primary"
              @click="pasoSiguiente()"
              :disable="!valid"
            >
              <p class="mt-3 hidden-sm-and-down">Siguiente</p>
              <v-icon>mdi-chevron-right</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-form>
    </div>
  </div>
</template>



<script>
import swal from "sweetalert";
import Repository from "../../../services/repositories/repositoryFactory";
import { EventBus } from "../../../main.js";
const MetodologiaRepository = Repository.get("Metodologia");
const EdicionesRepository = Repository.get("Metodologia");
import MetodologiaEditar from "./Metodologia.vue";

export default {
  data() {
    return {
      file: "",
      valid: true,
      muestraPonderada: [],
      date: new Date().toISOString().substr(0, 10),
      dateFormatted: this.formatDate(new Date().toISOString().substr(0, 10)),
      menu1: false,
      menu2: false,
      rules: {} = {
                required: (value) =>
                (!!value && value !== "" && value !== undefined) || "Este campo es requerido",
                muestra: (value) =>
                (!!value && value > 0) || "La muestra debe ser mayor a 0",
                textos: (value) => 
                (value.length <= 280) || "El texto es demasiado largo",
                poblacion: (value) => 
                (value.length <= 50) || "El texto es demasiado largo",
            }
    };
  },
  props: {
    ediciones: Array,
    tipo: String,
  },
  components: {
    MetodologiaEditar,
  },
  computed: {
    computedDateFormatted() {
      return this.formatDate(this.date);
    },
  },

  methods: {
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

    pasoAnterior() {
      if (this.tipo == "Estudio") {
        EventBus.$emit("pasoAnterior", this.form);
      } else {
        EventBus.$emit("pasoAnteriorEdi", this.form);
      }
    },
    pasoSiguiente() {
      EventBus.$emit("pasoSiguienteEdicion",this.ediciones)
    },
    goRoute(route) {
      this.$router.push("/" + route);
    },
  },
  watch: {
    date() {
      this.fechaFin = this.formatDate(this.date);
    },
  },
};
</script>

<style>
@import "../../../styles/main.css";
@import "../../../styles/components/participantes.css";
</style>