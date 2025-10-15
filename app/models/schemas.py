"""
Pydantic models for API request/response validation
"""
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field


class TranslationRequest(BaseModel):
    """Request model for text translation"""
    text: str = Field(..., min_length=1, max_length=5000, description="Text to translate")
    sourceLang: str = Field(default="auto", description="Source language code")
    targetLang: str = Field(default="en", description="Target language code")


class TranslationResponse(BaseModel):
    """Response model for text translation"""
    original_text: str
    source_language: str
    target_language: str
    translation: str
    confidence: float
    translations: Dict[str, str] = {}
    error: Optional[str] = None


class LanguageDetectionRequest(BaseModel):
    """Request model for language detection"""
    text: str = Field(..., min_length=1, max_length=1000, description="Text to analyze")


class LanguageDetectionResponse(BaseModel):
    """Response model for language detection"""
    text: str
    detected_language: str
    language_name: str


class SupportedLanguagesResponse(BaseModel):
    """Response model for supported languages"""
    languages: Dict[str, str]


class HealthCheckResponse(BaseModel):
    """Response model for health check"""
    status: str
    translator_status: str
    supported_languages_count: int


class StatsResponse(BaseModel):
    """Response model for API statistics"""
    api_version: str
    translator_initialized: bool
    supported_languages: int
    features: list[str]