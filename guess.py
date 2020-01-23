from random import randint

def main():
    y = randint(0,21)
    while True:
        x = int(input("What number do you guess? :"))
        if x == y:
            print ("You win, you guessed the right number")
            break
        elif x > y :
            print ("this is just too high")
        elif x < y :
            print ("this is just too low")

if __name__ == "__main__":
    main()

