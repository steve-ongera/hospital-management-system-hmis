<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <h2>Hospital MS</h2>
    </div>

    <div class="navbar-menu">
      <div class="navbar-user">
        <span class="user-name">{{ authStore.userName }}</span>
        <span class="user-role" :class="`role-${authStore.userRole}`">
          {{ authStore.userRole }}
        </span>
      </div>

      <button @click="handleLogout" class="btn-logout">
        Logout
      </button>
    </div>
  </nav>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useAuthStore } from '../../stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const handleLogout = () => {
  authStore.logout()
  router.push('/login')
}
</script>

<style scoped>
.navbar {
  background: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 15px 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.navbar-brand h2 {
  color: #667eea;
  margin: 0;
  font-size: 24px;
}

.navbar-menu {
  display: flex;
  align-items: center;
  gap: 20px;
}

.navbar-user {
  display: flex;
  align-items: center;
  gap: 10px;
}

.user-name {
  color: #333;
  font-weight: 500;
}

.user-role {
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 500;
  text-transform: uppercase;
}

.role-doctor {
  background: #e3f2fd;
  color: #1976d2;
}

.role-nurse {
  background: #f3e5f5;
  color: #7b1fa2;
}

.role-pharmacist {
  background: #e8f5e9;
  color: #388e3c;
}

.btn-logout {
  padding: 8px 20px;
  background: #f44336;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: 500;
  transition: background 0.3s;
}

.btn-logout:hover {
  background: #d32f2f;
}
</style>
