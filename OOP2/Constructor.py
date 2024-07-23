from abc import ABC, abstractmethod
class Person:
    def __init__(self, firstName, lastName):
        print("parameterized consturctor is called")
        self.firstName = firstName
        self.lastName = lastName



    def __str__(self):
        print(f'name: {self.__firstName}')

    @property
    def firstName(self):
        return self.__firstName
    @firstName.setter
    def firstName(self, firstName):
        self.__firstName = firstName.strip().title()
class MemberCard(Person, ABC):

    def discount(self, amount):
        return amount * .03

    @abstractmethod
    def rewardXPoint(self):
        pass


    def calcPoint(self, amount):
        return (amount/10) * self.rewardXPoint()
class GoldCard(MemberCard):

    def discount(self, amount):
        if amount > 2000:
            return amount * .10
        else:
            return amount * .05

    def rewardXPoint(self):
        return 2
class PlatinumCard(MemberCard):

    def discount(self, amount):
        if amount > 2000:
            return amount * .15
        else:
            return amount * .05

    def accessLounge(self):
        return True


    def rewardXPoint(self):
        return 3


if __name__ == '__main__':
    p1 = Person("JoHN", "Snow")
    # p2 = MemberCard("Tyrian", "Lannistor")
    # print(p2.discount(1000))
    p3 = GoldCard("Tywin", "Lannistor")
    print(p3.discount(1000))
    print(p3.calcPoint(1000))
    p4 = PlatinumCard("Jamie", "Lannistor")
    print(p4.discount(1000))
    print(p4.calcPoint(1000))
    print(p4.accessLounge())

