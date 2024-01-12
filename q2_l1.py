# Question 2 - Level 1
# Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

def calculate_factorial(x):
    """This function calculates the factorial of a 'x' number"""
    if x == 0:
        return 1
    return x * calculate_factorial(x-1)

if __name__ == '__main__':
    # A test condition of the developed function
    x = int(input("Please, enter a number to calculate the factorial: "))

    fact = calculate_factorial(x)

    print(f"The factorial of {x} is {fact}")