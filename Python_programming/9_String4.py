# !String format 2
# padding technique
def demo():
    print("{} {} ".format("th","Thailand")) #{} is called place holder
    print("{:5}|{:15}| ".format("th","Thailand"))
    print("{:>5}|{:>15}| ".format("th","Thailand")) #> is right indent  alignment tool
    print("{:^5}|{:^15}| ".format("th","Thailand")) #> is center alignment tool


    print("{:*>5}|{:->15}| ".format("th","Thailand"))
def demo_dict():
    "Using padding with dictionary variable "
    menu = {"name": "mocha", "price": 40, "size":"medium"}
    print(menu["name"])
    print("{} {}".format(menu["name"],menu["price"]))
    # อีกแบบหนึ่ง
    print(("menu name = {name} price = {price} size = {size}".format(**menu)))


def mult_table(n):
    for i in range(1,13):
        print("{} X {} = {}".format(n,i,n*i))

def ascii_table():
    for i in range(65,128):
        print("{0:3} {0:#08b} {0:#x} {0:c}".format(i))

if __name__ == '__main__':
    # #demo()
    # demo_dict()
    # mult_table(3)
    ascii_table()
