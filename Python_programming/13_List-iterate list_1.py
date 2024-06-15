def demo1():
    aircraft_names = ["Zero", "Mustang", "Wildcat", "Spitfire"]
    for i in aircraft_names:
        print(i)

    for i in range(len(aircraft_names)):
        print("{} {}".format(i+1,aircraft_names[i]))

    for i,e in enumerate(aircraft_names):
        print(f"No.{i+1} Aircraft: {e:^5} ")

def demo2():
    countries = [('TH', 'Thailand', 'ไทย'),
                 ('JP', 'Japan', 'ญี่ปุ่น'),
                 ('USA', 'United States', 'สหรัฐอเมริกา'),
                 ('DE', 'Germany', 'เยอรมนี'),
                 ('KR', 'Korea', 'เกาหลี'),
                 ('FR', 'France', 'ฝรั่งเศส')
                 ]
    for i in countries:
        print(i)

    for i, j in enumerate(countries):
        print(f"{i}  {j}")

# demo1()
demo1()