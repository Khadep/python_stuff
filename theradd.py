from fraction_class import Fraction

class Theradd:
    def __init__(self, val):
        self.val = val


    def __add__(self, other):
        Fraction(self.val, other)._add_()

    def __radd__(self, other):
        import pdb; pdb.set_trace()
        if type(other) == int or type(other) == float:
            Fraction((self.convert(other)),self.val)._add_()
        else:
            Fraction(other,self.val)._add_()
        

    def convert(self, other):
        newother = str(str(other)+"/"+str(1))
        return newother



if __name__ == "__main__":
    x = Theradd("1/4")
    y = x + "2/4"
    w = 2 + x
