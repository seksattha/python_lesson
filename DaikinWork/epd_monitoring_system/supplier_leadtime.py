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
                    SELECT date_info.case_id, date_info.sent_date, supplier_info.supplier_name, supplier_info.lt_normal
                    FROM date_info
                    JOIN main ON main.case_id = date_info.case_id
                    JOIN supplier_info ON main.supplier_id = supplier_info.id
                    where main.req_supplier = true and sent_date is not null;
                    """
                    cur.execute(sql_cmd)
                    rows = cur.fetchall()


                    df = pd.DataFrame(rows, columns=['id', 'sent_date', 'supplier_name', 'lt'])
                    return df







    except Exception as e:
        print(f'error => {e}')

def leadtime_calculate(x):
    sent_date = x['sent_date']
    leadtime = x['lt']
    count = 0
    due_date =sent_date
    while count < leadtime:
        due_date = due_date + timedelta(days=1)
        if due_date.isoweekday() not in (6,7):
            count = count + 1
    return  due_date

def determine_leadtime(x, reminder_day):
    due_date = x['due_date']
    if due_date < date.today() + timedelta(days=reminder_day):
        status = 'overdue'
    else:
        status = 'on track'
    return status


if __name__ == '__main__':
    df= query_data('localhost', 'root', 'ditepd', 'pcb')
    df['due_date'] = df.apply(leadtime_calculate, axis=1)
    df['status'] = df.apply(determine_leadtime, axis=1, reminder_day = 3)
    print(df)