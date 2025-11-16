# MyLessonPlanner

Full-stack lesson planning application with FastAPI backend, MongoDB database, and responsive web UI. Features include lesson plan CRUD operations, AI-powered content generation, and multi-format exports (PDF, DOCX, PowerPoint).

## Quick Start (Backend + Frontend)

### Prerequisites

- **Python 3.9+** (for FastAPI backend)
- **MongoDB 4.4+** (local or cloud instance)
- **Node.js 18+** (optional, for frontend tooling)

### 1. Backend Setup

#### Install Python Dependencies

```powershell
# Clone or navigate to the project directory
cd c:\Users\Windows\Desktop\MyLessonPlanner

# Create a virtual environment (recommended)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

#### Configure Environment Variables

Copy `.env.example` to `.env` and update values:

```powershell
Copy-Item .env.example .env
```

Edit `.env`:

```ini
MONGO_URL="mongodb://localhost:27017"
DB_NAME="lesson_planner_db"
CORS_ORIGINS="http://localhost:3000,http://localhost:8000"
SECRET_KEY="your-secure-secret-key-change-in-production"
```

#### Start MongoDB

##### Option A: Local MongoDB

```powershell
# If MongoDB is installed locally
mongod
```

##### Option B: Docker MongoDB

```powershell
# Pull and run MongoDB in Docker
docker run -d -p 27017:27017 --name mongo mongo:6.0
```

##### Option C: Cloud MongoDB

Use MongoDB Atlas (cloud service):

- Create a free cluster at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- Get your connection string and paste into `MONGO_URL` in `.env`

#### Create Test User

```powershell
python create_user.py --email "teacher@example.com" --name "Test Teacher" --password "password123"
```

#### Start FastAPI Backend

```powershell
# Start the development server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Server will be available at `http://localhost:8000`

- API docs: [`http://localhost:8000/docs`](http://localhost:8000/docs) (Swagger UI)
- ReDoc: [`http://localhost:8000/redoc`](http://localhost:8000/redoc)

### 2. Frontend Setup

#### Option A: Open HTML File Directly

Simply open `index.html` in a web browser. Update the API base URL in the JS if needed:

```javascript
// In index.html, find this line:
const API_BASE_URL = 'http://localhost:8000/api';
```

#### Option B: Serve with Python HTTP Server

```powershell
# In the project directory
python -m http.server 3000
```

Open `http://localhost:3000` in browser.

### 3. Test the Application

#### Login to the App

1. Open the web UI (or `index.html`)
2. Enter credentials:
   - Email: `teacher@example.com`
   - Password: `password123`
3. Click "Login"

#### Create a Lesson Plan

1. Fill in the form fields (subject, grade level, topic, etc.)
2. Click "Generate" (uses Gemini API or fills placeholder data)
3. Click "Save" to store in MongoDB

#### Download Exports

- Click "Download PDF" to get a PDF file (Times New Roman 12pt)
- Click "Download DOCX" to get a Word document (Times New Roman 12pt)
- Click "Download PPTX" (backend endpoint) to get a PowerPoint presentation

## API Endpoints

All endpoints require JWT authentication (Bearer token from login).

### Authentication

- `POST /api/auth/register` — Register a new user
- `POST /api/auth/login` — Login and get access token
- `GET /api/auth/me` — Get current user info

### Lesson Plans

- `POST /api/lesson-plans` — Create lesson plan
- `GET /api/lesson-plans` — List user's lesson plans
- `DELETE /api/lesson-plans/{plan_id}` — Delete a lesson plan
- `GET /api/lesson-plans/{plan_id}/download/word` — Download DOCX
- `GET /api/lesson-plans/{plan_id}/download/pdf` — Download PDF
- `GET /api/lesson-plans/{plan_id}/download/powerpoint` — Download PPTX

### Activities

- `POST /api/activities` — Create activity
- `GET /api/activities` — List activities
- `DELETE /api/activities/{activity_id}` — Delete activity

### Presentations

- `POST /api/presentations` — Create presentation
- `GET /api/presentations` — List presentations
- `DELETE /api/presentations/{presentation_id}` — Delete presentation

## Deployment

### Docker

Build and run with Docker:

```powershell
# Build image with provided base image
docker build --build-arg BASE_IMAGE=fastapi_react_mongo_shadcn_base_image_cloud_arm:release-11112025-1 -t mylessonplanner:latest .

# Run container (expose port 8000 for API)
docker run -it -p 8000:8000 -p 3000:3000 \
  -e MONGO_URL="mongodb://mongo:27017" \
  -e DB_NAME="lesson_planner_db" \
  -e SECRET_KEY="your-secret" \
  -e CORS_ORIGINS="*" \
  mylessonplanner:latest
```

### Docker Compose (Recommended)

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  mongo:
    image: mongo:6.0
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db

  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      MONGO_URL: mongodb://mongo:27017
      DB_NAME: lesson_planner_db
      SECRET_KEY: your-secret-key
      CORS_ORIGINS: "*"
    depends_on:
      - mongo
    command: uvicorn main:app --host 0.0.0.0 --port 8000

  web:
    image: nginx:alpine
    ports:
      - "3000:80"
    volumes:
      - ./index.html:/usr/share/nginx/html/index.html
      - ./styles.css:/usr/share/nginx/html/styles.css

volumes:
  mongo_data:
```

Run with: `docker-compose up -d`

### Cloud Deployment

#### Azure App Service

```powershell
# Install Azure CLI
winget install Microsoft.AzureCLI

# Login
az login

# Create resource group
az group create --name MyLessonPlannerRG --location eastus

# Create App Service plan
az appservice plan create --name MyLessonPlannerPlan --resource-group MyLessonPlannerRG --sku B1

# Create App Service
az webapp create --resource-group MyLessonPlannerRG --plan MyLessonPlannerPlan --name mylessonplanner-api --runtime "PYTHON|3.11"

# Deploy
az webapp deployment source config-zip --resource-group MyLessonPlannerRG --name mylessonplanner-api --src deployment.zip
```

#### AWS Elastic Beanstalk

```powershell
# Install EB CLI
pip install awsebcli

# Initialize
eb init -p python-3.11 mylessonplanner

# Create environment
eb create mylessonplanner-env

# Deploy
eb deploy
```

## Environment Variables Reference

| Variable | Default | Description |
|---|---|---|
| `MONGO_URL` | `mongodb://localhost:27017` | MongoDB connection string |
| `DB_NAME` | `test_database` | MongoDB database name |
| `SECRET_KEY` | See `.env.example` | JWT signing secret (change in production) |
| `CORS_ORIGINS` | `*` | Comma-separated allowed origins |
| `ENV_IMAGE_NAME` | `fastapi_react_mongo_shadcn_base_image_cloud_arm:release-11112025-1` | Docker base image |

## Security Notes

- **Never commit `.env` with real secrets** — use `.env.example` as template only.
- **JWT tokens expire in 7 days** — refresh logic not yet implemented.
- **Passwords are hashed with bcrypt** — never logged or transmitted plaintext.
- **CORS_ORIGINS should be restricted** in production (not `*`).
- **Use HTTPS in production** — configure reverse proxy or load balancer.

## File Exports

All exports use **Times New Roman 12pt** font for consistent professional formatting:

- **PDF**: Generated server-side using ReportLab
- **DOCX**: Generated server-side using python-docx
- **PPTX**: Generated server-side using python-pptx

## Troubleshooting

### MongoDB Connection Error

If you get `pymongo.errors.ServerSelectionTimeoutError`:

1. Ensure MongoDB is running (`mongod` or Docker container)
2. Check `MONGO_URL` in `.env` matches your MongoDB instance
3. For MongoDB Atlas, ensure IP whitelist includes your machine

### API 401 Unauthorized

Ensure:

1. You're logged in (check browser console for access token)
2. Token is included in request headers: `Authorization: Bearer <token>`
3. Token hasn't expired (expires in 7 days)

### CORS Errors

If frontend can't reach API:

1. Ensure `CORS_ORIGINS` in `.env` includes your frontend URL
2. For development, set `CORS_ORIGINS="*"` (not safe for production)

### Export Files Not Generating

1. Check backend logs for errors
2. Ensure all required fonts are available (Times New Roman)
3. Verify file permissions in `/tmp` or temp directory

---

## Quick Local Test: Exports and Server Flow

Follow these minimal steps to verify the save-and-download workflow (PPTX server flow) and the image proxy used for DOCX/PDF inlining.

1. Activate your virtualenv and install dependencies if needed:

```powershell
& C:/Users/Windows/Desktop/MyLessonPlanner/venv/Scripts/Activate.ps1
pip install fastapi uvicorn[standard] motor passlib[bcrypt] python-multipart python-docx python-pptx reportlab httpx
```

2. Create the default owner user (the frontend demo expects these credentials):

```powershell
python create_user.py --default
```

3. Run the API server:

```powershell
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

4. Serve the frontend (recommended so fetch requests have predictable origins):

```powershell
# from project root
python -m http.server 5500
# then open http://localhost:5500/index.html
```

5. In the web UI login modal use either:
- Email: `rxvebxutista@gmail.com` and Password: `Bautista_03202000` (server-backed login)
- OR Username: `Ravebautista` and Password: `Bautista_03202000` (local fallback)

6. Generate a lesson plan and click `PPTX`. If you logged in with server-backed credentials the frontend will POST the plan to `/api/lesson-plans` and then download the server-generated PPTX. If not logged in, the client-side PPTX generator is used as a fallback.

If you want, I can also add a small script to run both the backend and a static file server together.
