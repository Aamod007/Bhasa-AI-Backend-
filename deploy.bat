@echo off
REM Deployment Helper Script for Bhasa-AI Backend (Windows)
REM This script helps you prepare and deploy to Railway

echo ==========================================
echo Bhasa-AI Backend - Railway Deployment
echo ==========================================
echo.

REM Check if git is initialized
if not exist ".git" (
    echo [32m📦 Initializing Git repository...[0m
    git init
    git add .
    git commit -m "Initial commit - Bhasa-AI Backend"
    git branch -M main
    echo [32m✅ Git initialized[0m
) else (
    echo [32m✅ Git repository already exists[0m
)

echo.
echo ==========================================
echo Next Steps:
echo ==========================================
echo 1. Create a GitHub repository for your backend
echo 2. Run: git remote add origin YOUR-REPO-URL
echo 3. Run: git push -u origin main
echo 4. Go to https://railway.app
echo 5. Click 'New Project' -^> 'Deploy from GitHub repo'
echo 6. Select your backend repository
echo 7. Railway will auto-deploy using railway.toml
echo 8. Get your Railway URL after deployment
echo 9. Update VITE_RAILWAY_API_URL in Vercel
echo.
echo ==========================================
echo Useful Commands:
echo ==========================================
echo Test locally: python main.py
echo Run tests: python test_api.py
echo Check status: git status
echo Push to GitHub: git push
echo.

pause