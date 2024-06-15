def demo():
    m = {
        "th": {"g": 5, "s": 3, "b": 7},
        "sg": {"g": 3, "s": 2, "b": 1},
        "jp": {"g": 3, "s": 7, "b": 2}
    }

def demo():
    m = {
        ("th", 2016): {"g": 5, "s": 3, "b": 7},
        ("th", 2015): {"g": 3, "s": 2, "b": 1},
        ("jp", 2016): {"g": 3, "s": 7, "b": 2}
    }

    print(m)
    print(m[(("th", 2015))])
    print(m[("th", 2015)]["g"])

    # การแก้ไขค่าภายใน dictionary
    m[("th", 2015)]["g"] = 99
    print(m[("th", 2015)]["g"])

    # การแก้ไขค่าหลายๆ ค่าพร้อมกัน
    m[("th", 2015)] = {"g": 10, "s": 37, "b": 3}
    print(m[("th", 2015)])

    # การลบค่าใน dictionary
    del m[("jp", 2016)]
    print(m)

    if ("th",2016) in m:
        print("Found")
    else:
       print("not here")

    #การเพิ่มข้อมูล้
    m[("DE", 2015)] = {"g": 99, "s": 777, "b": 123}
    print(f"{m}", end="")



if __name__ == '__main__':
    demo()