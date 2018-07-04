import math

print('''
Operations
e Exponents
+ Addition 
- Subtraction
* Multiplication
/ Division''')

Number1 = float(input("enter a number: "))
Operator = str(input("enter one of the operators:  "))
Number2 = float(input("enter another number: "))

Choice = str(input("Would you like to add another variable? y/n"))

if Operator == '+':
    print(Number1, "+", Number2, "=", Number1 + Number2)
    Answer = Number1 + Number2
    print(Answer)
    print("..."*20)

elif Operator == '-':
    print(Number1, "-", Number2, "=", Number1 - Number2)
    Answer = Number1 - Number2
    print(Answer)
    print("..."*20)

elif Operator == '*':
    print(Number1, "*", Number2, "=", Number1 * Number2)
    Answer = Number1 * Number2
    print(Answer)
    print("..."*20)

elif Operator == '/':
    print(Number1, "/", Number2, "=", Number1 / Number2)
    Answer = Number1 / Number2
    print(Answer)
    print("..."*20)

elif Operator == 'e':
    print(math.pow(Number1,Number2)),"=",Number1, "^", Number2

if Choice == 'n' or Choice == "N":
    print("Thank you")
    print("..."*20)

while Choice == 'y' or Choice == 'Y' or Choice == 'Yes' or Choice == 'yes':
    Number3 = float(input("enter another number:  "))
    Operator2 = str(input("enter another operator:"))

    if Operator2 == "+":
        print(Answer, "+", Number3, "=", Answer + Number3)
        Answer = Answer + Number3
        print(Answer)
        print("..."*20)
    elif Operator2 == "-":
        print(Answer, "-", Number3, "=", Answer - Number3)
        Answer = Answer - Number3
        print(Answer)
        print("..."*20)

    elif Operator2 == "*":
        print(Answer, "*", Number3, "=", Answer * Number3)
        Answer = Answer * Number3
        print(Answer)
        print("..."*20)

    elif Operator2 == "/":
        print(Answer, "/", Number3, "=", Answer / Number3)
        Answer = Answer / Number3
        print(Answer)
        print("..."*20)

    Choice = input("Would you like to continue? y/n  ")


