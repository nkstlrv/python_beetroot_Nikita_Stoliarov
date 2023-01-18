# Task 3
#
# A simple calculator.
#
# Create a function called make_operation,
# which takes in a simple arithmetic operator as a first parameter
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’)
# and an arbitrary number of arguments (only numbers) as the second parameter.
# Then return the sum or product of all the numbers in the arbitrary parameter.
#
# For example:
#
# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42

# I tried to use same loop for all operations but unfortunately strange things happens with Division and Subtraction
def make_operation(math_operator, *args: int or float):
    for ind, num in enumerate(args):
        if math_operator == "+":
            return sum(args)
        elif math_operator == "*":
            x = 1
            x = x * num
        elif math_operator == "/":
            try:
                d = list(args)
                for div_i, div_item in enumerate(d):
                    if div_i == len(d) - 1:
                        break
                    d[0] = d[0] / d[div_i + 1]
                return d[0]
            except ZeroDivisionError:
                print("You can't divide by zero")
                break

        elif math_operator == "-":
            s = list(args)
            for subs_i, subs_item in enumerate(s):
                if subs_i == len(s) - 1:
                    break
                s[0] = s[0] - s[subs_i + 1]
            return s[0]

        else:
            print("\n Wrong format")


print(make_operation('/', 16, 2, 4, 1))




