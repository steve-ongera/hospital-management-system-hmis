<template>
  <div class="dashboard-layout">
    <Navbar />
    <div class="main-content">
      <Sidebar />
      <div class="content">
        <div class="page-header">
          <h1>Patients</h1>
          <button @click="showAddModal = true" class="btn-primary">
            + Add Patient
          </button>
        </div>

        <div class="search-box">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search patients..."
            @input="handleSearch"
          />
        </div>

        <div v-if="patientStore.loading" class="loading">Loading...</div>
        <div v-else-if="patientStore.patients.length === 0" class="empty-state">
          No patients found
        </div>
        <div v-else class="patients-grid">
          <div
            v-for="patient in patientStore.patients"
            :key="patient.id"
            class="patient-card"
          >
            <div class="patient-header">
              <div class="patient-avatar">
                {{ patient.first_name[0] }}{{ patient.last_name[0] }}
              </div>
              <div class="patient-info">
                <h3>{{ patient.first_name }} {{ patient.last_name }}</h3>
                <p>{{ patient.age }} years • {{ patient.gender === 'M' ? 'Male' : 'Female' }}</p>
              </div>
            </div>
            <div class="patient-details">
              <p><strong>Phone:</strong> {{ patient.phone }}</p>
              <p><strong>Blood Group:</strong> {{ patient.blood_group || 'N/A' }}</p>
              <p><strong>Email:</strong> {{ patient.email || 'N/A' }}</p>
            </div>
            <button @click="addVitalSigns(patient)" class="btn-vitals">
              Record Vital Signs
            </button>
          </div>
        </div>

        <!-- Add Patient Modal (same as doctor) -->
        <div v-if="showAddModal" class="modal-overlay" @click="showAddModal = false">
          <div class="modal-content" @click.stop>
            <div class="modal-header">
              <h2>Add New Patient</h2>
              <button @click="showAddModal = false" class="btn-close">✕</button>
            </div>
            <form @submit.prevent="handleAddPatient" class="modal-form">
              <div class="form-row">
                <div class="form-group">
                  <label>First Name *</label>
                  <input v-model="newPatient.first_name" type="text" required />
                </div>
                <div class="form-group">
                  <label>Last Name *</label>
                  <input v-model="newPatient.last_name" type="text" required />
                </div>
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label>Date of Birth *</label>
                  <input v-model="newPatient.date_of_birth" type="date" required />
                </div>
                <div class="form-group">
                  <label>Gender *</label>
                  <select v-model="newPatient.gender" required>
                    <option value="">Select</option>
                    <option value="M">Male</option>
                    <option value="F">Female</option>
                    <option value="O">Other</option>
                  </select>
                </div>
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label>Phone *</label>
                  <input v-model="newPatient.phone" type="tel" required />
                </div>
                <div class="form-group">
                  <label>Blood Group</label>
                  <input v-model="newPatient.blood_group" type="text" />
                </div>
              </div>

              <div class="form-group">
                <label>Email</label>
                <input v-model="newPatient.email" type="email" />
              </div>

              <div class="form-group">
                <label>Address *</label>
                <textarea v-model="newPatient.address" rows="3" required></textarea>
              </div>

              <div class="modal-actions">
                <button type="button" @click="showAddModal = false" class="btn-secondary">
                  Cancel
                </button>
                <button type="submit" class="btn-primary" :disabled="patientStore.loading">
                  {{ patientStore.loading ? 'Adding...' : 'Add Patient' }}
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
import { ref, onMounted } from 'vue'
import { usePatientStore } from '../../stores/patient'
import Navbar from '../../components/common/Navbar.vue'
import Sidebar from '../../components/common/Sidebar.vue'

const patientStore = usePatientStore()

const showAddModal = ref(false)
const searchQuery = ref('')

const newPatient = ref({
  first_name: '',
  last_name: '',
  date_of_birth: '',
  gender: '',
  phone: '',
  email: '',
  address: '',
  blood_group: '',
})

const handleSearch = () => {
  patientStore.fetchPatients({ search: searchQuery.value })
}

const handleAddPatient = async () => {
  try {
    await patientStore.createPatient(newPatient.value)
    showAddModal.value = false
    resetForm()
  } catch (error) {
    alert('Failed to add patient')
  }
}

const addVitalSigns = (patient) => {
  alert(`Record vital signs for ${patient.first_name} ${patient.last_name}`)
}

const resetForm = () => {
  newPatient.value = {
    first_name: '',
    last_name: '',
    date_of_birth: '',
    gender: '',
    phone: '',
    email: '',
    address: '',
    blood_group: '',
  }
}

onMounted(() => {
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
  background: #7b1fa2;
  color: white;
  border: none;
  border-radius: 5px;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.3s;
}

.btn-primary:hover {
  background: #6a1b9a;
}

.search-box {
  margin-bottom: 20px;
}

.search-box input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 14px;
}

.patients-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 20px;
}

.patient-card {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.patient-header {
  display: flex;
  gap: 15px;
  margin-bottom: 15px;
}

.patient-avatar {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: linear-gradient(135deg, #7b1fa2 0%, #9c27b0 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  font-weight: 600;
}

.patient-info h3 {
  color: #333;
  font-size: 18px;
  margin-bottom: 5px;
}

.patient-info p {
  color: #666;
  font-size: 14px;
}

.patient-details p {
  color: #666;
  font-size: 14px;
  margin: 8px 0;
}

.btn-vitals {
  width: 100%;
  margin-top: 15px;
  padding: 10px;
  background: #7b1fa2;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background 0.3s;
}

.btn-vitals:hover {
  background: #6a1b9a;
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
  max-height: 90vh;
  overflow-y: auto;
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
