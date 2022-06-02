<template>
  <v-row
    align="center"
    class="list px-3 mx-auto nav-separator container mt-12"
    style="display: flex; align-items: flex-start"
  >
    <v-col cols="6" sm="6" class="mt-2">
      <div
        class="form-group"
        style="display: flex; justify-content: center; width: 100%"
      >
        <v-select
          v-model="tipoGrafico"
          :items="tiposGrafico"
          item-text="nombre"
          item-value="id"
          label="Tipo de gráfico"
        ></v-select>
      </div>
      <canvas id="chart"></canvas>
    </v-col>
  </v-row>
</template>

<script>
import Chart from "chart.js";

export default {
  name: "Grafico",
  data() {
    return {
      datos: {
        data: {
          labels: ["Inscritos", "No inscritos"],
          datasets: [
            {
              label: "Historico Inscripciones",
              data: [100, 120],
              backgroundColor: ["rgba(54,73,93,.5)", "rgba(4,7,93,.5)"],
              borderWidth: 3,
            },
          ],
        },
        options: {
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        }
      },
      tipoGrafico: null,
      tiposGrafico: [
        { id: 1, nombre: "Torta" },
        { id: 2, nombre: "Barras" },
      ],
    };
  },
  methods: {
    crearGraficoTorta() {
      this.datos.type = "pie";
      const ctx = document.getElementById("chart");
      new Chart(ctx, this.datos);
    },
    crearGraficoBarra() {
      this.datos.type = "bar";
      const ctx = document.getElementById("chart");
      new Chart(ctx, this.datos);
    },
  },
  mounted() {
    this.crearGraficoBarra();
    // const ctx = document.getElementById("chart");
    // new Chart(ctx, this.datos);
  },
};
</script>