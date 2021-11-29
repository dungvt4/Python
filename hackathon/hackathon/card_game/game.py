from player import Player
from deck import Deck
from card import Card
import db
import error

class Game:
    '''
    Class chứa các chức năng chính của game

    Game chứa danh sách người chơi, và bộ bài
    '''
    
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.is_dealt = False
        self.is_flipped = False
        self.is_playing = False
        self.min_player = 2
        self.max_player = 12

    def setup(self):
        '''Khởi tạo trò chơi, nhập số lượng và lưu thông tin người chơi'''
        # print("Wellcome!!!, Mời bạn nhập số người chơi:")
        num_of_player = 0
 
        try:
            num_of_player = int(input('Wellcome!!!, Mời bạn nhập số người chơi: '))
        except Exception as e:
            raise error.NotIntegerError
        
        if num_of_player < 0: raise error.NotIntegerError
        if (num_of_player >=0 and num_of_player < 2) : raise error.MinimumPlayersError
        elif num_of_player > 12: raise error.MaximumPlayersError
        else:            
            id = 0
            for c in range (0,num_of_player):
                id += 1
                name = str(input(f'Tên Người chơi {id} : '))
                self.players.append(Player(id,name))

    def guide(self):
        # '''Hiển thị menu chức năng/hướng dẫn chơi'''
        print('\n')
        print('Hướng dẫn chơi')
        print('1. Danh sách người chơi')
        print('2. Thêm người chơi')
        print('3. Loại người chơi')
        print('4. Chia bài')
        print('5. Lât bài')
        print('6. Xem lại game vừa chơi')
        print('7. Xem lịch sử chơi hôm nay')
        print('8. Thoát game')

    def list_players(self):
        # '''Hiển thị danh sách người chơi'''
        print("ID     Tên")
        for player in self.players: 
            # temp = vars(player)
            print(f"{player.id:2}     {player.name:15}")

    def add_player(self):
        # '''Thêm một người chơi mới'''
        if (len(self.players) >= self.max_player): raise error.MaximumPlayersError
        elif (self.is_playing): raise error.isPlayingError
        else:  
            last_player = self.players[-1]      # lấy ra player cuối list là player có id lớn nhất (cho case xóa ng chơi rồi thêm ng chơi sẽ ko bị trùng id)
            id = last_player.id + 1
            name = str(input(f'Tên Người chơi {id} : '))
            self.players.append(Player(id,name))        

    def remove_player(self):
        # '''
        # Loại một người chơi
        # Mỗi người chơi có một ID (có thể lấy theo index trong list)
        # '''
        id = 0
        if (len(self.players) <= self.min_player): raise error.MinimumPlayersError
        elif (self.is_playing): raise error.isPlayingError
        else: 
            try:
                id = int(input(f'Mời bạn nhập ID người muốn loại : '))
            except Exception as e:
                raise error.NotIntegerError
            
            id_found = False 
            for player in self.players: 
                # temp = vars()
                # if temp['id'] == id: 
                if player.id == id:
                    id_found = True
                    self.players.remove(player)
                    print("Một player đã out khỏi cuộc chơi !!!!!!!")
            
            if (id_found == False): raise error.NotFoundPlayerError

    def deal_card(self):
        '''Chia bài cho người chơi'''
        if (self.is_dealt): raise error.isDealtError
        elif (self.is_flipped): raise error.isFlipedError
        else:          
            self.deck.build()
            self.deck.shuffle_card()   
            c = 0
            for c in range(3):
                for player in self.players:
                    card = self.deck.deal_card()
                    player.add_card(card)
            self.is_playing = True
            self.is_dealt = True
            
            print("Chia bài thành công, cùng lật bài xem ai là người thắng cuộc nào.")

    def flip_cards(self):
        '''Lật bài tất cả người chơi, thông báo người chiến thắng'''
        if (self.is_flipped): raise error.isFlipedError
        elif (self.is_dealt == False ): raise error.isNotDealtError
        else:
            mx_point = 0
            winner = self.players[0]
            players = []
            for player in self.players:
                print (f"{player.name:15}{player.flip_card():5}  Điểm:{player.point:2}  Lá bài lớn nhất là:{player.biggest_card}")
                players.append({'player': player.name, 'cards': player.flip_card(), 'point': player.point, 'biggest_card': player.biggest_card}) # gán vào list players để lưu DB
            
                if mx_point < player.point: 
                    mx_point = player.point
                    winner = player
                elif mx_point ==  player.point:
                    if player.biggest_card == max (player.biggest_card, winner.biggest_card):
                        winner = player
            print(f"Người thắng cuộc là: {winner.name}")
    
        self.is_flipped = True
        self.is_playing = True
        db.log(winner.name,players)
    
                
    

# game1 = Game()
# game1.setup()
# # game1.guide()
# game1.list_players()
# # game1.add_player()
# # game1.list_players()
# # game1.remove_player()
# # game1.list_players()
# game1.deal_card()
# game1.flip_card()
# # input_menu = input()
# # if input_menu == 1: game1.list_players()