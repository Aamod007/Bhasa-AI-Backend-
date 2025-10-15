#!/usr/bin/env python3
"""
Bhasa-AI Translation API - Main Application
FastAPI Backend for Railway Deployment
"""
import os
import sys
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router
from app.services import get_translator

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Bhasa-AI Translation API",
    version="1.0.0",
    description="Production-ready translation API deployed on Railway",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS for Railway deployment with Vercel frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your Vercel domain
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """Initialize services on startup"""
    try:
        logger.info("Starting Bhasa-AI Translation API...")
        logger.info(f"Environment: {os.environ.get('RAILWAY_ENVIRONMENT', 'development')}")
        
        # Initialize translator
        translator = get_translator()
        logger.info("Translation service initialized successfully")
        
        # Log supported languages count
        langs = translator.get_supported_languages()
        logger.info(f"Loaded {len(langs)} supported languages")
        
    except Exception as e:
        logger.error(f"Failed to initialize services: {e}")
        sys.exit(1)


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    logger.info("Shutting down Bhasa-AI Translation API...")


@app.get("/")
async def root():
    """Root endpoint - API information"""
    return {
        "message": "Bhasa-AI Translation API",
        "status": "running",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }


# Include API routes with prefix
app.include_router(router, prefix="/api")

# Also add health check at root level for Railway
@app.get("/health")
async def root_health():
    """Root level health check for Railway"""
    try:
        translator = get_translator()
        return {
            "status": "healthy",
            "service": "translation-api",
            "translator": "initialized" if translator else "not initialized"
        }
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return {
            "status": "unhealthy",
            "error": str(e)
        }


if __name__ == "__main__":
    import uvicorn
    
    # Get port from environment variable (Railway provides this)
    port = int(os.environ.get("PORT", 8000))
    
    logger.info(f"Starting server on port {port}")
    
    # Run the server
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=False,  # Disable reload in production
        log_level="info",
        access_log=True
    )