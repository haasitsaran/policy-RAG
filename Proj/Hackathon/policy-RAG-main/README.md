# Policy RAG Webhook

A high-accuracy RAG (Retrieval-Augmented Generation) engine for insurance policy analysis, deployed as a webhook.

## 🚀 Quick Deploy

### Option 1: Railway (Recommended)
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway init
railway up

# Set environment variables
railway variables set GOOGLE_API_KEY=your_google_api_key
railway variables set PINECONE_API_KEY=your_pinecone_api_key
```

### Option 2: Render
1. Connect your GitHub repo to Render
2. Create a new Web Service
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables in dashboard

### Option 3: Heroku
```bash
heroku create your-app-name
heroku config:set GOOGLE_API_KEY=your_google_api_key
heroku config:set PINECONE_API_KEY=your_pinecone_api_key
git push heroku main
```

## 📋 Prerequisites

- Google Gemini API key
- Pinecone API key
- Pinecone index named `hackrx-gemini-index`

## 🔧 API Endpoints

### Health Check
```
GET /health
```

### Main API
```
POST /hackrx/run
Content-Type: application/json

{
  "documents": "https://example.com/policy.pdf",
  "questions": ["What is covered?", "What are the exclusions?"]
}
```

## 🧪 Testing

```bash
# Test your deployed webhook
python test_webhook.py https://your-app.railway.app
```

## 📦 Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
uvicorn main:app --reload

# Or with Docker
docker-compose up
```

## 🔗 Webhook Integration Examples

### Slack Bot
```python
import requests

webhook_url = "https://your-app.railway.app/hackrx/run"
response = requests.post(webhook_url, json={
    "documents": "https://example.com/policy.pdf",
    "questions": ["What is covered?"]
})
```

### Discord Bot
```python
@bot.command()
async def ask(ctx, *, question):
    response = requests.post("https://your-app.railway.app/hackrx/run", json={
        "documents": "https://example.com/policy.pdf",
        "questions": [question]
    })
    await ctx.send(response.json()["answers"][0])
```

## 📊 Monitoring

- Health check: `/health`
- Logs: Platform-specific (Railway: `railway logs`)
- Uptime monitoring: Set up alerts for `/health` endpoint

## 🔒 Security

- Environment variables for API keys
- Consider adding rate limiting for production
- Add authentication for production use

## 📚 Documentation

See `DEPLOYMENT.md` for detailed deployment instructions.

## 🛠️ Architecture

- **FastAPI**: Web framework
- **Google Gemini**: LLM and embeddings
- **Pinecone**: Vector database
- **unstructured.io**: Document parsing
- **Docker**: Containerization

## 📄 License

MIT License
