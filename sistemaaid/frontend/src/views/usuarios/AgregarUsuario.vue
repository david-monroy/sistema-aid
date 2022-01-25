<template>
  <div class="col-md-12 nav-separator pt-1">
    <div class="card card-container mt-0 form-card">
      <h3 class="primary--text mx-auto mb-6 mt-0">Registrar nuevo usuario</h3>
      <v-spacer></v-spacer>
  
      <v-form
        ref="registerForm"
        v-model="valid"
        lazy-validation
      >
          <v-row class="pb-0 mb-0 form-row" >
            <v-col md="4" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.first_name"
                        label="Nombre *"
                        required
                        :rules='[rules.required]'
                    ></v-text-field>
                </div>
            </v-col>
            <v-col md="4" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.last_name"
                        label="Apellido *"
                        name="apellido"
                        required
                        :rules='[rules.required]'
                    ></v-text-field>
                </div>
            </v-col>
            <v-col md="4" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.username"
                        label="Nombre de usuario *"
                        required
                        :rules='[rules.required]'
                    ></v-text-field>
                </div>
            </v-col>
          </v-row>
          <v-row class="pb-0 mb-0 form-row" >
              <v-col md="4" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.email"
                        label="Correo electrónico *"
                        required
                        :rules='[rules.required]'
                    ></v-text-field>
                </div>
            </v-col>
            <v-col md="4" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.password"
                        label="Contraseña *"
                        name="password"
                        required
                        :append-icon="show ? 'fa-eye' : 'fa-eye-slash'"
                        :type="show ? 'text' : 'password'"
                        @click:append="show = !show"
                        :rules='[rules.required]'
                    ></v-text-field>
                </div>
            </v-col>
            <v-col md="4" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.confirmPassword"
                        label="Confirmar contraseña *"
                        name="confirmPassword"
                        required
                        :append-icon="show ? 'fa-eye' : 'fa-eye-slash'"
                        :type="show ? 'text' : 'password'"
                        @click:append="show = !show"
                        :rules='[rules.required]'
                    ></v-text-field>
                </div>
            </v-col>
          </v-row>

            <v-btn @click="registrarUsuario"
                :disabled="!valid"
                class="btn success btn-block w-50 my-2 mx-auto  d-none d-sm-flex">
                Registrar
            </v-btn>
            <v-btn @click="goRoute('/inicio')"
                class="btn-block accent1 w-25 mx-auto  mb-0 d-none d-sm-flex">
                Regresar
            </v-btn>
      </v-form>
    </div>

  </div>
</template>


<script>
import swal from 'sweetalert';
import Repository from "../../services/repositories/repositoryFactory";
const UsuariosRepository = Repository.get("Usuarios");
export default {
    data(){
        return {
            valid: false,
            form: {
                nombre: '',
                apellido: '',
                username: '',
                password: null,
                confirmPassword: '',
                email: ''
            },
            rules: {} = {
                required: (value) =>
                (!!value && value !== "" && value !== undefined) || "Este campo es requerido",
                
            },
        }
    },
    computed: {
    },

    methods: {
        async registrarUsuario() {
            let validatedForm = this.$refs.registerForm.validate();

            if (validatedForm){
                    try{
                        let res = await UsuariosRepository.agregar(this.form);
                        swal("Usuario creado satisfactoriamente", "", "success")
                        this.goRoute('inicio')
                    }
                    catch(err){
                        console.log(err)
                        swal("El usuario no pudo ser creado", "", "error")
                    }
            }
        },

        goRoute(route) {
            this.$router.push("/" + route);
        },
    },
    watch: {
      date () {
        this.fechaNacimiento = this.formatDate(this.date)
      },

    },
    mounted(){
    }
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>