from random import sample
from csv import reader
from time import sleep
import matplotlib.pyplot as plt
import datetime


# Check to see if the user provides a valid question count
def get_questions():
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
    f = open("country-capitals.csv", "r")
    terms = list(reader(f))
    f.close()
    return sample(terms, question_count)


# Quiz Loop

def start_quiz(questions):
    num_correct = 0
    question_count = len(questions)
    for question in questions:
        answer = input("What is the capital of {}?  ".format(question[0]))
        if answer.lower() == question[1].lower():
            print("Correct")
            num_correct += 1
        else:
            print("Incorrect. The correct answer is {}".format(question[1]))
        sleep(2)
    print("You got {} out of {} ({}%) correct.".format(num_correct, question_count,
                                                       str(num_correct / question_count * 100)[:5]))

# Capture the progress made in each quiz

    progress = open("progress.csv", "a")
    progress.write("{}, {}, {}, {}\n".format(num_correct, question_count, num_correct / question_count * 100,
                                             datetime.datetime.now()))
    progress.close()


# Plot progress data

def plot_data(data):
    plt.plot(data)
    plt.show()  # TODO: need to fix y-axis scale


# Main Loop for the MENU options

if __name__ == "__main__":
    while True:
        choice = input("---- Menu ----\n"
                       "1. Take a test \n2. View Progress \n3. Quit \n>> ")
        if choice == "1":
            questions = get_questions()
            start_quiz(questions)

        elif choice == "2":
            progress = open("progress.csv", "r")
            trials = list(reader(progress))
            progress.close()
            plot_data([trial[2] for trial in trials])    # trial = [num_correct, question_count, percentage]

        elif choice == "3":
            break
