import random
from characters import characters, p1Inputs, p2Inputs
from stagelists import starter_legal_stages, counter_stage_picks

mode = 0


def cpumode():
    p1wins = 0
    cpuwins = 0
    userinput = input(
        "What is your tag? : "
    )  # Asks for the name to refer to the user as
    print(
        "{} :".format(userinput), random.choice(characters)
    )  # Displays the random choice of character for the user
    print(
        "CPU :", random.choice(characters)
    )  # Displays the random choice of character for the computer player
    print(
        "Game 1 : {}".format(random.choice(starter_legal_stages))
    )  # Displays the random choice of stage for game one
    print(
        "Game 2 : {}".format(random.choice(counter_stage_picks + starter_legal_stages))
    )  # Displays the random choice of stage for game two
    print(
        "Game 3 : {}".format(random.choice(counter_stage_picks + starter_legal_stages))
    )  # Displays the random choice of stage for game three
    userinput = input("Who won? : ")  # Asks for the winner of the set
    # if statement to raise the win variable for each player
    if userinput == "CPU":
        cpuwins += 1
    elif userinput == "human":
        p1wins += 1
    else:
        print("Please provide an acceptable input")
    print("Human has won {} times!".format(p1wins))  # Display each player's wins
    print("CPU has won {} times!".format(cpuwins))  # Display each player's wins


def pvpmode():
    p1wins = 0
    p2wins = 0
    userinput1 = input("P1 tag: ")  # Asks for the tag of player 1
    userinput2 = input("P2 tag: ")  # Asks for the tag of player 2
    print(
        userinput1, "{} : {}".format(userinput1, random.choice(characters))
    )  # Displays random choice of character for player 1
    print(
        userinput2, "{} : {}".format(userinput2, random.choice(characters))
    )  # Displays random choice of character for player 1
    print("Game 1 : {}".format(random.choice(starter_legal_stages)))
    print(
        "Game 2 : {}".format(random.choice(starter_legal_stages + counter_stage_picks))
    )
    print(
        "Game 3 : {}".format(random.choice(starter_legal_stages + counter_stage_picks))
    )
    userinput = input("Who won? : ")
    if userinput == "Player 1":
        p1wins += 1
    elif userinput == "Player 2":
        p2wins += 1
    else:
        print("Please provide an acceptable input")
    print("P1 has won {} times!".format(p1wins))
    print("P2 has won {} times!".format(p2wins))


while mode == 0:
    modeinput = input(
        "Are you playing against a CPU or a human? Or would you like to see records? : "
    )
    if modeinput == "CPU":
        mode = 1
    elif modeinput == "human":
        mode = 2
    elif modeinput == "records":
        mode = 3
    else:
        print("Please provide an acceptable answer")

while mode == 1:
    cpumode()

while mode == 2:
    pvpmode()
