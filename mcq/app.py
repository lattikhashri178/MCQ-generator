import streamlit as st
from huggingface_hub import InferenceClient
import os
import re


st.set_page_config(
    page_title="AI MCQ Generator",
    page_icon="📝",
    layout="centered"
)



st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

.question-box {
    padding: 15px;
    border-radius: 10px;
    margin-top: 20px;
}

.option {
    padding: 8px;
    margin: 5px 0;
    border-radius: 6px;
}

.answer {
    padding: 10px;
    margin-top: 10px;
    border-radius: 6px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="main-title">📝 AI MCQ Generator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Generate unique multiple-choice questions using Artificial Intelligence</div>',
    unsafe_allow_html=True
)

st.markdown("---")



HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    st.error("Hugging Face token is not configured.")
    st.info(
        "Please set the HF_TOKEN environment variable in your terminal."
    )
    st.stop()



client = InferenceClient(
    api_key=HF_TOKEN
)



st.subheader("📚 Create Your MCQs")

topic = st.text_input(
    "Enter Topic",
    placeholder="Example: Python Programming"
)

number = st.number_input(
    "Number of Questions",
    min_value=1,
    max_value=10,
    value=5,
    step=1
)

difficulty = st.selectbox(
    "Select Difficulty",
    [
        "Easy",
        "Medium",
        "Hard"
    ]
)



generate = st.button(
    "✨ Generate MCQs",
    use_container_width=True
)



if generate:

    if topic.strip() == "":
        st.warning("⚠️ Please enter a topic first.")

    else:

        
        prompt = f"""
You are an expert educational MCQ generator.

Create exactly {number} unique multiple-choice questions about:

TOPIC: {topic}

DIFFICULTY: {difficulty}

The questions are for college students.

IMPORTANT:
- Generate exactly {number} questions.
- Every question must be different.
- Do not repeat questions.
- Each question must have exactly four options.
- Only one option must be correct.
- Options must be labeled A, B, C and D.
- Put every option on a separate line.
- Keep the questions clear and meaningful.
- Include a mixture of conceptual, practical and application-based questions.
- Do not include explanations.
- Do not add extra text before or after the questions.

Use EXACTLY this format:

Question 1: Write the question here

A. First option

B. Second option

C. Third option

D. Fourth option

Correct Answer: A


Question 2: Write the question here

A. First option

B. Second option

C. Third option

D. Fourth option

Correct Answer: B

Continue the same format until Question {number}.
"""

        try:

            with st.spinner("🤖 Generating your MCQs..."):

                response = client.chat.completions.create(
                    model="Qwen/Qwen2.5-72B-Instruct",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a professional educational "
                                "multiple-choice question generator. "
                                "Always follow the requested format exactly."
                            )
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    max_tokens=4000,
                    temperature=0.8
                )

            result = response.choices[0].message.content

           

            result = result.strip()

           
            result = result.replace("```text", "")
            result = result.replace("```markdown", "")
            result = result.replace("```", "")

          
            result = re.sub(
                r'\s+A\.\s*',
                '\n\nA. ',
                result
            )

            result = re.sub(
                r'\s+B\.\s*',
                '\n\nB. ',
                result
            )

            result = re.sub(
                r'\s+C\.\s*',
                '\n\nC. ',
                result
            )

            result = re.sub(
                r'\s+D\.\s*',
                '\n\nD. ',
                result
            )

            result = re.sub(
                r'\s+Correct Answer:\s*',
                '\n\n**Correct Answer:** ',
                result
            )

         
            result = re.sub(
                r'\s+(Question\s+\d+:)',
                r'\n\n\1',
                result
            )

           
            st.success("✅ MCQs generated successfully!")

            st.markdown("---")

            st.subheader("🎯 Generated MCQs")

            st.markdown(result)

            
            st.markdown("---")

            st.download_button(
                label="📥 Download MCQs",
                data=result,
                file_name="generated_mcqs.txt",
                mime="text/plain",
                use_container_width=True
            )

        except Exception as e:

            st.error("❌ Error while generating MCQs.")

            st.write(str(e))
