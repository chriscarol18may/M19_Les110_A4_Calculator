def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Main program

# Take input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
    
# Display results
print(f"The sum of {num1} and {num2} is: {add(num1, num2)}")
print(f"The difference when {num2} is subtracted from {num1} is: {subtract(num1, num2)}")