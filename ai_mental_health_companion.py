# ai_mental_health_companion.py

import streamlit as st
from textblob import TextBlob
import random

# Motivational quotes
quotes = [
    "Keep going, you’re stronger than you think.",
    "Every day may not be good, but there is something good in every day.",
    "Your feelings are valid, and it’s okay to not be okay.",
    "Believe in yourself and all that you are.",
    "You are not alone. Keep moving forward."
]

# Streamlit App UI
st.set_page_config(page_title="AI Mental Health Companion", page_icon="🧠")
st.title("🧠 AI-Powered Mental Health Companion")
st.write("Hello! I'm here to listen and support you 💙")

# User input
user_input = st.text_input("How are you feeling today?")

if user_input:
    # Sentiment Analysis
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        mood = "😊 Positive"
        response = "I'm glad you're feeling good! Keep shining!"
    elif polarity < 0:
        mood = "😔 Negative"
        response = "I'm sorry you're feeling low. Remember, tough times don't last."
    else:
        mood = "😐 Neutral"
        response = "I see, thanks for sharing. Remember, it's okay to have calm days too."

    # Display results
    st.subheader("Mood Detection")
    st.write(f"Your mood: {mood}")

    st.subheader("Companion Response")
    st.write(response)

    st.subheader("Motivational Quote for You")
    st.write(random.choice(quotes))
