import datetime


def demo():
    t = [("sun", "red"), ("mon", "yellow"), ("tue", "pink"), ("wed", "green"),
         ("thu", "orange"), ("fri", "blue"), ("sat", "purple")]
    d={}

    #Create a dictionary form list
    for k,v in t:
        d[k] = v
    print(d)
    #Using dictionary comprehension

    d1 = {k.capitalize(): v.title() for k,v in t }
    print(d1)

    today = datetime.datetime.now()
    print(today.strftime("%a"))
    weekday = today.strftime("%a")
    weekcolor = d1[weekday]
    print(f"Today is {weekday} \ncolor of the day:{weekcolor}")

def demo2():
    weekday = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
    weekcolor = ["red", "yellow", "pink", "green", "orange", "blue", "purple"]

    z = zip(weekday,weekcolor) # generator
    d1 = {k.capitalize(): v for k,v in z}
    print(d1)


if __name__ == '__main__':
    demo()
    # demo2()