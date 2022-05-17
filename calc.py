from multiprocessing.managers import ValueProxy

operation = input(''' 
please type in the math operation you would like to complete:
+ for addition
- for substraction
* for multiplication
/ for division
% for modulus
''')
number_1 = int(input("Enter your first number: "))
number_2 = int(input("Enter your second numbet: "))

#addition
if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)
# substraction
elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)
    # multiplication
elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

# division
elif operation == '/':
    print(' {} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)
# modulos
elif operation == '%':
    print('{} % {} = '.format(number_1, number_2))
    print(number_1 % number_2)
else:
    print('Put valid operator')

