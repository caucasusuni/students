import random
class Tuple():
    def __init__(self):
        self.elements = ()
    def add(self):
        for i in range(0,5):
            self.elements = (self.elements) + (random.randint(0,10),)
    def remove(self,number):
        new=()
        if number not in self.elements:
            raise Exception("Element is not present in Tuple")
        else:
            for i in self.elements:
                if i!=number:
                    new+=i,

        self.elements=new

    def __add__(self, other):
        new=()
        for i in range(len(self.elements)):
            new=new+(self.elements[i]+other.elements[i],)
        return new
    def mutual(self,other):
        tupa=()
        for i in self.elements:
            if i in other.elements:
                tupa += (i,)
        return tupa
    
    def __str__(self):
        return "result : " + str(self.elements)
bruh=Tuple()
bruh.add()
print(bruh)
brev=Tuple()
brev.add()
print(brev)
print(bruh+brev)
print(bruh.mutual(brev))


