# Policy RAG Webhook

A FastAPI-based webhook service for processing insurance policy documents using RAG (Retrieval-Augmented Generation) with Google Gemini and Pinecone.

## Features

- PDF document processing and indexing
- Query expansion for better search results
- Concurrent question answering
- Pinecone vector database integration
- Google Gemini AI for embeddings and generation

## API Endpoints

### POST `/hackrx/run`

Process insurance policy documents and answer questions.

**Request Body:**
```json
{
  "documents": "https://example.com/policy.pdf",
  "questions": [
    "What is the coverage limit?",
    "What are the exclusions?"
  ]
}
```

**Response:**
```json
{
  "answers": [
    "The coverage limit is $500,000...",
    "Exclusions include..."
  ]
}
```

## Deployment to Render

### Prerequisites

1. Create a Render account at [render.com](https://render.com)
2. Set up your Google Generative AI API key
3. Set up your Pinecone API key and index

### Deployment Steps

1. **Fork/Clone this repository** to your GitHub account
2. **Connect to Render:**
   - Go to your Render dashboard
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the repository: `Akhil3517/llm`

3. **Configure the service:**
   - **Name:** `policy-rag-webhook`
   - **Environment:** `Python`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`

4. **Set Environment Variables:**
   - `GOOGLE_API_KEY`: Your Google Generative AI API key
   - `PINECONE_API_KEY`: Your Pinecone API key

5. **Deploy:**
   - Click "Create Web Service"
   - Render will automatically build and deploy your application

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Google Generative AI API key | Yes |
| `PINECONE_API_KEY` | Pinecone API key | Yes |
| `PINECONE_INDEX_NAME` | Pinecone index name (default: hackrx-gemini-index) | No |

## Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Akhil3517/llm.git
   cd llm
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   cp env.example .env
   # Edit .env with your API keys
   ```

4. **Run the application:**
   ```bash
   uvicorn main:app --reload
   ```

## API Usage

Once deployed, your webhook will be available at:
`https://your-app-name.onrender.com/hackrx/run`

### Example cURL request:

```bash
curl -X POST "https://your-app-name.onrender.com/hackrx/run" \
  -H "Content-Type: application/json" \
  -d '{
    "documents": "https://example.com/insurance-policy.pdf",
    "questions": [
      "What is the maximum coverage amount?",
      "What are the policy exclusions?"
    ]
  }'
```

## Architecture

- **FastAPI**: Web framework for the API
- **Google Gemini**: AI model for embeddings and text generation
- **Pinecone**: Vector database for document storage and retrieval
- **Unstructured**: PDF document processing
- **LangChain**: Document handling and processing

## License

MIT License
