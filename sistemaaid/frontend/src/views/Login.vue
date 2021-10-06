<template>
    <div class="col-md-12 nav-separator pt-1">
      <div class="card card-container mt-0 form-card">
        <v-form
        ref="registerForm"
        v-model="valid"
        lazy-validation
        >
          <v-row class="pb-0 mb-0 form-row" >
            <v-col md="12" cols="12" class="py-0">
              <div class="form-group">
                <v-text-field
                  v-model="form.username"
                  label="Nombre de Usuario"
                  required
                  :rules='[rules.required]'
                ></v-text-field>
              </div>
            </v-col>
          </v-row>

          <v-row class="pb-0 mb-0 form-row" >
            <v-col md="12" cols="12" class="py-0">
              <div class="form-group">
                <v-text-field
                  v-model="form.password"
                  label="Contraseña"
                  required
                  :rules='[rules.required]'
                ></v-text-field>
              </div>
            </v-col>
          </v-row>

          <v-btn @click="login()"
                class="btn-block accent1 w-25 mx-auto  mb-0 d-none d-sm-flex">
                Iniciar Sesión
            </v-btn>
        </v-form>
      </div>
    </div>
</template>

<script>
import Repository from "../services/repositories/repositoryFactory";
const AutorizacionRepository = Repository.get("Autorizacion");
export default {
  data() {
      return {
          form:{
            username:'',
            password:''
          },
          valid:true,
          rules: {} = {
                required: (value) =>
                (!!value && value !== "" && value !== undefined) || "Este campo es requerido",
                emailRules: 
                (v) => /.+@.+\..+/.test(v) || "Dirección de correo inválida",       
            },
      }
    },
  methods:{
    async login() {
      
      this.$store.dispatch("logout");

      let validatedForm = this.$refs.registerForm.validate();
      if (validatedForm){
          await this.$store.dispatch("users/authorize", this.form);
          this.error = this.$store.getters["users/getError"].error;
          if (this.error !== "") console.log('error');
          else this.$router.push("/Home");
      }
    },
  }
}
</script>

<style>
@import "../styles/main.css";
@import "../styles/forms.css";
</style>