class Clock():
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def str_update(self, time_list):
        self.time_list = time_list.split(":")

        if self.time_list[0][0] != "0":
            self.hours = self.time_list[0]
        else:
            self.hours = self.time_list[0][1]
        self.minutes = self.time_list[1]
        self.seconds = self.time_list[2]

    def add_clocks(self, clock):
        hours = int(self.hours) + int(clock.hours)
        minutes = int(self.minutes) + int(clock.minutes)
        seconds = int(self.seconds) + int(clock.seconds)

        if seconds >= 60:
            quotient, remainder = divmod(seconds, 60)
            seconds = remainder
            minutes += quotient

        if minutes >= 60:
            quotient, remainder = divmod(minutes, 60)
            minutes = remainder
            hours += quotient 

        if hours > 24:
            quotient, remainder = divmod(hours, 24)
            hours = remainder

        new_clock = Clock(hours, minutes, seconds)    
        return new_clock

    def __str__(self):
        return "{} hours, {} minutes and {} seconds".format(self.hours, self.minutes, self.seconds)
    

clock1 = Clock()
clock2 = Clock()
clock1.str_update("20:10:52")
clock2.str_update("08:49:24")
print(clock1)
print(clock2)
clock3 = clock1.add_clocks(clock2)
print(clock3)

'''
Implement a class called Clock with the following attributes:

Constructor with three parameters: hours, minutes, seconds with default values 0.
Three instance variables: hours, minutes, seconds.
A method called str_update(). It takes as an argument a string of the form hh:mm:ss and updates
the three instances variables.
A __str__() method for responding to the print() method. 
It should write out: "{} hours, {} minutes and {} seconds"
A method called add_clocks(). It takes another clock object as a parameter, 
adds the two clocks and returns a new clock instance.  In this method, 
you need to add the respective values of the two clocks together and remember 
the resulting hours, minutes and seconds. Remember that the sum of seconds cannot exceed 60, 
in which case there is a carry over to the minutes values. Same for minutes, 
it cannot exceed 60 and carries over to hours. For hours, the summed values cannot exceed
24. If hours is exceeded, we ignore it and start from zero.  
Use the divmod() built-in Python function in your implementation.'''