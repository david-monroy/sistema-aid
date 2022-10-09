<template>
  <div class="col-md-12 nav-separator pt-1">
    <div class="card card-container mt-0 form-card">
      <Loading :show=activeLoading />
      <h3 class="primary--text mx-auto mb-6 mt-0">
        Creación de árboles de decisión
      </h3>
      <v-spacer></v-spacer>

      <div class="section">
        <div class="container">
          <div class="mb-8">
            <p>
              A continuación, cargue el archivo .xlsx con la información a trabajar, para detectar los patrones de los grupos en base a su probabilidad de estudio en la UCAB. 
            </p>
            <p>
              La columna de la variable a predecir debe estar ubicada de última, y se llama Probabilidad
            </p>
          </div>
          <v-row class="pb-0 mb-0 form-row">
            <v-col md="10" cols="10" class="py-0">
              <div class="form-group">
                <v-file-input
                  v-model="file"
                  truncate-length="15"
                  label="Carga el archivo aquí"
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
          <v-row>
            <v-btn
                :small="$vuetify.breakpoint.smAndDown"
                class="primary"
                @click="exportarArbol()"
                :disable="!valid"
              >
                <p class="mt-3 hidden-sm-and-down">Exportar árbol</p>
              </v-btn>
          </v-row>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import swal from "sweetalert";
import Repository from "../../services/repositories/repositoryFactory";
import Loading from "../../components/comunes/Loading.vue"
const IaRepository = Repository.get("IA");
export default {
  data() {
    return {
      file: "",
      respuesta: [],
      activeLoading: false
    };
  },
  components: {
        Loading
    },
  methods: {
    async cargarCSV() {
      const formData = new FormData();
      formData.append("file", this.file);
      try {
        this.activeLoading = true;
        this.respuesta = await IaRepository.entrenarArbol(formData);
        this.activeLoading = false;
        if (this.respuesta.status == 200 ){
            swal("", this.respuesta.detail, "success");
        }
      } catch (err) {
        this.activeLoading = false;
        console.log(err);
        swal("No se ha podido cargar el archivo", "", "error");
      }
    },
    async exportarArbol() {
      try {
        this.activeLoading = true;
        this.respuesta = await IaRepository.exportarArbol();
        this.activeLoading = false;
        if (this.respuesta.status == 200 ){
            swal("", this.respuesta.detail, "success");
        }
      } catch (err) {
        this.activeLoading = false;
        console.log(err);
        swal("No se ha podido cargar el archivo", "", "error");
      }
    },
  }
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