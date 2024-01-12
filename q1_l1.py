# Question 01 - Level 01
# Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

def verify_number(begin_interval: int, end_interval: int) -> list:
    """This function verifies the numbers that are divisible by 7 but are not a multiple of 5.
    Input: begin_interval, end_interval
    Output: A list of numbers that correspond to the conditions"""
    numbers = []

    for i in range(begin_interval, end_interval+1):
        if (i%7 == 0) and (i%5 != 0):
            numbers.append(i)
    
    return numbers

if __name__ == '__main__':
    # A test condition of the developed function
    begin = int(input("Please, enter the begin of the interval: "))
    end = int(input("Please, enter the end of the interval: "))

    values = verify_number(begin, end)

    for i in values:
        print(i, end=", ")