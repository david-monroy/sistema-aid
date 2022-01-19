<template>
  <div class="d-flex login-background">
    <div class="col-md-12 pt-1">
      <div class="login-card login-card-container rounded-card">
        <div class="w-100 d-flex mb-8" style="justify-content: center">
          <img src="../assets/logo_AID.png" alt="Logo Controlca" class="login-logo ma-0">
        </div>

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

          <v-row class="pb-0 mb-0 form-row" style="margin-top: -10px !important">
            <v-col md="12" cols="12" class="py-0">
              <div class="form-group">
                <v-text-field
                  v-model="form.password"
                  label="Contraseña"
                  required
                  :append-icon="show ? 'fa-eye' : 'fa-eye-slash'"
                  :type="show ? 'text' : 'password'"
                  @click:append="show = !show"
                  :rules='[rules.required]'
                ></v-text-field>
              </div>
            </v-col>
          </v-row>

          <v-btn @click="login()"
                class="btn-block success w-75 mx-auto  mb-0 d-none d-sm-flex"
                :disabled="loading">
                Iniciar Sesión
            </v-btn>
        </v-form>
      </div>
    </div>
  </div>
</template>

<script>
import swal from 'sweetalert'
export default {
  data() {
      return {
          form:{
            username:'',
            password:''
          },
          loading: false,
          show: false,
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
          if (this.error !== "") swal("Las credenciales son inválidas", "", "error");
          else this.$router.push("/inicio");
      }
    },
  }
}
</script>

<style>
@import "../styles/main.css";
@import "../styles/login.css";
</style>