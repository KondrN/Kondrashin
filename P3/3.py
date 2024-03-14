class Human:
    default_name = "Nikita"
    default_age = 18

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = "False"

    def info(self):
        print(f"{self.name}, {self.age}, {self.__money}, {self.__house}")

    @staticmethod
    def default_info():
        print(f"{Human.default_name}, {Human.default_age}")

    def earn_money(self, amount):
        self.__money += amount

    def __make_deal(self, house, price):
        if self.__money >= price:
            self.__money -= price
            self.__house = house.name
            print(f"{self.name} купил дом за {price}")

    def buy_house(self, house):
        if self.__money >= house.final_price():
            self.__make_deal(house, house.final_price())
        else:
            print("Нехватает денег")


class House:
    def __init__(self, area=60, price=1000, name="Дом 1"):
        self._area = area
        self._price = price
        self.name = name
    def final_price(self, discount=0):
        return self._price - discount
class SmallHouse(House):
    def __init__(self, price=1000, name="Дом 1"):
        self._area = 40
        self._price = price
        self.name = name
Human.default_info()
Roman=Human("Roman",23)
Roman.info()
House1=SmallHouse(1200,"Люкс")
Roman.earn_money(2000)
Roman.info()
print(House1.final_price())
Roman.buy_house(House1)
Roman.info()