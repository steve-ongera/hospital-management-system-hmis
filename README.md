# Hospital Management System - Setup Guide
## Django (Single App) + Vue.js

## Directory Structure

```
hospital-management-system/
├── backend/
│   ├── hospital_management/           # Django project
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   │
│   ├── hosp_app/                      # Single Django app
│   │   ├── migrations/
│   │   │   └── __init__.py
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── create_roles.py
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py                  # All models here
│   │   ├── serializers.py             # All serializers
│   │   ├── views.py                   # All views
│   │   ├── urls.py                    # All URL patterns
│   │   ├── permissions.py             # Role-based permissions
│   │   └── tests.py
│   │
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env
│   └── .gitignore
│
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   └── favicon.ico
│   │
│   ├── src/
│   │   ├── assets/
│   │   │   └── main.css
│   │   │
│   │   ├── components/
│   │   │   ├── common/
│   │   │   │   ├── Navbar.vue
│   │   │   │   ├── Sidebar.vue
│   │   │   │   └── DataTable.vue
│   │   │   │
│   │   │   ├── doctor/
│   │   │   │   ├── PatientList.vue
│   │   │   │   ├── AppointmentCalendar.vue
│   │   │   │   └── PrescriptionForm.vue
│   │   │   │
│   │   │   ├── nurse/
│   │   │   │   ├── VitalSignsForm.vue
│   │   │   │   ├── PatientAdmission.vue
│   │   │   │   └── MedicalRecordForm.vue
│   │   │   │
│   │   │   └── pharmacist/
│   │   │       ├── MedicationInventory.vue
│   │   │       ├── DispensePrescription.vue
│   │   │       └── StockManagement.vue
│   │   │
│   │   ├── views/
│   │   │   ├── auth/
│   │   │   │   └── Login.vue
│   │   │   │
│   │   │   ├── doctor/
│   │   │   │   ├── DoctorDashboard.vue
│   │   │   │   ├── MyPatients.vue
│   │   │   │   └── MyAppointments.vue
│   │   │   │
│   │   │   ├── nurse/
│   │   │   │   ├── NurseDashboard.vue
│   │   │   │   └── PatientCare.vue
│   │   │   │
│   │   │   └── pharmacist/
│   │   │       ├── PharmacistDashboard.vue
│   │   │       ├── Inventory.vue
│   │   │       └── Prescriptions.vue
│   │   │
│   │   ├── router/
│   │   │   └── index.js
│   │   │
│   │   ├── stores/                    # Pinia stores
│   │   │   ├── auth.js
│   │   │   ├── patient.js
│   │   │   ├── appointment.js
│   │   │   └── pharmacy.js
│   │   │
│   │   ├── services/                  # API services
│   │   │   ├── api.js
│   │   │   ├── authService.js
│   │   │   ├── patientService.js
│   │   │   ├── appointmentService.js
│   │   │   └── pharmacyService.js
│   │   │
│   │   ├── utils/
│   │   │   ├── auth.js
│   │   │   └── constants.js
│   │   │
│   │   ├── App.vue
│   │   └── main.js
│   │
│   ├── package.json
│   ├── vite.config.js
│   ├── .env
│   └── .gitignore
│
├── .gitignore
└── README.md
```

---

## Installation Steps

### 1. Backend Setup (Django)

#### Create `backend/requirements.txt`:
```txt
Django==5.0
djangorestframework==3.14.0
djangorestframework-simplejwt==5.3.1
django-cors-headers==4.3.1
python-decouple==3.8
psycopg2-binary==2.9.9
Pillow==10.1.0
django-filter==23.5
```

#### Installation Commands:
```bash
# Navigate to project root
mkdir hospital-management-system
cd hospital-management-system

# Create backend directory
mkdir backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install Django first
pip install django

# Create Django project
django-admin startproject hospital_management .

# Create requirements.txt (as shown above)
# Then install all dependencies
pip install -r requirements.txt

# Create the single app
python manage.py startapp hosp_app
```

---

### 2. Frontend Setup (Vue.js)

#### Prerequisites:
- Node.js (v18 or higher recommended)
- npm (comes with Node.js)

#### Installation Commands:
```bash
# Navigate to project root
cd hospital-management-system

# Create Vue project
npm create vue@latest frontend

# When prompted, select:
# ✔ Add TypeScript? › No
# ✔ Add JSX Support? › No
# ✔ Add Vue Router? › Yes
# ✔ Add Pinia? › Yes
# ✔ Add Vitest? › No
# ✔ Add ESLint? › Yes
# ✔ Add Prettier? › Yes

# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Install additional packages
npm install axios
npm install @vueuse/core
npm install date-fns
```

#### Optional - Add Tailwind CSS (Recommended):
```bash
cd frontend
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

---

## Environment Configuration

### Backend `.env` file:
Create `backend/.env`:
```env
SECRET_KEY=your-secret-key-here-generate-a-strong-one
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (SQLite for development)
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3

# Or PostgreSQL for production
# DB_ENGINE=django.db.backends.postgresql
# DB_NAME=hospital_db
# DB_USER=postgres
# DB_PASSWORD=yourpassword
# DB_HOST=localhost
# DB_PORT=5432

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173

# JWT
ACCESS_TOKEN_LIFETIME=60
REFRESH_TOKEN_LIFETIME=1440
```

### Frontend `.env` file:
Create `frontend/.env`:
```env
VITE_API_BASE_URL=http://127.0.0.1:8000/api
```

---

## Quick Start Commands

### Backend (Django):
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

**Backend will run at:** `http://127.0.0.1:8000`

### Frontend (Vue):
```bash
cd frontend

# Run development server
npm run dev
```

**Frontend will run at:** `http://localhost:5173`

---

## System Roles

The system will have 3 main roles:

1. **Doctor**
   - View/manage patients
   - Create/view appointments
   - Write prescriptions
   - View medical records

2. **Nurse**
   - View patients
   - Record vital signs
   - Update medical records
   - Manage patient admissions

3. **Pharmacist**
   - View prescriptions
   - Dispense medications
   - Manage medication inventory
   - Track stock levels

---

## Core Features to Implement

### Backend (hosp_app):
- User authentication with roles (Doctor, Nurse, Pharmacist)
- Patient management (CRUD)
- Appointment scheduling
- Prescription management
- Medical records
- Medication inventory
- Role-based permissions

### Frontend:
- Login/Authentication
- Role-based dashboards
- Patient management interface
- Appointment calendar
- Prescription forms
- Inventory management
- Responsive design

---

## Database Models (in hosp_app/models.py)

Key models to create:
- `User` (Custom user with role field)
- `Patient`
- `Appointment`
- `MedicalRecord`
- `Prescription`
- `Medication`
- `MedicationDispense`

---

## API Endpoints Structure

```
/api/auth/
  - POST /login/
  - POST /register/
  - POST /logout/
  - POST /refresh/

/api/patients/
  - GET, POST /
  - GET, PUT, DELETE /{id}/

/api/appointments/
  - GET, POST /
  - GET, PUT, DELETE /{id}/

/api/prescriptions/
  - GET, POST /
  - GET, PUT, DELETE /{id}/

/api/medications/
  - GET, POST /
  - GET, PUT, DELETE /{id}/

/api/medical-records/
  - GET, POST /
  - GET, PUT, DELETE /{id}/
```

---

## Next Steps

1. Set up the backend configuration in `settings.py`
2. Create models in `hosp_app/models.py`
3. Create serializers in `hosp_app/serializers.py`
4. Create views in `hosp_app/views.py`
5. Configure URLs in `hosp_app/urls.py`
6. Set up frontend routing
7. Create API service layer
8. Build Vue components
9. Implement authentication flow
10. Test and deploy

---

## Git Ignore Files

### Backend `.gitignore`:
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
*.sqlite3
.env

# Django
*.log
local_settings.py
db.sqlite3
media/
staticfiles/
```

### Frontend `.gitignore`:
```
# Node
node_modules/
dist/
.DS_Store

# Env
.env
.env.local
.env.*.local

# Editor
.vscode/
.idea/
*.swp
*.swo
```

---

## Recommended Development Tools

- **Backend IDE:** PyCharm, VS Code with Python extensions
- **Frontend IDE:** VS Code with Volar extension
- **API Testing:** Postman or Thunder Client
- **Database:** DB Browser for SQLite (development), pgAdmin (PostgreSQL)
- **Version Control:** Git

---

Would you like me to start creating the actual code files for the models, views, or frontend components?