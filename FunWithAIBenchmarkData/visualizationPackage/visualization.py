# visualization.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def visualize_question_correct_answers(questions):
    # Extract correct answers for each question
    correct_answers = [q['correct answer'] for q in questions]  # Correct answers (A, B, C, D)

    # Generate x-axis as question numbers
    question_numbers = [f"Q{i+1}" for i in range(len(questions))]  # Q1, Q2, ..., Q103

    # Create a DataFrame to plot with a custom y-axis order
    data = pd.DataFrame({
        'Questions': question_numbers,
        'Correct Answer': correct_answers
    })

    # Set the custom order for the y-axis: A at the bottom and D at the top
    correct_order = ['A', 'B', 'C', 'D']

    # Create the scatter plot with custom y-axis order and correct hue legend
    plt.figure(figsize=(20, 6))
    sns.scatterplot(x='Questions', y='Correct Answer', hue='Correct Answer', 
                    palette="deep", s=100, data=data, hue_order=correct_order)

    # Add vertical lines connecting each point to the x-axis for better visibility
    for i, question in enumerate(question_numbers):
        plt.vlines(x=question, ymin='A', ymax=correct_answers[i], colors='gray', alpha=0.5)

    # Set the custom order for the y-axis (A at the bottom, D at the top)
    plt.yticks(correct_order)  # Ensure the y-ticks are in A, B, C, D order

    # Customize plot
    plt.xticks(rotation=75, ha='right', fontsize=8)  # Rotate labels more and reduce font size
    plt.xlabel('Questions')
    plt.ylabel('Correct Answer')
    plt.title('Correct Answer for Each Question')
    plt.legend(title='Correct Answer', loc='upper right')  # Adjust the legend
    plt.tight_layout()  # Adjust the layout to fit labels
    plt.show()

