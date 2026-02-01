import api from './api'

export default {
  async getMedicalRecords(params = {}) {
    const response = await api.get('/medical-records/', { params })
    return response.data
  },

  async getMedicalRecord(id) {
    const response = await api.get(`/medical-records/${id}/`)
    return response.data
  },

  async createMedicalRecord(data) {
    const response = await api.post('/medical-records/', data)
    return response.data
  },

  async updateMedicalRecord(id, data) {
    const response = await api.put(`/medical-records/${id}/`, data)
    return response.data
  },

  async deleteMedicalRecord(id) {
    const response = await api.delete(`/medical-records/${id}/`)
    return response.data
  },
}
