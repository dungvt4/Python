
from card import Card
from deck import Deck

class Player:
    '''
    Class đại diện cho mỗi người chơi

    Người chơi chỉ cần lưu tên, và các lá bài người chơi có
    '''

    def __init__(self, name, deck):  # dễ
        self.name = name
        self.deck = deck
        self.card_list = []
        pass

    @property
    def point(self):  # trung bình
        '''Tính điểm cho bộ bài'''
        p = 0 
        for c in self.card_list:
            # print(type(c))
            p += c.score()
        p = p % 10
        if p == 0: return 10
        else: return p

    @property
    def biggest_card(self):
        # '''
        # Tìm lá bài lớn nhất
        # Trong trường hợp điểm bằng nhau, sẽ so sánh lá bài lớn nhất để tìm ra người chiến thắng
        # '''
        mx = self.card_list[0]
        for c in range (1, len(self.card_list)):
            # print(f"{self.card_list[c]} > {mx}:{self.card_list[c] > mx}")
            if (self.card_list[c] > mx):
              mx = self.card_list[c]
        return mx

    def add_card(self):
        # '''Thêm một lá bài vào bộ (rút từ bộ bài)'''
        if len(self.card_list) > 3:
            return
        self.card_list.append(self.deck.deal_card())

    def remove_card(self):
        # '''Reset bộ bài khi chơi game mới'''
        self.card_list.clear()


    def flip_card(self):
        # '''Lật bài, hiển thị các lá bài'''
        return f"{self.card_list[0].__str__()},{self.card_list[1].__str__()},{self.card_list[2].__str__()}"

    # def __str__(self):
    #     return f"{self.card_list[0].__str__()},{self.card_list[1].__str__()},{self.card_list[2].__str__()}"



deck1 = Deck()
deck1.build()
deck1.shuffle_card()
dung = Player("dung", deck1)
for i in range (3):
    dung.add_card()
# print(dung)
# dung.point
# print(dung.biggest_card)
dung.flip_card()

