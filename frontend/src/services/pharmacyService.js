import api from './api'

export default {
  // Medications
  async getMedications(params = {}) {
    const response = await api.get('/medications/', { params })
    return response.data
  },

  async getMedication(id) {
    const response = await api.get(`/medications/${id}/`)
    return response.data
  },

  async createMedication(data) {
    const response = await api.post('/medications/', data)
    return response.data
  },

  async updateMedication(id, data) {
    const response = await api.put(`/medications/${id}/`, data)
    return response.data
  },

  async deleteMedication(id) {
    const response = await api.delete(`/medications/${id}/`)
    return response.data
  },

  async updateStock(id, quantity) {
    const response = await api.post(`/medications/${id}/update_stock/`, { quantity })
    return response.data
  },

  // Prescriptions
  async getPrescriptions(params = {}) {
    const response = await api.get('/prescriptions/', { params })
    return response.data
  },

  async getPrescription(id) {
    const response = await api.get(`/prescriptions/${id}/`)
    return response.data
  },

  async createPrescription(data) {
    const response = await api.post('/prescriptions/', data)
    return response.data
  },

  async updatePrescription(id, data) {
    const response = await api.put(`/prescriptions/${id}/`, data)
    return response.data
  },

  async deletePrescription(id) {
    const response = await api.delete(`/prescriptions/${id}/`)
    return response.data
  },

  async dispensePrescription(id) {
    const response = await api.post(`/prescriptions/${id}/dispense/`)
    return response.data
  },

  async cancelPrescription(id) {
    const response = await api.post(`/prescriptions/${id}/cancel/`)
    return response.data
  },
}
