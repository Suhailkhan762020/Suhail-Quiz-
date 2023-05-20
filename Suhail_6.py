import streamlit as st

def quiz_app():
    # Define the quiz questions and answers
    questions = [
        {
            'question': 'What is the capital of France?',
            'options': ['Paris', 'London', 'Berlin', 'Rome'],
            'answer': 'Paris'
        },
        {
            'question': 'Which planet is known as the Red Planet?',
            'options': ['Mars', 'Jupiter', 'Saturn', 'Mercury'],
            'answer': 'Mars'
        },
        {
            'question': 'What is the largest ocean in the world?',
            'options': ['Pacific Ocean', 'Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean'],
            'answer': 'Pacific Ocean'
        }
    ]

    # Initialize variables
    total_questions = len(questions)
    correct_answers = 0

    # Display quiz questions and collect user answers
    for i, question in enumerate(questions):
        st.write(f"Question {i+1}: {question['question']}")
        selected_option = st.radio("Options", question['options'])
        if selected_option == question['answer']:
            correct_answers += 1

    # Display quiz results
    st.write(f"You scored {correct_answers} out of {total_questions}.")

# Run the quiz app
quiz_app()
