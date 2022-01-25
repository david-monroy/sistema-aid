import Vue from 'vue'
import Router from 'vue-router'
import jwt from '../common/jwt.service'
import store from '../store/index'

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
      meta: { requiresAuth: true },
      component: () => import("../views/Dashboard.vue")
    },
    {
      path: '/participantes',
      name: 'ListaParticipante',
      meta: { requiresAuth: true },
      component: () => import("../views/participantes/ListaParticipante.vue")
    },
    {
      path: '/participantes/:id/editar',
      name: 'EditarParticipante',
      meta: { requiresAuth: true },
      component: () => import("../components/Participante/EditarParticipante.vue")
    },
    {
      path: `/participantes/agregar`,
      name: 'ParticipanteManual',
      meta: { requiresAuth: true },
      component: () => import("../components/Participante/ParticipanteManual.vue")
    },
    {
      path: `/participantes/masivo`,
      name: 'ParticipanteMasivo',
      meta: { requiresAuth: true },
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
      meta: { requiresAuth: true },
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
      meta: { requiresAuth: true },
      component: () => import("../views/estudios/AgregarEstudio.vue")
    },
    {
      path: `/estudios/agregarEdicion`,
      name: 'AgregarEdicion',
      meta: { requiresAuth: true },
      component: () => import("../views/estudios/AgregarEdicion.vue")
    },
    {
      path: '/usuarios/agregar',
      name: 'AgregarUsuario',
      meta: { requiresAuth: true },
      component: () => import("../views/usuarios/AgregarUsuario.vue")
    },

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
      next();
      }
    };
});
});

export default router
