"""
few utility methods
"""


def factorial(num):
    # if type(num) is not int:
    #     return 0

    f = 1
    for i in range(2, num+1):
        f *= i
    return f

