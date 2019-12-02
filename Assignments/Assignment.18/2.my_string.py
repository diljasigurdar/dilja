class MyString():
    def __init__(self, a_string=''):
        self.a_string = str(a_string)
        self._data_len = len(a_string)
    
    def __str__(self):
        return self.a_string

    def __repr__(self):
        return self.a_string

    def __len__(self):
        return self._data_len
    
    def __gt__(self, other):
        return len(self) > len(other)

    def __sub__(self, other):
        if self > other:
            return len(self) - len(other)
        else:
            return len(other) - len(self)


obj1 = MyString('this is a string')
obj2 = MyString('this is another one')
print(obj1 > obj2)
print(obj1-obj2)
    









'''Write a class MyString() such that it has a method that gives the difference 
between the size of strings when the '-' (subtraction) operator is used between 
the two objects of the class (the difference should always be positive). Additionally, 
implement a method that returns True if object 1 is greater than object 2 and False 
otherwise when the (>) (greater than) operator is used. Object 1 is greater 
than object 2 if the string it stores is longer than the string stored in object 2.'''