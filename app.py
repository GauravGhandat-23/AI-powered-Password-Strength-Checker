import streamlit as st
import math
import requests
import json
from groq import Groq

# Initialize the Groq client with your API key
client = Groq(api_key="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")  # Replace with your actual API key

# Function to evaluate password strength
def evaluate_password(password):
    suggestions = []
    entropy = calculate_entropy(password)
    
    # Length check
    if len(password) < 8:
        suggestions.append("Password is too short. Use at least 8 characters.")
    
    # Complexity checks
    if not any(c.islower() for c in password):
        suggestions.append("Use at least one lowercase letter.")
    if not any(c.isupper() for c in password):
        suggestions.append("Use at least one uppercase letter.")
    if not any(c.isdigit() for c in password):
        suggestions.append("Use at least one digit.")
    if not any(c in '!@#$%^&*()_+' for c in password):
        suggestions.append("Include at least one special character.")

    # Entropy check (for complexity)
    if entropy < 40:
        suggestions.append("Increase password complexity for better security.")
    
    # Australian Cyber Security Centre Advice
    if "password" in password.lower() or "1234" in password:
        suggestions.append("Avoid easily guessable passwords like 'password' or '1234'.")

    strength = "Weak"
    if len(password) >= 12 and not suggestions:
        strength = "Strong"
    elif len(password) >= 8 and not suggestions:
        strength = "Medium"

    return strength, suggestions

# Function to calculate entropy of the password
def calculate_entropy(password):
    n = len(password)
    unique_chars = len(set(password))
    return math.log(unique_chars, 2) * n

# Function to get AI-generated feedback using Groq API
def get_ai_feedback(password):
    messages = [
        {"role": "user", "content": f"Analyze this password: {password}. Provide security feedback."}
    ]

    try:
        completion = client.chat.completions.create(
            model="deepseek-r1-distill-llama-70b",
            messages=messages,
            temperature=0.6,
            max_tokens=4096,
            top_p=0.95,
            stream=False,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error fetching AI feedback: {e}"

# Streamlit UI
st.image('logo.png', width=500)  # Add your logo image
st.title("AI-powered-Password-Strength-Checker")

# Password input from user
password = st.text_input("Enter your password:", type="password")

if password:
    # Evaluate password
    strength, suggestions = evaluate_password(password)

    # Display password strength
    st.subheader(f"Password Strength: {strength}")
    
    # Display suggestions
    if suggestions:
        st.write("Suggestions to improve your password:")
        for suggestion in suggestions:
            st.write(f"- {suggestion}")
    else:
        st.write("Your password is strong!")

    # Get AI feedback
    with st.spinner("Fetching AI feedback..."):
        ai_feedback = get_ai_feedback(password)

    st.subheader("AI Feedback:")
    st.write(ai_feedback)
