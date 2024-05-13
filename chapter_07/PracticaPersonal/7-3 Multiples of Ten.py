10# Ask the user for a number, and then report whether the number is a multiple of 10 or not.

user_number = int(input("Enter a number: "))
if user_number % 10 == 0:
    True
    print("It is a multiple of 10")
else:
    False
    print("It is not a multiple of 10")
