def demo():
    skills = {"Python","C","Java"}
    # The format is similar to dictionary,
    # The difference point there is no key just value
    print(type(skills))

    #Build เซ็ทว่าง
    #ห้ามทำแบบนี้จะกลายเป็น dictionary
    a = {}
    #ต้องทำแบบนี้
    b = set()
    print(type(a))
    print(type(b))

def demo2():
    #Immutable -> hasable e.g. tuple
    xy = {(3,7),(5,10),(15,9)}
    print(xy)
    print(type(xy))

    #basic operation
    # Union
    a = {"mango","coconut","mango","banana"}
    b = {"cherry","mango","apple"}
    m = a | b
    print(f"Union = {m}")

    # Intersection
    n = a & b
    print(f"intersection {n}")

    #difference
    p = a-b
    print(f"difference {p}")

    #Symmeteric differnce (a union b) - (a intersect b)
    q = a^b
    print(q)

if __name__ == '__main__':
    # demo()
    demo2()