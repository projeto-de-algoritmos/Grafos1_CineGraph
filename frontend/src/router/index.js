import Vue from 'vue'
import VueRouter from 'vue-router'
import GraphHome from '../views/GraphHome.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: GraphHome
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
