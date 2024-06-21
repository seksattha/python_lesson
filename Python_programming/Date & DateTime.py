from datetime import date, datetime, timedelta


def timedelta_demo():
    #create a year with timedelta
    year = timedelta(days=365)

    # it could be anything like 10 days
    day = timedelta(days=1)
    ten_days = 10* day
    print(ten_days)

    ten_years = 10 * year
    print(ten_years)

    #total second มันมีแค่ totoal second เพราะว่ามันเป็นหน่วยเวลาที่เล็กที่สุดนั้นเอง
    ten_week = timedelta(days= 7 ) * 10
    print(f'total second of 10 week = {ten_week.total_seconds()} seconds')
    # If we want to see in hour just divided by 60
    print(f'total second of 10 week = {ten_week.total_seconds() / 60} hours')

def date_demo():
    # ISO-8601 is format for date YYYY-MM-DD
    #Change into format of iso-8601
    ex_date = date.fromisoformat("2019-01-01")
    print(ex_date)
    ex_date = date.fromisoformat("20191204")
    print(ex_date)
    ex_date = date.fromisoformat('2021-W01-1')
    print(ex_date)
    print('*'*40)

    print("Extraction of string from date object")
    print("date.year date.month date.day")
    mydate = date.today()
    print(f' today = {mydate}')
    print(f'Extracting the year    date.year =>  {mydate.year}')
    print(f'Extracting the month    date.month =>  {mydate.month}')
    print(f'Extracting the day    date.day =>  {mydate.day}')

def operation_demo():
    sql_birthday = date(1974, 1, 1)
    today =date.today()
    print(f'elapsed_date = {today - sql_birthday}')

    #Comparison
        # == equal
        # != not equal
        # > , < , =!

    date1 = date(2024,12,1)
    date2 = date(1945, 8, 15)
    if date1 < date2:
        print('True')
    else:
        print('false')

def weekday_demo():
    today = date.today()
    # Use ISO weekday the result matched with our understanding.
    print(f'{today.isoweekday()}')

def findleadtime(date, leadtime:int):
    day = timedelta(days=1)
    count = 0
    while count < leadtime:
            date = date + day
            if date.isoweekday()  not in (5,6):
                count = count + 1
    return date


# timedelta_demo()
# date_demo()
# operation_demo()
# weekday_demo(
print(f'due date supplier = {findleadtime(date.today(), 15)}')