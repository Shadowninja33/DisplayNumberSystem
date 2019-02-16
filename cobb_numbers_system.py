def convert_decimal_to_base(decimalnum, base):
    """This will convert a given decimal number to a specified base (returns as a str)"""
    finalnum = []
    while decimalnum // base is not 0:
        finalnum.insert(0, decimalnum % base)
        decimalnum = decimalnum//base

    finalnum.insert(0, decimalnum)

    #converting digits greater than 9 to chars (for hex)
    i= 0
    while i < len(finalnum):
        if finalnum[i] > 9:
            finalnum[i] = chr((finalnum[i] - 9) + 64)
        i += 1

    result = ''.join(map(str, finalnum))
    return result


def convert_base_to_decimal(startnum, base):
    """Converts a number (in str form) in a given base to decimal (int)"""
    finalnum = 0
    i = 0
    numlist = list(startnum)

    x = len(numlist) - 1
    while x >= 0:
        #convert all digits greater than 9 into numbers
        if (ord(numlist[x]) > 57):
            numlist[x] = int(ord(numlist[x]) - 64) + 9

        finalnum += int(numlist[x]) * (int(base)**i)
        i += 1
        x -= 1

    return finalnum


def invalid_number(num, base):
    """Checks if a given number(str form) is valid for its given base e.g. no 3 digit in binary"""
    if len(num) < 1:
        return True

    x = 0
    numlist = list(num)
    while x < len(numlist):
        # convert all digits greater than 9 into numbers
        if (ord(numlist[x]) > 57):
            numlist[x] = int(ord(numlist[x]) - 64) + 9

        if int(numlist[x]) > int(base):
            return True
        x += 1
    return False


if __name__ == "__main__":
    numtoconvert = input("Num to convert:  ")
    base = input("Base of given number: ")
    print("-----------------------------")
    if invalid_number(numtoconvert, base):
        print("Invalid Number")

    else:
        convertednum = convert_base_to_decimal(numtoconvert, base)
        print("Decimal: " + str(convertednum))
        print("Binary: " + str(convert_decimal_to_base(convertednum, 2)))
        print("Ternary: " + str(convert_decimal_to_base(convertednum, 3)))
        print("Quaternary: " + str(convert_decimal_to_base(convertednum, 4)))
        print("Octal: " + str(convert_decimal_to_base(convertednum, 8)))
        print("Hexadecimal: " + str(convert_decimal_to_base(convertednum, 16)))