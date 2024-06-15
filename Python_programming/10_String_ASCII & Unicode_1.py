def demo():
    print(ord('a'))
    print(ord('A'))


    print(chr(65))

def ascii_Table():
    for i in range(0,256):
        print("{0} {0:b} {0:c}".format(i))

def unicode_table():
    for i in range(ord("ก"),ord("ฮ")+1):
        print("{0} {0:b} {0:c}".format(i))

unicode_table()
