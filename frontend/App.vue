<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useAuthStore } from './stores/auth'

const authStore = useAuthStore()

onMounted(() => {
  // Check if user is logged in on app mount
  authStore.checkAuth()
})
</script>

<style scoped>
#app {
  width: 100%;
  min-height: 100vh;
  background-color: #f5f5f5;
}
</style>
