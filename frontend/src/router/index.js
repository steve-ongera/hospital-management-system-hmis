import { createRouter, createWebHistory } from 'vue-router'
import authService from '../services/authService'

// Auth views
import Login from '../views/auth/Login.vue'

// Doctor views
import DoctorDashboard from '../views/doctor/DoctorDashboard.vue'
import DoctorPatients from '../views/doctor/DoctorPatients.vue'
import DoctorAppointments from '../views/doctor/DoctorAppointments.vue'

// Nurse views
import NurseDashboard from '../views/nurse/NurseDashboard.vue'
import NursePatients from '../views/nurse/NursePatients.vue'

// Pharmacist views
import PharmacistDashboard from '../views/pharmacist/PharmacistDashboard.vue'
import PharmacistInventory from '../views/pharmacist/PharmacistInventory.vue'
import PharmacistPrescriptions from '../views/pharmacist/PharmacistPrescriptions.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login,
      meta: { requiresAuth: false },
    },
    
    // Doctor routes
    {
      path: '/doctor',
      name: 'DoctorDashboard',
      component: DoctorDashboard,
      meta: { requiresAuth: true, role: 'doctor' },
    },
    {
      path: '/doctor/patients',
      name: 'DoctorPatients',
      component: DoctorPatients,
      meta: { requiresAuth: true, role: 'doctor' },
    },
    {
      path: '/doctor/appointments',
      name: 'DoctorAppointments',
      component: DoctorAppointments,
      meta: { requiresAuth: true, role: 'doctor' },
    },
    
    // Nurse routes
    {
      path: '/nurse',
      name: 'NurseDashboard',
      component: NurseDashboard,
      meta: { requiresAuth: true, role: 'nurse' },
    },
    {
      path: '/nurse/patients',
      name: 'NursePatients',
      component: NursePatients,
      meta: { requiresAuth: true, role: 'nurse' },
    },
    
    // Pharmacist routes
    {
      path: '/pharmacist',
      name: 'PharmacistDashboard',
      component: PharmacistDashboard,
      meta: { requiresAuth: true, role: 'pharmacist' },
    },
    {
      path: '/pharmacist/inventory',
      name: 'PharmacistInventory',
      component: PharmacistInventory,
      meta: { requiresAuth: true, role: 'pharmacist' },
    },
    {
      path: '/pharmacist/prescriptions',
      name: 'PharmacistPrescriptions',
      component: PharmacistPrescriptions,
      meta: { requiresAuth: true, role: 'pharmacist' },
    },
    
    // Default redirect
    {
      path: '/',
      redirect: () => {
        const user = authService.getUser()
        if (user) {
          return `/${user.role}`
        }
        return '/login'
      },
    },
  ],
})

// Navigation guard
router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth)
  const isAuthenticated = authService.isAuthenticated()
  const user = authService.getUser()

  if (requiresAuth && !isAuthenticated) {
    next('/login')
  } else if (to.path === '/login' && isAuthenticated) {
    next(`/${user.role}`)
  } else if (requiresAuth && to.meta.role && user.role !== to.meta.role) {
    next(`/${user.role}`)
  } else {
    next()
  }
})

export default router
