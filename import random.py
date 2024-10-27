#This 
import random
ascd = (random.randint(1,5))
acsd = int(input("Which number between 1 - 5 am I guessing"))
if (ascd == acsd):
    for i in range (10):
        print("You win!")
else:
    for i in range (10):
        print("You lose!")
