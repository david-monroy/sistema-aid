<template>
    <v-data-table
        :headers="getHeaders()"
        :items="items"
        hide-default-footer
        :items-per-page="-1"
        class="elevation-1"
    >
    </v-data-table>
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