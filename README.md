# HR-LLM-Assistant

An intelligent HR assistant built using Large Language Models (LLMs) to help HR managers and employees interact seamlessly. This chatbot can handle HR-related queries such as leave policies, benefits, and onboarding procedures while analyzing employee engagement metrics.

## Features
- HR assistant chatbot answering queries related to HR policies.
- Retrieval-Augmented Generation (RAG) to provide context-based answers using HR documents.
- Engagement metrics like average question and response sentiment.
- Support for HR managers to manage leave policies, benefits, and onboarding processes.

## Installation

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/Madhushan13/HR-LLM-Assistant.git
cd HR-LLM-Assistant
```


 ### Step 2: Set Up the Environment
  Create a Virtual Environment:

To create a virtual environment, run the following command:
```bash
python -m venv venv
```

Activate the Virtual Environment:

On Windows, run:
```
venv\Scripts\activate
```

On Mac/Linux, run:
```
source venv/bin/activate
```

### Step 3: Install Dependencies
Install the required Python dependencies using pip:
```
pip install -r requirements.txt
```

### Step 4: Create a .env File
To keep sensitive data like your OpenAI API key, create a **.env** file in the root of your project directory.

In the root folder (where **app.py** is located), create a file named **.env**.

Add the following content, replacing **your_openai_api_key** with your actual OpenAI API key:
```bash
OPENAI_API_KEY=your_openai_api_key
```
### Step 5: Run the Flask App
Once everything is set up, you can run the chatbot with the following command:
```
python app.py
```
Your chatbot should now be running locally at **http://localhost:5000**.

### Step 6: Testing the Chatbot with Postman
Once your bot is running, you can test it using Postman.

1: Test the **/ask** Endpoint:
Open Postman and create a POST request.

Use the following URL:
```
http://localhost:5000/ask

```
In the Headers section, add:

* Key: Content-Type

* Value: application/json

In the Body section, select raw and JSON format. Then add the following JSON to simulate a user query:

```
{
    "query": "What is the leave policy?"
}

```
Click Send. You should receive a response like this:

```
{
    "response": "Employees are entitled to 10 days of paid leave per year."
}
```
2: Test the **/analyze-engagement** Endpoint:
Create a GET request.

Use the following URL:

```
http://localhost:5000/analyze-engagement
```

Click Send. You should receive a response like:
```
{
    "avg_question_sentiment": 0.5,
    "avg_response_sentiment": 0.6
}
```


## Technologies Used
- **Python** - For programing language 
- **Flask** - For backend API
- **OpenAI GPT-3** - For natural language processing
- **Langchain** - For LLM pipeline management
- **ChromaDB** - For storing document embeddings
- **TextBlob** - For sentiment analysis
- **Pinecone** - For vector database storage (optional)




