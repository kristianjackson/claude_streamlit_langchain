import streamlit as st
import langchain
import claude

# Streamlit UI
st.set_page_config(page_title="My Chatbot", page_icon=":robot:") 

st.write("""
# My Chatbot
""")

# Create columns for chat interface
col1, col2 = st.columns([1,4])

with col1:
    st.image("bot_profile.png")

with col2:
    # Chat history placeholder
    chat_hist = st.empty() 

# User input text box
user_input = st.text_input("You: ", "", key="user_input")

if user_input:

    # Get bot response
    bot_response = get_bot_response(user_input)
    
    # Update chat history
    chat_hist_dict = {"You": user_input, "Bot": bot_response}
    chat_hist.json(chat_hist_dict)

    # Clear input field
    st.text_input("You: ", "", key="user_input") 

# Styling  
st.markdown("""
<style>
.stApp {
  background-image: linear-gradient(to bottom,#f4f4f4,#e0e0e0);
}

.element-container {
  max-width: 1000px;
}
</style>
""", unsafe_allow_html=True)
