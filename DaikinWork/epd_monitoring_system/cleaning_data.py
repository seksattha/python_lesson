import mysql.connector
import pandas as pd
from datetime import datetime, date, timedelta

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
                    select * from customer;
                    """
                    cur.execute(sql_cmd)
                    rows = cur.fetchall()


                    df = pd.DataFrame(rows, columns=['id', 'fname', 'lname'])
                    return df

    except Exception as e:
        print(f'error => {e}')


def update_data(df):
    conn = mysql.connector.connect(host='localhost', user='root', password='ditepd', database='test_cleaning_python')
    for i in df.index:
        id = i
        name = df.loc[i, 'fname_edited']
        sql_cmd_update = """
        update customer set fname = %s where id = %s    
        """
        cursor = conn.cursor()
        cursor.execute(sql_cmd_update, (name, id))
        conn.commit()
        cursor.close()
    conn.close()

if __name__ == '__main__':
    df= query_data('localhost', 'root', 'ditepd', 'test_cleaning_python')
    df.set_index('id', inplace=True)
    df['fname_edited'] = df.apply(lambda x: x['fname'].title(), axis=1)
    update_data()
    print(df)