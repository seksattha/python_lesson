# CRUD ( Create Read Update Delete)
import sqlite3

def create_db():
    with sqlite3.connect("crud_tutorial.db") as con:
        sql_cmd = """
            create table person(
                id integer primary key AUTOINCREMENT, 
                gender text, 
                weight real,
                height real);
        """
        con.execute(sql_cmd)

def insert_demo():
    with sqlite3.connect("crud_tutorial.db") as con:
        sql_cmd = """
            insert into person(gender, weight, height) 
            values('F', 46, 160)
        """
        con.execute(sql_cmd)
def select_demo():
    with sqlite3.connect("crud_tutorial.db") as con:
        sql_cmd = """
            select * from person;
        """
        cur= con.execute(sql_cmd)
        for row in cur:
            print(row)
if __name__ == '__main__':
    # create_db()
    insert_demo()
    select_demo()