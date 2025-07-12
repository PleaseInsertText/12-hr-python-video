import time

questions = ("What is the capital city of Qatar?: ",
             "Which of these mammals lay eggs?: ",
             "What is the hottest planet?: ",
             "What is the largest ocean?: ",
             "What temperature in celsius (℃) does water freeze at?:")

options = (("A: Abu Dhabi", "B: Doha", "C: Riyadh", "D: Muscat"),
           ("A: Wooly Mammoth", "B: Whale", "C: Cat", "D: Platypus"),
           ("A: Mercury", "B: Earth", "C: Venus", "D: Jupiter"),
           ("A: Pacific Ocean", "B: Atlantic Ocean", "C: Arctic Ocean", "D: Southern Ocean"),
           ("A: 1℃", "B: 0℃", "C: 0.5℃", "D: -1"))

answers = ("B", "D", "C", "A", "B")

guesses = []
score = 0
question_num=0

for question in questions:
    print("---------------------")
    print(question)
    print()
    for option in options[question_num]:
        print(option)

    guess = input("\nEnter your answer (A, B, C or D): ")
    guesses.append(guess)
    if guess.upper().strip() == answers[question_num]:
         print("CORRECT!")
         score+=1
         time.sleep(2)
    else:
        print(f"INCORRECT!")
        print(f"The correct answer is {answers[question_num]}")
        time.sleep(2)

    question_num+=1

print()
print("-----------------------------")
print("          RESULTS            ")
print("-----------------------------")

print("ANSWERS: ", end="")
for answer in answers:
    print(answer, end=" ")

print()
print()

print("YOUR GUESSES: ", end="")
for choice in guesses:
    print(choice.upper().strip(), end=" ")

print()

score = int((score/len(questions)) * 100)
print(f"YOUR SCORE IS {score}%!")