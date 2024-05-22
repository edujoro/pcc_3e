try:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
except ValueError:
    print('Invalid input')
else:
    suma = num1 + num2
    print('The sum of these numbers is: ', suma)
