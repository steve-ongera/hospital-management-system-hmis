<template>
  <div class="login-page d-flex align-items-center justify-content-center">
    <div class="card login-card shadow-lg border-0">
      <div class="card-body p-4 p-md-5">

        <!-- Header -->
        <div class="text-center mb-4">
          <i class="bi bi-hospital display-4 text-primary mb-3"></i>
          <h4 class="fw-bold mb-1">Hospital Management System</h4>
          <p class="text-muted small">Please login to continue</p>
        </div>

        <!-- Error -->
        <div
          v-if="authStore.error"
          class="alert alert-danger alert-dismissible fade show"
          role="alert"
        >
          {{ authStore.error }}
          <button
            type="button"
            class="btn-close"
            @click="authStore.clearError()"
          ></button>
        </div>

        <!-- Form -->
        <form @submit.prevent="handleLogin">
          <div class="mb-3">
            <label class="form-label">
              <i class="bi bi-person me-2"></i>Username
            </label>
            <input
              v-model="credentials.username"
              type="text"
              class="form-control form-control-lg"
              placeholder="Enter your username"
              required
              :disabled="authStore.loading"
            />
          </div>

          <div class="mb-4">
            <label class="form-label">
              <i class="bi bi-key me-2"></i>Password
            </label>
            <div class="input-group input-group-lg">
              <input
                v-model="credentials.password"
                :type="showPassword ? 'text' : 'password'"
                class="form-control"
                placeholder="Enter your password"
                required
                :disabled="authStore.loading"
              />
              <button
                type="button"
                class="btn btn-outline-secondary"
                @click="togglePasswordVisibility"
              >
                <i :class="showPassword ? 'bi bi-eye-slash' : 'bi bi-eye'"></i>
              </button>
            </div>
          </div>

          <button
            type="submit"
            class="btn btn-primary btn-lg w-100"
            :disabled="authStore.loading"
          >
            <span
              v-if="authStore.loading"
              class="spinner-border spinner-border-sm me-2"
            ></span>
            {{ authStore.loading ? 'Logging in...' : 'Login' }}
          </button>
        </form>

        <!-- Demo -->
        <div class="bg-light rounded p-3 mt-4 small">
          <strong class="d-block mb-2">
            <i class="bi bi-info-circle me-1"></i> Demo Credentials
          </strong>
          <div>Doctor: <code>doctor1</code> / <code>password123</code></div>
          <div>Nurse: <code>nurse1</code> / <code>password123</code></div>
          <div>Pharmacist: <code>pharmacist1</code> / <code>password123</code></div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../../stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const showPassword = ref(false)

const credentials = ref({
  username: '',
  password: '',
})

const togglePasswordVisibility = () => {
  showPassword.value = !showPassword.value
}

const handleLogin = async () => {
  await authStore.login(credentials.value)
  router.push(`/${authStore.user.role}`)
}
</script>

<style>
.login-page {
  min-height: 100vh;
  background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
}

.login-card {
  width: 100%;
  max-width: 420px;
  border-radius: 1rem;
  animation: fadeUp 0.5s ease-out;
}

.login-card code {
  background: rgba(13, 110, 253, 0.1);
  color: #0d6efd;
  padding: 2px 6px;
  border-radius: 4px;
}

@keyframes fadeUp {
  from {
    opacity: 0;
    transform: translateY(15px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>

