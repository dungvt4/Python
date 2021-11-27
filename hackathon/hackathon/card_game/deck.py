import sys
# sys.path.append(".")
from random import shuffle
from card import Card

class Deck:
    '''
    Class đại diện cho bộ bài, bao gồm 36 lá
    '''

    def __init__(self):
        self.cards = []

    def build(self):
        '''Tạo bộ bài'''
        self.cards = []
        for rank in ('A', 2, 3, 4, 5, 6, 7, 8, 9):
            for suit in ('♠', '♣', '♦', '♥'):
                self.cards.append(Card(rank, suit))
        


    def shuffle_card(self):
        '''Trộn bài'''
        shuffle(self.cards)


    def deal_card(self):
        '''Rút một lá bài từ bộ bài'''
        if len(self.cards) == 0:
            return 
        return self.cards.pop()


    def display(self):
        for a in self.cards:
            print(str(a))
        
        

# v = Deck()
# v.build()
# # v.shuffle_card()
# v.display()
# print("==========")
# a = v.deal_card()
# print(a.__str__())