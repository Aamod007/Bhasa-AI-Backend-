"""
Test script to verify the API is working correctly
Run this locally before deploying to Railway
"""
import requests
import json

# Base URL - change this to your Railway URL after deployment
BASE_URL = "http://localhost:8000"


def test_health_check():
    """Test health check endpoint"""
    print("\n=== Testing Health Check ===")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200


def test_translation():
    """Test translation endpoint"""
    print("\n=== Testing Translation ===")
    
    test_data = {
        "text": "Hello, how are you?",
        "sourceLang": "en",
        "targetLang": "es"
    }
    
    response = requests.post(
        f"{BASE_URL}/api/translate",
        json=test_data,
        headers={"Content-Type": "application/json"}
    )
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200


def test_language_detection():
    """Test language detection endpoint"""
    print("\n=== Testing Language Detection ===")
    
    test_data = {
        "text": "Bonjour le monde"
    }
    
    response = requests.post(
        f"{BASE_URL}/api/detect-language",
        json=test_data,
        headers={"Content-Type": "application/json"}
    )
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200


def test_supported_languages():
    """Test supported languages endpoint"""
    print("\n=== Testing Supported Languages ===")
    response = requests.get(f"{BASE_URL}/api/supported-languages")
    print(f"Status Code: {response.status_code}")
    data = response.json()
    print(f"Number of languages: {len(data.get('languages', {}))}")
    print(f"Sample languages: {list(data.get('languages', {}).items())[:5]}")
    return response.status_code == 200


def test_stats():
    """Test stats endpoint"""
    print("\n=== Testing Stats ===")
    response = requests.get(f"{BASE_URL}/api/stats")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200


if __name__ == "__main__":
    print("=" * 60)
    print("Bhasa-AI Backend API Test Suite")
    print("=" * 60)
    
    results = {
        "Health Check": test_health_check(),
        "Translation": test_translation(),
        "Language Detection": test_language_detection(),
        "Supported Languages": test_supported_languages(),
        "Stats": test_stats()
    }
    
    print("\n" + "=" * 60)
    print("Test Results Summary")
    print("=" * 60)
    
    for test_name, result in results.items():
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    all_passed = all(results.values())
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✅ All tests passed! API is ready for deployment.")
    else:
        print("❌ Some tests failed. Please check the errors above.")
    print("=" * 60)