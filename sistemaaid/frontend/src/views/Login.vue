<template>
    <div class="col-md-12 nav-separator pt-1">
      <div class="card card-container mt-0 form-card">
        <v-form
            
        >
          <v-row class="pb-0 mb-0 form-row" >
            <v-col md="12" cols="12" class="py-0">
              <div class="form-group">
                <v-text-field
                  v-model="form.correo"
                  label="Correo electrónico"
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
                  v-model="form.contraseña"
                  label="Contraseña"
                  required
                  :rules='[rules.required]'
                ></v-text-field>
              </div>
            </v-col>
          </v-row>

          <v-btn @click="Login()"
                class="btn-block accent1 w-25 mx-auto  mb-0 d-none d-sm-flex">
                Iniciar Sesión
            </v-btn>
        </v-form>
      </div>
    </div>
</template>

<script>
export default {
  data() {
      return {
          form:{
            correo:'',
            contraseña:''
          },
          rules: {} = {
                required: (value) =>
                (!!value && value !== "" && value !== undefined) || "Este campo es requerido",
                emailRules: 
                (v) => /.+@.+\..+/.test(v) || "Dirección de correo inválida",       
            },
      }
    },
}
</script>

<style>
@import "../styles/main.css";
@import "../styles/forms.css";
</style>