import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import IndexLayout from '@/views/Layout/IndexLayout.vue'


  const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
      {
        path: '/',
        name: 'index',
        component: IndexLayout,
        children: [
          {
            path: '/',
            name: 'home |',
            component: HomeView
          },
          {
            path: '/about',
            name: 'about',
            component: () => import('../views/AboutView.vue')
          },
          {
            path: '/blog',
            name: 'blog',
            component: () => import('../views/BlogView.vue')
          },


          {
            path: '/contact',
            name: 'contact',
            component: () => import('../views/ContactView.vue')
          },

          {
            path: '/detailed',
            name: 'detailed',
            component: () => import('../views/DetailedView.vue')
          },

          // {
          //   path: '/blog/:id',
          //   name: 'Blog Detailed',
          //   component: () => import('../views/BlogDetailView.vue')
          // },


        ]
      },
    ]
  })  

export default router
//