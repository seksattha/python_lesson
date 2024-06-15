
def demo3():

    m = {
        "th": {"g": 5, "s": 3, "b": 7},
        "sg": {"g": 3, "s": 2, "b": 1}
    }
    print(m)
    print(m["th"]["g"])
    print(m["th"]["g"] + m["th"]["s"] + m["th"]["b"])

def loop_dict():
    m = {
        "th": {"g": 5, "s": 3, "b": 7},
        "sg": {"g": 3, "s": 2, "b": 1},
        "jp": {"g": 3, "s": 7, "b": 2}
    }
    print("m")
    for c in m:
        print(c)
    print("*"*40)
    for c in m.values():
        print(c)
    print("*" * 40)
    for k,v in m.items():
        print(f"key:{k}  value:{v}")
    print("*" * 40)

    print(m.keys())
    for c in m.keys():
        print(c)
    print("*" * 40)

if __name__ == '__main__':
    # demo3()
    loop_dict()