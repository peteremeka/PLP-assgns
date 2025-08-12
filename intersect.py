set_a = set()
set_b = set()

print("User's input for set_a")
a_one = input("Enter first index string : ")
set_a.add(a_one)

a_two = input("Enter second index string : ")
set_a.add(a_two)

a_three = input("Enter third index string : ")
set_a.add(a_three)

a_four = input("Enter fourth index string : ")
set_a.add(a_four)

a_five = input("Enter fifth index string : ")
set_a.add(a_five)

print(set_a)


print("User's input for set_b")
b_one = input("Enter first index string : ")
set_b.add(b_one)

b_two = input("Enter second index string : ")
set_b.add(b_two)

b_three = input("Enter third index string : ")
set_b.add(b_three)

b_four = input("Enter fourth index string : ")
set_b.add(b_four)

b_five = input("Enter fifth index string : ")
set_b.add(b_five)

print(set_b)


intersect = set_a.intersection(set_b)

print("Set array for set_a intersection set_b = ", intersect)