import sqlite3, json
from sqlite3 import Error

def create_connection(database):
    try:
        conn = sqlite3.connect(database, check_same_thread=False)
    except:
        print(e)

    return conn

def create_table(conn):
    sql = '''CREATE TABLE IF NOT EXISTS POLL (
                QUESTION_ID INT PRIMARY KEY NOT NULL,
                OPTION_1               INT NOT NULL,
                OPTION_2               INT NOT NULL,
                OPTION_3               INT NOT NULL,
                OPTION_4               INT NOT NULL
            );
        '''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def initialise_record(conn):
    sql_insert = '''INSERT INTO POLL VALUES (1, 0, 0, 0, 0)'''
    sql_select_all = '''SELECT * FROM POLL'''

    cur = conn.cursor()
    cur.execute(sql_select_all)
    rows = cur.fetchall()
    if(not rows):
        cur.execute(sql_insert)

    conn.commit()

def update_record(conn, option):
    sql = '''UPDATE POLL SET ? = ? + 1'''
    sql = sql.replace('?', option)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def select_all_records(conn):
    sql = '''SELECT * FROM POLL'''
    cur = conn.cursor()
    return cur.execute(sql).fetchall()

def database_startup():
    database = './poll.db'
    conn = create_connection(database)
    create_table(conn)
    initialise_record(conn)
