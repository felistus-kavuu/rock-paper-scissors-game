import random


def play():
    print("Hello user! Want to play a fun game of rock, pape , scissors?")
    text = input("1. Yes 2. No")
    if (text == "yes"):
        print("Great\n Rock, paper or scissors?")
    else:
        print("No problem. We'll be here when you're ready")
        exit()

    print("Enter only the number assigned to the option and not the option itself")
    answer = input("1. Rock 2. Paper 3. Scissors")
    print("Now it's time for Fellz to choose:")
    fellz_option = random.choice(["Rock", "Paper", "Scissors"])
    print("Fellz chooses", fellz_option)

    if (answer == 1 and fellz_option == "Rock"):
        print("It's a tie!!")
        try_again()
    elif (answer == 2 and fellz_option == "Paper"):
        print("It's a tie!!")
        try_again()
    elif (answer == 3 and fellz_option == "Scissors"):
        print("It's a tie!!")
        try_again()
    elif(answer == 1 and fellz_option == "Paper"):
        print("Fellz wins")
        try_again = input("1. yes 2. exit")
        if (try_again == 1):
            play()
        else:
            exit()
    elif(answer == 1 and fellz_option == "Scissors"):
        print("You win!!!!")
        try_again = input("Wanna try again?\n1. yes 2. exit")
        if (try_again == 1):
            play()
        else:
            exit()
    elif(answer == 2 and fellz_option == "Rock"):
        print("You win!!!!")
        try_again = input("Wanna try again?\n1. yes 2. exit")
        if (try_again == 1):
            play()
        else:
            exit()
    elif(answer == 2 and fellz_option == "Scissors"):
        print("Fellz  wins!!!!")
        try_again = input("Wanna try again?\n1. yes 2. exit")
        if (try_again == 1):
            play()
        else:
            exit()
    elif(answer == 3 and fellz_option == "Rock"):
        print("Fellz wins!!!!")
        try_again = input("Wanna try again?\n1. yes 2. exit")
        if (try_again == 1):
            play()
        else:
            exit()
    elif(answer == 3 and fellz_option == "Paper"):
        print("You win!!!!")
        try_again = input("Wanna try again?\n1. yes 2. exit")
        if (try_again == 1):
            play()
        else:
            exit()


def exit():
    print("It's sad to see you leave but we're happy you came.")
    quit()


play()
