import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '@/views/Dashboard'
import ListaParticipante from '@/views/participantes/ListaParticipante'
import AgregarParticipante from '@/views/participantes/AgregarParticipante'
import EditarParticipante from '@/components/Participante/EditarParticipante'
import ParticipanteManual from '@/components/Participante/ParticipanteManual'
import ParticipanteMasivo from '@/components/Participante/ParticipanteMasivo'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
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
    }
  ],
  mode: 'history'
})
