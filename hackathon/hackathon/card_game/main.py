from game import Game
import error
import db

def main():  # khó
    '''Khởi tạo trò chơi, hiển thị menu và thực thi các chức năng tương ứng'''
    game = Game()
    while True:   ## while để setup khi nào ok mới đi tiếp các function ở dưới, nếu không có while thì kể cả khi bắn exception cũng sẽ đi tiếp
        try:
            game.setup()
            break          ## break để khi ko có exception --> dừng while và đi tiếp block code sau đó (nếu return sẽ quit cả main)
        except error.Error as e:
            print(e.message)  ##ko break để cho nhập lại số ng chơi đến khi nào đúng thì thôi

    game.guide()
    option = valiate_option()
        
    while (option !=8):
        if (option == 1):
            game.list_players()
                
            
        if (option == 2):
            while True:
                try:
                    game.add_player()
                    break
                except error.MaximumPlayersError as e: 
                    print(e.message)
                    break
                except error.Error as e:
                    print(e.message)
                    break
            
        if (option == 3):
            while True:
                try:
                    game.remove_player()
                    break
                except error.Error as e:
                    print(e.message)
                    break
                
                    
        if (option == 4):
            while True:
                try:
                    game.deal_card()
                    break
                except error.Error as e:
                    print(e.message)
                    break           
                   

            
        if (option == 5):
            while True:
                try:
                    game.flip_cards()
                    break
                except error.Error as e:
                    print(e.message)
                    break 
            
        
        if (option == 6):
            last_game = db.get_last_game()
            
            print(last_game[0]['created_time'])
            for p in last_game:
                print(f"{p['player']:15}{p['cards']:5}  Điểm:{p['point']:3}  Lá bài lớn nhất là:{p['biggest_card']:5}")
            print(f"Người thắng cuộc là: {last_game[0]['winner']}")
            
        
        if (option == 7):
            history_detail = db.history()
            sum = 0
            for row in history_detail:
                sum += row['count']
            print(f"Số ván chơi ngày hôm nay: {sum: 5}")
            for row in history_detail:
                print(f"{row['winner']:15}         thắng {row['count']: 3} ván")
                
                              
        if (option == 8):
            break
        
        game.guide()
        option = valiate_option()

def valiate_option():
    while True: 
        try:
            option = int(input())
            if option in range(1,9): break
            else: 
                print(f'Bạn phải nhập chức năng trong khoảng 1-8. Mời bạn nhập lại: ')  
        except Exception as e:
            print(f'Bạn phải nhập số nguyên dương. Mời bạn nhập lại: ')
    return option
                 
if __name__ == '__main__':
    main()
