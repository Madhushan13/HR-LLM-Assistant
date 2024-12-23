import os
import csv
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS 
import openai
import chromadb
from dotenv import load_dotenv
from textblob import TextBlob
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Initialize ChromaDB client
client = chromadb.Client()

# Create or connect to a ChromaDB collection for storing embeddings
collection_name = "hr-policies"
collection = client.create_collection(collection_name)

# Add HR documents and store their embeddings
documents = [
    "Leave Policy: Employees are entitled to 10 days of paid leave per year.",
    "Employee Benefits: The company offers healthcare, wellness, and travel reimbursement programs.",
    "Onboarding Process: New employees must complete HR forms and set up accounts with IT."
]

# Add documents and their embeddings to ChromaDB
for i, doc in enumerate(documents):
    # Generate embedding for the document using OpenAI
    response = openai.embeddings.create(
        model="text-embedding-ada-002",  # Use the correct embedding model
        input=doc
    )
    embedding = response.data[0].embedding  # Correctly access the embedding

    # Generate a unique ID for each document (e.g., "doc_0", "doc_1", etc.)
    doc_id = f"doc_{i}"

    # Add the document, ID, metadata, and embedding to ChromaDB
    collection.add(
        ids=[doc_id],  # Add the ID of the document
        documents=[doc],  # The document itself
        metadatas=[{"text": doc}],  # Metadata for the document
        embeddings=[embedding]  # The embedding for the document
    )

# Function to log interactions
def log_interaction(question, response):
    log_file = 'engagement_logs.csv'
    file_exists = os.path.isfile(log_file)

    # Analyze sentiment for the question and response
    question_sentiment = analyze_sentiment(question)
    response_sentiment = analyze_sentiment(response)

    with open(log_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write headers if the file doesn't exist
        if not file_exists:
            writer.writerow(['timestamp', 'question', 'response', 'question_sentiment', 'response_sentiment'])

        # Write the interaction data with sentiment
        writer.writerow([datetime.now(), question, response, question_sentiment, response_sentiment])

# Sentiment analysis function
def analyze_sentiment(text):
    # Use TextBlob to analyze sentiment (polarity)
    blob = TextBlob(text)
    return blob.sentiment.polarity

# Function to calculate average sentiment for questions and responses
def analyze_engagement():
    # Load the log file into a DataFrame
    df = pd.read_csv('engagement_logs.csv')
    
    # Check if the file contains data
    if df.empty:
        return "No data available for analysis."
    
    # Calculate average sentiment for queries and responses
    avg_question_sentiment = df['question_sentiment'].mean()
    avg_response_sentiment = df['response_sentiment'].mean()

    return avg_question_sentiment, avg_response_sentiment

@app.route('/ask', methods=['POST'])
def ask():
    # Parse user input from the POST request body
    data = request.json
    question = data.get("query", "")

    if question.lower() != "bye":
        try:
            # Get the embedding for the user query using OpenAI's new API
            query_response = openai.embeddings.create(  # Correct method in OpenAI >= 1.0.0
                model="text-embedding-ada-002",
                input=question
            )
            query_embedding = query_response.data[0].embedding  # Correctly access the query embedding

            # Search ChromaDB for the most relevant document
            results = collection.query(
                query_embeddings=[query_embedding],
                n_results=1
            )

            # Retrieve the most relevant document and prepare the prompt
            relevant_document = results['documents'][0] if results['documents'] else "No relevant document found."

            # Send the query along with the relevant document to OpenAI's chat model
            response = openai.chat.completions.create(  # Correct method for newer OpenAI API
                model="gpt-3.5-turbo",  # You can use a more suitable model
                messages=[ 
                    {"role": "system", "content": "You are a helpful HR assistant."},
                    {"role": "user", "content": f"Given the document: {relevant_document}\n\nAnswer this question: {question}"}
                ],
                max_tokens=150,
                temperature=0.7
            )

            # Extract GPT's response
            gpt_response = response.choices[0].message.content.strip()

            # Log the interaction
            log_interaction(question, gpt_response)

            return jsonify({"response": gpt_response})

        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"response": "Bye!"})

# Endpoint for analyzing engagement metrics
@app.route('/analyze-engagement', methods=['GET'])
def analyze_engagement_endpoint():
    try:
        avg_question_sentiment, avg_response_sentiment = analyze_engagement()
        return jsonify({
            "avg_question_sentiment": avg_question_sentiment,
            "avg_response_sentiment": avg_response_sentiment
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
