# Deployment Guide for Policy RAG Webhook

## Quick Deployment to Render

### Step 1: Prepare Your Repository

1. **Push your code to GitHub:**
   ```bash
   git add .
   git commit -m "Add deployment configuration for Render"
   git push origin main
   ```

### Step 2: Deploy to Render

1. **Go to [Render Dashboard](https://dashboard.render.com/)**
2. **Click "New +" → "Web Service"**
3. **Connect your GitHub repository:**
   - Select your GitHub account
   - Choose the repository: `Akhil3517/llm`
   - Click "Connect"

4. **Configure the service:**
   - **Name:** `policy-rag-webhook`
   - **Environment:** `Python`
   - **Region:** Choose closest to your users
   - **Branch:** `main`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`

5. **Set Environment Variables:**
   - Click "Advanced" → "Add Environment Variable"
   - Add these variables:
     - `GOOGLE_API_KEY`: Your Google Generative AI API key
     - `PINECONE_API_KEY`: Your Pinecone API key

6. **Deploy:**
   - Click "Create Web Service"
   - Wait for build to complete (usually 2-5 minutes)

### Step 3: Test Your Deployment

1. **Check health endpoint:**
   ```bash
   curl https://your-app-name.onrender.com/health
   ```

2. **Test the webhook:**
   ```bash
   curl -X POST "https://your-app-name.onrender.com/hackrx/run" \
     -H "Content-Type: application/json" \
     -d '{
       "documents": "https://example.com/sample-policy.pdf",
       "questions": ["What is the coverage limit?"]
     }'
   ```

## Environment Variables Setup

### Google Generative AI
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key to your Render environment variables

### Pinecone
1. Go to [Pinecone Console](https://app.pinecone.io/)
2. Create a new API key
3. Ensure your index is created with:
   - **Name:** `hackrx-gemini-index`
   - **Dimensions:** `768` (for Gemini embedding-001)
   - **Metric:** `cosine`

## Troubleshooting

### Common Issues:

1. **Build fails:**
   - Check that all dependencies are in `requirements.txt`
   - Ensure Python version is compatible

2. **Runtime errors:**
   - Verify environment variables are set correctly
   - Check logs in Render dashboard

3. **API key errors:**
   - Ensure API keys are valid and have proper permissions
   - Check that Pinecone index exists and is accessible

### Monitoring:

- **Health Check:** `GET /health`
- **Root Endpoint:** `GET /`
- **Main Webhook:** `POST /hackrx/run`

## Support

If you encounter issues:
1. Check the Render logs in your dashboard
2. Verify all environment variables are set
3. Test locally first with `uvicorn main:app --reload`
