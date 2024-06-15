import datetime


def demo():
    current_datetime = datetime.datetime.now()

    # Convert the current date and time to a string with a specific format
    timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    with open("test_writing.txt", 'a',
              encoding="utf-8") as f:
        f.write("Test writing textfile from python programming")


if __name__ == '__main__':
    demo()