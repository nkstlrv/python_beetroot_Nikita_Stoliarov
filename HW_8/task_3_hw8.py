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


def make_operation(math_operator: str, *args: int or float):
    if math_operator == "+":
        return sum(args)

    elif math_operator == "*":
        x = 1
        for m_item in list(args):
            x = x * m_item
        return x

    elif math_operator == "/":
        d = list(args)
        for div_i, div_item in enumerate(d):
            if div_i == len(d) - 1:
                break
            d[0] = d[0] / d[div_i + 1]
        return d[0]

    elif math_operator == "-":
        s = list(args)
        for subs_i, subs_item in enumerate(s):
            if subs_i == len(s) - 1:
                break
            s[0] = s[0] - s[subs_i + 1]
        return s[0]

    else:
        print("\n Wrong format")


print(make_operation('/', 10, 2, 5))

