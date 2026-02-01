import { defineStore } from 'pinia'
import pharmacyService from '../services/pharmacyService'

export const usePharmacyStore = defineStore('pharmacy', {
  state: () => ({
    medications: [],
    prescriptions: [],
    currentMedication: null,
    currentPrescription: null,
    loading: false,
    error: null,
  }),

  actions: {
    // Medications
    async fetchMedications(params = {}) {
      this.loading = true
      this.error = null
      try {
        const data = await pharmacyService.getMedications(params)
        this.medications = data.results || data
      } catch (error) {
        this.error = error.response?.data || 'Failed to fetch medications'
        throw error
      } finally {
        this.loading = false
      }
    },

    async createMedication(medicationData) {
      this.loading = true
      this.error = null
      try {
        const data = await pharmacyService.createMedication(medicationData)
        this.medications.unshift(data)
        return data
      } catch (error) {
        this.error = error.response?.data || 'Failed to create medication'
        throw error
      } finally {
        this.loading = false
      }
    },

    async updateMedication(id, medicationData) {
      this.loading = true
      this.error = null
      try {
        const data = await pharmacyService.updateMedication(id, medicationData)
        const index = this.medications.findIndex(m => m.id === id)
        if (index !== -1) {
          this.medications[index] = data
        }
        return data
      } catch (error) {
        this.error = error.response?.data || 'Failed to update medication'
        throw error
      } finally {
        this.loading = false
      }
    },

    async updateStock(id, quantity) {
      this.loading = true
      this.error = null
      try {
        const data = await pharmacyService.updateStock(id, quantity)
        const index = this.medications.findIndex(m => m.id === id)
        if (index !== -1) {
          this.medications[index] = data
        }
        return data
      } catch (error) {
        this.error = error.response?.data || 'Failed to update stock'
        throw error
      } finally {
        this.loading = false
      }
    },

    // Prescriptions
    async fetchPrescriptions(params = {}) {
      this.loading = true
      this.error = null
      try {
        const data = await pharmacyService.getPrescriptions(params)
        this.prescriptions = data.results || data
      } catch (error) {
        this.error = error.response?.data || 'Failed to fetch prescriptions'
        throw error
      } finally {
        this.loading = false
      }
    },

    async createPrescription(prescriptionData) {
      this.loading = true
      this.error = null
      try {
        const data = await pharmacyService.createPrescription(prescriptionData)
        this.prescriptions.unshift(data)
        return data
      } catch (error) {
        this.error = error.response?.data || 'Failed to create prescription'
        throw error
      } finally {
        this.loading = false
      }
    },

    async dispensePrescription(id) {
      this.loading = true
      this.error = null
      try {
        const data = await pharmacyService.dispensePrescription(id)
        const index = this.prescriptions.findIndex(p => p.id === id)
        if (index !== -1) {
          this.prescriptions[index] = data
        }
        return data
      } catch (error) {
        this.error = error.response?.data || 'Failed to dispense prescription'
        throw error
      } finally {
        this.loading = false
      }
    },

    async cancelPrescription(id) {
      this.loading = true
      this.error = null
      try {
        const data = await pharmacyService.cancelPrescription(id)
        const index = this.prescriptions.findIndex(p => p.id === id)
        if (index !== -1) {
          this.prescriptions[index] = data
        }
        return data
      } catch (error) {
        this.error = error.response?.data || 'Failed to cancel prescription'
        throw error
      } finally {
        this.loading = false
      }
    },
  },
})
