'''Kết nối CSDL'''
import mysql.connector as mysql
import pymysql
# '''db = pymysql.connect(
#     host = "remotemysql.com",
#     user = "UyMDXcxEoz",
#     passwd = "lFJmWnNbEC",
#     database = "UyMDXcxEoz"
# )'''
db = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Vid!1234",
    database = "cardgame_log"
)
cur = db.cursor(pymysql.cursors.DictCursor)


def log(winner, players):
    '''
    Ghi thông tin về game vào CSDL và 2 bảng games và logs

    Bảng games gồm tên người chiến thắng

    Bảng logs gồm danh sách người chơi, bộ bài, điểm và lá bài lớn nhất tương ứng với game

    Chú ý, sau khi INSERT vào games, có thể lấy id của game vừa tạo với cursor.lastrowid
    '''
    sql = '''
    INSERT INTO games (winner)
    VALUES (%s)
    '''
    cur.execute(sql,winner)
    game_id = cur.lastrowid

    sql = f'''
    INSERT INTO logs (game_id, player, cards, point, biggest_card )
    VALUES ({game_id}, %(player)s, %(cards)s, %(point)s, %(biggest_card)s)
    '''
    cur.executemany(sql,players)
    db.commit()    



def get_last_game():
    '''Lấy thông tin về game gần nhất từ cả 2 bảng games và logs'''
    
    
    sql = '''
    SELECT
            g.game_id, g.winner, logs.player, logs.cards, logs.point, logs.biggest_card, g.created_time
    FROM games AS g
    JOIN logs
    ON g.game_id = logs.game_id 
    WhERE  g.game_id = (SELECT max(g.game_id) from games AS g)
    '''
    cur.execute(sql)
    last_game = cur.fetchall()
    return last_game


def history():
    '''
    Lấy thông tin về lịch sử chơi

    Bao gồm tổng số game đã chơi, số game chiến thắng ứng với mỗi người chơi (sử dụng GROUP BY và các hàm tổng hợp)
    '''
    sql = '''
    SELECT
			g.winner as winner, count(*) as count
    FROM games AS g 
    WHERE  date(g.created_time) = current_date()
    group by winner
    order by count desc
    '''
    cur.execute(sql)
    history_detail = cur.fetchall()
    return history_detail