import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import ListParticipante from '@/components/Participante/ListParticipante'
import EditParticipante from '@/components/Participante/EditParticipante'
import DeleteParticipante from '@/components/Participante/DeleteParticipante'
import NewParticipante from '@/components/Participante/NewParticipante'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/participantes',
      name: 'ListParticipante',
      component: ListParticipante
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
      path: `/participantes/new`,
      name: 'NewParticipante',
      component: NewParticipante
    }
  ],
  mode: 'history'
})
