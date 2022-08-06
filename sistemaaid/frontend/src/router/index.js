import Vue from 'vue'
import Router from 'vue-router'
import jwt from '../common/jwt.service'
import store from '../store/index'
import swal from 'sweetalert';

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/login',
      name: 'Login',
      component: () => import("../views/Login.vue"),
      meta: {
        hideForAuth: true
      }
    },
    {
      path: '/inicio',
      name: 'Dashboard',
      meta: { requiresAuth: true, permission: "auth | user | log in" },
      component: () => import("../views/Dashboard.vue")
    },
    {
      path: '/participantes',
      name: 'ListaParticipante',
      meta: { requiresAuth: true, permission: 'backend | participante | Can view participante'},
      component: () => import("../views/participantes/ListaParticipante.vue")
    },
    {
      path: '/participantes/:id/editar',
      name: 'EditarParticipante',
      meta: { requiresAuth: true, permission: 'backend | participante | Can change participante' },
      component: () => import("../components/Participante/EditarParticipante.vue")
    },
    {
      path: `/participantes/agregar`,
      name: 'ParticipanteManual',
      meta: { requiresAuth: true, permission: "backend | participante | Can add participante" },
      component: () => import("../components/Participante/ParticipanteManual.vue")
    },
    {
      path: `/participantes/masivo`,
      name: 'ParticipanteMasivo',
      meta: { requiresAuth: true, permission: "backend | participante | Can add participante" },
      component: () => import("../components/Participante/ParticipanteMasivo.vue")
    },
    {
      path: `/participantes/editar/masivo`,
      name: 'EditarParticipanteMasivo',
      meta: { requiresAuth: true },
      component: () => import("../components/Participante/EditarParticipanteMasivo.vue")
    },
    {
      path: '/estudios',
      name: 'ListaEstudios',
      meta: { requiresAuth: true, permission: "backend | estudio | Can view estudio" },
      component: () => import("../views/estudios/ListaEstudios.vue")
    },
    {
      path: `/estudios/agregar`,
      name: 'MenuAgregarEstudio',
      meta: { requiresAuth: true },
      component: () => import("../views/estudios/MenuAgregarEstudio.vue")
    },
    {
      path: `/estudios/agregarEstudio`,
      name: 'AgregarEstudio',
      meta: { requiresAuth: true, permission: "backend | estudio | Can add estudio" },
      component: () => import("../views/estudios/AgregarEstudio.vue")
    },
    {
      path: `/estudios/agregarEdicion`,
      name: 'AgregarEdicion',
      meta: { requiresAuth: true, permission: "backend | edicion | Can add edicion" },
      component: () => import("../views/estudios/AgregarEdicion.vue")
    },
    {
      path: '/configuracion',
      name: 'Configuracion',
      meta: { requiresAuth: true, permission: "auth | user | configuracion" },
      component: () => import("../views/ConfiguracionDashboard.vue")
    },
    {
      path: '/patrones',
      name: 'Patrones',
      meta: { requiresAuth: true },
      component: () => import("../views/estudios/Patrones.vue")
    },
    {
      path: '/usuarios',
      name: 'ListaUsuario',
      meta: { requiresAuth: true, permission: "auth | user | Can view user" },
      component: () => import("../views/usuarios/ListaUsuario.vue")
    },
    {
      path: '/usuarios/agregar',
      name: 'AgregarUsuario',
      meta: { requiresAuth: true, permission: "auth | user | Can add user" },
      component: () => import("../views/usuarios/AgregarUsuario.vue")
    },
    {
      path: '/usuarios/:id/editar',
      name: 'EditarUsuario',
      meta: { requiresAuth: true, permission: "auth | user | Can change user" },
      component: () => import("../views/usuarios/EditarUsuario.vue")
    },
    {
      path: `/estudios/agregarListaCodigo`,
      name: 'AgregarListaCodigo',
      meta: { requiresAuth: true, permission: "backend | lista codigo | Can add lista codigo" },
      component: () => import("../views/estudios/listasDeCodigo/AgregarListaCodigo.vue")
    },
    {
      path: `/ListasCodigos`,
      name: 'ListasDeCodigos',
      meta: { requiresAuth: true, permission: "backend | lista codigo | Can view lista codigo" },
      component: () => import("../views/estudios/listasDeCodigo/ListasDeCodigos.vue")
    },
    {
      path: `/ediciones/AgregarEncuestas/:id`,
      name: 'AgregarEncuestas',
      meta: { requiresAuth: true, permission: "backend | encuesta | Can add encuesta" },
      component: () => import("../views/estudios/AgregarEncuestas.vue")
    },
    {
      path: `/ediciones/:id`,
      name: 'ConsultarEdicion',
      meta: { requiresAuth: true, permission: "backend | edicion | Can view edicion" },
      component: () => import("../views/estudios/ConsultarEdicion.vue")
    }


  ],
  mode: 'history',

})

router.beforeEach((to, from, next) => {
  to.matched.some((route) => {
    if (!jwt.isTokenValid()) {
      store.dispatch("logout");
      if (route.meta.requiresAuth) {
        jwt.destroyToken();
        next({ name: "Login" });
      } else {
        next();
        }  
    } else {
      if (route.meta.hideForAuth) {
        next({ name: "Dashboard" });
      } else {
        if (store.getters["users/getPermisos"].includes(route.meta.permission)){
          next();
        }
        else {
          swal("No tiene permisos para ingresar a esta dirección", "", "error")
        }
      }
    };
    });
});

export default router
