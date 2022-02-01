<template>
<div class="col-md-12 nav-separator pt-1">
    <div class="card card-container mt-0 form-card">
      <h3 class="primary--text mx-auto mb-6 mt-0">Registrar lista de código</h3>
      <v-spacer></v-spacer>
      <v-form
        ref="registerForm"
        v-model="valid"
        lazy-validation
      >
    <v-row class="pb-0 mb-0 form-row" >
        <v-col md="12" cols="12" class="py-0">
            <div class="form-group">
                    <v-text-field
                        v-model="form.nombre"
                        label="Nombre *"
                        required
                        dense
                        :rules='[rules.required]'
                    ></v-text-field>
                </div>
        </v-col>
    </v-row>
    <v-row class="pb-0 mb-0 form-row" >
        <v-col md="12" cols="12" class="py-0">
            <div class="form-group">
                     <v-textarea
                    v-model="form.descripcion"
                    dense
                    label="Descripción"
                    :rules='[rules.textos]'
                    auto-grow
                    counter
                    rows="2"
                    ></v-textarea>
                </div>
        </v-col>
    </v-row>
    <v-row class="pb-0 mb-0 form-row" >
        <v-col md="12" cols="12" class="py-0">
            <div class="form-group">
                <v-file-input
                        v-model="file"
                        truncate-length="15"
                        label="Carga el archivo .csv con la lista de código"
                        :rules='[rules.required]'
                ></v-file-input>
            </div>
        </v-col>
    </v-row>
      </v-form>
        <div>
            <p>El archivo debe contener en la primera columna el código y en la segunda columna la descripción.</p>
            <p>La primera fila puede ir vacía o tal como se muestra en la siguiente imagen</p>
            <img
                src="../../../assets/tablaListaCodigo.png"
            />  
            <p> Por último siempre asegúrese de no dejar filas vacías al final del archivo</p>
        </div>
        <v-row justify="center">
            <v-btn
                    :small="$vuetify.breakpoint.smAndDown"
                    class="primary"
                    @click="cargarListaCodigo()"
                    :disable=!valid
            >
            <p class="mt-3 hidden-sm-and-down"> Registrar </p>
            <v-icon>mdi-chevron-right</v-icon>
            </v-btn>
        </v-row>
    </div>
</div>
</template>



<script>
import swal from 'sweetalert'
import Repository from "../../../services/repositories/repositoryFactory";
const ListaCodigoRepository = Repository.get("ListaCodigo");

export default {
    data(){
        return {
            file: "",
            valid:true,
            form:{
                nombre:"",
                descripcion:""
            },
            rules: {} = {
                required: (value) =>
                (!!value && value !== "" && value !== undefined) || "Este campo es requerido",
                textos: (value) => 
                (value.length <= 280) || "El texto es demasiado largo",

            }
        }
    },
    props: {
        tamanoMuestral: String,
        tipo:String
    },
    methods: {
        async cargarListaCodigo(){
            const formData = new FormData();
            let validatedForm = this.$refs.registerForm.validate();
            if (validatedForm){
                try{
                    formData.append('file', this.file)
                    var idLista = await ListaCodigoRepository.crear(this.form);
                    
                    await ListaCodigoRepository.cargarListaCodigo(formData, idLista.id);
                }
                catch(err){
                    console.log(err)
                    swal("No se pudo procesar el archivo", "", "error")
                } 
            }
            
        },
        goRoute(route) {
            this.$router.push("/" + route);
        },
    },
}
</script>

<style>
@import "../../../styles/main.css";
@import "../../../styles/components/participantes.css";
</style>