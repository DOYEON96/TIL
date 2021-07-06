import Module_Class as mc
from Module_Class import Cal

class fourcal_chr(Cal):
    def __init__(self, num):
        super().__init__()
        self.number = num

    def add_2(self, num1):
        self.number = self.number + self.result + num1
        print(self.result)
        return self.number



# mc.Cal_cls.sum(20, 20 , 30, 50)

# obj1 = Cal()
# obj1.add(30)
# obj1.add(20)
# print(obj1.result)

obj2 = fourcal_chr(50)
print(obj2.result)
print(obj2.add(10))
print(obj2.result)
print(obj2.add_2(10))