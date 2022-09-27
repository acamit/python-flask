print("hellow"[4])
num_char = len(input("what is your name"))
# print("Your name has " + num_char + "character")
print("Your name has " + str(num_char) + "character")

two_digit_number = input("type a 2 digit number")
print(type(two_digit_number))

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)

print(result)

