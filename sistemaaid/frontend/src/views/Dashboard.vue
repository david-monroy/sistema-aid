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
    </div>
  </div>
</template>

<script>
import DashboardCard from "../components/dashboard/DashboardCard.vue";
export default {
  name: "Dashboard",
  components: {
    DashboardCard
  },
  computed: {

  },
  data: () => ({
      dashItems: [
      {
        id: 1,
        name: "Estudios",
        icon: "fa-file-alt",
        rol: 2,
        route: "estudios",
      },
      {
        id: 2,
        name: "Participantes",
        icon: "fa-users",
        rol: 1,
        route: "participantes",
      },
      {
        id: 3,
        name: "Reportes",
        icon: "fa-chart-pie",
        rol: 3,
        route: "reportes",
      },
      {
        id: 4,
        name: "Configuración",
        icon: "fa-cog",
        rol: 3,
        route: "configuracion",
      },
    ]
  })
};
</script>

<style>
  @import "../styles/components/dashboard.css";
  @import "../styles/main.css";
</style>