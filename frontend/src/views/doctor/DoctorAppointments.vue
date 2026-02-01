<template>
  <div class="dashboard-layout">
    <Navbar />
    <div class="main-content">
      <Sidebar />
      <div class="content">
        <div class="page-header">
          <h1>Appointments</h1>
          <button @click="showAddModal = true" class="btn-primary">
            + Schedule Appointment
          </button>
        </div>

        <div class="filter-tabs">
          <button
            :class="{ active: filter === 'all' }"
            @click="setFilter('all')"
          >
            All
          </button>
          <button
            :class="{ active: filter === 'scheduled' }"
            @click="setFilter('scheduled')"
          >
            Scheduled
          </button>
          <button
            :class="{ active: filter === 'completed' }"
            @click="setFilter('completed')"
          >
            Completed
          </button>
          <button
            :class="{ active: filter === 'cancelled' }"
            @click="setFilter('cancelled')"
          >
            Cancelled
          </button>
        </div>

        <div v-if="appointmentStore.loading" class="loading">Loading...</div>
        <div v-else-if="filteredAppointments.length === 0" class="empty-state">
          No appointments found
        </div>
        <div v-else class="appointments-list">
          <div
            v-for="appointment in filteredAppointments"
            :key="appointment.id"
            class="appointment-card"
          >
            <div class="appointment-main">
              <div class="appointment-date">
                <div class="date-day">{{ formatDay(appointment.appointment_date) }}</div>
                <div class="date-month">{{ formatMonth(appointment.appointment_date) }}</div>
              </div>
              <div class="appointment-info">
                <h3>{{ appointment.patient_full }}</h3>
                <p class="time">⏰ {{ appointment.appointment_time }}</p>
                <p class="reason">{{ appointment.reason }}</p>
              </div>
            </div>
            <div class="appointment-actions">
              <span :class="`status-badge status-${appointment.status}`">
                {{ appointment.status }}
              </span>
              <div class="action-buttons" v-if="appointment.status === 'scheduled'">
                <button @click="completeAppointment(appointment.id)" class="btn-complete">
                  Complete
                </button>
                <button @click="cancelAppointment(appointment.id)" class="btn-cancel">
                  Cancel
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Add Appointment Modal -->
        <div v-if="showAddModal" class="modal-overlay" @click="showAddModal = false">
          <div class="modal-content" @click.stop>
            <div class="modal-header">
              <h2>Schedule Appointment</h2>
              <button @click="showAddModal = false" class="btn-close">✕</button>
            </div>
            <form @submit.prevent="handleAddAppointment" class="modal-form">
              <div class="form-group">
                <label>Patient *</label>
                <select v-model="newAppointment.patient" required>
                  <option value="">Select Patient</option>
                  <option
                    v-for="patient in patientStore.patients"
                    :key="patient.id"
                    :value="patient.id"
                  >
                    {{ patient.first_name }} {{ patient.last_name }}
                  </option>
                </select>
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label>Date *</label>
                  <input v-model="newAppointment.appointment_date" type="date" required />
                </div>
                <div class="form-group">
                  <label>Time *</label>
                  <input v-model="newAppointment.appointment_time" type="time" required />
                </div>
              </div>

              <div class="form-group">
                <label>Reason *</label>
                <textarea v-model="newAppointment.reason" rows="4" required></textarea>
              </div>

              <div class="modal-actions">
                <button type="button" @click="showAddModal = false" class="btn-secondary">
                  Cancel
                </button>
                <button type="submit" class="btn-primary" :disabled="appointmentStore.loading">
                  {{ appointmentStore.loading ? 'Scheduling...' : 'Schedule' }}
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useAppointmentStore } from '../../stores/appointment'
import { usePatientStore } from '../../stores/patient'
import { useAuthStore } from '../../stores/auth'
import Navbar from '../../components/common/Navbar.vue'
import Sidebar from '../../components/common/Sidebar.vue'

const appointmentStore = useAppointmentStore()
const patientStore = usePatientStore()
const authStore = useAuthStore()

const showAddModal = ref(false)
const filter = ref('all')

const newAppointment = ref({
  patient: '',
  doctor: null,
  appointment_date: '',
  appointment_time: '',
  reason: '',
})

const filteredAppointments = computed(() => {
  if (filter.value === 'all') {
    return appointmentStore.appointments
  }
  return appointmentStore.appointments.filter(a => a.status === filter.value)
})

const setFilter = (newFilter) => {
  filter.value = newFilter
  if (newFilter !== 'all') {
    appointmentStore.fetchAppointments({ status: newFilter })
  } else {
    appointmentStore.fetchAppointments()
  }
}

const formatDay = (date) => {
  return new Date(date).getDate()
}

const formatMonth = (date) => {
  return new Date(date).toLocaleDateString('en-US', { month: 'short' })
}

const handleAddAppointment = async () => {
  try {
    newAppointment.value.doctor = authStore.user.id
    await appointmentStore.createAppointment(newAppointment.value)
    showAddModal.value = false
    resetForm()
  } catch (error) {
    alert('Failed to schedule appointment')
  }
}

const completeAppointment = async (id) => {
  if (confirm('Mark this appointment as completed?')) {
    try {
      await appointmentStore.completeAppointment(id)
    } catch (error) {
      alert('Failed to complete appointment')
    }
  }
}

const cancelAppointment = async (id) => {
  if (confirm('Cancel this appointment?')) {
    try {
      await appointmentStore.cancelAppointment(id)
    } catch (error) {
      alert('Failed to cancel appointment')
    }
  }
}

const resetForm = () => {
  newAppointment.value = {
    patient: '',
    doctor: null,
    appointment_date: '',
    appointment_time: '',
    reason: '',
  }
}

onMounted(() => {
  appointmentStore.fetchAppointments()
  patientStore.fetchPatients()
})
</script>

<style scoped>
.dashboard-layout {
  min-height: 100vh;
  background: #f5f5f5;
}

.main-content {
  display: flex;
}

.content {
  flex: 1;
  padding: 30px;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.page-header h1 {
  color: #333;
  font-size: 32px;
}

.btn-primary {
  padding: 10px 20px;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 5px;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.3s;
}

.btn-primary:hover {
  background: #5568d3;
}

.filter-tabs {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.filter-tabs button {
  padding: 10px 20px;
  background: white;
  border: 1px solid #ddd;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.3s;
}

.filter-tabs button.active {
  background: #667eea;
  color: white;
  border-color: #667eea;
}

.appointments-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.appointment-card {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.appointment-main {
  display: flex;
  gap: 20px;
  align-items: center;
}

.appointment-date {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 10px;
  padding: 15px;
  text-align: center;
  min-width: 70px;
}

.date-day {
  font-size: 24px;
  font-weight: 700;
}

.date-month {
  font-size: 12px;
  text-transform: uppercase;
}

.appointment-info h3 {
  color: #333;
  font-size: 18px;
  margin-bottom: 5px;
}

.appointment-info p {
  color: #666;
  font-size: 14px;
  margin: 3px 0;
}

.time {
  font-weight: 500;
}

.reason {
  color: #999;
}

.appointment-actions {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 10px;
}

.status-badge {
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 500;
  text-transform: capitalize;
}

.status-scheduled {
  background: #e3f2fd;
  color: #1976d2;
}

.status-completed {
  background: #e8f5e9;
  color: #388e3c;
}

.status-cancelled {
  background: #ffebee;
  color: #d32f2f;
}

.action-buttons {
  display: flex;
  gap: 8px;
}

.btn-complete,
.btn-cancel {
  padding: 6px 12px;
  border: none;
  border-radius: 5px;
  font-size: 12px;
  font-weight: 500;
  cursor: pointer;
}

.btn-complete {
  background: #4caf50;
  color: white;
}

.btn-cancel {
  background: #f44336;
  color: white;
}

.loading,
.empty-state {
  text-align: center;
  padding: 60px;
  color: #999;
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  border-radius: 10px;
  width: 90%;
  max-width: 600px;
  padding: 30px;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.modal-header h2 {
  color: #333;
  font-size: 24px;
}

.btn-close {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: #999;
}

.modal-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 15px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.form-group label {
  color: #333;
  font-weight: 500;
  font-size: 14px;
}

.form-group input,
.form-group select,
.form-group textarea {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 14px;
}

.modal-actions {
  display: flex;
  gap: 10px;
  justify-content: flex-end;
  margin-top: 20px;
}

.btn-secondary {
  padding: 10px 20px;
  background: #eee;
  color: #333;
  border: none;
  border-radius: 5px;
  font-weight: 500;
  cursor: pointer;
}
</style>
