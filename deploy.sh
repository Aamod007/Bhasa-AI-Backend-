#!/bin/bash

# Deployment Helper Script for Bhasa-AI Backend
# This script helps you prepare and deploy to Railway

echo "=========================================="
echo "Bhasa-AI Backend - Railway Deployment"
echo "=========================================="
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit - Bhasa-AI Backend"
    git branch -M main
    echo "✅ Git initialized"
else
    echo "✅ Git repository already exists"
fi

# Check if remote is set
REMOTE=$(git remote -v)
if [ -z "$REMOTE" ]; then
    echo ""
    echo "⚠️  No remote repository found."
    echo "Please create a GitHub repository and run:"
    echo "git remote add origin <your-repo-url>"
    echo "git push -u origin main"
else
    echo "✅ Remote repository configured"
    echo "$REMOTE"
fi

echo ""
echo "=========================================="
echo "Next Steps:"
echo "=========================================="
echo "1. Create a GitHub repository for your backend"
echo "2. Push this code to GitHub"
echo "3. Go to https://railway.app"
echo "4. Click 'New Project' → 'Deploy from GitHub repo'"
echo "5. Select your backend repository"
echo "6. Railway will auto-deploy using railway.toml"
echo "7. Get your Railway URL after deployment"
echo "8. Update VITE_RAILWAY_API_URL in Vercel"
echo ""
echo "=========================================="
echo "Useful Commands:"
echo "=========================================="
echo "Test locally: python main.py"
echo "Run tests: python test_api.py"
echo "Check status: git status"
echo "Commit changes: git add . && git commit -m 'your message'"
echo "Push to GitHub: git push"
echo ""