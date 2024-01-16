# Question 4 - Level 1
# Question: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. tuple() method can convert list to tuple

def create_sequence(values):
    """This function creates two sequences based on the input values, one sequence is a list and the another is a tuple"""
    l = values.split(',')
    t = tuple(l)
    return l, t

if __name__ == '__main__':
    values = input("Please, type a series of comma-separated numbers: ")

    l,t = create_sequence(values)

    print(f"List: {l}")
    print(f"Tuple: {t}")


