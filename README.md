# Bhasa-AI Backend API

Production-ready FastAPI translation service for deployment on Render.

## 🚀 Features

- **Text Translation** - Translate text between 50+ languages
- **Language Detection** - Automatically detect the language of input text
- **Fast & Reliable** - Built with FastAPI for high performance
- **Production Ready** - Optimized for Render deployment
- **CORS Enabled** - Works seamlessly with Vercel frontend

## 📋 Prerequisites

- Python 3.9 or higher
- Render account (for deployment)
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

## 🎨 Deploy to Render

For detailed Render deployment instructions, see [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md)

### Quick Deploy to Render:

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Add Render configuration"
   git push origin main
   ```

2. **Deploy on Render**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New +" → "Blueprint"
   - Connect your repository
   - Render will auto-detect `render.yaml`
   - Click "Apply"

3. **Get your Render URL**
   - After deployment: `https://your-service.onrender.com`
   - Use this URL in your frontend configuration

📖 **See [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md) for complete guide**



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
curl -X POST "https://your-service.onrender.com/api/translate" \
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
curl -X POST "https://your-service.onrender.com/api/detect-language" \
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
curl "https://your-service.onrender.com/api/supported-languages"
```

## 🔗 Connect with Frontend

After deploying to Render, update your frontend environment variables:

### For Vercel Frontend:

1. Go to your Vercel project settings
2. Navigate to "Environment Variables"
3. Add/Update:
   ```
   VITE_API_URL=https://your-service.onrender.com
   ```
4. Redeploy your frontend

### For Local Frontend Development:

Create/Update `.env` file in your frontend project:
```env
VITE_API_URL=https://your-service.onrender.com
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