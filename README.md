# HR-LLM-Assistant

**HR-LLM-Assistant** is an intelligent chatbot designed to assist HR teams in answering queries related to employee benefits, leave policies, onboarding, and more. It uses the power of OpenAI’s GPT-3 and other tools to analyze employee engagement, provide sentiment analysis, and retrieve HR-related documents.



## Features
- Answer HR-related queries regarding leave policies, benefits, onboarding, etc.
- Retrieve and summarize employee handbook documents.
- Sentiment analysis of employee queries and responses.
- HR manager dashboard for viewing employee engagement metrics.


## Installation

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Set up environment variables by creating a `.env` file with your OpenAI API key:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```

3. Run the application:
    ```bash
    python app.py
    ```

## Technologies Used
- **Flask** - For backend API
- **OpenAI GPT-3** - For natural language processing
- **Langchain** - For LLM pipeline management
- **ChromaDB** - For storing document embeddings
- **TextBlob** - For sentiment analysis
- **Pinecone** - For vector database storage (optional)




