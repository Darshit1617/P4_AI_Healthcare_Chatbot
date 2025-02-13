import streamlit as st
from transformers import pipeline
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# essential nltk information
nltk.download('punkt')
nltk.download('stopwords')

# using a pre-trained Hugging Face model
chatbot = pipeline("text-generation", model="distilgpt2")

# defining healthcare-specific response logic
def healthcare_chatbot(user_input):

    if "symptom" in user_input:
        return "It looks that you are experiencing symptoms. Please consult a doctor for accurate advice."
    elif "appointment" in user_input:
        return "Would you like me to make an appointment with a doctor?"
    elif "medication" in user_input:
        return "It is necessary that you take your prescribed medicines on a regular schedule. If you experience any concerns, consult your doctor."
    else:
        # for additional inputs, using the Hugging Face model to generate a response
        response = chatbot(user_input, max_length=500, num_return_sequences=1)
        # specifies the max length of the generated text response, including the input & generated tokens
        # when set to 3, the model uses the input to generate three alternative answers
        return response[0]['generated_text']


# Streamlit for web app interface
def main():
    # basic web app setup: title and input area
    st.title("Healthcare Assistant Chatbot")
    
    # display a simple text input for user inquiries
    user_input = st.text_input("How can I assist you today?", "")
    
    # display chatbot response
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            # response = healthcare_chatbot(user_input)
            with st.spinner("Your query is being processed; please wait..."):
                response = healthcare_chatbot(user_input)
            print("response ",response)
            print("<--------------------------------------------------->")
            st.write("Healthcare Assistant: ", response)
        else:
            st.write("Please write your query")
            
if __name__ == "__main__":
    main()