#!/usr/bin/env python3
"""
Comprehensive API endpoint testing for Policy RAG Webhook
Tests all specific endpoints with proper authentication
"""

import requests
import json
import sys
from typing import Dict, Any

# Configuration
BASE_URL = "https://policy-rag-webhook.onrender.com"
API_BASE_URL = f"{BASE_URL}/api/v1"
AUTH_TOKEN = "f7fb3e8bfa0186112f7cf3a001f2913eeebe59e40ca19d0400174f3fc3f0311d"

def get_headers():
    """Get headers with authentication."""
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }

def test_root_endpoint() -> bool:
    """Test the root endpoint."""
    print("1. Testing ROOT endpoint (/)...")
    try:
        response = requests.get(f"{BASE_URL}/", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Root endpoint working:")
            print(f"   Message: {data.get('message', 'N/A')}")
            print(f"   Version: {data.get('version', 'N/A')}")
            return True
        else:
            print(f"❌ Root endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Root endpoint error: {e}")
        return False

def test_health_endpoint() -> bool:
    """Test the health check endpoint."""
    print("\n2. Testing HEALTH endpoint (/health)...")
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health check working:")
            print(f"   Status: {data.get('status', 'N/A')}")
            print(f"   Message: {data.get('message', 'N/A')}")
            return True
        else:
            print(f"⚠️  Health check returned: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False

def test_api_v1_root() -> bool:
    """Test the API v1 root endpoint."""
    print("\n3. Testing API V1 ROOT endpoint (/api/v1)...")
    try:
        response = requests.get(f"{API_BASE_URL}/", headers=get_headers(), timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API v1 root working:")
            print(f"   Response: {data}")
            return True
        else:
            print(f"❌ API v1 root failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ API v1 root error: {e}")
        return False

def test_hackrx_run_endpoint() -> bool:
    """Test the main hackrx/run endpoint."""
    print("\n4. Testing HACKRX/RUN endpoint (/api/v1/hackrx/run)...")
    test_data = {
        "documents": "https://www.africau.edu/images/default/sample.pdf",
        "questions": ["What is this document about?", "What are the main sections?"]
    }
    
    try:
        response = requests.post(
            f"{API_BASE_URL}/hackrx/run",
            json=test_data,
            headers=get_headers(),
            timeout=60
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ HackRx run endpoint working:")
            print(f"   Questions: {test_data['questions']}")
            print(f"   Answers: {data.get('answers', [])}")
            return True
        else:
            print(f"⚠️  HackRx run endpoint returned: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ HackRx run endpoint error: {e}")
        return False

def test_docs_endpoint() -> bool:
    """Test the documentation endpoint."""
    print("\n5. Testing DOCS endpoint (/docs)...")
    try:
        response = requests.get(f"{BASE_URL}/docs", timeout=10)
        if response.status_code == 200:
            print(f"✅ Docs endpoint working (Swagger UI available)")
            return True
        else:
            print(f"❌ Docs endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Docs endpoint error: {e}")
        return False

def test_openapi_endpoint() -> bool:
    """Test the OpenAPI schema endpoint."""
    print("\n6. Testing OPENAPI endpoint (/openapi.json)...")
    try:
        response = requests.get(f"{BASE_URL}/openapi.json", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ OpenAPI schema working:")
            print(f"   Title: {data.get('info', {}).get('title', 'N/A')}")
            print(f"   Version: {data.get('info', {}).get('version', 'N/A')}")
            return True
        else:
            print(f"❌ OpenAPI endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ OpenAPI endpoint error: {e}")
        return False

def test_authentication() -> bool:
    """Test authentication with invalid token."""
    print("\n7. Testing AUTHENTICATION...")
    try:
        # Test with invalid token
        invalid_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer invalid_token"
        }
        response = requests.post(
            f"{API_BASE_URL}/hackrx/run",
            json={"documents": "test", "questions": ["test"]},
            headers=invalid_headers,
            timeout=10
        )
        
        if response.status_code == 401:
            print(f"✅ Authentication properly rejects invalid tokens")
            return True
        else:
            print(f"⚠️  Authentication test returned: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Authentication test error: {e}")
        return False

def main():
    """Main test function."""
    print("🚀 Policy RAG Webhook - Comprehensive API Testing")
    print("=" * 70)
    print(f"Base URL: {BASE_URL}")
    print(f"API Base URL: {API_BASE_URL}")
    print(f"Authentication: Bearer token configured")
    print("=" * 70)
    
    # Test all endpoints
    results = []
    results.append(("Root", test_root_endpoint()))
    results.append(("Health", test_health_endpoint()))
    results.append(("API V1 Root", test_api_v1_root()))
    results.append(("HackRx Run", test_hackrx_run_endpoint()))
    results.append(("Docs", test_docs_endpoint()))
    results.append(("OpenAPI", test_openapi_endpoint()))
    results.append(("Auth", test_authentication()))
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 70)
    
    passed = 0
    total = len(results)
    
    for endpoint, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{endpoint:15} | {status}")
        if success:
            passed += 1
    
    print("=" * 70)
    print(f"Overall: {passed}/{total} endpoints working")
    
    if passed >= 5:  # Most endpoints should work
        print("\n🎉 API deployment is successful!")
        print("\n📋 Your API endpoints:")
        print(f"   Root: {BASE_URL}/")
        print(f"   Health: {BASE_URL}/health")
        print(f"   API V1: {API_BASE_URL}/")
        print(f"   HackRx Run: {API_BASE_URL}/hackrx/run")
        print(f"   Docs: {BASE_URL}/docs")
        print(f"   OpenAPI: {BASE_URL}/openapi.json")
        
        print("\n🔧 Usage example:")
        print(f"curl -X POST '{API_BASE_URL}/hackrx/run' \\")
        print(f"  -H 'Content-Type: application/json' \\")
        print(f"  -H 'Authorization: Bearer {AUTH_TOKEN}' \\")
        print(f"  -d '{{\"documents\": \"your-document-url\", \"questions\": [\"your-question\"]}}'")
        
        print("\n🔧 Next steps:")
        print("1. Set GOOGLE_API_KEY and PINECONE_API_KEY in Render dashboard")
        print("2. Test with real documents and questions")
        print("3. Integrate with your applications")
    else:
        print("\n❌ Some critical endpoints failed. Check your deployment.")
        sys.exit(1)

if __name__ == "__main__":
    main()
