class Card:
    '''
    Class đại diện cho mỗi lá bài

    Mỗi lá bài bao gồm rank ('A', 2, 3, 4, 5, 6, 7, 8, 9) và suit ('♠', '♣', '♦', '♥')
    '''

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        # '''Hiển thị lá bài'''
        return f"{self.rank}{self.suit}"
       

    def __gt__(self, other):
        # '''So sánh 2 lá bài'''
        if self.suit_point() > other.suit_point(): return True
        elif self.suit_point() == other.suit_point(): 
            if self.score() == 1: return True
            elif self.score() > other.score() and other.score() != 1: return True
        #     else: return False
        # else: return False
        

    def suit_point(self):
        if self.suit == '♦': return 4
        elif self.suit == '♥': return 3
        elif self.suit == '♣': return 2
        elif self.suit == '♠' : return 1

    # def pointbySuit(self):
    #     return self.suit_point() * 10 + self.score()
    
    
    def score(self):
        if self.rank == 'A': return 1
        else: return int(self.rank)
            

# la1 = Card('5','♦')
# la2 = Card("6",'♠')
# la3 = Card("A",'♣')
# card_lst= [la1,la2,la3]
# print(max(card_lst))
# print(la1 > la2)
# print(la1)
# print(la2)
# print(la1.score())
