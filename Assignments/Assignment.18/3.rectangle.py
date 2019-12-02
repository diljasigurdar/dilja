class Rectangle():
    def __init__(self, length=0, width=0):
        if length < 0:
            self.__length = 0
        else:
            self.__length = length
        if width < 0:
            self.__width = 0
        else:
            self.__width = width
    
    def __str__(self):
        return "Length: {}, Width: {}".format(self.__length, self.__width)
    
    def __repr__(self):
        return "Rectangle({},{})".format(self.__length, self.__width)
    
    def __eq__(self, other):
        return self.area() == other.area()
    
    def area(self):
        return self.__length * self.__width
    
    def perimeter(self):
        return (self.__length * 2) + (self.__width * 2)

a = Rectangle()
b = Rectangle(2,2)
print(a)
print(a.area())
print(a.perimeter())
print(a.__repr__())
print(a == b)





'''Write a class called Rectangle. A Rectangle should have two private attributes that represent 
the length and width of the rectangle.
You should be able to create a Rectangle instance by supplying a value for its 
length and its width (in that order). If no arguements are given the default 
value 0 should be set for both attributes. Also, if a negative number is passed 
as an argument it should default to zero.

You should implement the following methods on the class:

area() returns the area of the Rectangle
perimeter() returns the perimeter of the rectangle
__str__() which should print the the length and width of the rectangle 
like this "Length: 2, Width: 4" where 2 and 4 are the values that were 
supplied when the Rectangle was created.
by using the == operator. Two Rectangles are equal if the have the same area.

You should also implement the __repr__() method. If a Rectangle has a length 
of 10 and a width of 2 this method should return a string like this: "Rectangle(10,2)"'''