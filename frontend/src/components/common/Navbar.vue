<template>
  <nav class="navbar">
    <div class="navbar-container">
      <div class="navbar-brand">
        <div class="brand-icon">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M22 12h-4l-3 9L9 3l-3 9H2"/>
          </svg>
        </div>
        <h2 class="brand-text">Hospital MS</h2>
      </div>

      <div class="navbar-menu">
        <div class="navbar-user">
          <div class="user-avatar">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
              <circle cx="12" cy="7" r="4"/>
            </svg>
          </div>
          <div class="user-info">
            <span class="user-name">{{ authStore.userName }}</span>
            <span class="user-role" :class="`role-${authStore.userRole}`">
              {{ formatRole(authStore.userRole) }}
            </span>
          </div>
        </div>

        <button @click="handleLogout" class="btn-logout" aria-label="Logout">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/>
            <polyline points="16 17 21 12 16 7"/>
            <line x1="21" y1="12" x2="9" y2="12"/>
          </svg>
          <span class="logout-text">Logout</span>
        </button>
      </div>

      <!-- Mobile Menu Toggle -->
      <button class="mobile-menu-toggle" @click="toggleMobileMenu" aria-label="Toggle menu">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="3" y1="12" x2="21" y2="12"/>
          <line x1="3" y1="6" x2="21" y2="6"/>
          <line x1="3" y1="18" x2="21" y2="18"/>
        </svg>
      </button>
    </div>

    <!-- Mobile Menu Dropdown -->
    <div class="mobile-menu" :class="{ active: mobileMenuOpen }">
      <div class="mobile-user-info">
        <div class="user-avatar">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
            <circle cx="12" cy="7" r="4"/>
          </svg>
        </div>
        <div class="user-info">
          <span class="user-name">{{ authStore.userName }}</span>
          <span class="user-role" :class="`role-${authStore.userRole}`">
            {{ formatRole(authStore.userRole) }}
          </span>
        </div>
      </div>
      <button @click="handleLogout" class="btn-logout-mobile">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/>
          <polyline points="16 17 21 12 16 7"/>
          <line x1="21" y1="12" x2="9" y2="12"/>
        </svg>
        <span>Logout</span>
      </button>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../../stores/auth'

const router = useRouter()
const authStore = useAuthStore()
const mobileMenuOpen = ref(false)

const handleLogout = () => {
  authStore.logout()
  router.push('/login')
  mobileMenuOpen.value = false
}

const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
}

const formatRole = (role) => {
  return role ? role.charAt(0).toUpperCase() + role.slice(1) : ''
}
</script>

<style scoped>
.navbar {
  background: #ffffff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  position: sticky;
  top: 0;
  z-index: 1000;
  border-bottom: 1px solid #e5e7eb;
}

.navbar-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0.875rem 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Brand */
.navbar-brand {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  cursor: pointer;
  transition: opacity 0.2s ease;
}

.navbar-brand:hover {
  opacity: 0.8;
}

.brand-icon {
  width: 36px;
  height: 36px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.brand-icon svg {
  width: 20px;
  height: 20px;
}

.brand-text {
  color: #1f2937;
  margin: 0;
  font-size: 1.375rem;
  font-weight: 700;
  letter-spacing: -0.025em;
}

/* Navbar Menu */
.navbar-menu {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.navbar-user {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.5rem 1rem;
  background: #f9fafb;
  border-radius: 12px;
  border: 1px solid #e5e7eb;
}

.user-avatar {
  width: 38px;
  height: 38px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.user-avatar svg {
  width: 20px;
  height: 20px;
}

.user-info {
  display: flex;
  flex-direction: column;
  gap: 0.125rem;
}

.user-name {
  color: #1f2937;
  font-weight: 600;
  font-size: 0.875rem;
  line-height: 1.2;
}

.user-role {
  padding: 0.125rem 0.5rem;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.025em;
  width: fit-content;
}

.role-doctor {
  background: #dbeafe;
  color: #1e40af;
}

.role-nurse {
  background: #fae8ff;
  color: #86198f;
}

.role-pharmacist {
  background: #dcfce7;
  color: #166534;
}

.role-admin {
  background: #fef3c7;
  color: #92400e;
}

/* Logout Button */
.btn-logout {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.625rem 1.25rem;
  background: #ef4444;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.875rem;
  transition: all 0.2s ease;
  box-shadow: 0 1px 3px rgba(239, 68, 68, 0.2);
}

.btn-logout:hover {
  background: #dc2626;
  transform: translateY(-1px);
  box-shadow: 0 4px 6px rgba(239, 68, 68, 0.3);
}

.btn-logout:active {
  transform: translateY(0);
}

.btn-logout svg {
  width: 18px;
  height: 18px;
}

/* Mobile Menu Toggle */
.mobile-menu-toggle {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
  color: #4b5563;
  transition: color 0.2s ease;
}

.mobile-menu-toggle:hover {
  color: #667eea;
}

.mobile-menu-toggle svg {
  width: 24px;
  height: 24px;
}

/* Mobile Menu Dropdown */
.mobile-menu {
  display: none;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease;
  background: #f9fafb;
  border-top: 1px solid #e5e7eb;
}

.mobile-menu.active {
  max-height: 300px;
  padding: 1rem 1.5rem;
}

.mobile-user-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem;
  background: white;
  border-radius: 12px;
  margin-bottom: 1rem;
  border: 1px solid #e5e7eb;
}

.btn-logout-mobile {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  background: #ef4444;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.875rem;
  transition: all 0.2s ease;
}

.btn-logout-mobile:hover {
  background: #dc2626;
}

.btn-logout-mobile svg {
  width: 18px;
  height: 18px;
}

/* Responsive Design */
@media (max-width: 768px) {
  .navbar-container {
    padding: 0.75rem 1rem;
  }

  .brand-text {
    font-size: 1.125rem;
  }

  .brand-icon {
    width: 32px;
    height: 32px;
  }

  .brand-icon svg {
    width: 18px;
    height: 18px;
  }

  .navbar-menu {
    display: none;
  }

  .mobile-menu-toggle {
    display: block;
  }

  .mobile-menu {
    display: block;
  }
}

@media (max-width: 480px) {
  .navbar-container {
    padding: 0.625rem 0.875rem;
  }

  .brand-text {
    font-size: 1rem;
  }

  .brand-icon {
    width: 28px;
    height: 28px;
  }

  .brand-icon svg {
    width: 16px;
    height: 16px;
  }
}

@media (min-width: 769px) {
  .logout-text {
    display: inline;
  }
}

@media (max-width: 1024px) {
  .user-info {
    display: none;
  }

  .navbar-user {
    padding: 0.5rem;
  }
}

@media (min-width: 1025px) {
  .user-info {
    display: flex;
  }
}
</style>