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
        if self.score() > other.score():
            return True
        elif self.rank == other.rank:  
            if self.suit == '♦':
                return True
            elif other.suit == '♠':
                return True
            elif self.suit == '♥' and other.suit == '♣':
                return True
            else: return False
        else: return False

    def suit_point(self):
        if self.suit == '♦': return 4
        elif self.suit == '♥': return 3
        elif self.suit == '♣': return 2
        else : return 1

    def compare_suit(self, other):
        # '''So sánh 2 lá bài theo chất'''
        if self.suit_point() > other.suit_point(): return 1
        elif self.suit_point() == other.suit_point(): 
            if self.score() > other.score(): return 1
            else: return 0
        else: return 0
    
    
    def score(self):
        if self.rank == 'A': return 10
        else: return int(self.rank)
            

la1 = Card('A','♠')
la2 = Card("A",'♦')

print(la1 > la2)
print(la1)
print(la2)
print(la1.score())
