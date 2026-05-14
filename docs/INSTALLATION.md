# Installation Guide - Roadmap AI Tools

## Prerequisites

Before starting, ensure you have:

- **Node.js 18+** - [Download](https://nodejs.org/)
- **Python 3.10+** - [Download](https://www.python.org/)
- **MongoDB Atlas Account** - [Create Free](https://www.mongodb.com/cloud/atlas)
- **Git** - [Download](https://git-scm.com/)
- **Code Editor** - VS Code recommended

## Step 1: Clone Repository

```bash
git clone https://github.com/infoaliali0-design/roadmap-ai-tools.git
cd roadmap-ai-tools
```

## Step 2: Backend Setup (Python Flask)

### 2.1 Create Virtual Environment

```bash
cd backend

# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2.2 Install Dependencies

```bash
pip install -r requirements.txt
```

### 2.3 Setup Environment Variables

```bash
cp .env.example .env
```

**Edit .env file with your configuration:**

```env
# Flask Configuration
FLASK_ENV=development
FLASK_APP=run.py
FLASK_DEBUG=True

# Database - MongoDB Atlas Connection String
DATABASE_URL=mongodb+srv://username:password@cluster.mongodb.net/roadmap_ai?retryWrites=true&w=majority

# JWT Authentication
JWT_SECRET_KEY=your-super-secret-key-change-this-in-production
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24

# Google OAuth
GOOGLE_CLIENT_ID=your-google-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-google-client-secret
GOOGLE_REDIRECT_URI=http://localhost:5000/api/auth/google/callback

# CORS Configuration
CORS_ORIGINS=http://localhost:3000

# Email Configuration (Gmail SMTP)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
SMTP_FROM_EMAIL=noreply@roadmapaitools.com

# AWS S3 Configuration (Optional)
AWS_ACCESS_KEY_ID=your-aws-key
AWS_SECRET_ACCESS_KEY=your-aws-secret
AWS_S3_BUCKET=roadmap-ai-uploads
AWS_REGION=us-east-1

# File Upload Configuration
MAX_FILE_SIZE=52428800  # 50MB in bytes
ALLOWED_EXTENSIONS=pdf,docx,xlsx,pptx,jpg,jpeg,png,gif,webp,txt

# Pagination
PAGINATION_LIMIT=20

# Server Configuration
HOST=0.0.0.0
PORT=5000
```

### 2.4 Setup MongoDB Atlas

1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create a free account
3. Create a new project
4. Create a cluster (free tier available)
5. Create a database user:
   - Username: `roadmap_user`
   - Password: Generate strong password
6. Get connection string:
   - Click "Connect"
   - Select "Connect your application"
   - Copy connection string
7. Replace credentials in .env

### 2.5 Run Backend

```bash
# Make sure venv is activated
python run.py
```

You should see:
```
🚀 Starting Roadmap AI Tools API
📍 Server: http://0.0.0.0:5000
🔧 Environment: development
✨ Ready to handle AI workflows and file conversions!
```

Backend is now running on: **http://localhost:5000**

## Step 3: Frontend Setup (Next.js)

### 3.1 Install Dependencies

```bash
cd ../frontend
npm install
```

This installs all dependencies including:
- React 18
- Next.js 14
- TypeScript
- Tailwind CSS
- Framer Motion
- React Query
- Zustand
- next-auth
- And more (30+ packages)

### 3.2 Setup Environment Variables

```bash
cp .env.local.example .env.local
```

**Edit .env.local file:**

```env
# API Configuration
NEXT_PUBLIC_API_URL=http://localhost:5000
NEXT_PUBLIC_APP_URL=http://localhost:3000

# Google OAuth
NEXT_PUBLIC_GOOGLE_CLIENT_ID=your-google-client-id.apps.googleusercontent.com

# Analytics (Optional)
NEXT_PUBLIC_GA_ID=G-XXXXXXXXXX

# Feature Flags
NEXT_PUBLIC_ENABLE_BLOG=true
NEXT_PUBLIC_ENABLE_ANALYTICS=true
NEXT_PUBLIC_ENABLE_PREMIUM=false
```

### 3.3 Get Google OAuth Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (name: "Roadmap AI Tools")
3. Enable Google+ API:
   - Search for "Google+ API"
   - Click Enable
4. Create OAuth 2.0 credentials:
   - Go to "Create Credentials" → "OAuth client ID"
   - Select "Web application"
   - Add authorized redirect URIs:
     ```
     http://localhost:3000
     http://localhost:3000/api/auth/callback/google
     http://localhost:5000/api/auth/google/callback
     ```
   - Copy Client ID and Client Secret
5. Add to .env files

### 3.4 Run Frontend

```bash
npm run dev
```

You should see:
```
▲ Next.js 14.0.0
- Local:        http://localhost:3000
- Environments: .env.local

✓ Ready in 2.3s
```

Frontend is now running on: **http://localhost:3000**

## Step 4: Verify Installation

### Check Backend Health

Open terminal and run:
```bash
curl http://localhost:5000/api/health
```

Expected response:
```json
{
  "status": "healthy",
  "service": "Roadmap AI Tools API",
  "version": "1.0.0",
  "timestamp": "2024-01-10T12:00:00"
}
```

### Check Frontend

Visit in browser: `http://localhost:3000`

You should see the homepage loading.

## Troubleshooting

### Python venv not activating

```bash
# Windows (Command Prompt)
venv\Scripts\activate.bat

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# macOS/Linux
source venv/bin/activate
```

### Port already in use

```bash
# Kill process on port 5000 (Backend)
lsof -ti:5000 | xargs kill -9

# Kill process on port 3000 (Frontend)
lsof -ti:3000 | xargs kill -9

# Windows: Use Task Manager or
netstat -ano | findstr :5000
```

### MongoDB Connection Error

1. **Verify connection string:**
   - Check username and password
   - Ensure no special characters or URL encoding issues

2. **IP Whitelist:**
   - Go to MongoDB Atlas
   - Network Access
   - Add your IP or 0.0.0.0/0 for development

3. **Database existence:**
   - MongoDB creates database automatically
   - First connection creates the database

### Module not found errors

```bash
# Backend
pip install -r requirements.txt --force-reinstall

# Frontend
rm -rf node_modules package-lock.json
npm install
```

### CORS errors

Ensure frontend URL is in `CORS_ORIGINS` environment variable:
```env
CORS_ORIGINS=http://localhost:3000
```

## Next Steps

✅ Setup complete! Now:

1. **Customize branding** - Update colors, logos
2. **Implement components** - Frontend pages and components
3. **Implement routes** - Backend API endpoints
4. **Add database models** - User, Tools, Blog, etc.
5. **Implement authentication** - JWT, Google OAuth
6. **Add file converters** - PDF, Image, Office conversions
7. **Setup payment** - Optional premium features
8. **Deploy to production** - See DEPLOYMENT.md

## Useful Commands

```bash
# Backend
python run.py              # Start development server
python -m pip list         # List installed packages
pip install <package>     # Install new package

# Frontend
npm run dev                # Start development server
npm run build              # Build for production
npm run lint               # Run ESLint
npm run type-check         # Check TypeScript
npm run format             # Format code with Prettier
```

## Support

If you encounter issues:

1. Check the documentation
2. Review error messages carefully
3. Search similar issues on GitHub
4. Contact support@roadmapaitools.com
