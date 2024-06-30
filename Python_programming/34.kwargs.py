def f(**kwargs):
    print(kwargs)
    print(f'{type(kwargs)}')
    #จะใช้งานเหมือน ditionary ทั่วไปเลย
    print(kwargs['age'])

def fullname(**parts):
    for k in ('fname', 'mname', 'lname'):
        if k in parts.keys():
            print(parts[k])

def build_query(table, **filters):
    #จะเป็นการสร้างฟังก์ชั่นที่จะค่าครับมาเป็น sql command ที่ผู้ใช้ จะกำหนดเงื่อนไขในการค้นหาได้
    sql_cmd = f'select * from {table} where '
    conditions = [ f"{k} = '{v}'"for k,v in filters.items() ]
    # จะเป็นการนำแต่ละเงื่อนมาต่อกันหลัง and
    sql_cmd = sql_cmd + "AND ".join(conditions)
    print(sql_cmd)

f(name = 'Peter', age = 21)
#จะได้ค่าออกมาเป็น dictionary

#จะใส่ไปกี่อันก็ได้
f(name= 'Peter', age =23, hero='spiderman')

#ลองสร้าง function ที่ชื่อว่า fullname ขึ้นมา
fullname(fname = 'George', mname = "F", lname = 'Mood')
fullname(fname = 'John', lname = 'Kenedy')


#อีกหนึ่งตัวอย่างที่สามารถทำได้คือการใช้ sql queery
build_query('user', name='Alice', age = 30, country = 'USA')