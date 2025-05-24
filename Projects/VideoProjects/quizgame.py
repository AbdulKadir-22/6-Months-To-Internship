
questions = ("Python was developed by ",
             "Which type of Programming does Python support?: ",
             "Is Python case sensitive when dealing with identifiers?: ",
             "Which of the following is the correct extension of the Python file?: ",
             "Which of the following is used to define a block of code in Python language?: ")

options = (("A. Guido Van",    "B. Dennis Ritchi",       "C.Bjarne ",        "D. Brenden"),
           ("A. object-oriented programming",     "B.  structured programming",       "C. functional programming",         "D.  all of the mentioned"),
           ("A. no", "B.  yes",         "C. machine dependent", "D.  none of the mentioned"),
           ("A. .python",    "B.  .pl", "C.  .py",     "D.  .p"),
           ("A. Indentation",      "B. Key",         "C. Brackets",    "D. All of the mentioned"))

answers = ("A", "D", "B" , "C", "A")
guesses = []
score = 0
question_num = 1

for question in questions:
    print("--------------------------------------")
    print(f"{question_num}. {question}")
    for option in options[question_num]:
        print(option)

    guess = input("Enter your Answer: ").upper()

    guesses.append(guess)
    
    if guess == answers[question_num]:
        score +=1
        print("Correct")
    else:
        print(f"The right Answer is: {answers[question_num]}")

    question_num +=1

print("----------------------------------")
print("              RESULT               ")
print("----------------------------------")

print(f"Your score is: {score}")
