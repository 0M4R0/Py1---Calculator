#This is one of my first projects with python being a beginner.

print('This is a calculator')
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

option = int(input("Set an option (1/2/3/4): "))

if option == 1:
    number1 = int(input("Insert a number: "))
    number2 = int(input("Insert a number: "))

    result = number1 + number2
    print('The result is:', result)

elif option == 2:
    number1 = int(input("Insert a number: "))
    number2 = int(input("Insert a number: "))

    result = number1 - number2
    print('The result is:', result)

elif option == 3:
    number1 = int(input("Insert a number: "))
    number2 = int(input("Insert a number: "))

    result = number1 * number2
    print('The result is:', result)

elif option == 4:
    number1 = int(input('Insert a number: '))
    number2 = int(input('Insert a number: '))
    if number2 == 0:
        print("Can't divide by 0")
    else:
        result = number1 / number2
        print('The result is:', result)



















#number = int(input("Insert a number: "))
#number2 = int(input("Insert a number: "))

#Number3 = number + number2
#print(Number3)
