<template>
  <div class="dashboard-layout">
    <Navbar />
    <div class="main-content">
      <Sidebar />
      <div class="content">
        <div class="page-header">
          <h1>Nurse Dashboard</h1>
          <p>Welcome back, {{ authStore.userName }}!</p>
        </div>

        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-icon">👥</div>
            <div class="stat-info">
              <h3>Total Patients</h3>
              <p class="stat-value">{{ patientStore.patients.length }}</p>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon">📋</div>
            <div class="stat-info">
              <h3>Medical Records</h3>
              <p class="stat-value">{{ medicalRecords.length }}</p>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon">📅</div>
            <div class="stat-info">
              <h3>Appointments Today</h3>
              <p class="stat-value">{{ todayAppointments }}</p>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon">🩺</div>
            <div class="stat-info">
              <h3>Active Cases</h3>
              <p class="stat-value">{{ activeCases }}</p>
            </div>
          </div>
        </div>

        <div class="quick-actions">
          <h2>Quick Actions</h2>
          <div class="action-cards">
            <router-link to="/nurse/patients" class="action-card">
              <div class="action-icon">👥</div>
              <h3>View Patients</h3>
              <p>Manage patient records</p>
            </router-link>

            <div class="action-card" @click="showAddRecordModal = true">
              <div class="action-icon">📝</div>
              <h3>Add Medical Record</h3>
              <p>Record patient vitals</p>
            </div>

            <div class="action-card">
              <div class="action-icon">🔔</div>
              <h3>View Alerts</h3>
              <p>Check patient alerts</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '../../stores/auth'
import { usePatientStore } from '../../stores/patient'
import Navbar from '../../components/common/Navbar.vue'
import Sidebar from '../../components/common/Sidebar.vue'

const authStore = useAuthStore()
const patientStore = usePatientStore()

const medicalRecords = ref([])
const todayAppointments = ref(0)
const activeCases = ref(0)
const showAddRecordModal = ref(false)

onMounted(() => {
  patientStore.fetchPatients()
  // Mock data for demo
  medicalRecords.value = []
  todayAppointments.value = 5
  activeCases.value = 12
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

.quick-actions {
  background: white;
  padding: 25px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.quick-actions h2 {
  color: #333;
  font-size: 20px;
  margin-bottom: 20px;
}

.action-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}

.action-card {
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  padding: 30px;
  border-radius: 10px;
  text-align: center;
  cursor: pointer;
  transition: transform 0.3s;
  text-decoration: none;
}

.action-card:hover {
  transform: translateY(-5px);
}

.action-icon {
  font-size: 48px;
  margin-bottom: 15px;
}

.action-card h3 {
  color: #333;
  font-size: 18px;
  margin-bottom: 8px;
}

.action-card p {
  color: #666;
  font-size: 14px;
}
</style>
