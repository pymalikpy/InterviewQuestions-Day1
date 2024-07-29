def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


## Iterative way to do it

def old_factorial(num):
    if num < 0:
        return "Factorial does not exist for negative numbers"
    elif num == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        return factorial


# Prompt the user to enter a number
num = int(input("Enter the number: "))

# Call the 'factorial' function to calculate and print the result
result = old_factorial(num)
print(f"The factorial of {num} is {result}")
