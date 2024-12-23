# HR-LLM-Assistant
HR-LLM-Assistant is an AI-powered chatbot designed to assist HR teams by answering employee queries, managing policies, and providing insights into employee engagement metrics. Built using large language models (LLMs), it enhances HR operations with intelligent automation and data-driven decision support

Features
Answer HR-related queries regarding leave policies, benefits, onboarding, etc.
Retrieve and summarize employee handbook documents.
Sentiment analysis of employee queries and responses.
HR manager dashboard for viewing employee engagement metrics.
Installation
Install dependencies:

pip install -r requirements.txt
Set up environment variables by creating a .env file with your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key
Run the application:

python app.py
Technologies Used
Flask - For backend API
OpenAI GPT-3 - For natural language processing
Langchain - For LLM pipeline management
ChromaDB - For storing document embeddings
TextBlob - For sentiment analysis
Pinecone - For vector database storage (optional)
