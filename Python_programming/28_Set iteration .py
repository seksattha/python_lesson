def demo_loop():
    s = {"apple","banana","mango","cherry"}
    for f in s:
        print(f)
    print("*"*40)
    # Please be aware that the information within the set is not arranged in a specific order.


    # Change set into list and use sort method.
    s = {"apple", "banana", "mango", "cherry"}
    a = list(s)
    a.sort()
    for f in a:
        print(f)

def demo_loop2():
    countries = { ("th","Thailand"),
                  ("jp","Japan"),
                  ("kr","Korean")
                  }
    print(countries)
    print("*"*40)


    for i in countries:
        print(i)
    print("*"*40)


    # display on country name with out abbreavation
    for i in countries:
        print(i[1])
    print("*" * 40)

    #display both abbreavation and full contry name
    for count_id , count_name in countries:
        print(count_name)
    print("*" * 40)

    #display no. in additional
    for i ,(count_id,count_name) in enumerate(countries):
        print(f"No.{i+1}  Abbrevation:'{count_id}' Full country name: {count_name}")
    print("*" * 40)

    # Checking element in set
    if ("jp","Japan") in countries:
        print("Found")
    else:
        print("not found")

def immutable_set():
    # frozen set
    fz = frozenset(["lilly", "carnation"])
    print(fz)
    print(type(fz))


if __name__ == '__main__':
    # demo_loop()
    demo_loop2()
    # immutable_set()