<template>
  <div class="dashboard-layout">
    <Navbar />
    <div class="main-content">
      <Sidebar />
      <div class="content">
        <div class="page-header">
          <h1>Medication Inventory</h1>
          <button @click="showAddModal = true" class="btn-primary">
            + Add Medication
          </button>
        </div>

        <div class="filter-tabs">
          <button
            :class="{ active: filter === 'all' }"
            @click="setFilter('all')"
          >
            All Medications
          </button>
          <button
            :class="{ active: filter === 'low_stock' }"
            @click="setFilter('low_stock')"
          >
            Low Stock
          </button>
        </div>

        <div v-if="pharmacyStore.loading" class="loading">Loading...</div>
        <div v-else-if="pharmacyStore.medications.length === 0" class="empty-state">
          No medications found
        </div>
        <div v-else class="medications-table">
          <table>
            <thead>
              <tr>
                <th>Name</th>
                <th>Manufacturer</th>
                <th>Unit Price</th>
                <th>Stock</th>
                <th>Status</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="med in pharmacyStore.medications" :key="med.id">
                <td><strong>{{ med.name }}</strong></td>
                <td>{{ med.manufacturer || 'N/A' }}</td>
                <td>${{ med.unit_price }}</td>
                <td>{{ med.stock_quantity }} units</td>
                <td>
                  <span :class="`stock-badge ${getStockClass(med.stock_quantity)}`">
                    {{ getStockStatus(med.stock_quantity) }}
                  </span>
                </td>
                <td>
                  <button @click="updateStock(med)" class="btn-small">
                    Update Stock
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Add Medication Modal -->
        <div v-if="showAddModal" class="modal-overlay" @click="showAddModal = false">
          <div class="modal-content" @click.stop>
            <div class="modal-header">
              <h2>Add New Medication</h2>
              <button @click="showAddModal = false" class="btn-close">✕</button>
            </div>
            <form @submit.prevent="handleAddMedication" class="modal-form">
              <div class="form-group">
                <label>Medication Name *</label>
                <input v-model="newMedication.name" type="text" required />
              </div>

              <div class="form-group">
                <label>Manufacturer</label>
                <input v-model="newMedication.manufacturer" type="text" />
              </div>

              <div class="form-group">
                <label>Description</label>
                <textarea v-model="newMedication.description" rows="3"></textarea>
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label>Unit Price *</label>
                  <input v-model="newMedication.unit_price" type="number" step="0.01" required />
                </div>
                <div class="form-group">
                  <label>Initial Stock *</label>
                  <input v-model="newMedication.stock_quantity" type="number" required />
                </div>
              </div>

              <div class="modal-actions">
                <button type="button" @click="showAddModal = false" class="btn-secondary">
                  Cancel
                </button>
                <button type="submit" class="btn-primary" :disabled="pharmacyStore.loading">
                  {{ pharmacyStore.loading ? 'Adding...' : 'Add Medication' }}
                </button>
              </div>
            </form>
          </div>
        </div>

        <!-- Update Stock Modal -->
        <div v-if="showStockModal" class="modal-overlay" @click="showStockModal = false">
          <div class="modal-content" @click.stop>
            <div class="modal-header">
              <h2>Update Stock: {{ selectedMedication?.name }}</h2>
              <button @click="showStockModal = false" class="btn-close">✕</button>
            </div>
            <form @submit.prevent="handleUpdateStock" class="modal-form">
              <div class="form-group">
                <label>Current Stock</label>
                <input :value="selectedMedication?.stock_quantity" type="text" disabled />
              </div>

              <div class="form-group">
                <label>Quantity to Add/Remove *</label>
                <input v-model="stockQuantity" type="number" required placeholder="Use negative number to remove" />
                <small>Enter positive number to add stock, negative to remove</small>
              </div>

              <div class="modal-actions">
                <button type="button" @click="showStockModal = false" class="btn-secondary">
                  Cancel
                </button>
                <button type="submit" class="btn-primary" :disabled="pharmacyStore.loading">
                  {{ pharmacyStore.loading ? 'Updating...' : 'Update Stock' }}
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
import { usePharmacyStore } from '../../stores/pharmacy'
import Navbar from '../../components/common/Navbar.vue'
import Sidebar from '../../components/common/Sidebar.vue'

const pharmacyStore = usePharmacyStore()

const showAddModal = ref(false)
const showStockModal = ref(false)
const filter = ref('all')
const selectedMedication = ref(null)
const stockQuantity = ref(0)

const newMedication = ref({
  name: '',
  manufacturer: '',
  description: '',
  unit_price: '',
  stock_quantity: '',
})

const setFilter = (newFilter) => {
  filter.value = newFilter
  if (newFilter === 'low_stock') {
    pharmacyStore.fetchMedications({ low_stock: 'true' })
  } else {
    pharmacyStore.fetchMedications()
  }
}

const getStockClass = (quantity) => {
  if (quantity === 0) return 'out-of-stock'
  if (quantity < 10) return 'low-stock'
  return 'in-stock'
}

const getStockStatus = (quantity) => {
  if (quantity === 0) return 'Out of Stock'
  if (quantity < 10) return 'Low Stock'
  return 'In Stock'
}

const handleAddMedication = async () => {
  try {
    await pharmacyStore.createMedication(newMedication.value)
    showAddModal.value = false
    resetForm()
  } catch (error) {
    alert('Failed to add medication')
  }
}

const updateStock = (medication) => {
  selectedMedication.value = medication
  stockQuantity.value = 0
  showStockModal.value = true
}

const handleUpdateStock = async () => {
  try {
    await pharmacyStore.updateStock(selectedMedication.value.id, stockQuantity.value)
    showStockModal.value = false
    selectedMedication.value = null
    stockQuantity.value = 0
  } catch (error) {
    alert('Failed to update stock')
  }
}

const resetForm = () => {
  newMedication.value = {
    name: '',
    manufacturer: '',
    description: '',
    unit_price: '',
    stock_quantity: '',
  }
}

onMounted(() => {
  pharmacyStore.fetchMedications()
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
  background: #388e3c;
  color: white;
  border: none;
  border-radius: 5px;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.3s;
}

.btn-primary:hover {
  background: #2e7d32;
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

.medications-table {
  background: white;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

table {
  width: 100%;
  border-collapse: collapse;
}

thead {
  background: #f5f5f5;
}

th {
  padding: 15px;
  text-align: left;
  font-weight: 600;
  color: #333;
  border-bottom: 2px solid #ddd;
}

td {
  padding: 15px;
  border-bottom: 1px solid #eee;
  color: #666;
}

tr:hover {
  background: #f9f9f9;
}

.stock-badge {
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 500;
}

.in-stock {
  background: #e8f5e9;
  color: #388e3c;
}

.low-stock {
  background: #fff3e0;
  color: #f57c00;
}

.out-of-stock {
  background: #ffebee;
  color: #d32f2f;
}

.btn-small {
  padding: 6px 12px;
  background: #388e3c;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 12px;
  cursor: pointer;
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
.form-group textarea {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 14px;
}

.form-group small {
  color: #999;
  font-size: 12px;
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
