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
<style>

/* This is the size of the path of the scrollbar */
#wrapper2{
      width: 100%;
      overflow-x: scroll; 
      overflow-y:hidden;
  }

/* This div allow to make the scroll function and show the scrollbar */
  #div2 {
      height: 1px;
      overflow: scroll;
  }

  /* This is the size of the scrollbar */
  .width-scroll{
    width:1800px;
  }

</style>