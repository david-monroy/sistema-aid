<template>
  <div class="col-md-12 nav-separator pt-1">
    <div class="card card-container mt-0 form-card">
      <h3 class="primary--text mx-auto mb-6 mt-0">Registrar nuevos participantes</h3>
      <v-spacer></v-spacer>

      <div class="section">
          <div class="container">

            <v-row class="pb-0 mb-0 form-row" >
            <v-col md="10" cols="10" class="py-0">
                <div class="form-group">
                    <v-file-input
                        v-model="file"
                        truncate-length="15"
                        label="Cargue el archivo con los participantes"
                    ></v-file-input>
                </div>
            </v-col>
            <v-col md="2" cols="2" align="end">
                <v-btn
                    :small="$vuetify.breakpoint.smAndDown"
                    class="primary"
                    @click="cargarCSV()"
                    :disable=!valid
                >
                    <p class="mt-3 hidden-sm-and-down">Enviar</p>
                    <v-icon>mdi-chevron-right</v-icon>
                </v-btn>
            </v-col>
        </v-row>
            <div>
                <p> A continuación, descargue <a href="/assets/files/Plantilla_Participantes.xlsx"  download>esta plantilla</a>
                 y luego inserte en ella todos los participantes a <b>agregar o editar,</b> cárguela nuevamente y haga click en el botón Enviar.</p>
                <p>Tenga en cuenta:</p>
                <ul>
                    <li>El formato para la fecha de nacimiento debe ser <b>día/mes/año</b>.</li>
                    <li>Los participantes deben ser <b>mayores de 11 años.</b></li>
                </ul>
                <!-- <img
                class="img-zoom"
                src="../../assets/Tabladeparticipantes.png"
                /> -->
            </div>

          </div>
      </div> 

    </div>

  </div>
</template>


<script>
import swal from 'sweetalert';
import Repository from "../../services/repositories/repositoryFactory";
const ParticipantesRepository = Repository.get("Participantes");
export default {
    data(){
        return {
            file: ""
        }
    },
    computed: {
      computedDateFormatted () {
        return this.formatDate(this.date)
      }
    },
    methods: {
        seleccionarCSV(){
            this.file = this.$refs.file.files[0]
        },
        goRoute(route) {
            this.$router.push("/" + route);
        },
        async cargarCSV(){
            const formData = new FormData();
            formData.append('file', this.file)
            try{
                await ParticipantesRepository.cargaMasiva(formData);
                swal("Archivo cargado exitosamente", "", "success")
                this.goRoute('participantes')
            }
            catch(err){
              console.log(err)
              swal("No se ha podido cargar el archivo", "", "error")
            }
        },
    },
    created(){

    }
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
.img-zoom{
    max-width: 100%;
    transition: transform .2s; /* Animation */
}
.img-zoom:hover{
    transform: scale(1.5);
}
</style>