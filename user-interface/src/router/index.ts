import { createRouter, createWebHistory } from 'vue-router'
import { isAuthenticated } from '@/services/apiAxios'

const pagesWithoutGuard = ['login', 'app', 'register']
 
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      alias: '/app',
      name: 'app',
      component: () => import('@/views/WelcomeView.vue'),
    },
    {
      path: '/experiment',
      alias: '/experiment',
      name: 'experiment',
      component: () => import('@/views/ExperimentView.vue'),
    },
    {
      path: '/login',
      alias: '/login',
      name: 'login',
      component: () => import('@/views/LoginView.vue'),
    },
    {
      path: '/register',
      alias: '/register',
      name: 'register',
      component: () => import('@/views/RegisterView.vue'),
    }
  ],
})

router.beforeEach(async (to, from) => {
  const isAuth = await isAuthenticated()
  if (!isAuth && pagesWithoutGuard.includes(to.name!.toString())) {
    return { name: 'login' }
  }
})

export default router
