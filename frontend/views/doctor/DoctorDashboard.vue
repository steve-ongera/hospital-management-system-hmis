<template>
  <div class="dashboard-layout">
    <Navbar />
    <div class="main-content">
      <Sidebar />
      <div class="content">
        <div class="page-header">
          <h1>Doctor Dashboard</h1>
          <p>Welcome back, {{ authStore.userName }}!</p>
        </div>

        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-icon">👥</div>
            <div class="stat-info">
              <h3>Total Patients</h3>
              <p class="stat-value">{{ stats.totalPatients }}</p>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon">📅</div>
            <div class="stat-info">
              <h3>Today's Appointments</h3>
              <p class="stat-value">{{ stats.todayAppointments }}</p>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon">📋</div>
            <div class="stat-info">
              <h3>Pending Appointments</h3>
              <p class="stat-value">{{ stats.pendingAppointments }}</p>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon">✅</div>
            <div class="stat-info">
              <h3>Completed Today</h3>
              <p class="stat-value">{{ stats.completedToday }}</p>
            </div>
          </div>
        </div>

        <div class="recent-section">
          <h2>Recent Appointments</h2>
          <div v-if="appointmentStore.loading" class="loading">Loading...</div>
          <div v-else-if="recentAppointments.length === 0" class="empty-state">
            No appointments found
          </div>
          <div v-else class="appointments-list">
            <div
              v-for="appointment in recentAppointments"
              :key="appointment.id"
              class="appointment-item"
            >
              <div class="appointment-info">
                <h4>{{ appointment.patient_full }}</h4>
                <p>{{ formatDate(appointment.appointment_date) }} at {{ appointment.appointment_time }}</p>
                <p class="reason">{{ appointment.reason }}</p>
              </div>
              <div class="appointment-status">
                <span :class="`status-badge status-${appointment.status}`">
                  {{ appointment.status }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useAuthStore } from '../../stores/auth'
import { useAppointmentStore } from '../../stores/appointment'
import { usePatientStore } from '../../stores/patient'
import Navbar from '../../components/common/Navbar.vue'
import Sidebar from '../../components/common/Sidebar.vue'

const authStore = useAuthStore()
const appointmentStore = useAppointmentStore()
const patientStore = usePatientStore()

const stats = ref({
  totalPatients: 0,
  todayAppointments: 0,
  pendingAppointments: 0,
  completedToday: 0,
})

const recentAppointments = computed(() => {
  return appointmentStore.appointments.slice(0, 5)
})

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  })
}

const loadDashboardData = async () => {
  try {
    await Promise.all([
      appointmentStore.fetchAppointments(),
      patientStore.fetchPatients(),
    ])

    const today = new Date().toISOString().split('T')[0]
    const appointments = appointmentStore.appointments

    stats.value = {
      totalPatients: patientStore.patients.length,
      todayAppointments: appointments.filter(a => a.appointment_date === today).length,
      pendingAppointments: appointments.filter(a => a.status === 'scheduled').length,
      completedToday: appointments.filter(
        a => a.appointment_date === today && a.status === 'completed'
      ).length,
    }
  } catch (error) {
    console.error('Failed to load dashboard data:', error)
  }
}

onMounted(() => {
  loadDashboardData()
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
  margin-bottom: 30px;
}

.page-header h1 {
  color: #333;
  font-size: 32px;
  margin-bottom: 5px;
}

.page-header p {
  color: #666;
  font-size: 16px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.stat-card {
  background: white;
  padding: 25px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  gap: 20px;
}

.stat-icon {
  font-size: 40px;
}

.stat-info h3 {
  color: #666;
  font-size: 14px;
  font-weight: 500;
  margin-bottom: 8px;
}

.stat-value {
  color: #333;
  font-size: 28px;
  font-weight: 700;
  margin: 0;
}

.recent-section {
  background: white;
  padding: 25px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.recent-section h2 {
  color: #333;
  font-size: 20px;
  margin-bottom: 20px;
}

.appointments-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.appointment-item {
  padding: 15px;
  border: 1px solid #eee;
  border-radius: 8px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: background 0.3s;
}

.appointment-item:hover {
  background: #f9f9f9;
}

.appointment-info h4 {
  color: #333;
  font-size: 16px;
  margin-bottom: 5px;
}

.appointment-info p {
  color: #666;
  font-size: 14px;
  margin: 3px 0;
}

.reason {
  color: #999;
  font-size: 13px;
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

.loading,
.empty-state {
  text-align: center;
  padding: 40px;
  color: #999;
}
</style>
