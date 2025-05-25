import streamlit as st

# Predefined Q&A responses
QA_PAIRS = {
  "what is lachesis": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how does lachesis monitor heart rate": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how does lachesis monitor hydration": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how does lachesis detect sleep quality": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how does lachesis detect falls": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "what is a healthy heart rate for seniors": "Lachesis monitors heart rate continuously and provides alerts if the rate exceeds or drops below healthy thresholds.",
  "what is a healthy hydration level for elderly": "Lachesis estimates hydration levels by monitoring body temperature, motion, and daily patterns to ensure elderly users stay well-hydrated.",
  "how many hours of sleep do seniors need": "Using motion sensors and heart rate variability, Lachesis tracks sleep stages, interruptions, and overall sleep quality.",
  "how accurate is lachesis in detecting falls": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "can lachesis send alerts to caregivers": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how often should seniors check their blood pressure": "Elderly individuals should check their blood pressure at least once daily, especially if they have a history of heart conditions. Those on medication or with irregular rhythms may benefit from continuous or twice-daily monitoring using wearables like Lachesis.",
  "how does dehydration affect older adults": "Lachesis estimates hydration levels by monitoring body temperature, motion, and daily patterns to ensure elderly users stay well-hydrated.",
  "what causes low heart rate in seniors": "Lachesis monitors heart rate continuously and provides alerts if the rate exceeds or drops below healthy thresholds.",
  "how can seniors stay hydrated": "This information is tracked and managed by Lachesis to provide personalized health insights for elderly users.",
  "what are early signs of a fall risk": "Fall detection is enabled through real-time motion analysis, triggering emergency alerts when sudden impact patterns are identified.",
  "how does lachesis track steps and movement": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "what sleep issues are common in elderly people": "Using motion sensors and heart rate variability, Lachesis tracks sleep stages, interruptions, and overall sleep quality.",
  "how can seniors improve their sleep quality": "Using motion sensors and heart rate variability, Lachesis tracks sleep stages, interruptions, and overall sleep quality.",
  "how can lachesis help detect sleep apnea": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how does lachesis provide weekly health summaries": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how can lachesis help monitor chronic conditions": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how does lachesis calculate hydration scores": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how does lachesis measure sleep interruptions": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "can lachesis detect irregular heartbeat": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "can lachesis integrate with other health apps": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "what is normal blood pressure for elderly": "This information is tracked and managed by Lachesis to provide personalized health insights for elderly users.",
  "how does lachesis track stress levels": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how can wearables improve elderly health care": "This information is tracked and managed by Lachesis to provide personalized health insights for elderly users.",
  "what are common heart problems in elderly": "This information is tracked and managed by Lachesis to provide personalized health insights for elderly users.",
  "what data does lachesis collect daily": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how does lachesis calculate sleep efficiency": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "what is heart rate variability": "Lachesis monitors heart rate continuously and provides alerts if the rate exceeds or drops below healthy thresholds.",
  "what is normal range of oxygen saturation for elderly": "This information is tracked and managed by Lachesis to provide personalized health insights for elderly users.",
  "how often should lachesis be charged": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how to wear lachesis correctly": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "what happens if lachesis detects a fall": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "what is average weekly sleep duration for seniors": "Using motion sensors and heart rate variability, Lachesis tracks sleep stages, interruptions, and overall sleep quality.",
  "what hydration reminders does lachesis offer": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "can lachesis detect fever": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "what to do after fall detection alert": "Fall detection is enabled through real-time motion analysis, triggering emergency alerts when sudden impact patterns are identified.",
  "can lachesis track outdoor activity": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "what kind of sensors does lachesis use": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "is lachesis waterproof": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how does lachesis monitor temperature": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how to read weekly health reports from lachesis": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how is senior heart rate different from younger adults": "Lachesis monitors heart rate continuously and provides alerts if the rate exceeds or drops below healthy thresholds.",
  "can lachesis help prevent hospital admissions": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how does lachesis learn personal health trends": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "what is lachesis made of": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how does lachesis notify emergency contacts": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "can lachesis work without internet": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how does lachesis measure blood oxygen levels": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how to reset lachesis": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "what to do if lachesis band feels loose": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how can caregivers access lachesis data": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how often is lachesis data updated": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how secure is the lachesis system": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how does lachesis track daytime napping": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "can lachesis identify sleep disorders": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "can lachesis support remote health monitoring": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "what kind of battery life does lachesis offer": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how does movement affect hydration estimation": "Lachesis estimates hydration levels by monitoring body temperature, motion, and daily patterns to ensure elderly users stay well-hydrated.",
  "how can lachesis assist in elder fall prevention programs": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "can lachesis differentiate between walking and running": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "what health metrics does lachesis average weekly": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how does lachesis measure sleep quality score": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "what factors reduce sleep quality in older adults": "Using motion sensors and heart rate variability, Lachesis tracks sleep stages, interruptions, and overall sleep quality.",
  "can lachesis store historical health data": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "what alerts does lachesis provide": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "can lachesis be used during exercise": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "can seniors wear lachesis at night": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how does temperature impact elderly hydration": "Lachesis estimates hydration levels by monitoring body temperature, motion, and daily patterns to ensure elderly users stay well-hydrated.",
  "does lachesis support voice commands": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how does lachesis determine physical inactivity": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how can lachesis promote active aging": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "what are the benefits of lachesis for caregivers": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "can lachesis monitor breathing rate": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "can lachesis detect abnormal pulse": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how often are health reports generated": "This information is tracked and managed by Lachesis to provide personalized health insights for elderly users.",
  "can lachesis provide daily health tips": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how to troubleshoot lachesis connectivity issues": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how does lachesis differentiate between sleep stages": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "can lachesis integrate with hospital systems": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "what physical signs does lachesis detect": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how customizable is the lachesis dashboard": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how does hydration impact heart rate": "Lachesis monitors heart rate continuously and provides alerts if the rate exceeds or drops below healthy thresholds.",
  "what does lachesis recommend after detecting poor sleep": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how does age impact hydration needs": "Lachesis estimates hydration levels by monitoring body temperature, motion, and daily patterns to ensure elderly users stay well-hydrated.",
  "how does lachesis respond to fall confirmation": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "can lachesis show weekly exercise summaries": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "can lachesis help in managing hypertension": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how does lachesis track posture changes": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "can lachesis sync data with mobile apps": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "can lachesis assist in senior rehabilitation": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "what medical conditions can lachesis monitor": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how does lachesis flag emergency conditions": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "what improvements are coming to lachesis": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "how accurate is lachesis sleep tracking": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "what makes lachesis different from other wearables": "Lachesis is designed to assist elderly individuals with health monitoring through advanced sensors and AI-powered analysis. It helps track vitals and improve overall well-being.",
  "what is redback operations": "Redback Operations is the student innovation team behind Lachesis, responsible for system design, software development, and integration.",
  "what is my heart rate right now": "Your current heart rate is 92 bpm, which is within the normal range for light activity. No action needed.",
  "what is my hydration level right now": "Your hydration level is currently LOW (1.2L today). Please drink a glass of water and check again in 30 minutes.",
  "what is my average heart rate over last week": "Your average heart rate over the last 7 days was 78 bpm. This is a healthy range for your age group.",
  "what is my sleep pattern like": "You've averaged 6.4 hours of sleep over the past week with 4 sleep interruptions per night. Try limiting screen time before bed.",
  "how much water did I drink today": "You’ve consumed 1.5 liters of water today. Aim for at least 2.2 liters for optimal hydration.",
  "how many steps have I taken today": "You’ve walked 3,450 steps today. Let’s aim for at least 5,000 steps to stay active.",
  "how many hours did I sleep last night": "You slept 7 hours and 10 minutes last night. Well done maintaining good sleep hygiene.",
  "what is my average hydration level this week": "Your weekly average hydration intake is 1.7 liters/day. You're slightly under the target—keep sipping!",
  "how many falls were detected this week": "No falls were detected this week. Keep using handrails and watch for uneven surfaces to stay safe.",
  "what was my lowest heart rate this week": "Your lowest recorded heart rate this week was 58 bpm during deep sleep, which is normal."
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
