<template>
  <aside class="sidebar">
    <nav class="sidebar-nav">
      <router-link
        v-for="item in menuItems"
        :key="item.path"
        :to="item.path"
        class="nav-item"
        active-class="active"
      >
        <span class="nav-icon">{{ item.icon }}</span>
        <span class="nav-text">{{ item.label }}</span>
      </router-link>
    </nav>
  </aside>
</template>

<script setup>
import { computed } from 'vue'
import { useAuthStore } from '../../stores/auth'

const authStore = useAuthStore()

const menuItems = computed(() => {
  const role = authStore.userRole

  if (role === 'doctor') {
    return [
      { path: '/doctor', label: 'Dashboard', icon: '📊' },
      { path: '/doctor/patients', label: 'Patients', icon: '👥' },
      { path: '/doctor/appointments', label: 'Appointments', icon: '📅' },
    ]
  } else if (role === 'nurse') {
    return [
      { path: '/nurse', label: 'Dashboard', icon: '📊' },
      { path: '/nurse/patients', label: 'Patients', icon: '👥' },
    ]
  } else if (role === 'pharmacist') {
    return [
      { path: '/pharmacist', label: 'Dashboard', icon: '📊' },
      { path: '/pharmacist/inventory', label: 'Inventory', icon: '💊' },
      { path: '/pharmacist/prescriptions', label: 'Prescriptions', icon: '📋' },
    ]
  }

  return []
})
</script>

<style scoped>
.sidebar {
  width: 250px;
  background: white;
  box-shadow: 2px 0 4px rgba(0, 0, 0, 0.1);
  min-height: calc(100vh - 60px);
  padding: 20px 0;
}

.sidebar-nav {
  display: flex;
  flex-direction: column;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 15px;
  padding: 15px 30px;
  color: #666;
  text-decoration: none;
  transition: all 0.3s;
  border-left: 3px solid transparent;
}

.nav-item:hover {
  background: #f5f5f5;
  color: #667eea;
}

.nav-item.active {
  background: #f0f4ff;
  color: #667eea;
  border-left-color: #667eea;
  font-weight: 500;
}

.nav-icon {
  font-size: 20px;
}

.nav-text {
  font-size: 15px;
}
</style>
