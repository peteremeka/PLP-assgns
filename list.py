list_integer = []

num1 = int(input("Enter first index : "))
list_integer.append(num1)

num2 = int(input("Enter second index : "))
list_integer.append(num2)

num3 = int(input("Enter third index : "))
list_integer.append(num3)

num4 = int(input("Enter fourth index : "))
list_integer.append(num4)

num5 = int(input("Enter fifth index : "))
list_integer.append(num5)

print(list_integer)

sum_of_integer = int(list_integer[0] + list_integer[1] + list_integer[2] + list_integer[3] + list_integer[4])

print("The Sum Array Index(es) is = ", sum_of_integer)