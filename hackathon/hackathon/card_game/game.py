from player import Player
from deck import Deck
from card import Card

class Game:
    '''
    Class chứa các chức năng chính của game

    Game chứa danh sách người chơi, và bộ bài
    '''

    def __init__(self):
        pass

    def setup(self):
        '''Khởi tạo trò chơi, nhập số lượng và lưu thông tin người chơi'''
        inc = int(input("Wellcome!!!, Mời bạn nhập số người chơi:"))
        id = 0
        self.players = []
        for c in range (0,inc):
            id += 1
            name = str(input(f'Tên Người chơi {id} : '))
            self.players.append(Player(id,name))

    def guide(self):
        # '''Hiển thị menu chức năng/hướng dẫn chơi'''
        print('Hướng dẫn chơi')
        print('1. Danh sách người chơi')
        print('2. Thêm người chơi')
        print('3. Loại người chơi')
        print('4. Chia bài')
        print('5. Lât bài')
        print('6. Xem lại game vừa chơi')
        print('7. Xem lịch sử chơi hôm nay')

    def list_players(self):
        # '''Hiển thị danh sách người chơi'''
        print("ID     Tên")
        for player in self.players: 
            temp = vars(player)
            print(f"{temp['id']:2}     {temp['name']:15}")

    def add_player(self):
        # '''Thêm một người chơi mới'''
        id = len(self.players) + 1
        name = str(input(f'Tên Người chơi {id} : '))
        self.players.append(Player(id,name))        

    def remove_player(self):
        # '''
        # Loại một người chơi
        # Mỗi người chơi có một ID (có thể lấy theo index trong list)
        # '''
        id = int(input(f'Mời bạn nhập ID người muốn loại : '))
        for player in self.players: 
            temp = vars(player)
            if temp['id'] == id: 
                self.players.remove(player)

    def deal_card(self):
        '''Chia bài cho người chơi'''
        deck_game = Deck()
        deck_game.build()
        deck_game.shuffle_card()   
        c = 0
        for c in range(3):
            for player in self.players:
                card = deck_game.deal_card()
                player.add_card(card)
        

    def flip_card(self):
        '''Lật bài tất cả người chơi, thông báo người chiến thắng'''
        mx_point = 0
        winner = self.players[0]
        for player in self.players:
            temp = vars(player)
            print (f"{temp['name']:15}{player.flip_card():5}  Điểm:{player.point:2}  Lá lớn nhất là:{player.biggest_card}")
            if mx_point < player.point: 
                mx_point = player.point
                winner = player
            elif mx_point ==  player.point:
                if player.biggest_card == max (player.biggest_card, winner.biggest_card):
                    winner = player
        temp = vars(winner)
        print(f"Người thắng cuộc là: {temp['name']}")
                
    

game1 = Game()
game1.setup()
# game1.guide()
game1.list_players()
# game1.add_player()
# game1.list_players()
# game1.remove_player()
# game1.list_players()
game1.deal_card()
game1.flip_card()
# input_menu = input()
# if input_menu == 1: game1.list_players()