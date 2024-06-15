def demo():
    flower_names = ["Rose", "Tulip", "Sunflower", "Lily", "Daisy"]
    #Search in list
    print("Daisy" in flower_names)
    # Or in the same way with variable "is_exist"
    is_exist = "Daisy" in flower_names
    print(is_exist)

    #Another way with index
    print(flower_names.index("Tulip"))
    # return the index in list, when found
    print(flower_names.index("Jasmine"))
    # raised exception when not found.

def demo_editList():
    flower_names = ["Rose", "Tulip", "Sunflower", "Lily", "Daisy"]
    print(flower_names)
    # Edit 2 position from "Sunflower" to "Jasmine"
    flower_names[2] = "Jasmine"
    print(flower_names)

    # Edit all member in list with loop, Changing the first letter into upper case alphabet.
    for i in range(len(flower_names)):
        flower_names[i] = flower_names[i].capitalize()

    # Clear all member in list
    flower_names.clear()
    print(flower_names)

def demo_append():
    # adding single element in the end of existing list.
    countries = [('TH', 'Thailand', 'ไทย'),
                 ('JP', 'Japan', 'ญี่ปุ่น'),
                 ('USA', 'United States', 'สหรัฐอเมริกา'),
                 ('DE', 'Germany', 'เยอรมนี'),
                 ('KR', 'Korea', 'เกาหลี'),
                 ('FR', 'France', 'ฝรั่งเศส')
                 ]
    print(countries)
    print("*" * 40)

    #adding element in the end of existing list.
    UK = ("UK","United Kingdom","อังกฤษ")
    countries.append(UK)
    print(countries)
    print("*"*40)

    #We could do in this way,appending element into list
    countries.append(("SG","Singapore","สิงค์โปร์"))
    print(countries)
    print("*" * 40)


    # We could insert element into list with specific index
    SW = ("SW","Switzerland","สวิตเซอร์แลนด์")
    countries.insert(2,SW)
    print(countries)
    print("*" * 40)


def demo_StringToList():
    #convert string into list.
    alphabet= list("abcdefghijklimnopqrstuvwxyz")
    print(alphabet)
    # repeating element in list
    a = [0] * 10
    print(a)

    b = [1,3]*5
    print(b)

# demo()
# demo_append()
demo_StringToList()