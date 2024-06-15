from collections import OrderedDict


def demo():
    menus = {'mocha':50,'latte':55,'espressor':30,'water':15}
    print(menus.items())

    sort_by_key = sorted(menus.items(), key=lambda x: x[0],reverse= False)
    print(sort_by_key)
    # it will return as sorted information in tuple
    #If we want to create a dictionary accoridngly

    #Do it manualy
    dict ={}
    for key,value in sort_by_key:
        dict[key] = value

    print(dict)

    # Or we can use method
    menu_by_name_dict = OrderedDict(sort_by_key)
    print(menu_by_name_dict)

def demo2():
    #sort by value
    menus = {'mocha': 50, 'latte': 55, 'espressor': 30, 'water': 15}

    sort_by_value = sorted(menus.items(), key=lambda x: x[1], reverse=False)
    print(sort_by_value)
    # As the same, sorted method return the sorted informaton as tuple variable

    #we can create a dictionary format mannually
    d = {}
    for k,v in sort_by_value:
        d[k] = v

    print(d)

    #or we can use the method
    sort_by_price = OrderedDict(sort_by_value)
    print(sort_by_price)

if __name__ == '__main__':
    demo2()
