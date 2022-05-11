name = input("What is your name: ")
question = input("What question do you wnat to ask the all knowing Magic 8-Ball?")
answer = ""

import random
random_number = random.randint(1, 11)

if random_number == 1:
    answer = "Yes - definitely."
elif random_number == 2:
    answer = "It is decidedly so."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Replay hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful"
elif random_number == 10:
    answer = "Hmm I don't know"
elif random_number == 11:
    answer = "Maybe?"
else:
    answer = "Error"

if name == "":
    print("Question: " + question)
else:
    print(name + " asks: " + question)

if question == "":
    print("Error, please ask a question")
else:
    print("Magic 8-Ball's answer: " + answer)
