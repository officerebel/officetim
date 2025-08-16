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
            path: '/blog/:id',
            name: 'blog-detail',
            component: () => import('../views/BlogDetailView.vue')
          },


          {
            path: '/contact',
            name: 'contact',
            component: () => import('../views/ContactView.vue')
          },

          {
            path: '/contact/thank-you',
            name: 'contact-thank-you',
            component: () => import('../views/ThankYouView.vue')
          },

          {
            path: '/detailed',
            name: 'detailed',
            component: () => import('../views/DetailedView.vue')
          },

          // End routes


        ]
      },
    ]
  })  

export default router
//