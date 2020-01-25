class Fraction:
    def __init__(self, thefraction=""):
        apart = thefraction.split("/") 
        self.num  = int(apart[0])
        self.den = int(apart[1])
        
        
    
    def gcd(self, m,n):
        while m%n !=0:
            oldm = m 
            oldn = n

            m = oldn
            n = oldm%oldn
        return n

    def _str_(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    def _add_(self, otherfraction):
        p = Fraction(otherfraction)
        common = self.gcd(self.num, self.den)
        print (str(common))
        commonother = self.gcd(p.num, p.den)
        print (str(commonother))
        print ((str(self.num//common)+"/"+str(self.den//common)))
        gcdorig = Fraction((str(self.num//common)+"/"+str(self.den//common)))
        gcdorig.show()
        gcdnew = Fraction(str(p.num//commonother)+"/"+str(p.den//commonother))
        gcdnew.show()
        newnum = gcdorig.num*gcdnew.den + \
                    gcdorig.den*gcdnew.num
        newden = gcdorig.den * gcdnew.den
        

        Fraction(str(newnum)+"/"+str(newden)).show()

    def _eq_(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum


if __name__ == "__main__":
    thefraction = input("Put your fraction here: ")  
    otherguy = input("What is the other fraction?: ")
    Fraction(thefraction)._add_(otherguy)
