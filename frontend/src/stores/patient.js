import { defineStore } from 'pinia'
import patientService from '../services/patientService'

export const usePatientStore = defineStore('patient', {
  state: () => ({
    patients: [],
    currentPatient: null,
    loading: false,
    error: null,
  }),

  actions: {
    async fetchPatients(params = {}) {
      this.loading = true
      this.error = null
      try {
        const data = await patientService.getPatients(params)
        this.patients = data.results || data
      } catch (error) {
        this.error = error.response?.data || 'Failed to fetch patients'
        throw error
      } finally {
        this.loading = false
      }
    },

    async fetchPatient(id) {
      this.loading = true
      this.error = null
      try {
        const data = await patientService.getPatient(id)
        this.currentPatient = data
        return data
      } catch (error) {
        this.error = error.response?.data || 'Failed to fetch patient'
        throw error
      } finally {
        this.loading = false
      }
    },

    async createPatient(patientData) {
      this.loading = true
      this.error = null
      try {
        const data = await patientService.createPatient(patientData)
        this.patients.unshift(data)
        return data
      } catch (error) {
        this.error = error.response?.data || 'Failed to create patient'
        throw error
      } finally {
        this.loading = false
      }
    },

    async updatePatient(id, patientData) {
      this.loading = true
      this.error = null
      try {
        const data = await patientService.updatePatient(id, patientData)
        const index = this.patients.findIndex(p => p.id === id)
        if (index !== -1) {
          this.patients[index] = data
        }
        if (this.currentPatient?.id === id) {
          this.currentPatient = data
        }
        return data
      } catch (error) {
        this.error = error.response?.data || 'Failed to update patient'
        throw error
      } finally {
        this.loading = false
      }
    },

    async deletePatient(id) {
      this.loading = true
      this.error = null
      try {
        await patientService.deletePatient(id)
        this.patients = this.patients.filter(p => p.id !== id)
        if (this.currentPatient?.id === id) {
          this.currentPatient = null
        }
      } catch (error) {
        this.error = error.response?.data || 'Failed to delete patient'
        throw error
      } finally {
        this.loading = false
      }
    },
  },
})
