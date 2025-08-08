#!/usr/bin/env python3
"""
Basic test script for Render deployment
Tests endpoints that don't require API keys
"""

import requests
import json
import sys

def test_basic_deployment():
    """Test basic deployment functionality."""
    
    RENDER_URL = "https://policy-rag-webhook.onrender.com"
    
    print(f"🧪 Testing basic deployment at: {RENDER_URL}")
    print("=" * 60)
    
    # Test 1: Root endpoint
    print("1. Testing root endpoint...")
    try:
        response = requests.get(f"{RENDER_URL}/", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Root endpoint working: {data}")
        else:
            print(f"❌ Root endpoint failed: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Root endpoint error: {e}")
    
    # Test 2: Test endpoint (new)
    print("\n2. Testing test endpoint...")
    try:
        response = requests.get(f"{RENDER_URL}/test", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Test endpoint working: {data}")
        else:
            print(f"❌ Test endpoint failed: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Test endpoint error: {e}")
    
    # Test 3: Health check (might fail without API keys)
    print("\n3. Testing health check...")
    try:
        response = requests.get(f"{RENDER_URL}/health", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health check working: {data}")
        else:
            print(f"⚠️  Health check returned: {response.status_code}")
            print(f"   This is expected if API keys are not set")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Health check error: {e}")
    
    print("\n" + "=" * 60)
    print("📋 Deployment Status:")
    print("✅ If root and test endpoints work, your deployment is successful!")
    print("⚠️  Health check may fail if API keys are not set")
    print("\n🔧 Next steps:")
    print("1. Set GOOGLE_API_KEY and PINECONE_API_KEY in Render dashboard")
    print("2. Test the main API endpoint: /hackrx/run")
    print("3. Use your webhook in integrations")

if __name__ == "__main__":
    test_basic_deployment()
