import streamlit as st
import openai
import os

# Set OpenAI API key (from Streamlit secrets or env)
openai.api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))

# Streamlit setup
st.set_page_config(page_title="Lachesis Assistant", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #D7263D;'>Redback Operations</h1>
    <h3 style='text-align: center; color: #444;'>Lachesis – Elderly Wearable Tech Assistant</h3>
    <hr>
""", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.sidebar.button("Reset Chat"):
    st.session_state.chat_history = []

# Display previous messages
for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(msg)

user_input = st.chat_input("Ask a question about Lachesis...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are Lachesis, a helpful elderly health assistant. Answer clearly and concisely based on elderly health guidance."},
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
                assistant_reply = f"Error from OpenAI: {str(e)}"

            st.markdown(assistant_reply)
            st.session_state.chat_history.append(("assistant", assistant_reply))
