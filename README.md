**AI-Powered Healthcare Chatbot:**

**Overview:**

The AI-Powered Healthcare Chatbot is a smart, interactive assistant designed to provide healthcare-related guidance to users. Built using Python, it utilizes Natural Language Processing (NLP) and AI-driven responses to assist users with medical inquiries such as symptoms, medications, and appointments.


**Used Tech Stack:**

Frontend: Streamlit (for the user interface)
Backend: Python(3.12), Hugging Face Transformers (distilgpt2)
NLP: NLTK (for text preprocessing)
AI Model: Hugging Face pipeline (GPT-2 based model)


**Installation & Setup:**

1️⃣ Clone the Repository

    git clone https://github.com/Darshit1617/P4_AI_Healthcare_Chatbot.git
    cd healthcare-chatbot
    
2️⃣ Install Dependencies

    pip install -r requirements.txt

3️⃣ Run the Chatbot


**How It Works:**

  User enters a query (e.g., "I have a headache").
  The chatbot analyzes the input and checks for predefined responses.
  If a predefined response exists, it is returned immediately.
  Otherwise, the chatbot generates an AI-driven response using distilgpt2.
  The answer is displayed on the Streamlit web interface.
