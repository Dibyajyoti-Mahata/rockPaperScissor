import random    
user_choice = input("rock paper or scissor ? = ")
items = ["rock","paper","scissor"]
comp_choice = random.choice(items)
if user_choice == comp_choice:
    print("It's a tie")
elif user_choice == "rock":
    if comp_choice =="paper":
        print(f"computer won, computer chose {comp_choice} and you chose {user_choice}")
    else:
        print(f"you won, computer chose {comp_choice}")
elif user_choice == "paper":
    if comp_choice =="rock":
        print(f"you won, computer chose {comp_choice} and you chose {user_choice}")
    else:
        print(f"computer win, computer chose {comp_choice}")
elif user_choice == "scissor":
    if comp_choice =="rock":
        print(f"Computer won, computer chose {comp_choice} and you chose {user_choice}")
    else:
        print(f"you win, computer chose {comp_choice}")
else:
    print("I dont know")
