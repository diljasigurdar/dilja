class RockGuitar():
    def __init__(self, guitarist='', guitar=''):
        self.set_entry(guitarist, guitar)
    
    def __str__(self):
        return "{:<20s} {:<20s}".format(self.guitarist, self.guitar)
    
    def set_entry(self, guitarist='', guitar=''):
        self.guitarist = guitarist
        self.guitar = guitar


g = RockGuitar()

g.set_entry("Keith Richards", "Micawber Fender Telecaster")

f = RockGuitar()

f.set_entry("Eddie Van Halen","Frankenstrat")

h = RockGuitar()

h.set_entry("Tony Iommi")

print(g)
print(f)
print(h)
'''
Write a class called RockGuitar() that has attributes: 'guitarist' and 'guitar'. 
It has a constructor with three parameters, self, guitarist and guitar. 
The default value of guitarist and guitar should be empty string.

The class should have __str__ method to return a string for output using this 
format: "{:<20s} {:<20s}". Lastly, it has the following method to set guitarist and guitar:

set_entry(guitarist, guitar): both 'guitarist' and 'guitar' are strings.  
'guitar" has the default value as the empty string. '''