# Function to calculate circumference
def find_circumference(radius):
    pi = 3.1416
    circumference = 2 * pi * radius
    return circumference

# Taking input from user
r = float(input("Enter the radius of the circle: "))

# Calling the function
result = find_circumference(r)

# Displaying the result
print("The circumference of the circle is:", result)
