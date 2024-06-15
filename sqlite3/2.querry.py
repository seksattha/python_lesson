import sqlite3
def demo_selct():
    with sqlite3.connect("tutorial.db") as con:
        sql_cmd = """
        select * from person;
        
        """
        for row in con.execute(sql_cmd):
            print(row)
            print('select only some specified column')
            print(row[1], row[2])


def demo_selct2():
    with sqlite3.connect("tutorial.db") as con:
        con.row_factory = sqlite3.Row
        #เขียนแบบนี้จะอ้างอิงถึงข้อมูลโดยใช้ชื่อ column ได้เลย
        sql_cmd = """
        select * from person;

        """
        for row in con.execute(sql_cmd):


            print(row["gender"], row["height"])


def demo_selct3():
    with sqlite3.connect("tutorial.db") as con:
        con.row_factory = sqlite3.Row
        # เขียนแบบนี้จะอ้างอิงถึงข้อมูลโดยใช้ชื่อ column ได้เลย
        sql_cmd = """
        select gender, height, weight, 
            (weight/ (height/100) * (height/100)) as bmi
            from person
            where gender = 'F' AND height < 170

        """
        for row in con.execute(sql_cmd):
            print(row["gender"], row["height"], row['bmi'])


if __name__ == '__main__':
    demo_selct()
    print('*' * 40)
    print("demo2 ")
    demo_selct3()
