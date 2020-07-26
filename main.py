from random import sample
from csv import reader
from time import sleep

# Check to see if the user provides a valid question count
while True:
    question_count = input("How many questions do you want to answer?  ")
    try:
        value = int(question_count)
        if value <= 0:
            print("Please enter a valid number.")
            continue
        question_count = value
        break
    except ValueError:
        print("Please enter a valid number.")

# Initialize questions with question count
f = open("country-capitals.csv", "r")
terms = list(reader(f))

questions = sample(terms, question_count)
num_correct = 0

# Quiz Loop
for question in questions:
    answer = input("What is the capital of {}?  ".format(question[0]))
    if answer.lower() == question[1].lower():
        print("Correct")
        num_correct += 1
    else:
        print("Incorrect. The correct answer is {}".format(question[1]))
    sleep(3)
print("You got {} out of {} ({}%) correct.".format(num_correct, question_count, num_correct/question_count*100))