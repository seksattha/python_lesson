import mysql.connector
import pandas as pd

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
                    SELECT date_info.case_id, date_info.sent_date, supplier_info.supplier_name
                    FROM date_info
                    JOIN main ON main.case_id = date_info.case_id
                    JOIN supplier_info ON main.supplier_id = supplier_info.id
                    where main.req_supplier = true and sent_date is not null;
                    """
                    cur.execute(sql_cmd)
                    rows = cur.fetchall()

                    for row in rows:
                        print(row)




    except Exception as e:
        print(f'error => {e}')

if __name__ == '__main__':
    query_data('localhost', 'root', 'ditepd', 'pcb' )