# This console program will grade a student from 0 to 100%.
#  > Enter the correct exam answers in a string
#  > Enter the student's answers in a string
#  > You'll get the student's score in percentage and... in a string!

# imports
from sys import exit

# enter the correct exam answers without spaces
# example: "abcddcda"
CORRECT_ANSWERS = str(input("Correct answers without spaces: "))

if len(CORRECT_ANSWERS) <= 0:
    exit("Blank input. Exiting...")

# enter student's answers
valid = False
while not valid:
    studentAnswers = str(input("Student's answers: "))

    if len(studentAnswers) == len(CORRECT_ANSWERS):
        valid = True

    elif len(studentAnswers) > len(CORRECT_ANSWERS):
        exit("Student answers exceed the number of correct answers!")

    else:
        print("Student answers less than number of correct answers!")
        intentional = str(input("Is that intentional?(Y/N): "))
        if intentional == "Y" or intentional == "y":
            valid = True

            while len(studentAnswers) < len(CORRECT_ANSWERS):
                studentAnswers += " "

# check answers
numAnswers = len(CORRECT_ANSWERS)
numCorrectAnswers = 0
results = ""

for i in range(numAnswers):
    if studentAnswers[i] == CORRECT_ANSWERS[i]:
        numCorrectAnswers += 1
        results += studentAnswers[i]

    else:
        results += "X"

# grade the student
percentage = float(100 / numAnswers)
scorePercentage = round(numCorrectAnswers * percentage)


# print output
print("-" * 5, end = "")
print("Results", end = "")
print("-" * 5)

if scorePercentage == 100:
    print("Excellent! Every answer is correct")

else:
    print("Missed %d questions: %s" % (numAnswers - numCorrectAnswers, results))

print("Student's score is", scorePercentage, "percent")
