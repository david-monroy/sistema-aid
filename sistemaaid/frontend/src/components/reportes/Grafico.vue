<template>
    <v-col cols="12" class="mt-2">
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
      <canvas :id="chartID"></canvas>
    </v-col>
</template>

<script>
import Chart from "chart.js";

export default {
  name: "Grafico",
  props:{
      chartID: Number,
  },
  data() {
    return {
      chart: null,
      datos: {
        data: {
          labels: ["Inscritos", "No inscritos"],
          datasets: [
            {
              label: "Historico Inscripciones",
              data: [100, 120],
              backgroundColor: ["rgba(54,73,93,.5)", "rgba(4,7,93,.5)"],
              borderWidth: 3,
              yAxisID: 0,
            },
          ],
        },
        options: {
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: true,
                },
              },
            ],
          },
        },
      },
      tipoGrafico: null,
      tiposGrafico: [
        { id: "pie", nombre: "Torta" },
        { id: "bar", nombre: "Barras" },
      ],
    };
  },
  watch: {
    tipoGrafico: function (val) {
      this.crearGrafico(this.tipoGrafico);
    },
  },
  methods: {
    crearGrafico(tipo) {
      this.datos.type = tipo;
      if (!this.chart) {
        const ctx = document.getElementById(this.chartID);
        this.chart = new Chart(ctx, this.datos);
      } else {
        this.chart.update()
      }
    },
  },
  mounted() {
      this.crearGrafico('pie')
  },
};
</script>