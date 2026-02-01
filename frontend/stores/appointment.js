import { defineStore } from 'pinia'
import appointmentService from '../services/appointmentService'

export const useAppointmentStore = defineStore('appointment', {
  state: () => ({
    appointments: [],
    currentAppointment: null,
    loading: false,
    error: null,
  }),

  actions: {
    async fetchAppointments(params = {}) {
      this.loading = true
      this.error = null
      try {
        const data = await appointmentService.getAppointments(params)
        this.appointments = data.results || data
      } catch (error) {
        this.error = error.response?.data || 'Failed to fetch appointments'
        throw error
      } finally {
        this.loading = false
      }
    },

    async fetchAppointment(id) {
      this.loading = true
      this.error = null
      try {
        const data = await appointmentService.getAppointment(id)
        this.currentAppointment = data
        return data
      } catch (error) {
        this.error = error.response?.data || 'Failed to fetch appointment'
        throw error
      } finally {
        this.loading = false
      }
    },

    async createAppointment(appointmentData) {
      this.loading = true
      this.error = null
      try {
        const data = await appointmentService.createAppointment(appointmentData)
        this.appointments.unshift(data)
        return data
      } catch (error) {
        this.error = error.response?.data || 'Failed to create appointment'
        throw error
      } finally {
        this.loading = false
      }
    },

    async updateAppointment(id, appointmentData) {
      this.loading = true
      this.error = null
      try {
        const data = await appointmentService.updateAppointment(id, appointmentData)
        const index = this.appointments.findIndex(a => a.id === id)
        if (index !== -1) {
          this.appointments[index] = data
        }
        return data
      } catch (error) {
        this.error = error.response?.data || 'Failed to update appointment'
        throw error
      } finally {
        this.loading = false
      }
    },

    async deleteAppointment(id) {
      this.loading = true
      this.error = null
      try {
        await appointmentService.deleteAppointment(id)
        this.appointments = this.appointments.filter(a => a.id !== id)
      } catch (error) {
        this.error = error.response?.data || 'Failed to delete appointment'
        throw error
      } finally {
        this.loading = false
      }
    },

    async completeAppointment(id) {
      this.loading = true
      this.error = null
      try {
        const data = await appointmentService.completeAppointment(id)
        const index = this.appointments.findIndex(a => a.id === id)
        if (index !== -1) {
          this.appointments[index] = data
        }
        return data
      } catch (error) {
        this.error = error.response?.data || 'Failed to complete appointment'
        throw error
      } finally {
        this.loading = false
      }
    },

    async cancelAppointment(id) {
      this.loading = true
      this.error = null
      try {
        const data = await appointmentService.cancelAppointment(id)
        const index = this.appointments.findIndex(a => a.id === id)
        if (index !== -1) {
          this.appointments[index] = data
        }
        return data
      } catch (error) {
        this.error = error.response?.data || 'Failed to cancel appointment'
        throw error
      } finally {
        this.loading = false
      }
    },
  },
})
