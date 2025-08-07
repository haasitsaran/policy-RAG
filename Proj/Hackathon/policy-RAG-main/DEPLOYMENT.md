# Policy RAG Webhook Deployment Guide

This guide will help you deploy your Policy RAG application as a webhook on various platforms.

## Prerequisites

1. **Environment Variables**: You need to set up these environment variables:
   - `GOOGLE_API_KEY`: Your Google Gemini API key
   - `PINECONE_API_KEY`: Your Pinecone API key

2. **Pinecone Index**: Ensure your Pinecone index `hackrx-gemini-index` is created and ready.

## Deployment Options

### Option 1: Railway (Recommended - Free Tier Available)

1. **Install Railway CLI**:
   ```bash
   npm install -g @railway/cli
   ```

2. **Login to Railway**:
   ```bash
   railway login
   ```

3. **Deploy**:
   ```bash
   railway init
   railway up
   ```

4. **Set Environment Variables**:
   ```bash
   railway variables set GOOGLE_API_KEY=your_google_api_key
   railway variables set PINECONE_API_KEY=your_pinecone_api_key
   ```

5. **Get your webhook URL**:
   ```bash
   railway domain
   ```

### Option 2: Render (Free Tier Available)

1. **Connect your GitHub repository** to Render
2. **Create a new Web Service**
3. **Configure**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Health Check Path**: `/health`
4. **Add Environment Variables** in the dashboard
5. **Deploy**

### Option 3: Heroku

1. **Install Heroku CLI**:
   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login**:
   ```bash
   heroku login
   ```

3. **Create app**:
   ```bash
   heroku create your-app-name
   ```

4. **Set environment variables**:
   ```bash
   heroku config:set GOOGLE_API_KEY=your_google_api_key
   heroku config:set PINECONE_API_KEY=your_pinecone_api_key
   ```

5. **Deploy**:
   ```bash
   git push heroku main
   ```

### Option 4: Docker Deployment

1. **Build the image**:
   ```bash
   docker build -t policy-rag .
   ```

2. **Run locally**:
   ```bash
   docker run -p 8000:8000 -e GOOGLE_API_KEY=your_key -e PINECONE_API_KEY=your_key policy-rag
   ```

3. **Deploy to cloud**:
   - **Google Cloud Run**:
     ```bash
     gcloud run deploy policy-rag --image gcr.io/PROJECT_ID/policy-rag --platform managed
     ```
   - **AWS ECS/Fargate**
   - **Azure Container Instances**

## Testing Your Webhook

### 1. Health Check
```bash
curl https://your-app-url.railway.app/health
```

### 2. Test the API
```bash
curl -X POST "https://your-app-url.railway.app/hackrx/run" \
  -H "Content-Type: application/json" \
  -d '{
    "documents": "https://example.com/sample-policy.pdf",
    "questions": ["What is the coverage limit?", "What are the exclusions?"]
  }'
```

## Webhook Integration Examples

### 1. Slack Bot Integration
```python
import requests

def send_to_slack(webhook_url, message):
    payload = {"text": message}
    requests.post(webhook_url, json=payload)

# Usage
webhook_url = "https://your-app-url.railway.app/hackrx/run"
response = requests.post(webhook_url, json={
    "documents": "https://example.com/policy.pdf",
    "questions": ["What is covered?"]
})
send_to_slack(slack_webhook, response.json()["answers"][0])
```

### 2. Discord Bot Integration
```python
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def ask(ctx, *, question):
    response = requests.post("https://your-app-url.railway.app/hackrx/run", json={
        "documents": "https://example.com/policy.pdf",
        "questions": [question]
    })
    await ctx.send(response.json()["answers"][0])
```

### 3. Zapier Integration
1. Create a Zap with trigger (e.g., new email)
2. Add HTTP POST action
3. Configure:
   - URL: `https://your-app-url.railway.app/hackrx/run`
   - Method: POST
   - Headers: `Content-Type: application/json`
   - Body: JSON with your document and questions

## Monitoring and Maintenance

### 1. Health Monitoring
- Set up uptime monitoring (UptimeRobot, Pingdom)
- Monitor the `/health` endpoint
- Set up alerts for downtime

### 2. Logs and Debugging
- Railway: `railway logs`
- Render: Dashboard → Logs
- Heroku: `heroku logs --tail`

### 3. Scaling
- Railway: Automatic scaling based on usage
- Render: Manual scaling in dashboard
- Heroku: `heroku ps:scale web=2`

## Security Considerations

1. **API Keys**: Never commit API keys to your repository
2. **Rate Limiting**: Consider adding rate limiting for production
3. **CORS**: Configure CORS if needed for web frontend
4. **Authentication**: Add API key authentication for production use

## Troubleshooting

### Common Issues:

1. **Build Failures**:
   - Check if all dependencies are in `requirements.txt`
   - Ensure Python version compatibility

2. **Runtime Errors**:
   - Check environment variables are set correctly
   - Verify Pinecone index exists and is accessible

3. **Timeout Issues**:
   - Increase timeout limits in deployment platform
   - Optimize document processing for large files

### Support:
- Check logs: `railway logs` or platform-specific commands
- Test locally first: `docker-compose up`
- Verify API keys and Pinecone connectivity
