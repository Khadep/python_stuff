class Fraction:
    def __init__(self, thefraction="", otherfraction=""):
        """Take fractions and reduce to the lowest terms using the greatest common denominator"""
        #THefraction is the first number, otherfraction is an additional number.
        apart = thefraction.split("/") 
        self.num  = int(apart[0])
        self.den = int(apart[1])
        common = self.gcd(self.num, self.den)
        if otherfraction:
            otherfrac = otherfraction.split("/") 
            self.othernum = int(otherfrac[0])
            self.otherden = int(otherfrac[1])
            commonother = self.gcd(self.othernum , self.otherden)
            self.gcdorignum = (self.num//common) 
            self.gcdorigden = (self.den//common)
            self.gcdnewnum = (self.othernum//commonother)
            self.gcdnewden = (self.otherden//commonother)
            self._add_()
        
        
    
    def gcd(self, m,n):
        """Greatest COmmon Denominator function"""
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

    def _add_(self):
        #Function to add the fractions from the main function.
        newnum = self.gcdorignum*self.gcdnewden + \
                    self.gcdorigden*self.gcdnewnum
        newden = self.gcdorigden * self.gcdnewden
        
        

        Fraction(str(newnum)+"/"+str(newden)).show()

    def _eq_(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum


if __name__ == "__main__":
    try:
        thefraction = input("Put your fraction here: ")  
        otherguy = input("What is the other fraction?: ")
        Fraction(thefraction, otherguy)
    except (ValueError, IndexError):
        print ("Please Enter proper fractions. Exe: 1/3")
