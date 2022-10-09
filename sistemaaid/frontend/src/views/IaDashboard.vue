<template>
  <div id="dashboard">
    <div
    class="mx-auto dashboard-main-card"
    >
      <v-card-text>
        <v-row>
          <v-col cols="12" class="dashboard-item-list">
            <div
              v-for="item in dashItems"
              :key="item.id"
            >
              <DashboardCard
                :name="item.name"
                :icon="item.icon"
                :route="item.route"
                class="text-center"
              >
              </DashboardCard>
            </div>
          </v-col>
        </v-row>
      </v-card-text>
      <v-btn @click="goRoute('inicio')"
          class="btn-block accent1 w-25 mx-auto  mb-0 d-none d-sm-flex">
          Regresar
      </v-btn>
    </div>
  </div>
</template>

<script>
import DashboardCard from "../components/dashboard/DashboardCard.vue";
export default {
  name: "IaDashboard",
  components: {
    DashboardCard
  },
  computed: {

  },
  data: () => ({
      dashItems: [
      {
        id: 1,
        name: "Patrones",
        icon: "fa-chart-line",
        rol: 2,
        route: "Patrones",
        permiso: "backend | edicion | patrones"
      },
      {
        id: 2,
        name: "Preprocesamiento",
        icon: "fa-clipboard-list",
        rol: 2,
        route: "Preprocesamiento",
        permiso: "backend | edicion | preprocesamiento"
      },
      {
        id: 3,
        name: "Entrenar modelo",
        icon: "fa-hammer",
        rol: 2,
        route: "Entrenar",
        permiso: "backend | edicion | entrenar"
      },

    ]
  }),
  methods: {
    goRoute(route) {
      this.$router.push("/" + route);
    },
  }
};
</script>

<style>
  @import "../styles/components/dashboard.css";
  @import "../styles/main.css";
</style>