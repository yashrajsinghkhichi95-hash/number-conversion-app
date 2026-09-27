
def octal_to_decimal(number):
    string = str(number)
    result = 0
    power = 0

    for i in reversed(string):
        result = result + int(i) * (2 ** power)
        power = power + 1

    return result

print(octal_to_decimal(17))