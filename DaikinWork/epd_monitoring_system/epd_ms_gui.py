import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import pandas as pd
import mysql.connector as mysql
from datetime import date, timedelta, datetime


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Processing GUI")
        self.create_widgets()

    def create_widgets(self):
        # Filepath input
        tk.Label(self.root, text="File Path:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.file_path_entry = tk.Entry(self.root, width=50)
        self.file_path_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Browse", command=self.browse_file).grid(row=0, column=2, padx=5, pady=5)

        # Time Backward input
        tk.Label(self.root, text="Time Backward (months):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.time_backward_entry = tk.Entry(self.root, width=20)
        self.time_backward_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Initial Date input
        tk.Label(self.root, text="Initial Date (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.initial_date_entry = tk.Entry(self.root, width=20)
        self.initial_date_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Output Path input
        tk.Label(self.root, text="Output Path:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.output_path_entry = tk.Entry(self.root, width=50)
        self.output_path_entry.grid(row=3, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Browse", command=self.browse_output).grid(row=3, column=2, padx=5, pady=5)

        # Process Button
        tk.Button(self.root, text="Process Data", command=self.process_data).grid(row=4, column=0, columnspan=3,
                                                                                  pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        self.file_path_entry.insert(0, file_path)

    def browse_output(self):
        output_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                   filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        self.output_path_entry.insert(0, output_path)

    def process_data(self):
        file_path = self.file_path_entry.get()
        time_backward = int(self.time_backward_entry.get())
        initial_date_str = self.initial_date_entry.get()
        output_path = self.output_path_entry.get()

        try:
            initial_date = datetime.strptime(initial_date_str, '%Y-%m-%d').date()
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")
            return

        # Create DataFrame Handler
        handler = DataframeHandler(file_path)
        df = handler.create_dataframefromExcel('Doc. No.',
                                               "Parts\nreceived date",
                                               "Basic investigate\nreceived date",
                                               "Actual \nSend\ndate",
                                               "Report",
                                               skiprow=8, sheet_name='Market claim2024')

        df.rename(columns={'Parts\nreceived date': 'receive_date',
                           'Basic investigate\nreceived date': 'basic_date',
                           'Actual \nSend\ndate': 'send_date',
                           'Doc. No.': 'id',
                           'Report': 'supplier_report_date'},
                  inplace=True)

        df = handler.convertStringtoDate(df, 'receive_date', 'basic_date', 'send_date', 'supplier_report_date')

        userTimeFrame = TimeFrame(initial_date, time_backward)
        timeFrame = userTimeFrame.create_time_frame()
        dataCheckerObj = dataChecker(df, timeFrame)

        print()
        print(f'Return part Status')
        dataCheckerObj.find_total()

        data = dataCheckerObj.check_receiveData()
        df_result = pd.DataFrame(data)
        print(df_result)

        try:
            with pd.ExcelWriter(output_path) as writer:
                df_result.to_excel(writer, sheet_name='Result')
            messagebox.showinfo("Success", f"Data processed and saved to {output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save the file: {e}")


class DataframeHandler:
    def __init__(self, filePath):
        self.filePath = filePath

    def create_dataframefromExcel(self, *columns, skiprow, sheet_name):
        print(f'creating from this directory {self.filePath}\nwith skiprow: {skiprow} sheetname :{sheet_name}')
        column_list = self.tuple_to_list(columns)
        df = pd.read_excel(self.filePath, usecols=column_list, sheet_name=sheet_name, skiprows=skiprow)
        return df

    def tuple_to_list(self, tuple_column):
        return [i for i in tuple_column]

    def convertStringtoDate(self, df, *columns):
        for column in columns:
            try:
                df[column] = pd.to_datetime(df[column], errors='coerce').dt.date
            except Exception as e:
                print(f'error as = {e}')
                pass
        return df


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
        for i in range(1, time_backward + 1):
            timeframe.append(date(year, month, 1))
            if month == 1:
                month = 12
                year = year - 1
            else:
                month = month - 1
        print('create time successfully')
        return timeframe


class dataChecker:
    def __init__(self, df, timeFrame):
        self.timeFrame = timeFrame
        self.df = df

    def check_receiveData(self):
        date_info = {}
        for i in range(len(self.timeFrame) - 1):
            receive_count = 0
            basic_count = 0
            send_count = 0
            report_count = 0
            for index, row in self.df.iterrows():
                receive_date = row['receive_date']
                basic_date = row['basic_date']
                send_date = row['send_date']
                report_date = row['supplier_report_date']
                if pd.notna(receive_date):
                    if self.timeFrame[i] > receive_date >= self.timeFrame[i + 1]:
                        receive_count = receive_count + 1
                        if pd.notna(basic_date):
                            basic_count = basic_count + 1
                        if pd.notna(send_date):
                            send_count = send_count + 1
                        if pd.notna(report_date):
                            report_count = report_count + 1
                    else:
                        pass
            date_info[self.timeFrame[i + 1]] = {
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
    root = tk.Tk()
    app = App(root)
    root.mainloop()
