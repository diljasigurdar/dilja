# Your function definition goes here

n = int(input("Input the length of Fibonacci sequence (n>=1): "))
# Call your function here   
 
def fibonacci(num):
    first = 1
    second = 1
    counter = 1
    current = 0
    if num >=1:
        print(1, end=' ')
    if num >=2:
        print(1, end=' ')
    while counter <= (num-2):
        current = first + second
        second, first = current, second
        counter += 1
        print(current, end=' ')

fibonacci(n)
