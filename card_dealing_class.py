import random

class Card:
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
  
        


    def __repr__(self):
        print (f'{self.value} of {self.suit}')



class Deck():
    def __init__(self):
        self.cards = []
        self.hand = []
        suitoptions = ["Hearts","Diamonds","Clubs", "Spades"]
        valueoptions = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        for x in suitoptions:
            for y in valueoptions:
                self.cards.append(f'{y} of {x}')
        

        
    def __repr__(self):
        print (f'Deck of {len(self.cards)} cards')

    def _deal(self, numcards):
        self.numcards = numcards
        
           
        if (len(self.cards) - self.numcards) < 0:
            return ValueError(f'You are asking for too many cards there are {len(self.cards)} left')
        elif self.numcards == 1:
            print (self.cards.pop())
        elif self.numcards > 1:
            
            while self.numcards >0:
                self.hand.append(self.cards.pop())
                self.numcards -=1
            print (self.hand)
        if self.cards == 0:
            return ValueError("All cards have been dealt")

    def count(self):
        print (len(self.cards))

    def shuffle(self):
        if len(self.cards) == 52:
            random.shuffle(self.cards)
        else:
            print ("cant")
            return ValueError ("Only full decks can be shuffled")
        
    def deal_card(self):
        self._deal(1)
        
        

    def deal_hand(self, num):
        self.num = num
        self._deal(num)

d = Deck()
d.shuffle()
d._deal(5)
d.deal_card()
d.deal_hand(10)
d.count()
d.shuffle()
