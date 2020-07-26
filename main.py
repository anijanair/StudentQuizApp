from random import sample
from csv import reader


f = open("country-capitals.csv", "r")
terms = list(reader(f))

questions = sample(terms, 10)

for question in questions:
    answer = input("What is the capital of {}?  ".format(question[0]))
    if answer.lower() == question[1].lower():
        print("Correct")
    else:
        print("Incorrect. The correct answer is {}".format(question[1]))
