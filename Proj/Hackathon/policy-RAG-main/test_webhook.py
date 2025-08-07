#!/usr/bin/env python3
"""
Test script for Policy RAG Webhook
"""

import requests
import json
import sys
from typing import Dict, Any

def test_health_check(base_url: str) -> bool:
    """Test the health check endpoint."""
    try:
        response = requests.get(f"{base_url}/health", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health check passed: {data}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False

def test_api_endpoint(base_url: str, test_data: Dict[str, Any]) -> bool:
    """Test the main API endpoint."""
    try:
        response = requests.post(
            f"{base_url}/hackrx/run",
            json=test_data,
            headers={"Content-Type": "application/json"},
            timeout=60
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API test passed:")
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

def main():
    """Main test function."""
    if len(sys.argv) < 2:
        print("Usage: python test_webhook.py <base_url>")
        print("Example: python test_webhook.py https://your-app.railway.app")
        sys.exit(1)
    
    base_url = sys.argv[1].rstrip('/')
    
    # Test data - replace with your actual document URL
    test_data = {
        "documents": "https://www.africau.edu/images/default/sample.pdf",  # Sample PDF
        "questions": [
            "What is this document about?",
            "What are the main sections?"
        ]
    }
    
    print(f"🧪 Testing webhook at: {base_url}")
    print("=" * 50)
    
    # Test health check
    print("1. Testing health check...")
    health_ok = test_health_check(base_url)
    
    # Test API endpoint
    print("\n2. Testing API endpoint...")
    api_ok = test_api_endpoint(base_url, test_data)
    
    # Summary
    print("\n" + "=" * 50)
    if health_ok and api_ok:
        print("🎉 All tests passed! Your webhook is ready to use.")
        print(f"\nYour webhook URL: {base_url}/hackrx/run")
        print("\nExample usage:")
        print(f"curl -X POST '{base_url}/hackrx/run' \\")
        print("  -H 'Content-Type: application/json' \\")
        print("  -d '{\"documents\": \"your-document-url\", \"questions\": [\"your-question\"]}'")
    else:
        print("❌ Some tests failed. Check your deployment and environment variables.")
        sys.exit(1)

if __name__ == "__main__":
    main()
