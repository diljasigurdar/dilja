def get_vector(vector_size):
    vector = []
    for counter in range(1, vector_size + 1):
        element = float(input("Element no " + str(counter) + ": "))
        vector.append(element)
    return vector

def calculate_dot_product(vector1, vector2):
    dot_product = 0
    for counter in range(0, vector_size):
        dot_product += vector1[counter] * vector2[counter]
    return dot_product

# Main program starts here


vector_size = int(input("Input vector size: "))

# Should only be a sequence of function calls
vector1 = get_vector(vector_size)
vector2 = get_vector(vector_size)
dot_product = calculate_dot_product(vector1,vector2)
print("Dot product is: ", dot_product)



# Write a Python program that calculates the dot product of two given vectors