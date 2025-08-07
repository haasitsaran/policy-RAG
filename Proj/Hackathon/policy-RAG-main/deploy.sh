#!/bin/bash

# Policy RAG Webhook Deployment Script
# This script helps you deploy your application to Railway

set -e

echo "🚀 Policy RAG Webhook Deployment Script"
echo "========================================"

# Check if Railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI not found. Installing..."
    npm install -g @railway/cli
fi

# Check if user is logged in
if ! railway whoami &> /dev/null; then
    echo "🔐 Please login to Railway..."
    railway login
fi

# Initialize Railway project if not already done
if [ ! -f "railway.json" ]; then
    echo "📁 Initializing Railway project..."
    railway init
fi

# Deploy the application
echo "🚀 Deploying to Railway..."
railway up

# Get the deployment URL
echo "🔗 Getting deployment URL..."
DEPLOY_URL=$(railway domain)

echo "✅ Deployment complete!"
echo "🌐 Your webhook URL: https://$DEPLOY_URL/hackrx/run"
echo "🏥 Health check URL: https://$DEPLOY_URL/health"

# Set environment variables if provided
if [ ! -z "$GOOGLE_API_KEY" ]; then
    echo "🔑 Setting Google API key..."
    railway variables set GOOGLE_API_KEY="$GOOGLE_API_KEY"
fi

if [ ! -z "$PINECONE_API_KEY" ]; then
    echo "🔑 Setting Pinecone API key..."
    railway variables set PINECONE_API_KEY="$PINECONE_API_KEY"
fi

echo ""
echo "📋 Next steps:"
echo "1. Set your environment variables:"
echo "   railway variables set GOOGLE_API_KEY=your_google_api_key"
echo "   railway variables set PINECONE_API_KEY=your_pinecone_api_key"
echo ""
echo "2. Test your webhook:"
echo "   python test_webhook.py https://$DEPLOY_URL"
echo ""
echo "3. Monitor your deployment:"
echo "   railway logs"
echo ""
echo "🎉 Your webhook is ready to use!"
