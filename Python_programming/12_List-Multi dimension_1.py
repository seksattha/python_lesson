scores = [10, 15, 7 ,8]
print(sum(scores))
average = (sum(scores)/len(scores))
print(average)

#Multi Dimension list
def multi_list():
    contries =[("th","Thailand","ไทย"),
               ("jp","Japan","ญี่ปุ่น"),
               ("de","Germany","เยอรมัน")]
    print(contries)
    print(contries[1])
    print(contries[1][1])
    print(contries[2][2])


def multi_list2():
    menus = [["Mocha",[1,2,3]],
             ["Latte",[4,5,6]]
             ]
    print(menus)
    print(menus[1][1])
    print(menus[1][1][1])
multi_list2()
