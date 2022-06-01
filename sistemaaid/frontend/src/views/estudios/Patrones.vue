<template>
  <div class="col-md-12 nav-separator pt-1">
    <div class="card card-container mt-0 form-card">
      <h3 class="primary--text mx-auto mb-6 mt-0">
        Variables
      </h3>
      <v-spacer></v-spacer>

      <div class="section">
        <div class="container">
          <div class="mb-8">
            <p>
              A continuación, cargue un archivo .csv con las
              <b>variables</b> a ser seleccionadas por el algoritmo.
            </p>
            <p>
              La columna de la <b>variable a predecir</b> debe estar ubicada <b>de última.</b>
            </p>
          </div>
          <v-row class="pb-0 mb-0 form-row">
            <v-col md="10" cols="10" class="py-0">
              <div class="form-group">
                <v-file-input
                  v-model="file"
                  truncate-length="15"
                  label="Carga el archivo con las variables"
                ></v-file-input>
              </div>
            </v-col>
            <v-col md="2" cols="2" align="end">
              <v-btn
                :small="$vuetify.breakpoint.smAndDown"
                class="primary"
                @click="cargarCSV()"
                :disable="!valid"
              >
                <p class="mt-3 hidden-sm-and-down">Enviar</p>
                <v-icon>mdi-chevron-right</v-icon>
              </v-btn>
            </v-col>
          </v-row>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import swal from "sweetalert";
import Repository from "../../services/repositories/repositoryFactory";
const ParticipantesRepository = Repository.get("Participantes");
const EstudiosRepository = Repository.get("Estudios");
export default {
  data() {
    return {
      file: "",
    //   variablesSeleccionadas: []
    };
  },
  computed: {
      csvData() {
      return this.variablesSeleccionadas.map(item => ({
        ...item
      }));
    }
    },
  methods: {
    seleccionarCSV() {
      this.file = this.$refs.file.files[0];
    },
    goRoute(route) {
      this.$router.push("/" + route);
    },
    async cargarCSV() {
      const formData = new FormData();
      formData.append("file", this.file);
      try {
        let variablesSeleccionadas = await EstudiosRepository.seleccionarVariablesRFE(formData);
        swal("Archivo cargado exitosamente", "", "success");
        // console.log(variablesSeleccionadas)
        let varlist = []
        for(var i in variablesSeleccionadas)
            varlist.push(variablesSeleccionadas [i]);

        
        this.exportarCSV(varlist)
      } catch (err) {
        console.log(err);
        swal("No se ha podido cargar el archivo", "", "error");
      }
    },
    exportarCSV(arrData){
          let csvContent = "data:text/csv;charset=utf-8,";
          csvContent += [
            Object.keys(arrData[0]).join(";"),
            ...arrData.map(item => Object.values(item).join(";"))
          ]
            .join("\n")
            .replace(/(^\[)|(\]$)/gm, "");

          const data = encodeURI(csvContent);
          const link = document.createElement("a");
          link.setAttribute("href", data);
          link.setAttribute("download", "variablesSeleccionadasRFE.csv");
          link.click();
          console.log(arrData)
        },
  },
  created() {},
};
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
.img-zoom {
  max-width: 100%;
  transition: transform 0.2s; /* Animation */
}
.img-zoom:hover {
  transform: scale(1.5);
}
</style>