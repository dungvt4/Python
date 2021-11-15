'''Kết nối CSDL'''
# import mysql.connector as mysql
# import pymysql
# '''db = pymysql.connect(
#     host = "remotemysql.com",
#     user = "UyMDXcxEoz",
#     passwd = "lFJmWnNbEC",
#     database = "UyMDXcxEoz"
# )'''
import mysql.connector as mysql
import pymysql
'''db = pymysql.connect(
    host = "remotemysql.com",
    user = "UyMDXcxEoz",
    passwd = "lFJmWnNbEC",
    database = "UyMDXcxEoz"
)'''
db = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Vid!1234",
    database = "blog_log"
)
cur = db.cursor(pymysql.cursors.DictCursor)

def log(post):
    sql = f'''
    INSERT INTO posts (title, content)
    VALUES (%s, %s)
    '''
    cur.execute(sql,post)
    db.commit()
    blog_id = cur.lastrowid
    return blog_id

    
    
def history():
    sql = '''
    SELECT
            *
    FROM posts AS p
    ORDER BY p.id DESC
    '''
    cur.execute(sql)
    posts = cur.fetchall()

    # if not posts:
    #     raise Exception('Không có bài post nào\n Mời bạn post vài bài 😉\n')   
    return posts

def get_detail(id):
    sql = '''    
    SELECT
            *
    FROM posts AS p
    WHERE p.id = %s'''

    cur.execute(sql,id)
    post = cur.fetchone()   
    return post

def update(post):
    sql = f'''
    UPDATE posts p
    SET p.title = %s, p.content = %s
    WHERE p.id = %s'''
    
    cur.execute(sql,post)
    db.commit()
    return post   

