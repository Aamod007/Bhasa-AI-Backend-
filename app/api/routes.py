"""
API Routes for Bhasa-AI Translation System
"""
from fastapi import APIRouter, HTTPException
from app.models import (
    TranslationRequest,
    TranslationResponse,
    LanguageDetectionRequest,
    LanguageDetectionResponse,
    SupportedLanguagesResponse,
    HealthCheckResponse,
    StatsResponse
)
from app.services import get_translator
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/translate", response_model=TranslationResponse)
async def translate_text(request: TranslationRequest):
    """
    Translate text using the translation service
    
    Args:
        request: Translation request with text, source and target languages
        
    Returns:
        TranslationResponse with translation results
    """
    try:
        translator = get_translator()
        
        if not request.text.strip():
            raise HTTPException(status_code=400, detail="Empty text provided")
        
        # Perform translation
        result = translator.translate_text(
            text=request.text,
            source_lang=request.sourceLang,
            target_lang=request.targetLang
        )
        
        if 'error' in result:
            raise HTTPException(status_code=500, detail=result['error'])
        
        # Get the primary translation (Google Translate)
        primary_translation = result['translations'].get('google', 'No translation available')
        
        return TranslationResponse(
            original_text=result['original_text'],
            source_language=result['source_language'],
            target_language=result['target_language'],
            translation=primary_translation,
            confidence=result['confidence'],
            translations=result['translations']
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Translation error: {e}")
        raise HTTPException(status_code=500, detail=f"Translation failed: {str(e)}")


@router.post("/detect-language", response_model=LanguageDetectionResponse)
async def detect_language(request: LanguageDetectionRequest):
    """
    Detect the language of the provided text
    
    Args:
        request: Language detection request with text
        
    Returns:
        LanguageDetectionResponse with detected language info
    """
    try:
        translator = get_translator()
        
        if not request.text.strip():
            raise HTTPException(status_code=400, detail="Empty text provided")
        
        detected_lang = translator.detect_language(request.text)
        supported_langs = translator.get_supported_languages()
        language_name = supported_langs.get(detected_lang, "Unknown")
        
        return LanguageDetectionResponse(
            text=request.text,
            detected_language=detected_lang,
            language_name=language_name
        )
        
    except Exception as e:
        logger.error(f"Language detection error: {e}")
        raise HTTPException(status_code=500, detail=f"Language detection failed: {str(e)}")


@router.get("/supported-languages", response_model=SupportedLanguagesResponse)
async def get_supported_languages():
    """
    Get list of supported languages
    
    Returns:
        SupportedLanguagesResponse with all supported languages
    """
    try:
        translator = get_translator()
        languages = translator.get_supported_languages()
        return SupportedLanguagesResponse(languages=languages)
        
    except Exception as e:
        logger.error(f"Error getting supported languages: {e}")
        raise HTTPException(status_code=500, detail="Failed to get supported languages")


@router.get("/health", response_model=HealthCheckResponse)
async def health_check():
    """
    Health check endpoint with detailed status
    
    Returns:
        HealthCheckResponse with system health information
    """
    try:
        translator = get_translator()
        translator_status = "initialized" if translator else "not initialized"
        
        return HealthCheckResponse(
            status="healthy",
            translator_status=translator_status,
            supported_languages_count=len(translator.get_supported_languages()) if translator else 0
        )
    except Exception as e:
        logger.error(f"Health check error: {e}")
        return HealthCheckResponse(
            status="unhealthy",
            translator_status="error",
            supported_languages_count=0
        )


@router.get("/stats", response_model=StatsResponse)
async def get_stats():
    """
    Get basic API statistics
    
    Returns:
        StatsResponse with API statistics
    """
    try:
        translator = get_translator()
        
        return StatsResponse(
            api_version="1.0.0",
            translator_initialized=translator is not None,
            supported_languages=len(translator.get_supported_languages()) if translator else 0,
            features=[
                "Text Translation",
                "Language Detection",
                "Multiple Translation Engines",
                "Auto Language Detection"
            ]
        )
    except Exception as e:
        logger.error(f"Stats error: {e}")
        raise HTTPException(status_code=500, detail="Failed to get statistics")