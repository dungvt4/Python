#from card import Card
from deck import Deck

class Player:
    '''
    Class đại diện cho mỗi người chơi

    Người chơi chỉ cần lưu tên, và các lá bài người chơi có
    '''

    def __init__(self, id,  name):  # dễ
        self.id = id
        self.name = name
        self.card_list = []
        pass

    @property
    def point(self):  # trung bình
        '''Tính điểm cho bộ bài'''
        p = 0 
        for c in self.card_list:
            p += c.score()
        p %= 10
        if p == 0: return 10
        else: return p

    @property
    def biggest_card(self):
        # '''
        # Tìm lá bài lớn nhất
        # Trong trường hợp điểm bằng nhau, sẽ so sánh lá bài lớn nhất để tìm ra người chiến thắng
        # '''
        return max(self.card_list)

    def add_card(self, card):
        # '''Thêm một lá bài vào bộ (rút từ bộ bài)'''
        if len(self.card_list) > 3:
            return
        self.card_list.append(card)

    def remove_card(self):
        # '''Reset bộ bài khi chơi game mới'''
        self.card_list.clear()


    def flip_card(self):
        # '''Lật bài, hiển thị các lá bài'''
        return ' '.join([str(c) for c in self.card_list])




# deck1 = Deck()
# deck1.build()
# deck1.shuffle_card()
# # deck1.display()
# dung = Player(1, "dung")
# print('===============')
# for i in range (3):
#     card = deck1.deal_card()
#     dung.add_card(card)
# # print(dung)
# # dung.point
# print(dung.biggest_card)
# print(dung.flip_card())

