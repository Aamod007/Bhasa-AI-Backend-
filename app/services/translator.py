"""
Simplified Text Translation Service
Using Google Translate for reliable translation
"""
import logging
from typing import Dict, Any
from googletrans import Translator

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class TranslationService:
    """Simple translation service using Google Translate"""
    
    def __init__(self):
        """Initialize the translation service"""
        self.google_translator = Translator()
        self.supported_languages = {
            'en': 'English',
            'es': 'Spanish',
            'fr': 'French',
            'de': 'German',
            'it': 'Italian',
            'pt': 'Portuguese',
            'ru': 'Russian',
            'ja': 'Japanese',
            'ko': 'Korean',
            'zh-CN': 'Chinese (Simplified)',
            'zh-TW': 'Chinese (Traditional)',
            'ar': 'Arabic',
            'hi': 'Hindi',
            'ne': 'Nepali',
            'si': 'Sinhala',
            'bn': 'Bengali',
            'ta': 'Tamil',
            'te': 'Telugu',
            'ml': 'Malayalam',
            'mr': 'Marathi',
            'gu': 'Gujarati',
            'kn': 'Kannada',
            'pa': 'Punjabi',
            'ur': 'Urdu',
            'vi': 'Vietnamese',
            'th': 'Thai',
            'id': 'Indonesian',
            'ms': 'Malay',
            'fil': 'Filipino',
            'tr': 'Turkish',
            'pl': 'Polish',
            'uk': 'Ukrainian',
            'ro': 'Romanian',
            'nl': 'Dutch',
            'sv': 'Swedish',
            'no': 'Norwegian',
            'da': 'Danish',
            'fi': 'Finnish',
            'cs': 'Czech',
            'hu': 'Hungarian',
            'el': 'Greek',
            'he': 'Hebrew',
            'fa': 'Persian',
        }
        logger.info("Translation Service initialized successfully")
    
    def translate_text(self, text: str, source_lang: str = 'auto', target_lang: str = 'en') -> Dict[str, Any]:
        """
        Translate text using Google Translate
        
        Args:
            text: Text to translate
            source_lang: Source language code ('auto' for auto-detection)
            target_lang: Target language code
            
        Returns:
            Dictionary with translation results
        """
        results = {
            'original_text': text,
            'source_language': source_lang,
            'target_language': target_lang,
            'translations': {},
            'confidence': 0.0
        }
        
        try:
            # Validate input
            if not text or not text.strip():
                results['error'] = "Empty text provided"
                return results
            
            # Perform translation
            google_result = self.google_translator.translate(
                text, 
                src=source_lang, 
                dest=target_lang
            )
            
            results['translations']['google'] = google_result.text
            results['confidence'] = 0.85  # Default confidence for Google Translate
            
            # Detect source language if auto
            if source_lang == 'auto':
                results['source_language'] = google_result.src
            
            logger.info(f"Translation completed: {source_lang} -> {target_lang}")
            return results
            
        except Exception as e:
            logger.error(f"Translation error: {e}")
            results['error'] = str(e)
            return results
    
    def get_supported_languages(self) -> Dict[str, str]:
        """
        Get list of supported languages
        
        Returns:
            Dictionary of language codes and names
        """
        return self.supported_languages
    
    def detect_language(self, text: str) -> str:
        """
        Detect language of given text
        
        Args:
            text: Text to analyze
            
        Returns:
            Detected language code
        """
        try:
            if not text or not text.strip():
                return 'unknown'
            
            detected = self.google_translator.detect(text)
            return detected.lang
        except Exception as e:
            logger.warning(f"Language detection failed: {e}")
            return 'unknown'


# Singleton instance
_translator_instance = None


def get_translator() -> TranslationService:
    """
    Get or create translator instance (singleton pattern)
    
    Returns:
        TranslationService instance
    """
    global _translator_instance
    if _translator_instance is None:
        _translator_instance = TranslationService()
    return _translator_instance