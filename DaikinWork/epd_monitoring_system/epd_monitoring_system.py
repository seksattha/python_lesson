import pandas as pd
import re
import mysql.connector as mysql
from datetime import date, timedelta, datetime


def insert_data(host: str, user: str, password: str, database_name: str, df):
    try:
        # Establish connection to MySQL database
        with mysql.connect(
                host=host,
                user=user,
                password=password,
                database=database_name
        ) as con:
            if con.is_connected():
                print("Connection to DIT_EPD successfully, \nWELCOME TO EPD DATABASE!")

                # Iterate through each row in the DataFrame and insert into MySQL table 'mpg'
                with con.cursor() as cur:
                    sql_cmd = """
                    INSERT INTO market_claim (case_id)
                    VALUES (%s)
                    ON DUPLICATE KEY UPDATE case_id=case_id
                    """
                    for index, row in df.iterrows():
                        values = (
                            row['case_id'],

                        )
                        cur.execute(sql_cmd, values)

                # Commit the transaction
                con.commit()
                print('Data has been inserted successfully')

    except mysql.Error as e:
        print(f'Error => {e}')


def query_data(host: str, user: str, password: str, database_name: str):
    try:
        # Establish connection to MySQL database
        con = mysql.connect(
            host=host,
            user=user,
            password=password,
            database=database_name
        )

        if con.is_connected():
            print("Connection to DIT_EPD successfully, \nWELCOME TO EPD DATABASE!")

            # Execute the SQL query
            sql_cmd = """
            SELECT 
                m.case_id, 
                d.receive_date, 
                d.basic_date, 
                d.sent_date, 
                d.finish_date 
            FROM 
                market_claim m
            LEFT JOIN 
                date_info d
            ON 
                m.case_id = d.case_id;
            """

            cur = con.cursor()
            cur.execute(sql_cmd)
            rows = cur.fetchall()

            # Define column names according to the SQL query
            columns = ['case_id', 'receive_date', 'basic_date', 'sent_date', 'finish_date']

            # Create DataFrame from query results
            df = pd.DataFrame(rows, columns=columns)

            # Close cursor and connection
            cur.close()
            con.close()

            return df

    except mysql.Error as e:
        print(f'Error => {e}')




def timeFrame(today, time_backward):
    year  = today.year
    month = today.month + 2

    timeframe = []
    for i in range(time_backward):

        if month == 1:
            month = 12
            year = year - 1

        else:
            month = month -1
        timeframe.append(date(year,month,1))
    return  timeframe


def check_date(timeframe, df):
    date_info = {}
    for i in range(len(timeframe) - 1):
        total_receive = 0
        for index, row in df.iterrows():
            # Convert 'receive_date' to a date object if it is not already and not None
            receive_date = row['receive_date']
            if receive_date is not None:
                if isinstance(receive_date, str):
                    receive_date = datetime.strptime(receive_date, '%Y-%m-%d').date()

                if timeframe[i] > receive_date >= timeframe[i + 1]:
                    total_receive += 1
        date_info[f"{timeframe[i].year}-{timeframe[i].month:02}"] = total_receive
        print(date_info)







if __name__ == '__main__':
    df = pd.read_excel(r'C:\Users\seksatta\Documents\epd_list.xlsx')
    df['case_id'] = df.F12.str.extract(r'\bMKG\b-\d{1,2}\b-(\w{4})')

    insert_data('localhost', 'root', 'ditepd', 'pcb', df)

    df = query_data('localhost', 'root', 'ditepd', 'pcb')

    timeframe = timeFrame(date.today(),4)
    check_date(timeframe,df)


