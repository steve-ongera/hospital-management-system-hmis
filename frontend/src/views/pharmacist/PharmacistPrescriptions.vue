<template>
  <div class="dashboard-layout">
    <Navbar />
    <div class="main-content">
      <Sidebar />
      <div class="content">
        <div class="page-header">
          <h1>Prescriptions</h1>
        </div>

        <div class="filter-tabs">
          <button
            :class="{ active: filter === 'pending' }"
            @click="setFilter('pending')"
          >
            Pending
          </button>
          <button
            :class="{ active: filter === 'dispensed' }"
            @click="setFilter('dispensed')"
          >
            Dispensed
          </button>
          <button
            :class="{ active: filter === 'cancelled' }"
            @click="setFilter('cancelled')"
          >
            Cancelled
          </button>
        </div>

        <div v-if="pharmacyStore.loading" class="loading">Loading...</div>
        <div v-else-if="pharmacyStore.prescriptions.length === 0" class="empty-state">
          No prescriptions found
        </div>
        <div v-else class="prescriptions-list">
          <div
            v-for="prescription in pharmacyStore.prescriptions"
            :key="prescription.id"
            class="prescription-card"
          >
            <div class="prescription-header">
              <div class="prescription-info">
                <h3>{{ prescription.medication_name }}</h3>
                <p class="patient-name">Patient: {{ prescription.patient_name }}</p>
                <p class="doctor-name">Doctor: {{ prescription.doctor_name }}</p>
              </div>
              <span :class="`status-badge status-${prescription.status}`">
                {{ prescription.status }}
              </span>
            </div>

            <div class="prescription-details">
              <div class="detail-row">
                <span class="label">Dosage:</span>
                <span>{{ prescription.dosage }}</span>
              </div>
              <div class="detail-row">
                <span class="label">Frequency:</span>
                <span>{{ prescription.frequency }}</span>
              </div>
              <div class="detail-row">
                <span class="label">Duration:</span>
                <span>{{ prescription.duration }}</span>
              </div>
              <div class="detail-row">
                <span class="label">Quantity:</span>
                <span>{{ prescription.quantity }} units</span>
              </div>
              <div v-if="prescription.instructions" class="detail-row">
                <span class="label">Instructions:</span>
                <span>{{ prescription.instructions }}</span>
              </div>
            </div>

            <div v-if="prescription.status === 'pending'" class="prescription-actions">
              <button @click="dispensePrescription(prescription.id)" class="btn-dispense">
                Dispense Prescription
              </button>
            </div>

            <div v-if="prescription.status === 'dispensed'" class="dispensed-info">
              <p>Dispensed by: {{ prescription.dispensed_by_name || 'N/A' }}</p>
              <p>Dispensed at: {{ formatDate(prescription.dispensed_at) }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { usePharmacyStore } from '../../stores/pharmacy'
import Navbar from '../../components/common/Navbar.vue'
import Sidebar from '../../components/common/Sidebar.vue'

const pharmacyStore = usePharmacyStore()

const filter = ref('pending')

const setFilter = (newFilter) => {
  filter.value = newFilter
  pharmacyStore.fetchPrescriptions({ status: newFilter })
}

const dispensePrescription = async (id) => {
  if (confirm('Dispense this prescription? This will deduct stock from inventory.')) {
    try {
      await pharmacyStore.dispensePrescription(id)
      alert('Prescription dispensed successfully!')
    } catch (error) {
      const errorMessage = error.response?.data?.error || 'Failed to dispense prescription'
      alert(errorMessage)
    }
  }
}

const formatDate = (dateString) => {
  if (!dateString) return 'N/A'
  return new Date(dateString).toLocaleString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  })
}

onMounted(() => {
  pharmacyStore.fetchPrescriptions({ status: 'pending' })
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
  background: #388e3c;
  color: white;
  border-color: #388e3c;
}

.prescriptions-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.prescription-card {
  background: white;
  padding: 25px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.prescription-header {
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin-bottom: 20px;
  padding-bottom: 15px;
  border-bottom: 1px solid #eee;
}

.prescription-info h3 {
  color: #333;
  font-size: 20px;
  margin-bottom: 8px;
}

.patient-name,
.doctor-name {
  color: #666;
  font-size: 14px;
  margin: 4px 0;
}

.status-badge {
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 13px;
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

.status-cancelled {
  background: #ffebee;
  color: #d32f2f;
}

.prescription-details {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 20px;
}

.detail-row {
  display: flex;
  gap: 10px;
  color: #666;
  font-size: 14px;
}

.label {
  font-weight: 600;
  min-width: 100px;
  color: #333;
}

.prescription-actions {
  margin-top: 20px;
  padding-top: 15px;
  border-top: 1px solid #eee;
}

.btn-dispense {
  padding: 10px 24px;
  background: #388e3c;
  color: white;
  border: none;
  border-radius: 5px;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.3s;
}

.btn-dispense:hover {
  background: #2e7d32;
}

.dispensed-info {
  margin-top: 15px;
  padding-top: 15px;
  border-top: 1px solid #eee;
}

.dispensed-info p {
  color: #666;
  font-size: 13px;
  margin: 4px 0;
}

.loading,
.empty-state {
  text-align: center;
  padding: 60px;
  color: #999;
}
</style>
