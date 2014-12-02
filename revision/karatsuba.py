# karatsuba multiplication
def karatsuba(num1, num2):
    num1Str = str(num1)
    num2Str = str(num2)
    # if one of the subnumber is less than 10, this is the base case
    if (num1 < 10) or (num2 < 10):
        return num1 * num2

    # define the max length of 2 numbers
    maxLength = max(len(num1Str), len(num2Str))
    # this is the number of digits as lower part
    splitPosition = maxLength / 2
    # notice the '-', this is for make sure the number of lower parts
    # constained
    high1 = int(num1Str[:-splitPosition])
    low1 = int(num1Str[-splitPosition:])
    high2 = int(num2Str[:-splitPosition])
    low2 = int(num2Str[-splitPosition:])
    # Gauss tricks
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    return (z2 * 10 ** (2 * splitPosition)) + \
            ((z1 - z2 - z0) * 10 ** splitPosition) + \
            z0
