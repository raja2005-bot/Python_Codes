import random as rd
# name = ['raja', 'ganesh', 'raji', 'sekaran']
# length = len(name)
# print(rd.choice(name))
# print(rd.randint(0,length))
# location = ['chennai', 'pondy', 'Cudallore']
# total = name , location
# print(name, location)
# print(total[1][1])

# rock paper Scissors game
print("Read to play, rock paper and Scissor game, for rock 0, paper 1, Scissor 2")
user_input = int(input())
print("Your Choice : ")
print("rock" if user_input == 0 else "Paper" if user_input == 1 else "Scissor")
print("Computers Choice : ")
computer_input = rd.randint(0,2)
print("rock" if computer_input == 0 else "Paper" if computer_input == 1 else "Scissor")

if user_input >=3 or user_input < 0:
    print("Enter a valid Number")
elif user_input == 0 and computer_input == 2:
    print("You win")
elif computer_input == 0 and user_input == 2:
    print("You lose")
elif computer_input > user_input:
    print("you lose")
elif computer_input < user_input:
    print("You win")
elif computer_input == user_input:
    print("Its a draw")

