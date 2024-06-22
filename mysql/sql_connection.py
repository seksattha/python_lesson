import mysql.connector

try:
    with mysql.connector.connect(
        host= 'localhost',
        user = 'root',
        password = 'ditepd',
        database = 'pcb'
    )as con:
        if con.is_connected():
            print("connection to DIT_EPD successfully")

            with con.cursor() as cur:
                sql_cmd =  """
                select * from main;
                """
                cur.execute(sql_cmd)

                rows = cur.fetchall()

                for row in rows:
                    print(row)

except Exception as e:
    print(f'error = {e}')

