<template>
  <v-container>
    <v-row
      align="center"
      class="list px-3 mx-auto nav-separator container mt-12"
      style="display: flex; justify-content: center"
    >
      <v-col cols="12" sm="6" class="mt-4">
        Seleccione una o dos ediciones del estudio <b>{{ estudio.nombre }}</b> para comparar sus resultados
        <v-select
          v-model="edicionesSelect"
          :items="ediciones"
          item-text="codigo"
          item-value="id"
          chips
          label="Ediciones"
          v-on:input="limiteOpciones"
          multiple
          outlined
          class="mt-2"
        ></v-select>
      </v-col>
    </v-row>
    <v-row
      align="center"
      class="list px-3 mx-auto nav-separator container mt-4"
      style="display: flex; align-items: flex-start"
    >
      <v-col cols="3" class="mt-2">
        <GraficoComponente :chartID="1"></GraficoComponente>
      </v-col>
      <v-col cols="3" class="mt-2">
        <GraficoComponente :chartID="2"></GraficoComponente>
      </v-col>
      <v-col cols="3" class="mt-2">
        <GraficoComponente :chartID="3"></GraficoComponente>
      </v-col>
      <v-col cols="3" class="mt-2">
        <GraficoComponente :chartID="4"></GraficoComponente>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Chart from "chart.js";
import GraficoComponente from "../../components/reportes/Grafico.vue";
import Repository from "../../services/repositories/repositoryFactory";
const EstudiosRepository = Repository.get("Estudios");
export default {
  name: "Graficos",
  components: { GraficoComponente },

  data() {
    return {
      estudio_id: null,
      ediciones: [],
      edicionesSelect: [],
      estudio: null
    };
  },
  methods: {
    async getEdiciones(id) {
      this.ediciones = await EstudiosRepository.obtenerEdiciones(id);
      console.log(this.ediciones)
    },
    limiteOpciones(e) {
      if(e.length > 2) {
        console.log('Solo puedes seleccionar dos', e)
        e.pop()
      }
    },
    async getEstudio(id){
      let estudios = await EstudiosRepository.consultar();
      estudios.forEach((est) => {
        if (est.id == id) {
          this.estudio = est;
        }
      });
    }
  },
  mounted() {
    this.estudio_id = this.$route.params.id;
    this.getEstudio(this.estudio_id);
    this.getEdiciones(this.estudio_id);
  },
};
</script>