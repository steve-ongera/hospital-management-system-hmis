import api from './api'

export default {
  async login(credentials) {
    const response = await api.post('/auth/login/', credentials)
    return response.data
  },

  async register(userData) {
    const response = await api.post('/users/', userData)
    return response.data
  },

  async getCurrentUser() {
    const response = await api.get('/users/me/')
    return response.data
  },

  logout() {
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    localStorage.removeItem('user')
  },

  isAuthenticated() {
    return !!localStorage.getItem('access_token')
  },

  getUser() {
    const user = localStorage.getItem('user')
    return user ? JSON.parse(user) : null
  },
}
