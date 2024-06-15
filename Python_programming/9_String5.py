# s = "peter"
# print(s.capitalize())
# print(s.upper())
#
# t ="PARKER"
# print(t.lower())
def demo():
    choice = (input("[M] male [F] male")).upper()
    if choice == "M":
        print("Male")
    else:
        print("Female")

def demo_title():
    s = "the land of smile"
    print(s.title())

def demo_split():
    s = "the land of smile"
    a = s.split()
    print(a)
    print(type(a))
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])
    t = ""

if __name__ == '__main__':
    demo_split()