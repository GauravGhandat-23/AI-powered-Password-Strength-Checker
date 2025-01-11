import streamlit as st
import math

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
    # Calculating entropy based on the characters in the password
    n = len(password)
    unique_chars = len(set(password))
    return math.log(unique_chars, 2) * n

# Streamlit UI
st.image('logo.png', width=500)  # Add your logo image with a width of 200px
st.title("Password Strength Checker")

# Password input from user
password = st.text_input("Enter your password:")

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
