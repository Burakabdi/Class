
class Animal():

    def __init__(self,legs_count):
        print("Animal object was created")

    def runs(self):
        print("Running started")

dog = Animal(4)
dog.runs() 
