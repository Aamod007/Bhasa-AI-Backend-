    # 🚀 Complete Setup Guide - Bhasa-AI with Separate Repositories

This guide walks you through setting up Bhasa-AI with separate frontend (Vercel) and backend (Railway) deployments.

## 📋 Overview

- **Frontend**: React + TypeScript → Deployed on Vercel
- **Backend**: FastAPI + Python → Deployed on Railway
- **Communication**: REST API via HTTPS

## 🎯 Quick Start (5 Steps)

### Step 1: Prepare Backend Repository

Your backend is ready at: `C:\Users\ASUS\OneDrive\Desktop\Bhasa-AI-Backend`

```bash
cd C:\Users\ASUS\OneDrive\Desktop\Bhasa-AI-Backend
```

### Step 2: Create GitHub Repository for Backend

1. Go to GitHub and create a new repository (e.g., `Bhasa-AI-Backend`)
2. **Don't** initialize with README (we already have files)
3. Copy the repository URL

### Step 3: Push Backend to GitHub

```bash
# In the Bhasa-AI-Backend directory
git init
git add .
git commit -m "Initial commit - Bhasa-AI Backend"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/Bhasa-AI-Backend.git
git push -u origin main
```

### Step 4: Deploy Backend to Railway

1. Go to [Railway](https://railway.app)
2. Sign in with GitHub
3. Click **"New Project"**
4. Select **"Deploy from GitHub repo"**
5. Choose your `Bhasa-AI-Backend` repository
6. Railway will automatically:
   - Detect `railway.toml`
   - Install dependencies from `requirements.txt`
   - Start the server
7. Wait for deployment to complete
8. Click on your project → **"Settings"** → Find your Railway URL
   - Example: `https://bhasa-ai-backend.railway.app`
9. **Copy this URL** - you'll need it next!

### Step 5: Update Frontend Environment Variables

#### On Vercel:

1. Go to your Vercel project dashboard
2. Navigate to **Settings** → **Environment Variables**
3. Add new variable:
   ```
   Name: VITE_RAILWAY_API_URL
   Value: https://bhasa-ai-backend.railway.app (your Railway URL)
   ```
4. Select **All** environments (Production, Preview, Development)
5. Click **Save**
6. Go to **Deployments** → Click **"Redeploy"** on latest deployment

#### That's it! 🎉

Your app should now work with:
- Frontend: `https://your-app.vercel.app`
- Backend: `https://bhasa-ai-backend.railway.app`

## 🧪 Testing

### Test Backend Directly

Visit these URLs in your browser (replace with your Railway URL):

1. **Health Check**: `https://bhasa-ai-backend.railway.app/health`
   - Should return: `{"status": "healthy", ...}`

2. **API Docs**: `https://bhasa-ai-backend.railway.app/docs`
   - Interactive API documentation

3. **Stats**: `https://bhasa-ai-backend.railway.app/api/stats`
   - API statistics

### Test Frontend Integration

1. Open your Vercel frontend URL
2. Try translating text
3. Open DevTools (F12) → Network tab
4. You should see API calls to your Railway backend

## 📁 Repository Structure

### Backend Repository (`Bhasa-AI-Backend`)

```
Bhasa-AI-Backend/
├── app/
│   ├── api/routes.py       # API endpoints
│   ├── models/schemas.py   # Data models
│   └── services/translator.py
├── main.py                 # FastAPI app
├── requirements.txt        # Dependencies
├── railway.toml           # Railway config
├── Procfile               # Alternative config
├── README.md              # Documentation
└── test_api.py            # Test script
```

### Frontend Repository (Your existing Vercel repo)

Keep your existing frontend repository as is. Just update the environment variable.

## 🔧 Local Development

### Running Backend Locally

```bash
cd Bhasa-AI-Backend

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server
python main.py
```

Backend will run at: `http://localhost:8000`

### Running Frontend Locally with Railway Backend

In your frontend project, create `.env.local`:

```env
VITE_RAILWAY_API_URL=https://your-railway-url.railway.app
```

Then run:
```bash
npm run dev
```

### Running Both Locally

Backend:
```bash
cd Bhasa-AI-Backend
python main.py
```

Frontend (in another terminal):
```bash
cd Bhasa-AI
npm run dev
```

Frontend will use `http://localhost:8000` automatically in development.

## 🐛 Troubleshooting

### Backend not deploying on Railway

**Check:**
- ✅ `requirements.txt` exists
- ✅ `railway.toml` exists
- ✅ GitHub repository is public or Railway has access
- ✅ Check Railway logs for errors

### Frontend can't connect to backend

**Check:**
- ✅ Railway backend is running (green status)
- ✅ `VITE_RAILWAY_API_URL` is set in Vercel
- ✅ Environment variable value is correct (no trailing slash)
- ✅ Frontend was redeployed after adding env variable

### CORS errors

Update `main.py` in backend:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-vercel-app.vercel.app"],  # Your Vercel domain
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Then commit and push to GitHub. Railway will auto-deploy.

### Translation not working

1. **Check Railway logs** (Railway dashboard → View logs)
2. **Test backend directly**: Visit `/health` endpoint
3. **Check browser console**: Look for errors
4. **Verify env variable**: Make sure it's set correctly

## 📊 Monitoring

### Railway Dashboard

- View logs: Click on project → Logs
- Check metrics: CPU, Memory, Network usage
- Monitor deployments: See build and deploy status

### Vercel Dashboard

- View deployments: See all builds
- Check logs: Click on deployment → View function logs
- Monitor analytics: Check usage and performance

## 🔄 Making Updates

### Updating Backend

```bash
cd Bhasa-AI-Backend

# Make your changes
# Edit files...

# Commit and push
git add .
git commit -m "Your update description"
git push

# Railway auto-deploys from GitHub!
```

### Updating Frontend

```bash
cd Bhasa-AI

# Make your changes
# Edit files...

# Commit and push
git add .
git commit -m "Your update description"
git push

# Vercel auto-deploys from GitHub!
```

## 🎯 Best Practices

### Security

1. **Use environment variables** for sensitive data
2. **Configure CORS** properly in production
3. **Monitor Railway logs** for suspicious activity
4. **Keep dependencies updated**

### Performance

1. **Monitor Railway metrics** (CPU, Memory)
2. **Check response times** in Vercel analytics
3. **Optimize translations** for common language pairs
4. **Use Railway's auto-scaling**

### Maintenance

1. **Check logs regularly** (Railway + Vercel)
2. **Update dependencies** monthly
3. **Test after updates**
4. **Keep README updated**

## 📞 Support Resources

- **Railway Docs**: https://docs.railway.app
- **Vercel Docs**: https://vercel.com/docs
- **FastAPI Docs**: https://fastapi.tiangolo.com
- **React Docs**: https://react.dev

## ✅ Deployment Checklist

- [ ] Backend code pushed to GitHub
- [ ] Backend deployed on Railway
- [ ] Railway URL obtained
- [ ] Railway health check passing
- [ ] `VITE_RAILWAY_API_URL` set in Vercel
- [ ] Frontend redeployed
- [ ] Translation feature tested
- [ ] No CORS errors
- [ ] API documentation accessible
- [ ] Both apps in production

## 🎉 Success!

Once all checklist items are complete, your app is fully deployed with:

- ✅ Frontend on Vercel (fast, global CDN)
- ✅ Backend on Railway (scalable, reliable)
- ✅ Automatic deployments from GitHub
- ✅ Professional setup with separate concerns

---

**Made with ❤️ for Bhasa-AI**

For questions or issues, check the troubleshooting section or review the Railway/Vercel logs.
