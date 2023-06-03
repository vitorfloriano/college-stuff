import random

class MyList(list):
    def choice(self):
        return random.choice(self)
    
x = MyList([1,2,3,4,5])
print(x.choice())

print(str(x))