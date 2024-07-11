
import pandas as pd
import re
import mysql.connector as mysql
from datetime import date, timedelta, datetime





def check_date(timeframe, df):
    date_info = {}
    for i in range(len(timeframe) - 1):
        total_receive = 0
        basic_count = 0
        sent_count = 0
        for index, row in df.iterrows():
            # Convert 'receive_date' to a date object if it is not already and not None
            receive_date = row['receive_date']
            basic_date = row.get('basic_date')
            sent_date = row.get('sent_date')

            if receive_date is not None:
                if isinstance(receive_date, str):
                    receive_date = datetime.strptime(receive_date, '%Y-%m-%d').date()

                if timeframe[i] > receive_date >= timeframe[i + 1]:
                    total_receive += 1
                    # Check basic_date and sent_date within the same receive_date condition
                    if basic_date is not None:
                        if isinstance(basic_date, str):
                            basic_date = datetime.strptime(basic_date, '%Y-%m-%d').date()
                        if timeframe[i] > basic_date >= timeframe[i + 1]:
                            basic_count += 1

                    if sent_date is not None:
                        if isinstance(sent_date, str):
                            sent_date = datetime.strptime(sent_date, '%Y-%m-%d').date()
                        if timeframe[i] > sent_date >= timeframe[i + 1]:
                            sent_count += 1
        date_info[timeframe[i+1]] = {
            'total_receive': total_receive,
            'basic_count': basic_count,
            'sent_count': sent_count
        }

    print(date_info)

class Database:
    def __init__(self, host, user, password, databaseName):
        self.host = host
        self.user = user
        self.password = password
        self.databaseName = databaseName

    def __str__(self):
        return f'connecting database name = {self.databaseName}, user => {self.user}'

    def _connect(self):
        try:
            con = mysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.databaseName
            )
            if con.is_connected():
                print("Connection to DIT_EPD successfully, \nWELCOME TO EPD DATABASE!")
                return con
        except mysql.Error as e:
            print(f'Error => {e}')
            return None

    def query(self, sql_cmd):
        con = self._connect()
        if con.is_connected():
            try:
                    cur = con.cursor()
                    cur.execute(sql_cmd)
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
            except Exception as e:
                print(f'error => {e}')


    def query_df(self, sql_cmd):
        con = self._connect()
        if con.is_connected():
            try:
                    cur = con.cursor()
                    cur.execute(sql_cmd)
                    rows = cur.fetchall()
                    columns = [desc[0] for desc in cur.description]
                    df = pd.DataFrame(rows, columns= columns)
                    return df
            except Exception as e:
                print(f'error => {e}')
            finally:
                con.close()
                cur.close()
        return None

    def count_row(self, tableName: str):
        con = self._connect()
        if con:
            cur = con.cursor()
            sql_cmd = f' select count(*) from {tableName}'
            cur.execute(sql_cmd)
            rowCount = cur.fetchone()[0]
            return rowCount
        else:
            return None

    def check_update(self, df, table_name:str):
        if df.shape[0] > db.count_row(table_name):
            print('Start Updating date')
            mysql_row = db.count_row(table_name)
            updated_row = ()
            while mysql_row < df.shape[0]:
                updated_row = updated_row + (mysql_row,)
                mysql_row = mysql_row + 1

            print(updated_row)
            return updated_row
        else:
            print('data is up to date')
            return []

    def insert(self, df, table_name:str):
        updated_rows = self.check_update(df, table_name)

        if not updated_rows:
            print('No data to update')
            return
        con = self._connect()

        if con:
            cur = con.cursor()
            for index, row in df.iterrows():
                if index in updated_rows:
                    print(f'found! index => {index} value = {row['case_id']}')
                    values = (
                        row['case_id'],
                    )

                    sql_cmd = """ 
                    insert into market_claim (case_id)
                    value(%s)
                    ON DUPLICATE KEY UPDATE case_id=case_id
                        
                    """
                    try:
                        cur.execute(sql_cmd, values)
                    except mysql.Error as e:
                        print(f' error => {e}')
                    finally:
                        print('Updated successfully')
            con.commit()
            print(updated_rows)
            con.close()





class TimeFrame:
    def __init__(self, start_date, time_backward):
        self.time_backward = time_backward
        self.start_date = start_date

    def create_time_frame(self):
        edit_date = self.start_date
        time_backward = self.time_backward
        month = edit_date.month + 1
        year = edit_date.year
        print(f'Month = {month}, Year = {year}')

        timeframe = []
        for i in range(1,time_backward+1):
            timeframe.append(date(year,month,1))
            if month == 1:
                month = 12
                year = year - 1
            else:
                month = month - 1
        print('create time succesfully')
        return timeframe




class DataframeHandler:
    def __init__(self, filePath):
        self.filePath =filePath

    def create_dataframefromExcel(self, *columns, skiprow, sheet_name):

        print(f'creating from this directory {self.filePath}\nwith skiprow: {skiprow} sheetname :{sheet_name}')
        column_list = self.tuple_to_list(columns)
        df = pd.read_excel(self.filePath, usecols = column_list, sheet_name=sheet_name, skiprows=skiprow )
        return df

    def tuple_to_list(self, tuple_column):
        list = []
        for i in tuple_column:
            list.append(i)
        return  list
if __name__ == '__main__':



    my_time_frame = TimeFrame(date.today(), 4)
    my_time_frame.create_time_frame()

    handler = DataframeHandler(r'C:\Users\seksatta\Desktop\Master List FY2024.xlsx')
    df = handler.create_dataframefromExcel('Doc. No.',
                                           "Parts\nreceived date",
                                           "Basic investigate\nreceived date",
                                           "Actual \nSend\ndate",
                                           "Report", skiprow = 8, sheet_name = 'Market claim2024')
    print(df)


