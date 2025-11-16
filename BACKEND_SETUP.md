# MyLessonPlanner - Backend Setup Guide

## Files Created

✓ `main.py` — FastAPI application with all routes (auth, CRUD, exports)
✓ `create_user.py` — Script to create test users
✓ `requirements.txt` — Complete Python dependencies
✓ `.env.example` — Environment variable template
✓ `README.md` — Full documentation

## Next Steps (Copy-Paste Commands)

### 1. Create Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 3. Setup MongoDB

#### Option: Docker (Easiest)

```powershell
docker run -d -p 27017:27017 --name mongo mongo:6.0
```

#### Option: Local MongoDB

```powershell
mongod
```

### 4. Create .env File

```powershell
Copy-Item .env.example .env
```

Edit `.env` with your settings (defaults work for local dev)

### 5. Create Test User

```powershell
python create_user.py --email "teacher@example.com" --name "Test Teacher" --password "password123"
```

### 6. Start Backend

```powershell
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 7. Access Frontend

- API Docs: [`http://localhost:8000/docs`](http://localhost:8000/docs)
- Frontend: Open `index.html` in browser
- Login with: `teacher@example.com` / `password123`

## What's Included

### FastAPI Endpoints

**Auth:**

- POST `/api/auth/register` — Register user
- POST `/api/auth/login` — Get JWT token
- GET `/api/auth/me` — Get current user

**Lesson Plans:**

- POST `/api/lesson-plans` — Create
- GET `/api/lesson-plans` — List
- DELETE `/api/lesson-plans/{id}` — Delete
- GET `/api/lesson-plans/{id}/download/word` — DOCX
- GET `/api/lesson-plans/{id}/download/pdf` — PDF
- GET `/api/lesson-plans/{id}/download/powerpoint` — PPTX

**Activities & Presentations:** Similar CRUD endpoints

### Database Models

- `User` — Authentication & profiles
- `LessonPlan` — Main lesson content
- `Activity` — Class activities
- `Presentation` — Presentation slides

### Security

- JWT authentication (7-day tokens)
- Bcrypt password hashing
- CORS middleware
- HTTP Bearer auth

## Troubleshooting

**MongoDB not connecting?**

- Ensure MongoDB is running on port 27017
- Check MONGO_URL in .env

**Port 8000 already in use?**

```powershell
uvicorn main:app --port 9000  # Use different port
```

**Import errors?**

```powershell
pip list  # Verify all packages installed
pip install -r requirements.txt --force-reinstall
```

Ready to go! The backend is fully functional and ready for frontend integration.
