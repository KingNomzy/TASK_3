import random

system_num, user_num = random.randint(1, 9), 0
while system_num != user_num:
    user_num = int(input("Guess a number between 1 to 9 untill u gess it right \n"))
    if (user_num == system_num):
        print("Guessed Right")
        