<template>
  <v-card 
  class="pa-4 ma-0 dashboard-card__item primary-color" 
  @click="goRoute(route)">
    <div class="text-center">
      <v-icon size="60" color="white"
              class="mb-2">{{icon}}
      </v-icon>
      <h4 class="">{{ name }}</h4>
    </div>
  </v-card>
</template>

<script>
export default {
  name: "DashboardCard",
  props: {
    name: String,
    icon: String,
    route: String,
  },
  methods: {
    goRoute(route) {
      this.$router.push("/" + route);
    },
  },
  data: () => ({}),
};
</script>

<style>
@import "../../styles/components/dashboard.css";
</style>