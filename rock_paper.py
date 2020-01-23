from random import randint


def main():
    selection = {"1":"rock","2":"paper","3":"scissors"}
    while True:
        try:
            choice = randint(1,3)
            Userchoice = input("Press q to quit /n Lets play Rock paper scissors!  1 for Rock, 2 for paper, 3 for scissors? : ")
            if Userchoice== "q":
                break
            elif selection[str(choice)] == selection[Userchoice]:
                print ("Tied Try again")
            elif selection[str(choice)] == selection["1"] and selection[Userchoice] == selection["2"]:
                print ("You won this round. Paper beats rock. Lets go again")
            elif selection[str(choice)] == selection["2"] and selection[Userchoice] == selection["1"]:
                print ("You lost this round. Paper beats rock. Lets go again")
            elif selection[str(choice)] == selection["2"] and selection[Userchoice] == selection["3"]:
                print ("You won this round. scissors beats paper. Lets go again")
            elif selection[str(choice)] == selection["3"] and selection[Userchoice] == selection["2"]:
                print ("You lost this round. scissors beats paper. Lets go again")
            elif selection[str(choice)] == selection["1"] and selection[Userchoice] == selection["3"]:
                print ("You lost this round. rock beats paper. Lets go again")
            elif selection[str(choice)] == selection["3"] and selection[Userchoice] == selection["1"]:
                print ("You won this round. rock beats paper. Lets go again")
        except KeyError:
            print ("You messed up , Pick one of the options")


if __name__ == "__main__":
    main()        