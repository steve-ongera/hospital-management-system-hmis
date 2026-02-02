<template>
  <div class="dashboard-layout">
    <Navbar />
    <div class="main-content">
      <Sidebar />
      <div class="content">
        <div class="page-header">
          <div class="header-left">
            <h1 class="page-title">Patients</h1>
            <p class="page-subtitle">Manage and view all patient records</p>
          </div>
          <button @click="showAddModal = true" class="btn-primary">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="12" y1="5" x2="12" y2="19"/>
              <line x1="5" y1="12" x2="19" y2="12"/>
            </svg>
            Add Patient
          </button>
        </div>

        <div class="table-container">
          <div class="table-header">
            <div class="search-box">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="11" cy="11" r="8"/>
                <path d="m21 21-4.35-4.35"/>
              </svg>
              <input
                v-model="searchQuery"
                type="text"
                placeholder="Search by name, phone, or email..."
                @input="handleSearch"
              />
            </div>
            <div class="table-actions">
              <button class="btn-filter">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/>
                </svg>
                Filter
              </button>
              <button class="btn-export">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                  <polyline points="7 10 12 15 17 10"/>
                  <line x1="12" y1="15" x2="12" y2="3"/>
                </svg>
                Export
              </button>
            </div>
          </div>

          <div v-if="patientStore.loading" class="loading-state">
            <div class="spinner"></div>
            <p>Loading patients...</p>
          </div>

          <div v-else-if="patientStore.patients.length === 0" class="empty-state">
            <div class="empty-icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                <circle cx="9" cy="7" r="4"/>
                <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
                <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
              </svg>
            </div>
            <h3>No patients found</h3>
            <p>Get started by adding your first patient</p>
            <button @click="showAddModal = true" class="btn-primary">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="12" y1="5" x2="12" y2="19"/>
                <line x1="5" y1="12" x2="19" y2="12"/>
              </svg>
              Add First Patient
            </button>
          </div>

          <div v-else class="table-wrapper">
            <table class="patients-table">
              <thead>
                <tr>
                  <th>
                    <input type="checkbox" class="checkbox" />
                  </th>
                  <th>Patient Name</th>
                  <th>Age</th>
                  <th>Gender</th>
                  <th>Phone</th>
                  <th>Email</th>
                  <th>Blood Group</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="patient in patientStore.patients"
                  :key="patient.id"
                  class="table-row"
                >
                  <td>
                    <input type="checkbox" class="checkbox" />
                  </td>
                  <td>
                    <div class="patient-cell">
                      <div class="patient-avatar">
                        {{ patient.first_name[0] }}{{ patient.last_name[0] }}
                      </div>
                      <div class="patient-name-info">
                        <span class="patient-name">{{ patient.first_name }} {{ patient.last_name }}</span>
                        <span class="patient-id">ID: #{{ patient.id }}</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <span class="cell-text">{{ patient.age }} yrs</span>
                  </td>
                  <td>
                    <span class="gender-badge" :class="`gender-${patient.gender.toLowerCase()}`">
                      <svg v-if="patient.gender === 'M'" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="10" cy="14" r="7"/>
                        <line x1="16.24" y1="7.76" x2="21.5" y2="2.5"/>
                        <line x1="21.5" y1="2.5" x2="21.5" y2="8.5"/>
                        <line x1="21.5" y1="2.5" x2="15.5" y2="2.5"/>
                      </svg>
                      <svg v-else-if="patient.gender === 'F'" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="8" r="7"/>
                        <line x1="12" y1="15" x2="12" y2="23"/>
                        <line x1="8" y1="19" x2="16" y2="19"/>
                      </svg>
                      <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10"/>
                      </svg>
                      {{ patient.gender === 'M' ? 'Male' : patient.gender === 'F' ? 'Female' : 'Other' }}
                    </span>
                  </td>
                  <td>
                    <div class="contact-info">
                      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
                      </svg>
                      <span>{{ patient.phone }}</span>
                    </div>
                  </td>
                  <td>
                    <div class="contact-info" v-if="patient.email">
                      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                        <polyline points="22,6 12,13 2,6"/>
                      </svg>
                      <span>{{ patient.email }}</span>
                    </div>
                    <span v-else class="text-muted">N/A</span>
                  </td>
                  <td>
                    <span class="blood-badge" v-if="patient.blood_group">
                      {{ patient.blood_group }}
                    </span>
                    <span v-else class="text-muted">N/A</span>
                  </td>
                  <td>
                    <div class="action-buttons">
                      <button @click="viewPatient(patient)" class="btn-action btn-view" title="View Details">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                          <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
                          <circle cx="12" cy="12" r="3"/>
                        </svg>
                      </button>
                      <button class="btn-action btn-edit" title="Edit Patient">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                          <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/>
                          <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>
                        </svg>
                      </button>
                      <button class="btn-action btn-delete" title="Delete Patient">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                          <polyline points="3 6 5 6 21 6"/>
                          <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>
                        </svg>
                      </button>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="table-footer" v-if="!patientStore.loading && patientStore.patients.length > 0">
            <div class="footer-info">
              Showing <strong>{{ patientStore.patients.length }}</strong> of <strong>{{ patientStore.patients.length }}</strong> patients
            </div>
            <div class="pagination">
              <button class="btn-pagination" disabled>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="15 18 9 12 15 6"/>
                </svg>
                Previous
              </button>
              <div class="pagination-numbers">
                <button class="pagination-number active">1</button>
              </div>
              <button class="btn-pagination" disabled>
                Next
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="9 18 15 12 9 6"/>
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- Add Patient Modal -->
        <transition name="modal">
          <div v-if="showAddModal" class="modal-overlay" @click="showAddModal = false">
            <div class="modal-content" @click.stop>
              <div class="modal-header">
                <div class="modal-title-wrapper">
                  <h2 class="modal-title">Add New Patient</h2>
                  <p class="modal-subtitle">Enter patient information below</p>
                </div>
                <button @click="showAddModal = false" class="btn-close">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="18" y1="6" x2="6" y2="18"/>
                    <line x1="6" y1="6" x2="18" y2="18"/>
                  </svg>
                </button>
              </div>
              
              <form @submit.prevent="handleAddPatient" class="modal-form">
                <div class="form-section">
                  <h3 class="section-title">Personal Information</h3>
                  
                  <div class="form-row">
                    <div class="form-group">
                      <label class="form-label">
                        First Name <span class="required">*</span>
                      </label>
                      <input 
                        v-model="newPatient.first_name" 
                        type="text" 
                        class="form-input"
                        placeholder="Enter first name"
                        required 
                      />
                    </div>
                    <div class="form-group">
                      <label class="form-label">
                        Last Name <span class="required">*</span>
                      </label>
                      <input 
                        v-model="newPatient.last_name" 
                        type="text" 
                        class="form-input"
                        placeholder="Enter last name"
                        required 
                      />
                    </div>
                  </div>

                  <div class="form-row">
                    <div class="form-group">
                      <label class="form-label">
                        Date of Birth <span class="required">*</span>
                      </label>
                      <input 
                        v-model="newPatient.date_of_birth" 
                        type="date" 
                        class="form-input"
                        required 
                      />
                    </div>
                    <div class="form-group">
                      <label class="form-label">
                        Gender <span class="required">*</span>
                      </label>
                      <select v-model="newPatient.gender" class="form-input" required>
                        <option value="">Select gender</option>
                        <option value="M">Male</option>
                        <option value="F">Female</option>
                        <option value="O">Other</option>
                      </select>
                    </div>
                  </div>

                  <div class="form-group">
                    <label class="form-label">Blood Group</label>
                    <select v-model="newPatient.blood_group" class="form-input">
                      <option value="">Select blood group</option>
                      <option value="A+">A+</option>
                      <option value="A-">A-</option>
                      <option value="B+">B+</option>
                      <option value="B-">B-</option>
                      <option value="O+">O+</option>
                      <option value="O-">O-</option>
                      <option value="AB+">AB+</option>
                      <option value="AB-">AB-</option>
                    </select>
                  </div>
                </div>

                <div class="form-section">
                  <h3 class="section-title">Contact Information</h3>
                  
                  <div class="form-row">
                    <div class="form-group">
                      <label class="form-label">
                        Phone Number <span class="required">*</span>
                      </label>
                      <input 
                        v-model="newPatient.phone" 
                        type="tel" 
                        class="form-input"
                        placeholder="+1 (555) 000-0000"
                        required 
                      />
                    </div>
                    <div class="form-group">
                      <label class="form-label">Email Address</label>
                      <input 
                        v-model="newPatient.email" 
                        type="email" 
                        class="form-input"
                        placeholder="patient@example.com"
                      />
                    </div>
                  </div>

                  <div class="form-group">
                    <label class="form-label">
                      Address <span class="required">*</span>
                    </label>
                    <textarea 
                      v-model="newPatient.address" 
                      rows="3" 
                      class="form-input"
                      placeholder="Enter full address"
                      required
                    ></textarea>
                  </div>
                </div>

                <div class="modal-actions">
                  <button 
                    type="button" 
                    @click="showAddModal = false" 
                    class="btn-secondary"
                  >
                    Cancel
                  </button>
                  <button 
                    type="submit" 
                    class="btn-primary" 
                    :disabled="patientStore.loading"
                  >
                    <svg v-if="!patientStore.loading" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <polyline points="20 6 9 17 4 12"/>
                    </svg>
                    <span class="spinner-small" v-if="patientStore.loading"></span>
                    {{ patientStore.loading ? 'Adding Patient...' : 'Add Patient' }}
                  </button>
                </div>
              </form>
            </div>
          </div>
        </transition>
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

const viewPatient = (patient) => {
  alert(`View patient: ${patient.first_name} ${patient.last_name}`)
}

onMounted(() => {
  patientStore.fetchPatients()
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Sora:wght@600;700;800&display=swap');

:root {
  --color-primary: #4f46e5;
  --color-primary-dark: #4338ca;
  --color-primary-light: #818cf8;
  --color-success: #10b981;
  --color-warning: #f59e0b;
  --color-danger: #ef4444;
  --color-info: #3b82f6;
  
  --color-text-primary: #0f172a;
  --color-text-secondary: #475569;
  --color-text-tertiary: #94a3b8;
  
  --color-bg-primary: #ffffff;
  --color-bg-secondary: #f8fafc;
  --color-bg-tertiary: #f1f5f9;
  
  --color-border: #e2e8f0;
  --color-border-light: #f1f5f9;
  
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.08), 0 2px 4px -2px rgb(0 0 0 / 0.06);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.08), 0 4px 6px -4px rgb(0 0 0 / 0.06);
  
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
  
  --transition-base: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dashboard-layout {
  min-height: 100vh;
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
  font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
}

.main-content {
  display: flex;
}

.content {
  flex: 1;
  padding: 2rem;
  max-width: 1600px;
  margin: 0 auto;
  width: 100%;
  animation: fadeIn 0.5s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Page Header */
.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  animation: slideDown 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.header-left {
  flex: 1;
}

.page-title {
  font-family: 'Sora', sans-serif;
  color: var(--color-text-primary);
  font-size: 2.25rem;
  font-weight: 800;
  margin-bottom: 0.375rem;
  letter-spacing: -0.025em;
}

.page-subtitle {
  color: var(--color-text-secondary);
  font-size: 1rem;
  font-weight: 400;
}

.btn-primary {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.875rem 1.5rem;
  background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-dark) 100%);
  color: white;
  border: none;
  border-radius: var(--radius-md);
  font-family: 'DM Sans', sans-serif;
  font-size: 0.9375rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition-base);
  box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 16px rgba(79, 70, 229, 0.4);
}

.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-primary svg {
  width: 18px;
  height: 18px;
}

/* Table Container */
.table-container {
  background: white;
  border-radius: var(--radius-lg);
  border: 1px solid var(--color-border-light);
  box-shadow: var(--shadow-sm);
  overflow: hidden;
  animation: fadeInUp 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.table-header {
  padding: 1.5rem;
  border-bottom: 1px solid var(--color-border-light);
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.search-box {
  position: relative;
  flex: 1;
  min-width: 300px;
  max-width: 500px;
}

.search-box svg {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: var(--color-text-tertiary);
  pointer-events: none;
}

.search-box input {
  width: 100%;
  padding: 0.75rem 1rem 0.75rem 3rem;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  font-family: 'DM Sans', sans-serif;
  font-size: 0.9375rem;
  color: var(--color-text-primary);
  transition: var(--transition-base);
  background: var(--color-bg-secondary);
}

.search-box input:focus {
  outline: none;
  border-color: var(--color-primary);
  background: white;
  box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
}

.search-box input::placeholder {
  color: var(--color-text-tertiary);
}

.table-actions {
  display: flex;
  gap: 0.75rem;
}

.btn-filter,
.btn-export {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.125rem;
  background: var(--color-bg-secondary);
  color: var(--color-text-primary);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  font-family: 'DM Sans', sans-serif;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition-base);
}

.btn-filter:hover,
.btn-export:hover {
  background: white;
  border-color: var(--color-primary);
  color: var(--color-primary);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.btn-filter svg,
.btn-export svg {
  width: 16px;
  height: 16px;
}

/* Table */
.table-wrapper {
  overflow-x: auto;
}

.patients-table {
  width: 100%;
  border-collapse: collapse;
}

.patients-table thead {
  background: var(--color-bg-secondary);
  border-bottom: 2px solid var(--color-border);
}

.patients-table th {
  padding: 1rem 1.5rem;
  text-align: left;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.8125rem;
  font-weight: 700;
  color: var(--color-text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  white-space: nowrap;
}

.patients-table tbody tr {
  border-bottom: 1px solid var(--color-border-light);
  transition: var(--transition-base);
}

.patients-table tbody tr:hover {
  background: var(--color-bg-secondary);
}

.patients-table td {
  padding: 1.25rem 1.5rem;
  font-size: 0.9375rem;
  color: var(--color-text-primary);
}

.checkbox {
  width: 18px;
  height: 18px;
  border-radius: 4px;
  cursor: pointer;
  accent-color: var(--color-primary);
}

.patient-cell {
  display: flex;
  align-items: center;
  gap: 0.875rem;
}

.patient-avatar {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--color-primary-light) 0%, var(--color-primary) 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.875rem;
  font-weight: 700;
  flex-shrink: 0;
}

.patient-name-info {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.patient-name {
  font-weight: 600;
  color: var(--color-text-primary);
  line-height: 1.3;
}

.patient-id {
  font-size: 0.8125rem;
  color: var(--color-text-tertiary);
}

.cell-text {
  color: var(--color-text-secondary);
}

.gender-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
  padding: 0.375rem 0.875rem;
  border-radius: var(--radius-sm);
  font-size: 0.8125rem;
  font-weight: 600;
}

.gender-badge svg {
  width: 14px;
  height: 14px;
}

.gender-m {
  background: #dbeafe;
  color: #1e40af;
}

.gender-f {
  background: #fce7f3;
  color: #be185d;
}

.gender-o {
  background: #f3e8ff;
  color: #6b21a8;
}

.contact-info {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--color-text-secondary);
}

.contact-info svg {
  width: 14px;
  height: 14px;
  color: var(--color-text-tertiary);
  flex-shrink: 0;
}

.blood-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 48px;
  padding: 0.375rem 0.75rem;
  background: #fee2e2;
  color: #991b1b;
  border-radius: var(--radius-sm);
  font-size: 0.8125rem;
  font-weight: 700;
}

.text-muted {
  color: var(--color-text-tertiary);
  font-style: italic;
  font-size: 0.875rem;
}

.action-buttons {
  display: flex;
  gap: 0.5rem;
}

.btn-action {
  width: 36px;
  height: 36px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--color-border);
  background: transparent;
  color: var(--color-text-tertiary);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: var(--transition-base);
}

.btn-action svg {
  width: 16px;
  height: 16px;
}

.btn-view:hover {
  background: #dbeafe;
  border-color: #3b82f6;
  color: #3b82f6;
}

.btn-edit:hover {
  background: #dcfce7;
  border-color: #10b981;
  color: #10b981;
}

.btn-delete:hover {
  background: #fee2e2;
  border-color: #ef4444;
  color: #ef4444;
}

/* Table Footer */
.table-footer {
  padding: 1.25rem 1.5rem;
  border-top: 1px solid var(--color-border-light);
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
}

.footer-info {
  color: var(--color-text-secondary);
  font-size: 0.875rem;
}

.footer-info strong {
  color: var(--color-text-primary);
  font-weight: 600;
}

.pagination {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.btn-pagination {
  display: flex;
  align-items: center;
  gap: 0.375rem;
  padding: 0.5rem 0.875rem;
  background: white;
  color: var(--color-text-primary);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  font-family: 'DM Sans', sans-serif;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition-base);
}

.btn-pagination:hover:not(:disabled) {
  background: var(--color-bg-secondary);
  border-color: var(--color-primary);
  color: var(--color-primary);
}

.btn-pagination:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

.btn-pagination svg {
  width: 14px;
  height: 14px;
}

.pagination-numbers {
  display: flex;
  gap: 0.25rem;
}

.pagination-number {
  width: 36px;
  height: 36px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--color-border);
  background: white;
  color: var(--color-text-primary);
  font-family: 'DM Sans', sans-serif;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition-base);
}

.pagination-number:hover {
  background: var(--color-bg-secondary);
  border-color: var(--color-primary);
  color: var(--color-primary);
}

.pagination-number.active {
  background: var(--color-primary);
  border-color: var(--color-primary);
  color: white;
}

/* Loading State */
.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
  gap: 1rem;
}

.spinner {
  width: 48px;
  height: 48px;
  border: 4px solid var(--color-border);
  border-top-color: var(--color-primary);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.loading-state p {
  color: var(--color-text-tertiary);
  font-size: 0.9375rem;
  font-weight: 500;
}

/* Empty State */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
  text-align: center;
}

.empty-icon {
  width: 80px;
  height: 80px;
  background: var(--color-bg-tertiary);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.5rem;
}

.empty-icon svg {
  width: 40px;
  height: 40px;
  color: var(--color-text-tertiary);
}

.empty-state h3 {
  color: var(--color-text-primary);
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.empty-state p {
  color: var(--color-text-tertiary);
  font-size: 0.9375rem;
  margin-bottom: 1.5rem;
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  padding: 1rem;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: white;
  border-radius: var(--radius-lg);
  width: 100%;
  max-width: 700px;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.25);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding: 2rem 2rem 1.5rem;
  border-bottom: 1px solid var(--color-border-light);
  position: sticky;
  top: 0;
  background: white;
  z-index: 10;
}

.modal-title-wrapper {
  flex: 1;
}

.modal-title {
  font-family: 'Sora', sans-serif;
  color: var(--color-text-primary);
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.25rem;
  letter-spacing: -0.02em;
}

.modal-subtitle {
  color: var(--color-text-tertiary);
  font-size: 0.875rem;
}

.btn-close {
  width: 36px;
  height: 36px;
  background: var(--color-bg-secondary);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  color: var(--color-text-tertiary);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: var(--transition-base);
  flex-shrink: 0;
}

.btn-close:hover {
  background: #fee2e2;
  border-color: #ef4444;
  color: #ef4444;
}

.btn-close svg {
  width: 18px;
  height: 18px;
}

.modal-form {
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.form-section {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.section-title {
  font-family: 'Sora', sans-serif;
  color: var(--color-text-primary);
  font-size: 1.125rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  letter-spacing: -0.01em;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.25rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-label {
  color: var(--color-text-primary);
  font-weight: 600;
  font-size: 0.875rem;
  letter-spacing: -0.01em;
}

.required {
  color: #ef4444;
}

.form-input {
  padding: 0.75rem 1rem;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  font-family: 'DM Sans', sans-serif;
  font-size: 0.9375rem;
  color: var(--color-text-primary);
  transition: var(--transition-base);
  background: var(--color-bg-secondary);
}

.form-input:focus {
  outline: none;
  border-color: var(--color-primary);
  background: white;
  box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
}

.form-input::placeholder {
  color: var(--color-text-tertiary);
}

textarea.form-input {
  resize: vertical;
  min-height: 80px;
}

.modal-actions {
  display: flex;
  gap: 0.75rem;
  justify-content: flex-end;
  padding-top: 1rem;
  border-top: 1px solid var(--color-border-light);
}

.btn-secondary {
  padding: 0.875rem 1.5rem;
  background: var(--color-bg-secondary);
  color: var(--color-text-primary);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  font-family: 'DM Sans', sans-serif;
  font-size: 0.9375rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition-base);
}

.btn-secondary:hover {
  background: white;
  border-color: var(--color-text-secondary);
  color: var(--color-text-primary);
}

.spinner-small {
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
  display: inline-block;
}

/* Modal Transitions */
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-active .modal-content,
.modal-leave-active .modal-content {
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.modal-enter-from .modal-content,
.modal-leave-to .modal-content {
  transform: scale(0.95) translateY(20px);
}

/* Responsive Design */
@media (max-width: 1024px) {
  .content {
    padding: 1.5rem;
  }

  .table-header {
    flex-direction: column;
    align-items: stretch;
  }

  .search-box {
    max-width: 100%;
  }

  .table-actions {
    width: 100%;
  }

  .btn-filter,
  .btn-export {
    flex: 1;
    justify-content: center;
  }
}

@media (max-width: 768px) {
  .content {
    padding: 1rem;
  }

  .page-header {
    flex-direction: column;
    align-items: stretch;
    gap: 1rem;
  }

  .page-title {
    font-size: 1.875rem;
  }

  .btn-primary {
    width: 100%;
    justify-content: center;
  }

  .form-row {
    grid-template-columns: 1fr;
  }

  .table-footer {
    flex-direction: column;
    align-items: stretch;
  }

  .pagination {
    justify-content: center;
  }

  .patients-table {
    font-size: 0.875rem;
  }

  .patients-table th,
  .patients-table td {
    padding: 0.875rem 1rem;
  }

  .action-buttons {
    flex-direction: column;
  }
}

@media (max-width: 480px) {
  .page-title {
    font-size: 1.5rem;
  }

  .modal-content {
    max-width: 100%;
  }

  .modal-form {
    padding: 1.5rem;
  }

  .modal-actions {
    flex-direction: column-reverse;
  }

  .btn-secondary,
  .modal-actions .btn-primary {
    width: 100%;
    justify-content: center;
  }
}
</style>