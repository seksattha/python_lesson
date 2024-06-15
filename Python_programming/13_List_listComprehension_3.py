def v1():
    for i in range(1,11):
        print(i,i*0.621371)

#list comprehension
def v2():
    [print(i,i*0.621371) for i in range(1,11)]
    m = [i*0.621371 for i in range(1,11)]
    print(m)


    # let's see a tradition way for append
    square = []
    for i in range(1,11):
        square.append(i**2)
    print(square)

    #Using list comprehension
    square = [i**2 for i in range(1,11)]
    print(square)
    # It's more readable compared with traditional approach.




if __name__ == '__main__':
    v2()