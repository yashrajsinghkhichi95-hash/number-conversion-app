def decimal_to_binary(number):
    if number == 0:
        return 0

    binary_list = []
    while number > 0:
        remainder = number % 2
        binary_list.append(remainder)
        number = number // 2

    reversed_binary_list = binary_list[::-1]
    str_result = "".join(str(x) for x in reversed_binary_list)
    return str_result


def decimal_to_octal(number):
    if number == 0:
       return 0

    octal_list = []
    while number > 0:
        remainder = number % 8
        octal_list.append(remainder)
        number = number // 8

    reversed_octal_list = octal_list[::-1]
    str_result = "".join(str(x) for x in reversed_octal_list)
    return str_result

def decimal_to_hexadecimal(number):
    if number == 0:
       return 0

    list = "0123456789ABCDEF"
    hexadecimal_list = []
    while number > 0:
        remainder = number % 16
        hexadecimal_list.append(list[remainder])
        number = number // 16

    reversed_hexadecimal_list = hexadecimal_list[::-1]
    str_result = "".join(str(x) for x in reversed_hexadecimal_list)
    return str_result

def binary_to_decimal(number):
    string = str(number)
    result = 0
    power = 0

    for i in reversed(string):
        result = result + int(i) * (2 ** power)
        power = power + 1

    return result


def octal_to_decimal(number):
    string = str(number)
    result = 0
    power = 0

    for i in reversed(string):
        result = result + int(i) * (8 ** power)
        power = power + 1

    return result


def hexadecimal_to_decimal(string):
    list = "0123456789ABCDEF"
    result = 0
    power = 0

    for i in reversed(string):
        digit_value = list.index(i)
        result = result + digit_value * (16 ** power)
        power = power + 1

    return result 

print("CONVERSIONS BY YRSK")
print("1.   DECIMAL TO BINARY")
print("2.     DECIMAL TO OCTAL") 
print("3.     DECIMAL TO HEXADECIMAL") 
print("4.     BINARY TO DECIMAL")
print("5.     OCTAL TO DECIMAL")
print("6.     HEXADECIMAL TO DECIMAL") 
print("7.     BINARY TO OCTAL") 
print("8.     BINARY TO HEXADECIMAL") 
print("9.     OCTAL TO BINARY")
print("10.    HEXADECIMAL TO BINARY") 
print("11.    OCTAl TO HEXADECIMAL")
print("12.    HEXADECIMAL TO OCTAL")

choice = int(input("Enter your choice: "))
raw_input_value = input("Enter the number: ")

if choice in (6, 10, 12):
    number = raw_input_value.upper()
else:
    number = int(raw_input_value)



if choice == 1:
    result = decimal_to_binary(number)
    print(result)
elif choice == 2:
    result = decimal_to_octal(number)
    print(result)
elif choice == 3:
    result = decimal_to_hexadecimal(number)
    print(result)
elif choice == 4:
    result = binary_to_decimal(number)
    print(result)
elif choice == 5:
    result = octal_to_decimal(number)
    print(result)
elif choice == 6:
    result = hexadecimal_to_decimal(number)
    print(result)
elif choice == 7:
    convert = binary_to_decimal(number)
    result = decimal_to_octal(convert)
    print(result)
elif choice == 8:
    convert = binary_to_decimal(number)
    result = decimal_to_hexadecimal(convert)
    print(result) 
elif choice == 9:
    convert = octal_to_decimal(number)
    result = decimal_to_binary(convert)
    print(result)
elif choice == 10:
    convert = hexadecimal_to_decimal(number)
    result = decimal_to_binary(convert)
    print(result)
elif choice == 11:
    convert = octal_to_decimal(number)
    result = decimal_to_hexadecimal(convert)
    print(result)
elif choice == 12:
    string = str(number)
    convert = hexadecimal_to_decimal(string)
    result = decimal_to_octal(convert)
    print(result)
else:
    print("BSDK DEKH KE NUMBER DAAL")