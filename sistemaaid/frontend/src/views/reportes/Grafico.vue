<template>
  <v-row
    align="center"
    class="list px-3 mx-auto nav-separator container mt-12"
    style="display: flex; align-items: flex-start"
  >
    <v-col cols="3" class="mt-2">
      <GraficoComponente chartID="1"></GraficoComponente>
    </v-col>
    <v-col cols="3" class="mt-2">
      <GraficoComponente chartID="2"></GraficoComponente>
    </v-col>
    <v-col cols="3" class="mt-2">
      <GraficoComponente chartID="3"></GraficoComponente>
    </v-col>
    <v-col cols="3" class="mt-2">
      <GraficoComponente chartID="4"></GraficoComponente>
    </v-col>
  </v-row>
</template>

<script>
import Chart from "chart.js";
import GraficoComponente from "../../components/reportes/Grafico.vue";

export default {
  name: "Grafico",
  components: { GraficoComponente },
  data() {
    return {
    }
  },
};
</script>