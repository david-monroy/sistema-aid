<template>
  <v-div>
    <v-spacer></v-spacer>
          <v-text-field
            v-model="search"
            append-icon="fa-search"
            label="Buscar"
            single-line
            hide-details
          ></v-text-field>
    <v-data-table
        :headers="getHeaders()"
        :items="items"
        :hide-default-footer="false"
        :items-per-page="10"
        class="elevation-1"
        :search="search"
    >
    </v-data-table>
  </v-div>
</template>

<script>
export default {
  props: {
    items: []
  },
  methods: {
    getHeaders(){
        var headers = []
        for (var key in this.items[0]){      
            var head = {
                text: key, 
                value: key
            }
            headers.push(head)
        }
        return headers
        },
  },
  data: () => ({}),
};
</script>