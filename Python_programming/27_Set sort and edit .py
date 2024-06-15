def basic_method():
    fruits = {"mango","banana"}
    #adding element into set
    fruits.add("apple")
    print(fruits)
    # the limitation of the 'add' method is that it can only add a single
    # element at a time.

    #if want update multiple element at once use update method instead.
    fruits.update({"coconut","papaya"})
    print(fruits)

    #we could unitilze union opeartion
    fruits = fruits | {"cherry","starwberry","kiwi"}
    print(fruits)

    #removing an element from set can be done using 'remove' or 'discard'
    fruits.remove("cherry")
    print(fruits)
    # # if the 'remove' method is uded with an element that doesn't belong to the set.
    # fruits.remove("durian")

    #in contrast with 'discard' methode, even if "durian" doesn't belong to the set.
    fruits.discard("durain")

    #searching in set
    print("durian" in fruits)
    # Boolean will be replied, either true of false
    #clear all information is set using 'clear' method
    fruits.clear()
    print(fruits)
    # The representation of an empty set using set() will be returned.

def pass_skill(required_skill,applicant_skill):
    return required_skill <= applicant_skill # <= subset symbol
    # required skill is subset of applicant skill


def pass_skill2in3(required_skill,applicant_skill):
    a =  required_skill & applicant_skill # using intersection
    print(a)
    if len(a) >= 2:
        return True
    else:
        return False

if __name__ == '__main__':
    basic_method()
    # req = {"python","r","Java"}
    # app = {"python","r","Java","HTML"}
    # print(pass_skill(req, app))
    #
    # req = {"python", "r", "Java"}
    # app = {"python","Java", "HTML"}
    # print(pass_skill2in3(req, app))
