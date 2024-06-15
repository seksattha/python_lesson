def demo_list1():
    flower = ['calla','lilly','Jasmine']
    print(flower)
    #list is mutable
    #tuple is immutable

    flower = flower + ["forget me not"]
    print(flower)
    del flower[2]
    print(flower)
    flower.remove('lilly')
    print(flower)
    flower.sort()
    print(flower)
    flower.append('rose')
    print(flower)

def demo():
    flower = ['calla', 'lilly', 'Jasmine', 'forget me not']
    # slicing
    print(flower[1:4])
    print(flower[-1:-4:-1])



demo()