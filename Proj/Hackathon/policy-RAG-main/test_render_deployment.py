#!/usr/bin/env python3
"""
Test script for Render deployment
Replace YOUR_RENDER_URL with your actual Render URL
"""

import requests
import json
import sys

def test_render_deployment():
    """Test the Render deployment."""
    
    # Replace with your actual Render URL
    RENDER_URL = "https://policy-rag-webhook.onrender.com"  # Your actual Render URL
    
    print(f"🧪 Testing Render deployment at: {RENDER_URL}")
    print("=" * 60)
    
    # Test 1: Health Check
    print("1. Testing health check...")
    try:
        response = requests.get(f"{RENDER_URL}/health", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health check passed: {data}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False
    
    # Test 2: Root endpoint
    print("\n2. Testing root endpoint...")
    try:
        response = requests.get(f"{RENDER_URL}/", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Root endpoint working: {data}")
        else:
            print(f"❌ Root endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Root endpoint error: {e}")
    
    # Test 3: API endpoint
    print("\n3. Testing API endpoint...")
    test_data = {
        "documents": "https://www.africau.edu/images/default/sample.pdf",
        "questions": ["What is this document about?", "What are the main sections?"]
    }
    
    try:
        response = requests.post(
            f"{RENDER_URL}/hackrx/run",
            json=test_data,
            headers={"Content-Type": "application/json"},
            timeout=60
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API test passed!")
            print(f"   Questions: {test_data['questions']}")
            print(f"   Answers: {data['answers']}")
            return True
        else:
            print(f"❌ API test failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ API test error: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Render Deployment Test")
    print("=" * 60)
    print("Before running this test:")
    print("1. Deploy your app to Render")
    print("2. Replace YOUR_RENDER_URL in this script")
    print("3. Make sure environment variables are set")
    print("=" * 60)
    
    success = test_render_deployment()
    
    if success:
        print("\n🎉 All tests passed! Your Render webhook is ready!")
        print("\n📋 Next steps:")
        print("1. Use your webhook URL in integrations")
        print("2. Set up monitoring for the /health endpoint")
        print("3. Consider adding authentication for production")
    else:
        print("\n❌ Some tests failed. Check your deployment and environment variables.")
        sys.exit(1)
