from player import Player

class Game:
    '''
    Class chứa các chức năng chính của game

    Game chứa danh sách người chơi, và bộ bài
    '''

    def __init__(self):
        pass

    def setup(self):
        '''Khởi tạo trò chơi, nhập số lượng và lưu thông tin người chơi'''
        print("Wellcome!!!, Mời bạn nhập số người chơi:")
        inc = input()
        self.players = []
        for c in range (0,inc):
            name = input('tên Người chơi',c,' là: ')
            p = Player(name)
            self.players.append(p)

    def guide(self):
        '''Hiển thị menu chức năng/hướng dẫn chơi'''
        print('Hướng dẫn chơi')
        print('1. Danh sách người chơi')
        print('2. Thêm người chơi')
        print('3. Loại người chơi')
        print('4. Chia bài')
        print('5. Lât bài')
        print('6. Xem lại game vừa chơi')
        print('7. Xem lịch sử chơi hôm nay')

    def list_players(self):
        '''Hiển thị danh sách người chơi'''
        for c in self.players:
            print(self.players[c])
        pass

    def add_player(self):
        '''Thêm một người chơi mới'''
        pass

    def remove_player(self):
        '''
        Loại một người chơi
        Mỗi người chơi có một ID (có thể lấy theo index trong list)
        '''
        pass

    def deal_card(self):
        '''Chia bài cho người chơi'''
        pass

    def flip_card(self):
        '''Lật bài tất cả người chơi, thông báo người chiến thắng'''
        pass
    