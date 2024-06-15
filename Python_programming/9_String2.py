# !String format
fname = "John"
lname = "Doe"
age = 21

print(fname,lname,age)
print("{} {} {}".format(fname,lname,age))
print("{0} {1} {2}".format(fname,lname,age))
print("{1} {0} age:{2}".format(fname,lname,age)) #position

def demo_number():
    n = 218123000
    print("{}".format(n))
    print("{:,}".format(n))

    d = 234324.78932
    print("{:.2f}".format(d))
    print("{:,.2f}".format(d))

    e = 9809834.23434
    print("{:15.2f}".format(n))
    print("{:15,.2f}".format(d))
    print("{:15,.2f}".format(e))



if __name__ == '__main__':
    demo_number()