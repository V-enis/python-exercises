# Create a trivia-style quiz game where the user can select different categories (e.g., General Knowledge, Science, History).
# For each category, create multiple questions with multiple-choice answers.
# Keep track of the score based on the user’s answers, and provide feedback at the end.
# Add difficulty levels: easy, medium, and hard.
# You could even add a timer for each question or a random set of questions.


# Importing the trivia data from trivia_data.py
from trivia_data import general_trivia, science_trivia, history_trivia, celebrities_trivia


print("Trivia fun!")
print("General,")
print("Science,")
print("History,")
print("or Celebrities?")
category = input("Please select your category: ")





if category.lower().strip() == "general":
  category = general_trivia
elif category.lower().strip() == "science":
  category = science_trivia
elif category.lower().strip() == "history":
  category = history_trivia
elif category.lower().strip() == "celebrities":
  category = celebrities_trivia


def display_questions(category):
    for x in range(0, 5):
        print(category[x]["Q"])
        print(category[x]["answers"])  
        
        while True:
            answer = input("Your answer (type 'end' to skip): ")  
            if answer == category[x]["correct"]:  
                print(f"Correct! {answer} is the right answer!")
                break  
            elif answer == "end":
              break
            else:
                print("Incorrect answer, try again") 

display_questions(category)


