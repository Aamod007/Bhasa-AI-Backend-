# Bhasa-AI Backend API

Production-ready FastAPI translation service for deployment on Railway.

## 🚀 Features

- **Text Translation** - Translate text between 50+ languages
- **Language Detection** - Automatically detect the language of input text
- **Fast & Reliable** - Built with FastAPI for high performance
- **Production Ready** - Optimized for Railway deployment
- **CORS Enabled** - Works seamlessly with Vercel frontend

## 📋 Prerequisites

- Python 3.9 or higher
- Railway account (for deployment)
- Git

## 🛠️ Local Development

### 1. Clone the repository

```bash
git clone <your-backend-repo-url>
cd Bhasa-AI-Backend
```

### 2. Create virtual environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the development server

```bash
python main.py
```

The API will be available at `http://localhost:8000`

- **API Documentation**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## 🚂 Deploy to Railway

### Method 1: Deploy from GitHub (Recommended)

1. **Create a new GitHub repository** for your backend

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <your-backend-repo-url>
   git push -u origin main
   ```

2. **Deploy on Railway**
   - Go to [Railway](https://railway.app)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your backend repository
   - Railway will automatically detect the configuration from `railway.toml`

3. **Configure Environment Variables** (Optional)
   - Railway automatically provides `PORT` variable
   - No additional environment variables needed

4. **Get your Railway URL**
   - After deployment, Railway will provide a URL like: `https://your-app.railway.app`
   - Save this URL for frontend configuration

### Method 2: Deploy using Railway CLI

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login to Railway
railway login

# Initialize and deploy
railway init
railway up
```

## 📡 API Endpoints

### Root
- `GET /` - API information
- `GET /health` - Health check endpoint

### Translation API (`/api` prefix)
- `POST /api/translate` - Translate text
- `POST /api/detect-language` - Detect language
- `GET /api/supported-languages` - Get supported languages
- `GET /api/stats` - API statistics

## 📝 API Usage Examples

### Translate Text

```bash
curl -X POST "https://your-app.railway.app/api/translate" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello, how are you?",
    "sourceLang": "en",
    "targetLang": "es"
  }'
```

**Response:**
```json
{
  "original_text": "Hello, how are you?",
  "source_language": "en",
  "target_language": "es",
  "translation": "Hola, ¿cómo estás?",
  "confidence": 0.85,
  "translations": {
    "google": "Hola, ¿cómo estás?"
  }
}
```

### Detect Language

```bash
curl -X POST "https://your-app.railway.app/api/detect-language" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Bonjour le monde"
  }'
```

**Response:**
```json
{
  "text": "Bonjour le monde",
  "detected_language": "fr",
  "language_name": "French"
}
```

### Get Supported Languages

```bash
curl "https://your-app.railway.app/api/supported-languages"
```

## 🔗 Connect with Frontend

After deploying to Railway, update your frontend environment variables:

### For Vercel Frontend:

1. Go to your Vercel project settings
2. Navigate to "Environment Variables"
3. Add/Update:
   ```
   VITE_RAILWAY_API_URL=https://your-app.railway.app
   ```
4. Redeploy your frontend

### For Local Frontend Development:

Create/Update `.env` file in your frontend project:
```env
VITE_RAILWAY_API_URL=https://your-app.railway.app
```

## 🔧 Project Structure

```
Bhasa-AI-Backend/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py          # API route handlers
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py         # Pydantic models
│   └── services/
│       ├── __init__.py
│       └── translator.py      # Translation service
├── main.py                     # FastAPI application
├── requirements.txt            # Python dependencies
├── railway.toml               # Railway configuration
├── Procfile                   # Alternative deployment config
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## 🌍 Supported Languages

The API supports translation between 50+ languages including:

- English, Spanish, French, German, Italian, Portuguese
- Russian, Japanese, Korean, Chinese (Simplified & Traditional)
- Arabic, Hindi, Nepali, Sinhala, Bengali
- Tamil, Telugu, Malayalam, Marathi, Gujarati
- And many more...

Get the full list at: `/api/supported-languages`

## 🐛 Troubleshooting

### Railway Deployment Issues

1. **Build fails**
   - Check that `requirements.txt` is present
   - Verify Python version compatibility

2. **App crashes on startup**
   - Check Railway logs: `railway logs`
   - Verify all dependencies are installed

3. **Health check fails**
   - Ensure `/health` endpoint is accessible
   - Check Railway health check timeout settings

### CORS Issues

If you encounter CORS errors:
1. Update `main.py` to include your specific Vercel domain in `allow_origins`
2. Redeploy to Railway

## 📊 Monitoring

- **Railway Dashboard** - Monitor resource usage and logs
- **Health Endpoint** - `/health` for uptime monitoring
- **API Logs** - Access via Railway dashboard or CLI

## 🔒 Security Notes

- The current configuration allows all origins (`*`) for CORS
- For production, update `allow_origins` in `main.py` to your specific domain:
  ```python
  allow_origins=["https://your-frontend-domain.vercel.app"]
  ```

## 📄 License

MIT License - Feel free to use this for your projects!

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📞 Support

- **Issues**: Open an issue on GitHub
- **Email**: your-email@example.com

## 🎯 Next Steps

1. ✅ Deploy backend to Railway
2. ✅ Get your Railway URL
3. ✅ Update frontend environment variables
4. ✅ Test the integration
5. 🚀 Go live!

---

Made with ❤️ for Bhasa-AI