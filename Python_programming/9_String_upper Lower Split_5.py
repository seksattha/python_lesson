def demo1():
    s = "peter"
    print(s.capitalize())
    print(s.upper())
    t = "parker"
    print(t.lower())

def demo2():
    choice = input("[M] Male,[F] Female")
    if choice.upper() == "M":
        print("Male")
    else:
        print("Female")
def title():
    s = "the land of smile"
    print(s.title())
def split():
    s = "the land of smile"
    a = s.split()
    print(a)
    print(type(a))

    print(a[0])
    print(a[1])
    print(a[2])

    t = "Thailand,5,7,3" # split with "," as seperator
    b = t.split(",")
    print(b)

    resolution = "1920x1080"
    c = resolution.split("x")
    print(c)

# demo1()
# demo2()
split()