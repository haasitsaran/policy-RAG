#!/usr/bin/env python3
"""
Render Deployment Verification Script
Checks if all required files are present and properly configured
"""

import os
import sys

def check_required_files():
    """Check if all required files for Render deployment are present."""
    required_files = [
        'main.py',
        'requirements.txt',
        'config.py',
        'schemas.py',
        'render.yaml',
        'Dockerfile',
        'README.md'
    ]
    
    print("🔍 Checking required files for Render deployment...")
    print("=" * 50)
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - MISSING")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n❌ Missing files: {', '.join(missing_files)}")
        return False
    else:
        print("\n✅ All required files are present!")
        return True

def check_requirements_txt():
    """Check if requirements.txt has all necessary dependencies."""
    print("\n📦 Checking requirements.txt...")
    
    if not os.path.exists('requirements.txt'):
        print("❌ requirements.txt not found!")
        return False
    
    with open('requirements.txt', 'r') as f:
        content = f.read()
    
    required_deps = [
        'fastapi',
        'uvicorn',
        'pinecone-client',
        'google-generativeai',
        'langchain-core',
        'unstructured'
    ]
    
    missing_deps = []
    for dep in required_deps:
        if dep in content:
            print(f"✅ {dep}")
        else:
            print(f"❌ {dep} - MISSING")
            missing_deps.append(dep)
    
    if missing_deps:
        print(f"\n❌ Missing dependencies: {', '.join(missing_deps)}")
        return False
    else:
        print("\n✅ All required dependencies are present!")
        return True

def check_main_py():
    """Check if main.py has the required endpoints."""
    print("\n🐍 Checking main.py...")
    
    if not os.path.exists('main.py'):
        print("❌ main.py not found!")
        return False
    
    with open('main.py', 'r') as f:
        content = f.read()
    
    required_endpoints = [
        '/health',
        '/api/v1',
        '/api/v1/hackrx/run'
    ]
    
    missing_endpoints = []
    for endpoint in required_endpoints:
        if endpoint in content:
            print(f"✅ {endpoint} endpoint")
        else:
            print(f"❌ {endpoint} endpoint - MISSING")
            missing_endpoints.append(endpoint)
    
    if missing_endpoints:
        print(f"\n❌ Missing endpoints: {', '.join(missing_endpoints)}")
        return False
    else:
        print("\n✅ All required endpoints are present!")
        return True

def main():
    """Main verification function."""
    print("🚀 Render Deployment Verification")
    print("=" * 50)
    
    # Check all requirements
    files_ok = check_required_files()
    deps_ok = check_requirements_txt()
    main_ok = check_main_py()
    
    print("\n" + "=" * 50)
    print("📋 SUMMARY:")
    print(f"Files: {'✅' if files_ok else '❌'}")
    print(f"Dependencies: {'✅' if deps_ok else '❌'}")
    print(f"Endpoints: {'✅' if main_ok else '❌'}")
    
    if files_ok and deps_ok and main_ok:
        print("\n🎉 All checks passed! Your app is ready for Render deployment.")
        print("\n📋 Next steps:")
        print("1. Go to https://dashboard.render.com/")
        print("2. Create new Web Service")
        print("3. Connect to GitHub repository: haasitsaran/policy-RAG")
        print("4. Select branch: deploy-render")
        print("5. Set environment variables: GOOGLE_API_KEY, PINECONE_API_KEY")
        print("6. Deploy!")
    else:
        print("\n❌ Some checks failed. Please fix the issues above before deploying.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
