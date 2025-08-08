#!/usr/bin/env python3
"""
Comprehensive test script for Policy RAG Webhook endpoints
Tests all specific endpoints on the deployed webhook
"""

import requests
import json
import sys
from typing import Dict, Any

def test_root_endpoint(base_url: str) -> bool:
    """Test the root endpoint."""
    print("1. Testing ROOT endpoint (/)...")
    try:
        response = requests.get(f"{base_url}/", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Root endpoint working:")
            print(f"   Message: {data.get('message', 'N/A')}")
            print(f"   Version: {data.get('version', 'N/A')}")
            print(f"   Endpoints: {data.get('endpoints', {})}")
            return True
        else:
            print(f"❌ Root endpoint failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Root endpoint error: {e}")
        return False

def test_health_endpoint(base_url: str) -> bool:
    """Test the health check endpoint."""
    print("\n2. Testing HEALTH endpoint (/health)...")
    try:
        response = requests.get(f"{base_url}/health", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health check working:")
            print(f"   Status: {data.get('status', 'N/A')}")
            print(f"   Message: {data.get('message', 'N/A')}")
            if 'pinecone_index' in data:
                print(f"   Pinecone Index: {data.get('pinecone_index', 'N/A')}")
                print(f"   Total Vectors: {data.get('total_vectors', 'N/A')}")
            return True
        else:
            print(f"⚠️  Health check returned: {response.status_code}")
            print(f"   This is expected if API keys are not set")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False

def test_test_endpoint(base_url: str) -> bool:
    """Test the test endpoint."""
    print("\n3. Testing TEST endpoint (/test)...")
    try:
        response = requests.get(f"{base_url}/test", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Test endpoint working:")
            print(f"   Status: {data.get('status', 'N/A')}")
            print(f"   Message: {data.get('message', 'N/A')}")
            print(f"   Timestamp: {data.get('timestamp', 'N/A')}")
            return True
        else:
            print(f"❌ Test endpoint failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Test endpoint error: {e}")
        return False

def test_docs_endpoint(base_url: str) -> bool:
    """Test the documentation endpoint."""
    print("\n4. Testing DOCS endpoint (/docs)...")
    try:
        response = requests.get(f"{base_url}/docs", timeout=10)
        if response.status_code == 200:
            print(f"✅ Docs endpoint working (Swagger UI available)")
            return True
        else:
            print(f"❌ Docs endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Docs endpoint error: {e}")
        return False

def test_api_endpoint(base_url: str) -> bool:
    """Test the main API endpoint."""
    print("\n5. Testing MAIN API endpoint (/hackrx/run)...")
    test_data = {
        "documents": "https://www.africau.edu/images/default/sample.pdf",
        "questions": ["What is this document about?", "What are the main sections?"]
    }
    
    try:
        response = requests.post(
            f"{base_url}/hackrx/run",
            json=test_data,
            headers={"Content-Type": "application/json"},
            timeout=60
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Main API endpoint working:")
            print(f"   Questions: {test_data['questions']}")
            print(f"   Answers: {data.get('answers', [])}")
            return True
        else:
            print(f"⚠️  Main API endpoint returned: {response.status_code}")
            print(f"   This is expected if API keys are not set")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Main API endpoint error: {e}")
        return False

def test_invalid_endpoint(base_url: str) -> bool:
    """Test invalid endpoint to ensure proper error handling."""
    print("\n6. Testing INVALID endpoint (/invalid)...")
    try:
        response = requests.get(f"{base_url}/invalid", timeout=10)
        if response.status_code == 404:
            print(f"✅ Invalid endpoint properly returns 404")
            return True
        else:
            print(f"⚠️  Invalid endpoint returned: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Invalid endpoint error: {e}")
        return False

def main():
    """Main test function."""
    RENDER_URL = "https://policy-rag-webhook.onrender.com"
    
    print("🚀 Policy RAG Webhook - Endpoint Testing")
    print("=" * 60)
    print(f"Testing deployment at: {RENDER_URL}")
    print("=" * 60)
    
    # Test all endpoints
    results = []
    results.append(("Root", test_root_endpoint(RENDER_URL)))
    results.append(("Health", test_health_endpoint(RENDER_URL)))
    results.append(("Test", test_test_endpoint(RENDER_URL)))
    results.append(("Docs", test_docs_endpoint(RENDER_URL)))
    results.append(("API", test_api_endpoint(RENDER_URL)))
    results.append(("Invalid", test_invalid_endpoint(RENDER_URL)))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 60)
    
    passed = 0
    total = len(results)
    
    for endpoint, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{endpoint:10} | {status}")
        if success:
            passed += 1
    
    print("=" * 60)
    print(f"Overall: {passed}/{total} endpoints working")
    
    if passed >= 4:  # At least root, test, docs, and invalid should work
        print("\n🎉 Deployment is successful!")
        print("\n📋 Your webhook endpoints:")
        print(f"   Root: {RENDER_URL}/")
        print(f"   Health: {RENDER_URL}/health")
        print(f"   Test: {RENDER_URL}/test")
        print(f"   Docs: {RENDER_URL}/docs")
        print(f"   API: {RENDER_URL}/hackrx/run")
        
        print("\n🔧 Next steps:")
        print("1. Set GOOGLE_API_KEY and PINECONE_API_KEY in Render dashboard")
        print("2. Test the main API with real documents")
        print("3. Integrate with your applications")
    else:
        print("\n❌ Some critical endpoints failed. Check your deployment.")
        sys.exit(1)

if __name__ == "__main__":
    main()
