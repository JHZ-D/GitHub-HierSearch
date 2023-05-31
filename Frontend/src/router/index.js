import { createRouter, createWebHashHistory } from 'vue-router'
import SectionWaterFall from '../views/SectionWaterFall.vue'
import Home from '../views/Home.vue'
import Search from '../views/SearchPage.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/section',
    name: 'Section',
    component: SectionWaterFall
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
