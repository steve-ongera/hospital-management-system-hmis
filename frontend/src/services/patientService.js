import api from './api'

export default {
  async getPatients(params = {}) {
    const response = await api.get('/patients/', { params })
    return response.data
  },

  async getPatient(id) {
    const response = await api.get(`/patients/${id}/`)
    return response.data
  },

  async createPatient(data) {
    const response = await api.post('/patients/', data)
    return response.data
  },

  async updatePatient(id, data) {
    const response = await api.put(`/patients/${id}/`, data)
    return response.data
  },

  async deletePatient(id) {
    const response = await api.delete(`/patients/${id}/`)
    return response.data
  },

  async getPatientAppointments(id) {
    const response = await api.get(`/patients/${id}/appointments/`)
    return response.data
  },

  async getPatientMedicalRecords(id) {
    const response = await api.get(`/patients/${id}/medical_records/`)
    return response.data
  },

  async getPatientPrescriptions(id) {
    const response = await api.get(`/patients/${id}/prescriptions/`)
    return response.data
  },
}
