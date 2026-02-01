# Django Backend Setup Instructions

## Files to Copy

Copy these files to your Django project:

1. **hosp_app/models.py** - Database models
2. **hosp_app/serializers.py** - DRF serializers
3. **hosp_app/permissions.py** - Custom permissions
4. **hosp_app/views.py** - ViewSets
5. **hosp_app/urls.py** - App URLs
6. **hosp_app/admin.py** - Admin configuration
7. **hospital_management/urls.py** - Main project URLs (use main_urls.py)
8. **hospital_management/settings.py** - Update with settings_snippet.py

## Step-by-Step Setup

### 1. Create Django Project and App

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Django
pip install django

# Create project
django-admin startproject hospital_management
cd hospital_management

# Create app
python manage.py startapp hosp_app
```

### 2. Install Dependencies

Create `requirements.txt`:
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

Install:
```bash
pip install -r requirements.txt
```

### 3. Create .env file

Create `.env` in the project root:
```env
SECRET_KEY=django-insecure-your-secret-key-here-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 4. Update settings.py

Copy content from `settings_snippet.py` and update your `hospital_management/settings.py`

Key changes:
- Add installed apps
- Add middleware
- Configure REST_FRAMEWORK
- Configure SIMPLE_JWT
- Configure CORS
- Set AUTH_USER_MODEL

### 5. Update URLs

Replace `hospital_management/urls.py` with content from `main_urls.py`

### 6. Copy App Files

Copy all the generated files to their respective locations:
- models.py → hosp_app/models.py
- serializers.py → hosp_app/serializers.py
- permissions.py → hosp_app/permissions.py
- views.py → hosp_app/views.py
- urls.py → hosp_app/urls.py
- admin.py → hosp_app/admin.py

### 7. Create Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Create Superuser

```bash
python manage.py createsuperuser
```

### 9. Run Server

```bash
python manage.py runserver
```

Your API will be available at: http://127.0.0.1:8000/api/

## API Endpoints

### Authentication
- POST `/api/auth/login/` - Login (get JWT tokens)
- POST `/api/auth/refresh/` - Refresh access token

### Users
- GET `/api/users/` - List users
- POST `/api/users/` - Create user (register)
- GET `/api/users/me/` - Get current user profile

### Patients
- GET `/api/patients/` - List patients
- POST `/api/patients/` - Create patient (Doctor/Nurse)
- GET `/api/patients/{id}/` - Get patient details
- PUT `/api/patients/{id}/` - Update patient
- DELETE `/api/patients/{id}/` - Delete patient
- GET `/api/patients/{id}/appointments/` - Get patient appointments
- GET `/api/patients/{id}/medical_records/` - Get patient medical records
- GET `/api/patients/{id}/prescriptions/` - Get patient prescriptions

### Appointments
- GET `/api/appointments/` - List appointments
- POST `/api/appointments/` - Create appointment (Doctor/Nurse)
- GET `/api/appointments/{id}/` - Get appointment details
- PUT `/api/appointments/{id}/` - Update appointment
- DELETE `/api/appointments/{id}/` - Delete appointment
- POST `/api/appointments/{id}/complete/` - Mark as completed
- POST `/api/appointments/{id}/cancel/` - Cancel appointment

### Medical Records
- GET `/api/medical-records/` - List medical records
- POST `/api/medical-records/` - Create record (Doctor/Nurse)
- GET `/api/medical-records/{id}/` - Get record details
- PUT `/api/medical-records/{id}/` - Update record
- DELETE `/api/medical-records/{id}/` - Delete record

### Medications
- GET `/api/medications/` - List medications
- POST `/api/medications/` - Create medication (Pharmacist)
- GET `/api/medications/{id}/` - Get medication details
- PUT `/api/medications/{id}/` - Update medication (Pharmacist)
- DELETE `/api/medications/{id}/` - Delete medication (Pharmacist)
- POST `/api/medications/{id}/update_stock/` - Update stock (Pharmacist)

### Prescriptions
- GET `/api/prescriptions/` - List prescriptions
- POST `/api/prescriptions/` - Create prescription (Doctor only)
- GET `/api/prescriptions/{id}/` - Get prescription details
- PUT `/api/prescriptions/{id}/` - Update prescription (Doctor)
- DELETE `/api/prescriptions/{id}/` - Delete prescription
- POST `/api/prescriptions/{id}/dispense/` - Dispense prescription (Pharmacist only)
- POST `/api/prescriptions/{id}/cancel/` - Cancel prescription (Doctor only)

## Role-Based Permissions

### Doctor
- Can create/view/update patients
- Can create/view/update appointments (only their own)
- Can create/view/update medical records
- Can create/view/update/cancel prescriptions (only their own)
- Can view medications

### Nurse
- Can create/view/update patients
- Can create/view/update appointments
- Can create/view/update medical records
- Can view prescriptions
- Can view medications

### Pharmacist
- Can view patients
- Can view appointments
- Can view medical records
- Can view/dispense prescriptions
- Can create/view/update medications
- Can update medication stock

## Testing with cURL

### Register a new doctor:
```bash
curl -X POST http://127.0.0.1:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "doctor1",
    "password": "securepass123",
    "email": "doctor1@hospital.com",
    "first_name": "John",
    "last_name": "Doe",
    "role": "doctor",
    "phone": "1234567890"
  }'
```

### Login:
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "doctor1",
    "password": "securepass123"
  }'
```

This will return access and refresh tokens.

### Create a patient (with JWT token):
```bash
curl -X POST http://127.0.0.1:8000/api/patients/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "first_name": "Jane",
    "last_name": "Smith",
    "date_of_birth": "1990-05-15",
    "gender": "F",
    "phone": "9876543210",
    "email": "jane@example.com",
    "address": "123 Main St, City",
    "blood_group": "O+"
  }'
```

## Admin Panel

Access the Django admin panel at: http://127.0.0.1:8000/admin/

Login with your superuser credentials to manage all data.

## Next Steps

1. Test all endpoints with Postman or similar tool
2. Create some sample data
3. Build the Vue.js frontend to consume this API
4. Implement additional features as needed

## Notes

- JWT tokens expire after 60 minutes (configurable in settings)
- All endpoints require authentication except user registration and login
- Role-based permissions are enforced automatically
- Pagination is enabled (20 items per page)