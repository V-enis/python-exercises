# Create a trivia-style quiz game where the user can select different categories (e.g., General Knowledge, Science, History).
# For each category, create multiple questions with multiple-choice answers.
# Keep track of the score based on the user’s answers, and provide feedback at the end.


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
  score = 0
  for x in range(0, 5):
    print(category[x]["Q"])
    print(category[x]["answers"])  
        
    while True:
      answer = input("Your answer (type 'end' to skip, will subtract from score): ")  
      if answer == category[x]["correct"]:  
        print(f"Correct! {answer} is the right answer!")
        score += 1
        break
      elif answer == "end":
        score -= 1
        break
      else:
        score -= 1
        print("Incorrect answer, try again") 
    print(f"Your score is {score}")


display_questions(category)


