import { defineStore } from 'pinia'
import authService from '../services/authService'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    isAuthenticated: false,
    loading: false,
    error: null,
  }),

  getters: {
    userRole: (state) => state.user?.role || null,
    isDoctor: (state) => state.user?.role === 'doctor',
    isNurse: (state) => state.user?.role === 'nurse',
    isPharmacist: (state) => state.user?.role === 'pharmacist',
    userName: (state) => state.user ? `${state.user.first_name} ${state.user.last_name}` : '',
  },

  actions: {
    async login(credentials) {
      this.loading = true
      this.error = null
      try {
        const data = await authService.login(credentials)
        
        // Store tokens
        localStorage.setItem('access_token', data.access)
        localStorage.setItem('refresh_token', data.refresh)
        
        // Fetch user data
        await this.fetchUser()
        
        this.isAuthenticated = true
        return true
      } catch (error) {
        this.error = error.response?.data?.detail || 'Login failed'
        throw error
      } finally {
        this.loading = false
      }
    },

    async register(userData) {
      this.loading = true
      this.error = null
      try {
        await authService.register(userData)
        // Auto login after registration
        await this.login({
          username: userData.username,
          password: userData.password,
        })
        return true
      } catch (error) {
        this.error = error.response?.data || 'Registration failed'
        throw error
      } finally {
        this.loading = false
      }
    },

    async fetchUser() {
      try {
        const userData = await authService.getCurrentUser()
        this.user = userData
        localStorage.setItem('user', JSON.stringify(userData))
      } catch (error) {
        console.error('Failed to fetch user:', error)
        this.logout()
      }
    },

    logout() {
      authService.logout()
      this.user = null
      this.isAuthenticated = false
      this.error = null
    },

    checkAuth() {
      if (authService.isAuthenticated()) {
        this.isAuthenticated = true
        const storedUser = authService.getUser()
        if (storedUser) {
          this.user = storedUser
        } else {
          this.fetchUser()
        }
      }
    },
  },
})
