<h1 align="center">🔒 AI-Powered Password Strength Checker 🔑</h1>

![image](https://github.com/user-attachments/assets/86a53b50-964c-42ce-843b-b906e2cf06f4)


# About the Project ⚙️

[![AI-Powered Password Strength Checker](https://img.shields.io/badge/AI--Powered%20Password%20Strength%20Checker-Active-brightgreen)](https://ai-powered-password-strength-checker-7qjikia53n4vf38dxx6dvh.streamlit.app/)

This project is a password strength checker built using Streamlit, Python, and Groq's AI-powered feedback. It evaluates the strength of a password based on several criteria, such as length, complexity, and entropy, and provides suggestions for improvement. Additionally, it uses Groq's AI model to generate personalized feedback to further enhance password security.It also provides suggestions to improve weak passwords, following the **Australian Cyber Security Centre**'s password guidelines.

## Features 🛠️
- **Password Evaluation**: Checks the strength of the password based on various criteria (length, complexity, entropy).
- **Real-Time Feedback**: Provides real-time strength feedback as you type.
- **Suggestions**: Suggests improvements for weak passwords, including using a combination of uppercase, lowercase, digits, and special characters.
- **Australian Cyber Security Centre** advice: Avoids common weak passwords like "password" or "1234."
- **AI Feedback**: Fetches personalized security feedback using Groq's AI model.

## Installation 📦

Follow these steps to get the application running locally on your machine.

1. Clone the Repository :
   
    ```bash
    git clone https://github.com/yourusername/AI-powered-Password-Strength-Checker.git
    cd AI-powered-Password-Strength-Checker

2. Set Up a Virtual Environment : 🔧
Create and activate a virtual environment
    
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    
3. Replace Groq api key in the client = **Groq(api_key="Groq api key")** line with your actual Groq API key. You can get your API key by signing up on Groq's platform.
   
4. Install Dependencies : 📦
Install the required libraries

    ```bash
    pip install streamlit requests groq

4. Run the Application : 🚀
Once the dependencies are installed, run the Streamlit app

    ```bash
    streamlit run app.py
    
The app will start running on http://localhost:8501/.

## How It Works 🛠️

- **Password Input**: Enter a password in the input field.
- **Evaluation**: The app evaluates the strength of the password using various checks (length, character types, entropy).
- **Feedback**: Displays the password's strength (Weak, Medium, Strong) and provides suggestions to improve it.
- **Suggestions**: Suggestions include adding uppercase letters, numbers, special characters, and ensuring the password has sufficient length.
- **AI Feedback**: Once the password is entered, the app sends the password to the Groq API to fetch AI-generated feedback. The AI evaluates the password and provides suggestions for improvement.

## Example Passwords and Expected Results 🔐

- **Weak Password**: password
  - **Result**: "Weak" with suggestions like "Avoid easily guessable passwords."
- **Medium Password**: Password123
  - **Result**: "Medium" with suggestions like "Include at least one special character."
- **Strong Password**: StrongPassword123!
  - **Result**: "Strong" with no suggestions.

## Contributing 🤝

Feel free to fork this repository, create an issue, or submit a pull request. All contributions are welcome!

## Acknowledgments

- **Streamlit**: For making it easy to build web apps.

- **Australian Cyber Security Centre (ACSC)**: For the password guidelines.
  
- **Groq Python SDK**

## Preview 💻

## Weak Password

![weak password_page-0001](https://github.com/user-attachments/assets/9ac731ec-75a6-49fd-8613-2d3f57699bbf)

## Strong Password

![strong password_page-0001](https://github.com/user-attachments/assets/c8bc39f5-dd38-4881-ad55-c4508b773e0e)

## Connect with Me 🌐

- 📧 [Email](mailto:gauravghandat12@gmail.com)
- 💼 [LinkedIn](www.linkedin.com/in/gaurav-ghandat-68a5a22b4)
















