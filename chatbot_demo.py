import streamlit as st
from openai import OpenAI
import os

# Set up the page
st.set_page_config(page_title="Lachesis Assistant", layout="centered")

# Page title and subtitle with styling
st.markdown("""
    <h1 style='text-align: center; color: #D7263D;'>Redback Operations</h1>
    <h3 style='text-align: center; color: #444;'>Lachesis – Elderly Wearable Tech Assistant</h3>
    <hr style='margin-top: 10px;'>
""", unsafe_allow_html=True)

# Initialize OpenAI client using API key from secrets or env
client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY")))

# Initialize session chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar: reset chat button
if st.sidebar.button("Reset Chat"):
    st.session_state.chat_history = []

# Display previous chat messages
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)

# Input field for user messages
user_input = st.chat_input("Ask something about Lachesis...")

if user_input:
    # Show user message
    st.session_state.chat_history.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate assistant reply
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are Lachesis, a friendly elderly health assistant developed by Redback Operations. Answer clearly, helpfully, and focus on elderly health and wearable technology guidance."},
                        *[
                            {"role": role, "content": msg}
                            for role, msg in st.session_state.chat_history
                            if role in ["user", "assistant"]
                        ],
                        {"role": "user", "content": user_input}
                    ]
                )
                assistant_reply = response.choices[0].message.content
            except Exception as e:
                assistant_reply = f"Error: {str(e)}"

            # Show assistant response and store it
            st.markdown(assistant_reply)
            st.session_state.chat_history.append(("assistant", assistant_reply))
