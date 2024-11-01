
import pandas as pd
import re
import mysql.connector as mysql
from datetime import date, timedelta, datetime






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
        list = [ i for i in tuple_column]
        return  list

    def convertStringtoDate(self, df, *columns):
        for column in columns:
            try:
                df[column] = pd.to_datetime(df[column], errors='coerce').dt.date

            except Exception as e:
                print(f'error as = {e}')
                pass
        return df
class dataChecker:
    def __init__(self, df, timeFrame):
        self.timeFrame = timeFrame
        self.df = df

    def check_receiveData(self):
        date_info = {}
        for i in range(len(self.timeFrame)-1):
            receive_count = 0
            basic_count = 0
            send_count = 0
            report_count = 0
            for index ,row in self.df.iterrows():
                receive_date = row['receive_date']
                basic_date = row['basic_date']
                send_date = row['send_date']
                report_date = row['supplier_report_date']
                if pd.notna(receive_date):
                    if self.timeFrame[i] > receive_date >= self.timeFrame[i+1]:
                        receive_count = receive_count + 1
                        if pd.notna(basic_date):
                            basic_count = basic_count + 1
                        if pd.notna(send_date):
                            send_count = send_count + 1
                        if pd.notna(report_date):
                            report_count = report_count + 1
                    else:
                        pass
            # print(f'{self.timeFrame[i + 1]} {receive_count} basic = {basic_count}\n send = {send_count} complete = {report_count}' )
            date_info[self.timeFrame[i+1]] = {
                'receive':receive_count,
                'basic':basic_count,
                'send': send_count,
                'report': report_count
            }
        return date_info

    def check_receive_data2(self):
        date_info = {}

        # Loop through the time frame intervals
        for i in range(len(self.timeFrame) - 1):
            # Initialize counters for the current time frame interval
            receive_count = basic_count = send_count = report_count = 0

            # Get the current and next time frame boundaries
            start_time = self.timeFrame[i]
            end_time = self.timeFrame[i + 1]

            # Filter rows within the current time frame interval
            filtered_df = self.df[(self.df['receive_date'] < start_time) & (self.df['receive_date'] >= end_time)]

            # Count the occurrences of each event
            receive_count = len(filtered_df)
            basic_count = filtered_df['basic_date'].notna().sum()
            send_count = filtered_df['send_date'].notna().sum()
            report_count = filtered_df['supplier_report_date'].notna().sum()

            # Store the results in the dictionary
            date_info[end_time] = {
                'receive': receive_count,
                'basic': basic_count,
                'send': send_count,
                'report': report_count
            }

        return date_info

    def find_total(self):
        data = self.check_receiveData()
        indices = ['receive', 'basic', 'send', 'report']
        for index in indices:
            value = 0

            for k in data.keys():
                value = value + data[k][index]
            print(f'{index} = {value}')

if __name__ == '__main__':





    handler = DataframeHandler(r'C:\Users\seksatta\Desktop\Master List FY2024.xlsx')
    df = handler.create_dataframefromExcel('Doc. No.',
                                           "Parts\nreceived date",
                                           "Basic investigate\nreceived date",
                                           "Actual \nSend\ndate",
                                           "Report",
                                           skiprow = 8, sheet_name = 'Market claim2024')

    df.rename(columns={'Parts\nreceived date': 'receive_date',
                       'Basic investigate\nreceived date': 'basic_date',
                       'Actual \nSend\ndate': 'send_date',
                       'Doc. No.': 'id',
                       'Report': 'supplier_report_date'},
              inplace=True)

    df = handler.convertStringtoDate(df, 'receive_date', 'basic_date', 'send_date', 'supplier_report_date')

    userTimeFrame = TimeFrame(date.today(), 5)
    timeFrame = userTimeFrame.create_time_frame()
    dataChecker = dataChecker(df, timeFrame)
    print()
    print(f'Return part Status')
    dataChecker.find_total()


    data = dataChecker.check_receive_data2()
    df = pd.DataFrame(data)
    print(df)


