import streamlit as st

# Predefined Q&A responses
QA_PAIRS = {
    "what is lachesis": "Lachesis is a wearable health monitoring device for elderly individuals. It tracks heart rate, hydration, sleep, and blood pressure.",
    "how does it monitor hydration": "Lachesis estimates hydration by analyzing temperature, motion, and general activity patterns.",
    "what is redback operations": "Redback Operations is the student team behind the development of the Lachesis health system.",
    "what is a normal heart rate": "A normal resting heart rate for elderly adults is between 60 and 100 beats per minute.",
    "what does lachesis do": "Lachesis provides real-time health insights, daily summaries, and alerts based on wearable data tailored to elderly care."
}

# Streamlit page layout styling
st.set_page_config(page_title="Lachesis Assistant", layout="centered")

# Title and subtitle
st.markdown("""
    <h1 style='text-align: center; color: #D7263D;'>Redback Operations</h1>
    <h3 style='text-align: center; color: #444;'>Lachesis – Elderly Wearable Tech Assistant</h3>
    <hr>
""", unsafe_allow_html=True)

# Session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Reset button
if st.sidebar.button("Reset Chat"):
    st.session_state.chat_history = []

# Display previous messages
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)

# Chat input
user_input = st.chat_input("Ask a question about Lachesis...")

if user_input:
    # Show user's message
    st.session_state.chat_history.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Simulate assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            query = user_input.lower().strip()
            matched = None
            for key in QA_PAIRS:
                if key in query:
                    matched = QA_PAIRS[key]
                    break
            response = matched if matched else "I'm sorry, I don't have an answer for that yet."
            st.markdown(response)
            st.session_state.chat_history.append(("assistant", response))
