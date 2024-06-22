import mysql.connector

def query_data(host:str, user:str, password, database_name):
    try:
        with mysql.connector.connect(
            host= host,
            user = user,
            password = password,
            database = database_name
        )as con:
            if con.is_connected():
                print("connection to DIT_EPD successfully, \nWELCOME TO EPD DATABASE!")

                with con.cursor() as cur:
                    sql_cmd =  """
                    select * from main where error_code = 'U4';
                    """
                    cur.execute(sql_cmd)
                    rows = cur.fetchall()

                    for row in rows:
                        print(row)

    except Exception as e:
        print(f'error => {e}')

if __name__ == '__main__':
    query_data('localhost', 'root', 'ditepd', 'pcb' )