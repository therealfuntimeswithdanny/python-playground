# Simple Multiple-Choice Quiz in Python

# Define a list of questions, where each question is a dictionary that contains the question,
# a list of possible options, and the correct option number (as a string for easy comparison).
quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "3"  # Paris is the 3rd option
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "2"  # 4 is the 2nd option
    },
    {
        "question": "What is the color of the sky on a clear day?",
        "options": ["Blue", "Green", "Red", "Yellow"],
        "answer": "1"  # Blue is the 1st option
    }
]

score = 0  # Initialize the player's score

print("Welcome to the Multiple-Choice Quiz!")
print("-------------------------------------\n")

# Loop through each question in the quiz list.
for item in quiz:
    print(item["question"])
    # Display the options with numbers.
    for index, option in enumerate(item["options"], start=1):
        print(f"{index}. {option}")
    
    user_answer = input("Your answer (enter the number of the correct option): ").strip()
    
    # Check if the user's answer matches the correct option.
    if user_answer == item["answer"]:
        print("Correct!\n")
        score += 1
    else:
        # Show the correct answer.
        correct_index = int(item["answer"]) - 1
        correct_option = item["options"][correct_index]
        print(f"Incorrect. The correct answer is {item['answer']}: {correct_option}.\n")

# After all questions, display the total score.
print(f"Your total score: {score} out of {len(quiz)}")
