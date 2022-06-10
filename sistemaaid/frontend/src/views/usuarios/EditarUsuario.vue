<template>
  <div class="col-md-12 nav-separator pt-1">
    <div class="card card-container mt-0 form-card">
      <h3 class="primary--text mx-auto mb-6 mt-0">Editar usuario</h3>
      <v-spacer></v-spacer>
  
      <v-form
        ref="registerForm"
        v-model="valid"
        lazy-validation
      >
          <v-row class="pb-0 mb-0 form-row" >
            <v-col md="3" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.first_name"
                        label="Nombre *"
                        required
                        :rules='[rules.required]'
                    ></v-text-field>
                </div>
            </v-col>
            <v-col md="3" cols="12" class="py-0">
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
            <v-col md="3" cols="12" class="py-0">
                <div class="form-group">
                    <v-text-field
                        v-model="form.email"
                        label="Correo electrónico *"
                        required
                        :rules='[rules.emailRules]'
                    ></v-text-field>
                </div>
            </v-col>
            <v-col md="3" cols="12" class="py-0">
                        <v-select
                        v-model="form.group"
                        :items="grupos"
                        label="Permisos *"
                        item-text="name"
                        item-value="id"
                        required
                        :rules='[rules.required]'
                        ></v-select>
                    </v-col>
          </v-row>
          <v-row class="pb-0 mb-0 form-row" >
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
                        :append-icon="show2 ? 'fa-eye' : 'fa-eye-slash'"
                        :type="show2 ? 'text' : 'password'"
                        @click:append="show2 = !show2"
                        :rules='[rules.required]'
                    ></v-text-field>
                </div>
            </v-col>
          </v-row>

            <v-btn @click="editarUsuario"
                :disabled="!valid"
                class="btn success btn-block w-50 my-2 mx-auto  d-none d-sm-flex">
                Registrar
            </v-btn>
            <v-btn @click="goRoute('usuarios')"
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
            show: false,
            show2: false,
            form: {
                first_name: '',
                last_name: '',
                username: '',
                password: null,
                confirmPassword: '',
                email: '',
                group: null
            },
            grupos: [],
            usuario: null,
            rules: {} = {
                required: (value) =>
                (!!value && value !== "" && value !== undefined) || "Este campo es requerido",
                emailRules: 
                (v) => /.+@.+\..+/.test(v) || "Dirección de correo inválida"           
            }
            }
    },
    computed: {
    },

    methods: {
        async editarUsuario() {
            let validatedForm = this.$refs.registerForm.validate();

            if (validatedForm){
                if (this.form.password == this.form.confirmPassword) {

                    try{
                        let res = await UsuariosRepository.agregar(this.form);
                        swal("Usuario creado satisfactoriamente", "", "success")
                        this.goRoute('usuarios')
                    }
                    catch(err){
                        console.log(err)
                        swal("El usuario no pudo ser creado", "", "error")
                    }
                } else {
                    swal("La contraseña no es la misma", "", "error")
                }
            }
        },

        goRoute(route) {
            this.$router.push("/" + route);
        },
        async getGrupos(){
            this.grupos = await UsuariosRepository.obtenerGrupos();
        },

        async getUsuario(id){
            this.usuario = await UsuariosRepository.obtenerPorId(id);
            console.log(this.usuario)
            this.form = this.usuario;
            console.log(this.usuario);
            console.log(this.form)
        },
    },
    mounted(){
        this.getGrupos();
        this.getUsuario(this.$route.params.id);
    }
}
</script>

<style>
@import "../../styles/main.css";
@import "../../styles/components/participantes.css";
</style>