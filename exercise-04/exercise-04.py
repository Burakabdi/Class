
class Animal():
    def __init__(self,legs_count):
        print("Animal object was created")
        self._number_of_legs = legs_count

    def runs(self):
        print("Running started")

    def count_legs(self):
        print(f"It has {self._number_of_legs} legs")

    def return_legs(self):
        return self._number_of_legs
        


class Dog(Animal):

    def __init__(self, name, legs_count):
        Animal.__init__(self, legs_count)
        self.name = name
    
    def bark(self):
        print("woof woof")


rocky = Dog("rocky", 4)
print(rocky.name)
rocky.bark()
rocky.count_legs()