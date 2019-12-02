class Student():
    def __init__(self, value=10):
        self.value = value
    
    def __str__(self):
        return "{}".format(self.value)

    def add_score(self, value=10):
        self.value += value
    
    def decrease_score(self, value=10):
        self.value -= value
    

p = Student()
print(p)
p.add_score()
print(p)
p.decrease_score()
print(p)
