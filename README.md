<h1 align="center">🔒 AI-Powered Password Strength Checker 🔑</h1>

![image](https://github.com/user-attachments/assets/86a53b50-964c-42ce-843b-b906e2cf06f4)


# About the Project ⚙️

![Phishing Detection](https://img.shields.io/badge/Phishing%20Detection-Active-brightgreen)

This is a password strength checker web application built using **Streamlit** and **Python**. The application evaluates the strength of user-entered passwords based on length, complexity, and entropy. It also provides suggestions to improve weak passwords, following the **Australian Cyber Security Centre**'s password guidelines.

## Features 🛠️
- **Password Evaluation**: Checks the strength of the password based on various criteria (length, complexity, entropy).
- **Real-Time Feedback**: Provides real-time strength feedback as you type.
- **Suggestions**: Suggests improvements for weak passwords, including using a combination of uppercase, lowercase, digits, and special characters.
- **Australian Cyber Security Centre** advice: Avoids common weak passwords like "password" or "1234."

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

3. Install Dependencies : 📦
Install the required libraries

    ```bash
    pip install streamlit

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

## Preview 💻

## Weak Password

![weak 1](https://github.com/user-attachments/assets/7a62e837-dbe9-435f-81e9-23cff8cd8b76)

![weak 2](https://github.com/user-attachments/assets/bdd9ceca-6b63-47d7-966d-2272e8959589)

## Strong Password

![strong 2](https://github.com/user-attachments/assets/461c4b3e-6bcd-4604-a51c-4c7cb59eee19)

## Connect with Me 🌐

- 📧 [Email](mailto:gauravghandat12@gmail.com)
- 💼 [LinkedIn](www.linkedin.com/in/gaurav-ghandat-68a5a22b4)
















