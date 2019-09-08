ab = 10
d = ab * ab 

while ab < 100:
    if ab == (d % 100):
        break
    ab += 1
    d = ab * ab

print(ab)