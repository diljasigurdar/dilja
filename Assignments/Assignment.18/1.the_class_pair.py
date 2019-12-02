class Pair():
    def __init__(self, value1=0, value2=0):
        self.value1 = value1
        self.value2 = value2
    
    def __str__(self):
        return("Value 1: {}, Value 2: {}").format(self.value1, self.value2)
    
    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return Pair(self.value1 + other.value1, self.value2 + other.value2)



    
a = Pair(20,30)
print(a)
b = Pair(40,50)
c = a + b
print(c)









'''Write a class 'Pair' that initializes two values 'v1' and 'v2' to '0' by default. 
It should print the values in this form: "Value 1: 20, Value 2: 30". When two objects 
of this class are added together using the '+' operator, the result is 'v1' of object 1 
gets added to 'v1' of object 2 and 'v2' of object 1 gets added to 'v2' of object 2.'''