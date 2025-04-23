import random

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return None

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return None

def rpsls(player_choice):    
    output = "------------\n"
    output += f"Player chooses {player_choice}\n"
    
    player_number = name_to_number(player_choice)
    if player_number is None:
        return "Error: Invalid input"

    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)

    output += f"Computer chooses {comp_choice}\n"

    diff = (comp_number - player_number) % 5

    if diff == 1 or diff == 2:
        output += "Computer wins!\n"
    elif diff == 3 or diff == 4:
        output += "Player wins!\n"
    else:
        output += "Player and computer tie!\n"
    
    return output

def get_input():
    from js import document
    choice = document.getElementById("user-input").value
    result = rpsls(choice.strip())
    document.getElementById("output").innerText = result