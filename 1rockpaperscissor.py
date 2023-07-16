def greet_user():
    print("Hello User, Hope you are having a nice day!\nAre you ready to play the game the game of rock paer scissor.")
    print(''' Instructions for game!
    1. You have to type the gesture you want from rock,paper,scissor.
    2. Rock will defeat scissor.
    3. Scissor will defear paper.
    4. Paper will defeat rock.
    ''')

def computer_choice():
    import random 
    gesture = ["rock", 'paper', 'scissor']
    return random.choice(gesture)

def get_choice():
    player_choice = input("Enter from {rock,paper,scissor}")
    computerchoice = computer_choice()
    choices = {"player": player_choice, 'computer': computerchoice}
    return choices

def winner(player_choice,computerchoice):
    if player_choice == computerchoice:
        return "Tie"
    else:
        if player_choice == "rock":
            if computer_choice== "paper":
                return("You lose")
            else:
                return " You win"
        if player_choice == "paper":
            if computer_choice== "rock":
                return("You win")
            else:
                return " You lose"
        if player_choice == "scissor":
            if computer_choice== "paper":
                return("You win")
            else:
                return " You lose"

greet_user()
choices = get_choice()
print(choices)
result = winner(choices["player"],choices['computer'])
print(result)


