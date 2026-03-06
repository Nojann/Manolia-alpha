import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      alias: '/app',
      name: 'app',
      component: () => import('@/views/ExperimentView.vue'),
    },
    {
      path: '/login',
      alias: '/login',
      name: 'login',
      component: () => import('@/views/AuthView.vue'),
    }
  ],
})

export default router
