<template>
  <v-row
    align="center"
    class="list px-3 mx-auto nav-separator container mt-12"
    style="display: flex; align-items: flex-start"
  > 
    <v-col cols="6" sm="6" class="mt-2">
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
      datos: null,
    };
  },
  methods: {
    setData() {
      this.datos = {
        type: "pie",
        data: {
          labels: [
            "Inscritos",
            "No inscritos"
          ],
          datasets: [
            {
              label: "Inscripciones 2022",
              data: [150,215],
              backgroundColor: [
                  "rgba(54,73,93,.5)",
                  "rgba(4,7,93,.5)"
                  ],
              borderWidth: 3,
            },
          ],
        },
      };
    },
  },
  mounted() {
    this.setData();
    const ctx = document.getElementById("chart");
    new Chart(ctx, this.datos);
  },
};
</script>