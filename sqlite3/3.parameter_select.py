import sqlite3

def demo_select_1():
    try:
        with sqlite3.connect("tutorial.db") as con:
            con.row_factory = sqlite3.Row
            sql_cmd = """
            select * from person where gender = 'M'
            
            """
            cur = con.execute(sql_cmd)
            for row in cur:
                print(f'{row['obs']} {row['gender']} {row['height']} {row['weight']} ')


    except Exception as e:
        print('error {}'.format(e))


def demo_select_2(sex:str, h):
    try:
        with sqlite3.connect("tutorial.db") as con:
            con.row_factory = sqlite3.Row
            #ใช้ ? เพื่อเป็นการกำหนด parameter ได้
            sql_cmd = """
            select * from person where gender = ? and height > ?
            
            """
            # ตัวแปรที่จะผ่านค่าเข้าไปจาก ? จะต้องเป็น list หรือว่า tuple เข้าไปได้
            # cur = con.execute(sql_cmd, [sex, h])
            cur = con.execute(sql_cmd, (sex, h))
            for row in cur:
                print(f'{row['obs']} {row['gender']} {row['height']} {row['weight']} ')


    except Exception as e:
        print('error {}'.format(e))
if __name__ == '__main__':
    # demo_select_1()
    demo_select_2('F', 180)