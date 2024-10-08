print('"Нужно больше этажей"')

class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor

        if new_floor >  self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor+1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, количество этажей: {self.number_of_floors}')

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        return House(self.name, self.number_of_floors + value)

    def __iadd__(self, other):
        self.number_of_floors += other
        return self

    def __radd__(self, other):
        return House(self.name, self.number_of_floors + other)


test1 = House('ЖК Строитель', 10)
test2 = House('ЖК Союз', 20)

print(test1)
print(test2)

print(test1 == test2)       # __eq__

test1 = test1 + 10    # __add__
print(test1)
print(test1 == test2)

test1 += 10     # __iadd__
print(test1)

test2 = 10 + test2      # __radd__
print(test2)

print(test1 > test2) # __gt__
print(test1 >= test2) # __ge__
print(test1 < test2) # __lt__
print(test1 <= test2) # __le__
print(test1 != test2) # __ne__