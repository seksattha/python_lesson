import sqlite3

def create_table_demo():
    try:
        with sqlite3.connect("sample.db") as con:
            sql_cmd = """
            create table medal(
                country text primary key, 
                gold integer, 
                silver integer, 
                bronze integer);
            
            """
            con.execute(sql_cmd)
    except Exception as e:
        print(f'error => {e}')

def insert_demo():
    try:
        with sqlite3.connect("sample.db") as con:
            sql_cmd = """
            insert into medal values('chn', 26, 18, 26)
            """
            con.execute(sql_cmd)
    except Exception as e:
        print(f'error => {e}')

def insert_demo2():
    try:
        with sqlite3.connect("sample.db") as con:
            sql_cmd = """
            insert into medal values('gbr', 27, 23, 17);
            insert into medal values('rus', 19, 17, 19);
            insert into medal values('ger', 17, 10, 15);
            """
            con.executescript(sql_cmd)
    except Exception as e:
        print(f'error => {e}')

def insert_demo3():
    try:
        with sqlite3.connect("sample.db") as con:
            sql_cmd = """
            begin;
            insert into medal values('gbr', 27, 23, 17);
            insert into medal values('rus', 19, 17, 19);
            insert into medal values('ger', 17, 10, 15);
            commit;
            """
            con.executescript(sql_cmd)
    except Exception as e:
        print(f'error => {e}')

def select_demo():
    try:
        with sqlite3.connect("sample.db") as con:
            sql_cmd = """
            select * from medal;
            """
            for row in con.execute(sql_cmd):
                print(row)
    except Exception as e:
        print(f'error => {e}')
if __name__ == '__main__':
    # create_table_demo()
    # insert_demo()
    insert_demo2()
    select_demo()

