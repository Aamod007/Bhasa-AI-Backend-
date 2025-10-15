# Render Deployment Guide for Bhasa-AI Backend

This guide will help you deploy your Bhasa-AI Translation API to Render.

## Prerequisites

- A [Render account](https://render.com) (free tier available)
- Your code pushed to a GitHub repository
- Python 3.11+ application

## Deployment Steps

### Option 1: Using render.yaml (Blueprint - Recommended)

1. **Push your code to GitHub** (if not already done)
   ```bash
   git add .
   git commit -m "Add Render configuration"
   git push origin main
   ```

2. **Deploy on Render**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click **"New +"** → **"Blueprint"**
   - Connect your GitHub repository
   - Render will automatically detect the `render.yaml` file
   - Review the configuration and click **"Apply"**

3. **Wait for deployment**
   - Render will automatically build and deploy your application
   - You'll get a URL like: `https://bhasa-ai-backend.onrender.com`

### Option 2: Manual Web Service Setup

1. **Create a new Web Service**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click **"New +"** → **"Web Service"**
   - Connect your GitHub repository

2. **Configure the service**
   - **Name**: `bhasa-ai-backend` (or your preferred name)
   - **Region**: Choose closest to your users
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Free (or choose paid plan)

3. **Environment Variables** (optional)
   - Add any custom environment variables if needed
   - `PYTHON_VERSION`: `3.11.0`

4. **Create Web Service**
   - Click **"Create Web Service"**
   - Wait for the deployment to complete

## Post-Deployment

### 1. Access Your API
Your API will be available at: `https://your-service-name.onrender.com`

### 2. Test the Endpoints

**Health Check:**
```bash
curl https://your-service-name.onrender.com/health
```

**API Documentation:**
- Swagger UI: `https://your-service-name.onrender.com/docs`
- ReDoc: `https://your-service-name.onrender.com/redoc`

**Translation Test:**
```bash
curl -X POST https://your-service-name.onrender.com/translate \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello", "target_language": "es"}'
```

### 3. Update CORS Settings
If you have a frontend deployed on Vercel or elsewhere:

1. Edit `main.py` and update the CORS origins:
   ```python
   allow_origins=[
       "https://your-frontend-domain.vercel.app",
       "http://localhost:3000"  # for local development
   ]
   ```

2. Push changes and Render will auto-deploy

## Important Notes

### Free Tier Limitations
- **Cold Starts**: Free tier services spin down after 15 minutes of inactivity
- **First request** after inactivity may take 30-60 seconds
- For production, consider upgrading to a paid plan

### Performance Optimization
- Free tier is suitable for testing and low-traffic applications
- For production, use **Starter** plan or higher
- Consider adding Redis for caching if needed

### Monitoring
- Check logs in the Render dashboard under **Logs** tab
- Set up **Health Checks** to monitor uptime
- Monitor response times and errors

## Troubleshooting

### Build Fails
- Check `requirements.txt` for conflicting dependencies
- Ensure Python version is compatible
- Check build logs in Render dashboard

### Application Won't Start
- Verify the start command is correct
- Check application logs for errors
- Ensure port binding uses `$PORT` environment variable

### 502 Bad Gateway
- Application may be crashing on startup
- Check logs for error messages
- Verify all dependencies are installed

### Slow Cold Starts
- This is normal on free tier
- Upgrade to paid plan for persistent instances
- Consider using a cron job to keep service warm

## Updating Your Application

Render automatically deploys when you push to your connected branch:

```bash
git add .
git commit -m "Update application"
git push origin main
```

Render will automatically:
1. Pull the latest code
2. Run the build command
3. Deploy the new version
4. Zero-downtime deployment (on paid plans)

## Custom Domain (Optional)

1. Go to your service settings in Render
2. Click **"Custom Domain"**
3. Add your domain and follow DNS configuration steps

## Support

- [Render Documentation](https://render.com/docs)
- [Render Community](https://community.render.com/)
- Check application logs in Render dashboard

## Cost Estimation

- **Free Tier**: $0/month (with cold starts)
- **Starter**: $7/month (no cold starts)
- **Standard**: $25/month (more resources)

Choose based on your traffic and performance needs.
