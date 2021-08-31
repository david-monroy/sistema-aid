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
import DashboardCard from "../../components/dashboard/DashboardCard.vue";
import AgregarParticipante from "../../components/Participante/ParticipanteManual.vue";
export default {
name: "AgregarParticipante",
components: {
    DashboardCard, AgregarParticipante
  },
  data() {
        return {
            dashItems: [
            {
                id: 1,
                name: "Agregar participante (manual)",
                icon: "fa-address-card",
                route: "/participantes/agregar/manual",
            },
            {
                id: 2,
                name: "Agregar participantes (masivo)",
                icon: "fa-users",
                route: "#",
            }
            ]
        }
    },
}
</script>

<style>
@import "../../styles/main.css";
</style>