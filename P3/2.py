class Dog:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def sit(self):
        print(f"{self.name}, cидит")
    def roll_over(self):
        print(f"{self.name}, перекатываеться")
my_dog1=Dog("willie","6")
my_dog2=Dog("lucy","3")
print(my_dog1.name,my_dog1.age)
print(my_dog2.name,my_dog2.age)
my_dog1.sit()
my_dog2.roll_over()