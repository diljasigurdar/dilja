file_object = open("test.txt", "r")

for line in file_object:
    line = line.strip().replace(" ","")
    print(line, end='')