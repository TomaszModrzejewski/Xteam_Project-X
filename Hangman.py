import random


def hangman():  # sourcery skip: low-code-quality
    word=random.choice(["solar","environment","ocean","superman","batman","forest","mountain","nation","asia","europe","pineapple","custard","science","engish","story","terminal","command","virtual"])
    validletters='abcdefghijklmnopqrstuvwxyz'
    turns=10
    guessmade=''

    missed=0

    while len(word)>0:
        main=''
        for letter in word:
            main = main +letter if letter in guessmade else f"{main}_ "
        if main == word :
            print(main)
            print("You Win!")
            break

        print("Guess the word: ", main)
        guess = input()

        if guess in validletters:
            guessmade=guessmade+guess
        else :
            print("Enter a valid character / Enter in small letter")
            print("")


        if guess not in word:
            turns=turns-1
            if turns == 0:
                print(" You Lost")
                print("You let a kind man die")
                print(" ----------- ")
                print("       O_|   ")
                print("    /  |  \  ")
                print("      / \    ")
                print("")
                print("")
                print("")
                break
            elif turns == 1:
                print(" 1 attempts left")
                print("Last breaths counting , Take care!")
                print(" ----------- ")
                print("    \  O_|/  ")
                print("       |     ")
                print("      / \    ")
                print("")
                print("")
                print("")
            elif turns == 2:
                print(" 2 attempts left")
                print(" ----------- ")
                print("    \  O |/  ")
                print("       |     ")
                print("      / \    ")
                print("")
                print("")
                print("")
            elif turns == 3:
                print(" 3 attempts left")
                print(" ----------- ")
                print("    \  O  /  ")
                print("       |     ")
                print("      / \    ")
                print("")
                print("")
                print("")
            elif turns == 4:
                print(" 4 attempts left")
                print(" ----------- ")
                print("    \  O     ")
                print("       |     ")
                print("      / \    ")
                print("")
                print("")
                print("")
            elif turns == 5:
                print(" 5 attempts left")
                print(" ----------- ")
                print("       O     ")
                print("       |     ")
                print("      / \    ")
                print("")
                print("")
                print("")
            elif turns == 6:
                print(" 6 attempts left")
                print(" ----------- ")
                print("       O     ")
                print("       |     ")
                print("      /      ")
                print("")
                print("")
                print("")
            elif turns == 7:
                print(" 7 attempts left")
                print(" ----------- ")
                print("       O     ")
                print("       |     ")
                print("")
                print("")
                print("")
            elif turns == 8:
                print("8 attempts left")
                print(" ----------- ")
                print("       O     ")
                print("")
                print("")
                print("")
            elif turns == 9:
                print("9 attempts left")
                print(" -----------  ")
                print("")
                print("")
                print("")



name= input("Enter Your Name")
print("Welcome ",name)
print("---------------------")
print("Before finishing 10 attempts guess the word")
hangman()
print("")
