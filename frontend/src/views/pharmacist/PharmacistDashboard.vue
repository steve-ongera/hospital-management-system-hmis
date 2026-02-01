<template>
  <div class="dashboard-layout">
    <Navbar />
    <div class="main-content">
      <Sidebar />
      <div class="content">
        <div class="page-header">
          <h1>Pharmacist Dashboard</h1>
          <p>Welcome back, {{ authStore.userName }}!</p>
        </div>

        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-icon">💊</div>
            <div class="stat-info">
              <h3>Total Medications</h3>
              <p class="stat-value">{{ pharmacyStore.medications.length }}</p>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon">⚠️</div>
            <div class="stat-info">
              <h3>Low Stock Items</h3>
              <p class="stat-value">{{ lowStockCount }}</p>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon">📋</div>
            <div class="stat-info">
              <h3>Pending Prescriptions</h3>
              <p class="stat-value">{{ pendingPrescriptions }}</p>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon">✅</div>
            <div class="stat-info">
              <h3>Dispensed Today</h3>
              <p class="stat-value">{{ dispensedToday }}</p>
            </div>
          </div>
        </div>

        <div class="dashboard-sections">
          <div class="section">
            <h2>Low Stock Alert</h2>
            <div v-if="lowStockMeds.length === 0" class="empty-state">
              All medications have sufficient stock
            </div>
            <div v-else class="low-stock-list">
              <div
                v-for="med in lowStockMeds"
                :key="med.id"
                class="stock-item"
              >
                <div class="med-info">
                  <h4>{{ med.name }}</h4>
                  <p>Current stock: {{ med.stock_quantity }} units</p>
                </div>
                <span class="alert-badge">Low Stock</span>
              </div>
            </div>
          </div>

          <div class="section">
            <h2>Recent Prescriptions</h2>
            <div v-if="recentPrescriptions.length === 0" class="empty-state">
              No pending prescriptions
            </div>
            <div v-else class="prescriptions-list">
              <div
                v-for="prescription in recentPrescriptions"
                :key="prescription.id"
                class="prescription-item"
              >
                <div class="prescription-info">
                  <h4>{{ prescription.medication_name }}</h4>
                  <p>Patient: {{ prescription.patient_name }}</p>
                  <p>Quantity: {{ prescription.quantity }}</p>
                </div>
                <span :class="`status-badge status-${prescription.status}`">
                  {{ prescription.status }}
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
import { usePharmacyStore } from '../../stores/pharmacy'
import Navbar from '../../components/common/Navbar.vue'
import Sidebar from '../../components/common/Sidebar.vue'

const authStore = useAuthStore()
const pharmacyStore = usePharmacyStore()

const pendingPrescriptions = ref(0)
const dispensedToday = ref(0)

const lowStockMeds = computed(() => {
  return pharmacyStore.medications.filter(m => m.stock_quantity < 10)
})

const lowStockCount = computed(() => lowStockMeds.value.length)

const recentPrescriptions = computed(() => {
  return pharmacyStore.prescriptions.slice(0, 5)
})

const loadDashboardData = async () => {
  try {
    await Promise.all([
      pharmacyStore.fetchMedications(),
      pharmacyStore.fetchPrescriptions({ status: 'pending' }),
    ])

    pendingPrescriptions.value = pharmacyStore.prescriptions.filter(
      p => p.status === 'pending'
    ).length

    dispensedToday.value = pharmacyStore.prescriptions.filter(
      p => p.status === 'dispensed' && isToday(p.dispensed_at)
    ).length
  } catch (error) {
    console.error('Failed to load dashboard data:', error)
  }
}

const isToday = (date) => {
  if (!date) return false
  const today = new Date().toISOString().split('T')[0]
  return date.split('T')[0] === today
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

.dashboard-sections {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 20px;
}

.section {
  background: white;
  padding: 25px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.section h2 {
  color: #333;
  font-size: 20px;
  margin-bottom: 20px;
}

.low-stock-list,
.prescriptions-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.stock-item,
.prescription-item {
  padding: 15px;
  border: 1px solid #eee;
  border-radius: 8px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.med-info h4,
.prescription-info h4 {
  color: #333;
  font-size: 16px;
  margin-bottom: 5px;
}

.med-info p,
.prescription-info p {
  color: #666;
  font-size: 14px;
  margin: 3px 0;
}

.alert-badge {
  padding: 6px 12px;
  background: #ffebee;
  color: #d32f2f;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 500;
}

.status-badge {
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 500;
  text-transform: capitalize;
}

.status-pending {
  background: #fff3e0;
  color: #f57c00;
}

.status-dispensed {
  background: #e8f5e9;
  color: #388e3c;
}

.empty-state {
  text-align: center;
  padding: 40px;
  color: #999;
}
</style>
