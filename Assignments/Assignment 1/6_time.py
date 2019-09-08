secs_str = input("Input seconds: ") # do not change this line
secs_int = int(secs_str)
# hours =
hours = secs_int // 3600
secs_int2 = secs_int % 3600
# minutes =
minutes = secs_int2 // 60
secs_int3 = secs_int2 % 60
# seconds =
seconds = secs_int3 
print(hours,":",minutes,":",seconds) # do not change this line
