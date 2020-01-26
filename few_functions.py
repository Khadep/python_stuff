


def find_missing(x, y):
    #Find missing items when comparing 2 lists
    if len(x) > len(y):
        longer = x
        shorter = y
    elif len(y) > len(x):
        longer = y
        shorter = x

    final = []
    for a in longer:
        if a not in shorter:
            final.append(a)
    print (final)
        
def reverse(w):
    #reverse a string
    g = w.split()
    final_phrase = ""
    while len(g) >= 1:
        final_phrase = final_phrase + " " +str(g.pop())
    print (final_phrase)
   



y = list(input("Enter a list of numbers"))
x = list(input("Enter a second list of numbers"))
find_missing(x,y)
w = input("enter your phrase")
reverse(w)


def coins_back(x):
    #Get the amount of loose coin change from a puchase
    u = str(x).split(".")
    change = float(u[1])/100
    #print (price)
    quarter = 0.25
    nickel = 0.05
    dime = 0.10 
    penny = 0.01
    give_back = []
    #print (change)
    
    if change>quarter :
        y = change%quarter
        numquarters = ((change - y)/quarter)
        give_back.append((str(numquarters)) + " " + "quarters")
        if y>dime:
            z = y%dime
            numdime = (y-z)/dime
            give_back.append((str(numdime)) + " " + "dime")
            if z > nickel:
                a = z%nickel
                numnickel = (z-a)/nickel
                give_back.append((str(numnickel)) + " " + "nickel")
                if a >= penny :
                    b = a%penny
                    numpenny = (a-b)/penny
                    give_back.append((str(numpenny)) + " " + "penny")
            elif z >= penny :
                    b = z%penny
                    numpenny = (z-b)/penny
                    give_back.append((str(numpenny)) + " " + "penny")
        elif y > nickel:
                a = y%nickel
                print (a)
                numnickel = (y-a)/nickel
                give_back.append((str(numnickel)) + " " + "nickel")
                if a != 0 :
                    b = a%penny
                    numpenny = (a-b)/penny
                    give_back.append((str(numpenny)) + " " + "penny")
        elif y >= penny :
                    b = y%penny
                    numpenny = (y-b)/penny
                    give_back.append((str(numpenny)) + " " + "penny")                              
    elif change>dime:
        z = change%dime
        numdime = (y-z)/dime
        give_back.append((str(numdime)) + " " + "dime")
        if z > nickel:
            a = z%nickel
            numnickel = (z-a)/nickel
            give_back.append((str(numnickel)) + " " + "nickel")
            if a >= penny :
                b = a%penny
                numpenny = (a-b)/penny
                give_back.append((str(numpenny)) + " " +  "penny")
        elif z >= penny :
                b = z%penny
                numpenny = (z-b)/penny
                give_back.append((str(numpenny)) + " " +  "penny")
    elif change > nickel:
        a = change%nickel
        numnickel = (z-a)/nickel
        give_back.append((str(numnickel)) + " " +  "nickel")
        if a != 0 :
            b = a%penny
            numpenny = (a-b)/penny
            give_back.append((str(numpenny)) + " " + "penny")
    elif change >= penny :
        b = change%penny
        numpenny = (a-b)/penny
        give_back.append((str(numpenny)) + " " +  "penny")
    print (give_back)



price = input("Put the total price to find the coins you will recieve: ")
coins_back(price)

