<template>
  <div class="col-md-12 pt-1">
    <div class="card-container mt-0 form-card">
      <v-row class="pb-0 mb-0 form-row mt-4" v-if="edicion.metodologia">
        <strong class="primary--text">METODOLOGÍA: </strong>
      </v-row>
      <v-row class="pb-0 mb-0 form-row mt-4">
        <v-col
          md="5"
          cols="12"
          class="py-0 info-text"
        >
          <strong>Cualitativa: </strong>
          <div class="form-group">
            <v-textarea
              v-model="edicion.metodologia.descripcionCualitativa"
              dense
              :rules="[rules.textos]"
              auto-grow
              counter
              rows="2"
            ></v-textarea>
          </div>
        </v-col>
        <v-col
          md="5"
          cols="12"
          class="py-0 info-text"
        >
          <strong>Modalidad: </strong>
          <v-select
            v-model="edicion.metodologia.modalidadCualitativa"
            :items="modalidades"
            label="Modalidad"
          ></v-select>
        </v-col>
        <v-col md="2" cols="12" align="center">
          <v-btn
            :small="$vuetify.breakpoint.smAndDown"
            class="success"
            @click="actualizarMetodologia(edicion.metodologia)"
            :disable="!valid"
          >
            <p class="mt-3 hidden-sm-and-down">{{boton}}</p>
          </v-btn>
        </v-col>
      </v-row>
      <v-row class="pb-0 mb-0 form-row mt-2">
        <v-col
          md="5"
          cols="12"
          class="py-0 info-text"
        >
          <strong>Cuantitativa: </strong>
          <v-textarea
            v-model="edicion.metodologia.descripcionCuantitativa"
            dense
            :rules="[rules.textos]"
            auto-grow
            counter
            rows="2"
          ></v-textarea>
        </v-col>
        <v-col
          md="5"
          cols="12"
          class="py-0 info-text"
        >
          <strong>Modalidad: </strong>
          <v-select
            v-model="edicion.metodologia.modalidadCuantitativa"
            :items="modalidades"
            label="Modalidad"
          ></v-select>
        </v-col>
        <v-col md="2" cols="12" align="center">
          <v-btn
            :small="$vuetify.breakpoint.smAndDown"
            class="success"
            @click="actualizarMetodologia(edicion.metodologia)"
            :disable="!valid"
          >
            <p class="mt-3 hidden-sm-and-down">{{boton}}</p>
          </v-btn>
        </v-col>
      </v-row>
    </div>
  </div>
</template>


<script>
import Repository from "../../../services/repositories/repositoryFactory";
const MetodologiaRepository = Repository.get("Metodologia");
export default {
  data: () => ({
    metodologia: {},
    modalidades: [
      "Presencial autoadministrado",
      "Presencial cara a cara",
      "Online(autoadministrado)",
    ],
    rules: ({} = {
      textos: (value) => value.length <= 280 || "El texto es demasiado largo",
    }),
    boton: "Actualizar"
  }),
  props: {
    edicion: {},
  },
  mounted() {
    // this.getMetodologia(this.edicion.id);
  },
  methods: {
    async getMetodologia(id) {
      this.metodologia = await MetodologiaRepository.buscarMetodologia(id);
    },
    async actualizarMetodologia(metodologia) {
      try {
        let editarMetodologia = await MetodologiaRepository.actualizar(
          metodologia.id,
          metodologia
        );
        swal("Modalidad actualizada satisfactoriamente", "", "success");
      } catch (error) {
        console.log(err);
        swal("La modalidad no pudo ser actualizado" + err, "", "error");
      }
    },
  },
};
</script>

<style>
@import "../../../styles/main.css";
@import "../../../styles/components/participantes.css";
</style>