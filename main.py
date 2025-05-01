import streamlit as st
import google.generativeai as gen_ai

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":brain:",
    layout="centered",
)

# Load API key from Streamlit Secrets
GOOGLE_API_KEY = st.secrets["api_keys"]["GOOGLE_API_KEY"]

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    return "assistant" if user_role == "model" else user_role

# Initialize chat session if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display chatbot title
st.title("🤖 Gemini Pro - ChatBot")

# Display chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input for user message
user_prompt = st.chat_input("Ask Gemini-Pro...")

if user_prompt:
    # Show user message
    st.chat_message("user").markdown(user_prompt)

    # Send to Gemini-Pro and get response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Show Gemini-Pro's reply
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
