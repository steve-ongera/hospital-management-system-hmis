<template>
  <div class="dashboard-layout">
    <Navbar />
    <div class="main-content">
      <Sidebar />
      <div class="content">
        <div class="page-header">
          <div class="header-content">
            <div class="header-text">
              <h1 class="page-title">Doctor Dashboard</h1>
              <p class="page-subtitle">Welcome back, <span class="user-highlight">{{ authStore.userName }}</span>!</p>
            </div>
            <div class="header-actions">
              <button class="btn-action btn-secondary">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
                </svg>
                <span>Messages</span>
              </button>
              <button class="btn-action btn-primary">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10"/>
                  <polyline points="12 6 12 12 16 14"/>
                </svg>
                <span>New Appointment</span>
              </button>
            </div>
          </div>
        </div>

        <div class="stats-grid">
          <div class="stat-card stat-card-1">
            <div class="stat-card-inner">
              <div class="stat-header">
                <div class="stat-icon-wrapper stat-icon-primary">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                    <circle cx="9" cy="7" r="4"/>
                    <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
                    <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
                  </svg>
                </div>
                <div class="stat-trend stat-trend-up">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/>
                    <polyline points="17 6 23 6 23 12"/>
                  </svg>
                  <span>+12%</span>
                </div>
              </div>
              <div class="stat-content">
                <h3 class="stat-label">Total Patients</h3>
                <p class="stat-value">{{ stats.totalPatients }}</p>
                <p class="stat-description">Active patients under care</p>
              </div>
            </div>
            <div class="stat-card-glow stat-glow-primary"></div>
          </div>

          <div class="stat-card stat-card-2">
            <div class="stat-card-inner">
              <div class="stat-header">
                <div class="stat-icon-wrapper stat-icon-info">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                    <line x1="16" y1="2" x2="16" y2="6"/>
                    <line x1="8" y1="2" x2="8" y2="6"/>
                    <line x1="3" y1="10" x2="21" y2="10"/>
                  </svg>
                </div>
                <div class="stat-trend stat-trend-neutral">
                  <span>Today</span>
                </div>
              </div>
              <div class="stat-content">
                <h3 class="stat-label">Today's Appointments</h3>
                <p class="stat-value">{{ stats.todayAppointments }}</p>
                <p class="stat-description">Scheduled for today</p>
              </div>
            </div>
            <div class="stat-card-glow stat-glow-info"></div>
          </div>

          <div class="stat-card stat-card-3">
            <div class="stat-card-inner">
              <div class="stat-header">
                <div class="stat-icon-wrapper stat-icon-warning">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="10"/>
                    <polyline points="12 6 12 12 16 14"/>
                  </svg>
                </div>
                <div class="stat-trend stat-trend-neutral">
                  <span>Pending</span>
                </div>
              </div>
              <div class="stat-content">
                <h3 class="stat-label">Pending Appointments</h3>
                <p class="stat-value">{{ stats.pendingAppointments }}</p>
                <p class="stat-description">Awaiting confirmation</p>
              </div>
            </div>
            <div class="stat-card-glow stat-glow-warning"></div>
          </div>

          <div class="stat-card stat-card-4">
            <div class="stat-card-inner">
              <div class="stat-header">
                <div class="stat-icon-wrapper stat-icon-success">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="20 6 9 17 4 12"/>
                  </svg>
                </div>
                <div class="stat-trend stat-trend-up">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/>
                    <polyline points="17 6 23 6 23 12"/>
                  </svg>
                  <span>+8%</span>
                </div>
              </div>
              <div class="stat-content">
                <h3 class="stat-label">Completed Today</h3>
                <p class="stat-value">{{ stats.completedToday }}</p>
                <p class="stat-description">Successfully completed</p>
              </div>
            </div>
            <div class="stat-card-glow stat-glow-success"></div>
          </div>
        </div>

        <div class="recent-section">
          <div class="section-header">
            <div class="section-title-wrapper">
              <h2 class="section-title">Recent Appointments</h2>
              <p class="section-subtitle">Your latest patient appointments</p>
            </div>
            <button class="btn-view-all">
              View All
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="9 18 15 12 9 6"/>
              </svg>
            </button>
          </div>

          <div v-if="appointmentStore.loading" class="loading-state">
            <div class="spinner"></div>
            <p>Loading appointments...</p>
          </div>

          <div v-else-if="recentAppointments.length === 0" class="empty-state">
            <div class="empty-icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                <line x1="16" y1="2" x2="16" y2="6"/>
                <line x1="8" y1="2" x2="8" y2="6"/>
                <line x1="3" y1="10" x2="21" y2="10"/>
              </svg>
            </div>
            <h3>No appointments found</h3>
            <p>You don't have any appointments scheduled yet</p>
          </div>

          <div v-else class="appointments-list">
            <div
              v-for="(appointment, index) in recentAppointments"
              :key="appointment.id"
              class="appointment-item"
              :style="{ animationDelay: `${index * 0.1}s` }"
            >
              <div class="appointment-avatar">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                  <circle cx="12" cy="7" r="4"/>
                </svg>
              </div>
              <div class="appointment-info">
                <h4 class="patient-name">{{ appointment.patient_full }}</h4>
                <div class="appointment-meta">
                  <span class="meta-item">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                      <line x1="16" y1="2" x2="16" y2="6"/>
                      <line x1="8" y1="2" x2="8" y2="6"/>
                      <line x1="3" y1="10" x2="21" y2="10"/>
                    </svg>
                    {{ formatDate(appointment.appointment_date) }}
                  </span>
                  <span class="meta-item">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <circle cx="12" cy="12" r="10"/>
                      <polyline points="12 6 12 12 16 14"/>
                    </svg>
                    {{ appointment.appointment_time }}
                  </span>
                </div>
                <p class="appointment-reason">{{ appointment.reason }}</p>
              </div>
              <div class="appointment-actions">
                <span :class="`status-badge status-${appointment.status}`">
                  <span class="status-dot"></span>
                  {{ appointment.status }}
                </span>
                <button class="btn-icon" aria-label="More options">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="1"/>
                    <circle cx="12" cy="5" r="1"/>
                    <circle cx="12" cy="19" r="1"/>
                  </svg>
                </button>
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
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Sora:wght@600;700;800&display=swap');

:root {
  --color-primary: #4f46e5;
  --color-primary-dark: #4338ca;
  --color-primary-light: #818cf8;
  --color-secondary: #06b6d4;
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
  --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.08), 0 8px 10px -6px rgb(0 0 0 / 0.06);
  
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --radius-xl: 20px;
  
  --transition-base: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-fast: all 0.15s cubic-bezier(0.4, 0, 0.2, 1);
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
  margin-bottom: 2.5rem;
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

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.header-text {
  flex: 1;
}

.page-title {
  font-family: 'Sora', sans-serif;
  color: var(--color-text-primary);
  font-size: 2.25rem;
  font-weight: 800;
  margin-bottom: 0.5rem;
  letter-spacing: -0.025em;
  line-height: 1.2;
}

.page-subtitle {
  color: var(--color-text-secondary);
  font-size: 1.125rem;
  font-weight: 400;
  line-height: 1.5;
}

.user-highlight {
  color: var(--color-primary);
  font-weight: 600;
}

.header-actions {
  display: flex;
  gap: 0.75rem;
  align-items: center;
}

.btn-action {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  border: none;
  border-radius: var(--radius-md);
  font-family: 'DM Sans', sans-serif;
  font-size: 0.9375rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition-base);
  position: relative;
  overflow: hidden;
}

.btn-action svg {
  width: 18px;
  height: 18px;
  transition: var(--transition-fast);
}

.btn-action::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.3);
  transform: translate(-50%, -50%);
  transition: width 0.6s, height 0.6s;
}

.btn-action:hover::before {
  width: 300px;
  height: 300px;
}

.btn-primary {
  background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-dark) 100%);
  color: white;
  box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 16px rgba(79, 70, 229, 0.4);
}

.btn-primary:active {
  transform: translateY(0);
}

.btn-secondary {
  background: white;
  color: var(--color-text-primary);
  border: 2px solid var(--color-border);
}

.btn-secondary:hover {
  border-color: var(--color-primary);
  color: var(--color-primary);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2.5rem;
}

.stat-card {
  background: white;
  border-radius: var(--radius-lg);
  padding: 1.75rem;
  position: relative;
  overflow: hidden;
  border: 1px solid var(--color-border-light);
  transition: var(--transition-base);
  animation: scaleIn 0.5s cubic-bezier(0.16, 1, 0.3, 1);
  animation-fill-mode: both;
}

.stat-card-1 { animation-delay: 0.1s; }
.stat-card-2 { animation-delay: 0.2s; }
.stat-card-3 { animation-delay: 0.3s; }
.stat-card-4 { animation-delay: 0.4s; }

@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.9) translateY(20px);
  }
  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-xl);
  border-color: transparent;
}

.stat-card-inner {
  position: relative;
  z-index: 2;
}

.stat-card-glow {
  position: absolute;
  top: -50%;
  right: -50%;
  width: 200%;
  height: 200%;
  opacity: 0;
  transition: opacity 0.6s ease;
  pointer-events: none;
  z-index: 1;
}

.stat-card:hover .stat-card-glow {
  opacity: 0.15;
}

.stat-glow-primary {
  background: radial-gradient(circle, var(--color-primary) 0%, transparent 70%);
}

.stat-glow-info {
  background: radial-gradient(circle, var(--color-info) 0%, transparent 70%);
}

.stat-glow-warning {
  background: radial-gradient(circle, var(--color-warning) 0%, transparent 70%);
}

.stat-glow-success {
  background: radial-gradient(circle, var(--color-success) 0%, transparent 70%);
}

.stat-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1.25rem;
}

.stat-icon-wrapper {
  width: 56px;
  height: 56px;
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.stat-icon-wrapper::before {
  content: '';
  position: absolute;
  inset: 0;
  opacity: 0.1;
}

.stat-icon-wrapper svg {
  width: 28px;
  height: 28px;
  position: relative;
  z-index: 2;
  stroke-width: 2.5;
}

.stat-icon-primary {
  background: linear-gradient(135deg, #4f46e515 0%, #4f46e525 100%);
  color: var(--color-primary);
}

.stat-icon-info {
  background: linear-gradient(135deg, #3b82f615 0%, #3b82f625 100%);
  color: var(--color-info);
}

.stat-icon-warning {
  background: linear-gradient(135deg, #f59e0b15 0%, #f59e0b25 100%);
  color: var(--color-warning);
}

.stat-icon-success {
  background: linear-gradient(135deg, #10b98115 0%, #10b98125 100%);
  color: var(--color-success);
}

.stat-trend {
  display: flex;
  align-items: center;
  gap: 0.375rem;
  padding: 0.375rem 0.75rem;
  border-radius: var(--radius-sm);
  font-size: 0.8125rem;
  font-weight: 600;
}

.stat-trend svg {
  width: 14px;
  height: 14px;
}

.stat-trend-up {
  background: #10b98110;
  color: var(--color-success);
}

.stat-trend-neutral {
  background: #94a3b810;
  color: var(--color-text-tertiary);
}

.stat-content {
  margin-top: 0.25rem;
}

.stat-label {
  color: var(--color-text-secondary);
  font-size: 0.9375rem;
  font-weight: 500;
  margin-bottom: 0.75rem;
  line-height: 1.4;
}

.stat-value {
  color: var(--color-text-primary);
  font-family: 'Sora', sans-serif;
  font-size: 2.5rem;
  font-weight: 700;
  line-height: 1;
  margin-bottom: 0.5rem;
  letter-spacing: -0.02em;
}

.stat-description {
  color: var(--color-text-tertiary);
  font-size: 0.8125rem;
  font-weight: 400;
  line-height: 1.4;
}

/* Recent Section */
.recent-section {
  background: white;
  border-radius: var(--radius-xl);
  padding: 2rem;
  border: 1px solid var(--color-border-light);
  box-shadow: var(--shadow-sm);
  animation: fadeInUp 0.6s cubic-bezier(0.16, 1, 0.3, 1);
  animation-delay: 0.5s;
  animation-fill-mode: both;
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

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  padding-bottom: 1.5rem;
  border-bottom: 2px solid var(--color-bg-tertiary);
}

.section-title {
  font-family: 'Sora', sans-serif;
  color: var(--color-text-primary);
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.25rem;
  letter-spacing: -0.02em;
}

.section-subtitle {
  color: var(--color-text-tertiary);
  font-size: 0.875rem;
  font-weight: 400;
}

.btn-view-all {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.625rem 1.125rem;
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

.btn-view-all svg {
  width: 16px;
  height: 16px;
  transition: var(--transition-fast);
}

.btn-view-all:hover {
  background: var(--color-primary);
  color: white;
  border-color: var(--color-primary);
  transform: translateX(4px);
}

.btn-view-all:hover svg {
  transform: translateX(4px);
}

/* Appointments List */
.appointments-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.appointment-item {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  padding: 1.25rem;
  background: var(--color-bg-secondary);
  border: 1px solid var(--color-border-light);
  border-radius: var(--radius-md);
  transition: var(--transition-base);
  animation: slideInLeft 0.5s cubic-bezier(0.16, 1, 0.3, 1);
  animation-fill-mode: both;
}

@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.appointment-item:hover {
  background: white;
  border-color: var(--color-primary);
  box-shadow: var(--shadow-md);
  transform: translateX(4px);
}

.appointment-avatar {
  width: 52px;
  height: 52px;
  border-radius: var(--radius-md);
  background: linear-gradient(135deg, var(--color-primary-light) 0%, var(--color-primary) 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.appointment-avatar svg {
  width: 26px;
  height: 26px;
}

.appointment-info {
  flex: 1;
  min-width: 0;
}

.patient-name {
  color: var(--color-text-primary);
  font-size: 1.0625rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  line-height: 1.3;
}

.appointment-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-bottom: 0.625rem;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 0.375rem;
  color: var(--color-text-secondary);
  font-size: 0.8125rem;
  font-weight: 500;
}

.meta-item svg {
  width: 14px;
  height: 14px;
  color: var(--color-text-tertiary);
}

.appointment-reason {
  color: var(--color-text-tertiary);
  font-size: 0.875rem;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.appointment-actions {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.status-badge {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  border-radius: var(--radius-sm);
  font-size: 0.8125rem;
  font-weight: 600;
  text-transform: capitalize;
  white-space: nowrap;
}

.status-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

.status-scheduled {
  background: #dbeafe;
  color: #1e40af;
}

.status-scheduled .status-dot {
  background: #1e40af;
}

.status-completed {
  background: #d1fae5;
  color: #065f46;
}

.status-completed .status-dot {
  background: #065f46;
}

.status-cancelled {
  background: #fee2e2;
  color: #991b1b;
}

.status-cancelled .status-dot {
  background: #991b1b;
}

.btn-icon {
  width: 36px;
  height: 36px;
  border-radius: var(--radius-sm);
  background: transparent;
  border: 1px solid var(--color-border);
  color: var(--color-text-tertiary);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: var(--transition-fast);
}

.btn-icon svg {
  width: 18px;
  height: 18px;
}

.btn-icon:hover {
  background: var(--color-bg-tertiary);
  color: var(--color-text-primary);
  border-color: var(--color-text-tertiary);
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
}

/* Responsive Design */
@media (max-width: 1024px) {
  .content {
    padding: 1.5rem;
  }

  .page-title {
    font-size: 1.875rem;
  }

  .stats-grid {
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1.25rem;
  }

  .stat-card {
    padding: 1.5rem;
  }
}

@media (max-width: 768px) {
  .content {
    padding: 1rem;
  }

  .header-content {
    flex-direction: column;
    align-items: flex-start;
  }

  .page-title {
    font-size: 1.625rem;
  }

  .page-subtitle {
    font-size: 1rem;
  }

  .header-actions {
    width: 100%;
    flex-direction: column;
  }

  .btn-action {
    width: 100%;
    justify-content: center;
  }

  .stats-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .recent-section {
    padding: 1.5rem;
  }

  .section-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }

  .btn-view-all {
    width: 100%;
    justify-content: center;
  }

  .appointment-item {
    flex-direction: column;
    align-items: flex-start;
  }

  .appointment-actions {
    width: 100%;
    justify-content: space-between;
  }

  .status-badge {
    flex: 1;
    justify-content: center;
  }
}

@media (max-width: 480px) {
  .page-title {
    font-size: 1.5rem;
  }

  .stat-value {
    font-size: 2rem;
  }

  .section-title {
    font-size: 1.25rem;
  }

  .appointment-meta {
    flex-direction: column;
    gap: 0.5rem;
  }
}
</style>