import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '@/views/Dashboard'
import ListaParticipante from '@/views/participantes/ListaParticipante'
import AgregarParticipante from '@/views/participantes/AgregarParticipante'
import EditParticipante from '@/components/Participante/EditParticipante'
import DeleteParticipante from '@/components/Participante/DeleteParticipante'
import ParticipanteManual from '@/components/Participante/ParticipanteManual'

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
      path: '/participantes',
      name: 'EditParticipante',
      component: EditParticipante
    },
    {
      path: `/participantes/:id/delete`,
      name: 'DeleteParticipante',
      component: DeleteParticipante
    },
    {
      path: `/participantes/agregar/manual`,
      name: 'ParticipanteManual',
      component: ParticipanteManual
    }
  ],
  mode: 'history'
})
