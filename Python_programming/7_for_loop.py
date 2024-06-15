def loop1():
    for i in range(11):
        print("hello world {}".format(i))
def loop2():
    for i in range(1,11):
        print("hello world {}".format(i))

def loop3():
    for i in range(1,11,2):
        print("hello world {}".format(i))
        print("-----------")
    print("Done!")
def loop_in_string():
    s = "over the rainbow"
    for c in s:
        print(c.upper())

def loop_tuple():
    Band = "Metalica","Dream Theater","rush"
    for b in range(len(Band)):
        print(Band[b].lower())

def loop_tuple2():
    Band = "Metalica","Dream Theater","rush"
    for b in range(len(Band)):
        print(b,Band[b].lower(),sep=(")"))



if __name__ == '__main__':
    loop1()
    print("*"*40)
    loop2()
    print("*" * 40)
    loop3()
    print("*" * 40)
    loop_in_string()
    print("*" * 40)
    loop_tuple()
    print("*" * 40)
    loop_tuple2()