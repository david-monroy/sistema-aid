<template>
  <v-card @click="goRoute(route)" class="pa-4 dashboard-card__item">
    <div style="display: flex; justify-content: center; flex: 1">
      <v-icon size="60" color="light" class="ml-12 pl-12">{{ icon }} </v-icon>
    </div>
    <div style="display: flex; justify-content: flex-start; flex: 1">
      <h4 color="light" cols="8">{{ name }}</h4>
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
@import "../../styles/main.css";
</style>