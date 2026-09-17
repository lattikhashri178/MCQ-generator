📝 AI MCQ Generator
📌 Overview

AI MCQ Generator is a simple AI-powered web application built using Python and Streamlit. It generates multiple-choice questions automatically based on a topic provided by the user.

The application uses a Hugging Face AI language model to create unique and educational MCQs with four options and the correct answer.

🎯 Objectives

Generate MCQs automatically using AI

Allow users to enter any educational topic

Allow users to select the number of questions

Provide different difficulty levels

Generate four options for each question

Display the correct answer

Allow generated MCQs to be downloaded



✨ Features

📚 Topic-based MCQ generation

🔢 Generate 1–10 questions

🎯 Easy, Medium, and Hard difficulty levels

🤖 AI-powered question generation

A, B, C, and D options displayed separately

✅ Correct answer for every question

📥 Download generated MCQs as a text file

🖥️ Simple Streamlit interface



🛠️ Technologies Used

Python

Streamlit

Hugging Face

Hugging Face InferenceClient

Regular Expressions (re)


📂 Project Structure

MCQ-Generator/
│
├── app.py
├── requirements.txt
└── README.md

<img width="1127" height="630" alt="1" src="https://github.com/user-attachments/assets/f52b9397-a4f9-48e3-a486-a101547e32e2" />
<img width="1217" height="590" alt="2" src="https://github.com/user-attachments/assets/78cf9079-dd33-416c-af74-3d614a47dbd9" />
<img width="1192" height="592" alt="3" src="https://github.com/user-attachments/assets/b248e961-925b-4019-8dd8-49068481b3fa" />
<img width="1166" height="655" alt="4" src="https://github.com/user-attachments/assets/2862c01b-a807-4284-8a9d-383b9a258451" />
<img width="1397" height="570" alt="5" src="https://github.com/user-attachments/assets/1595da62-465d-4a13-b3fc-bce1bf05ec7c" />


app.py

Contains the main Streamlit application and AI-based MCQ generation logic.

requirements.txt

Contains the Python libraries required to run the application.

README.md

Contains the project documentation.


🔄 Project Workflow

User Enters Topic
        ↓
Select Number of Questions
        ↓
Select Difficulty
        ↓
Create AI Prompt
        ↓
Hugging Face AI Model
        ↓
Generate MCQs
        ↓
Format Questions and Options
        ↓
Display MCQs
        ↓
Download MCQs


🚀 Installation

1. Clone or download the project

Open the project folder in VS Code.

2. Install required libraries

Open the terminal and run:

pip install -r requirements.txt

Or:

pip install streamlit huggingface_hub


🔑 Hugging Face Token Setup

The application requires a Hugging Face access token for AI inference.

Set the token as an environment variable.

Windows PowerShell
$env:HF_TOKEN="YOUR_HUGGINGFACE_TOKEN"

Do not share or upload your Hugging Face token to GitHub.


▶️ Run the Application

Run the following command in the terminal:

streamlit run app.py

The application will open in the browser.


💡 Example

Input

Topic: Python Programming

Number of Questions: 5

Difficulty: Medium

Output

Question 1: What is the correct way to define a function in Python?

A. def sum(a, b): return a + b

B. def sum(a, b): a + b

C. function sum(a, b): return a + b

D. def sum a, b: return a + b

Correct Answer: A

The application generates the requested number of questions in the same format.


📥 Download

After generating the MCQs, the user can click:

Download MCQs

The generated questions are saved as:

generated_mcqs.txt


🎓 Learning Outcomes

Through this project, I learned:

Python application development

Streamlit web application development

Prompt engineering

Hugging Face AI model integration

AI-based question generation

Text formatting using Regular Expressions

Environment variable management

Building an AI-powered educational application

👩‍💻 Author

LATTIKHASHRI.N.
