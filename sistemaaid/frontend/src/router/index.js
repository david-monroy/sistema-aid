import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '@/views/Dashboard'
import ListaParticipante from '@/views/participantes/ListaParticipante'
import AgregarParticipante from '@/views/participantes/AgregarParticipante'
import EditarParticipante from '@/components/Participante/EditarParticipante'
import EditarParticipanteMasivo from '@/components/Participante/EditarParticipanteMasivo'
import ParticipanteManual from '@/components/Participante/ParticipanteManual'
import ParticipanteMasivo from '@/components/Participante/ParticipanteMasivo'
import ListaEstudios from '@/views/estudios/ListaEstudios'
import MenuAgregarEstudio from '@/views/estudios/MenuAgregarEstudio'
import AgregarEstudio from '@/views/estudios/AgregarEstudio'
import AgregarEdicion from '@/views/estudios/AgregarEdicion'
import Login from '@/views/Login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
    path: '/Home',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/participantes',
      name: 'ListaParticipante',
      component: ListaParticipante
    },
    {
      path: '/participantes/agregar',
      name: 'AgregarParticipante',
      component: AgregarParticipante
    },
    {
      path: '/participantes/:id/editar',
      name: 'EditarParticipante',
      component: EditarParticipante
    },
    {
      path: `/participantes/agregar/manual`,
      name: 'ParticipanteManual',
      component: ParticipanteManual
    },
    {
      path: `/participantes/agregar/masivo`,
      name: 'ParticipanteMasivo',
      component: ParticipanteMasivo
    },
    {
      path: `/participantes/editar/masivo`,
      name: 'EditarParticipanteMasivo',
      component: EditarParticipanteMasivo
    },
    {
      path: '/estudios',
      name: 'ListaEstudios',
      component: ListaEstudios
    },
    {
      path: `/estudios/agregar`,
      name: 'MenuAgregarEstudio',
      component: MenuAgregarEstudio
    },
    {
      path: `/estudios/agregarEstudio`,
      name: 'AgregarEstudio',
      component: AgregarEstudio
    },
    {
      path: `/estudios/agregarEdicion`,
      name: 'AgregarEdicion',
      component: AgregarEdicion
    },

  ],
  mode: 'history'
})
