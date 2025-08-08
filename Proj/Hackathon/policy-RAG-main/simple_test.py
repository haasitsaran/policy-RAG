#!/usr/bin/env python3
"""
Simple connectivity test for Render deployment
"""

import requests
import time

def test_basic_connectivity():
    """Test basic connectivity to the deployment."""
    BASE_URL = "https://policy-rag-webhook.onrender.com"
    
    print("🔍 Testing basic connectivity...")
    print(f"URL: {BASE_URL}")
    print("=" * 50)
    
    # Test 1: Basic HTTP request
    print("1. Testing basic HTTP request...")
    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            print("   ✅ Basic connectivity working!")
            return True
        else:
            print(f"   ⚠️  Status code: {response.status_code}")
            return False
    except requests.exceptions.Timeout:
        print("   ❌ Timeout - Application not responding")
        return False
    except requests.exceptions.ConnectionError:
        print("   ❌ Connection Error - Application not reachable")
        return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def check_render_status():
    """Check if Render deployment is active."""
    print("\n2. Checking Render deployment status...")
    print("   Go to: https://dashboard.render.com/")
    print("   Find your service: policy-rag-webhook")
    print("   Check if it's 'Live' or 'Build Failed'")
    print("   If 'Build Failed', check the logs for errors")

def check_environment_variables():
    """Guide for setting environment variables."""
    print("\n3. Environment Variables Check:")
    print("   In Render dashboard, go to your service → Environment")
    print("   Add these variables:")
    print("   - GOOGLE_API_KEY = your_google_gemini_api_key")
    print("   - PINECONE_API_KEY = your_pinecone_api_key")
    print("   After adding, redeploy the service")

def main():
    print("🚀 Policy RAG Webhook - Simple Connectivity Test")
    print("=" * 60)
    
    # Test connectivity
    if test_basic_connectivity():
        print("\n✅ Basic connectivity is working!")
        print("   The application is deployed and responding")
        print("   Next: Set environment variables and test API endpoints")
    else:
        print("\n❌ Basic connectivity failed!")
        print("   The application is not responding")
        print("   Possible issues:")
        print("   1. Build failed during deployment")
        print("   2. Missing environment variables")
        print("   3. Application crashed on startup")
    
    # Provide guidance
    check_render_status()
    check_environment_variables()
    
    print("\n" + "=" * 60)
    print("📋 Next Steps:")
    print("1. Check Render dashboard for deployment status")
    print("2. Set environment variables if needed")
    print("3. Redeploy if necessary")
    print("4. Test again with: python test_api_endpoints.py")

if __name__ == "__main__":
    main()
