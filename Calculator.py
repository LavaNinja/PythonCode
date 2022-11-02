logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

num1 = 0
num2 = 0

operation = input("Pick and Operation- +, -, ÷, *: ")
if operation != "+" and operation != "-" and operation != "/" and operation != "*":
    print("Please use one of the operations given.")
    operation = input("Pick and Operation- +, -, ÷, *: ")
num1 = float(input("What is your first number: "))
num2 = float(input("What is your second number: "))

if operation == "+":
    solution = num1 + num2
    print(solution)

elif operation == "-":
    solution = num1 - num2
    print(solution)
elif operation == "/" or "÷":
    solution = num1 / num2
    print(solution)
elif operation == "*":
    solution = num1 * num2
    print(solution)

should_continue = input("Do you want to do another operation from that number y/n: ")
if should_continue == "Yes" or "yes" or "y" or "Y":
    should_continue = True
else:
    should_continue = False
while should_continue == True:
    operation = input("Pick and Operation- +, -, ÷, *: ")
    if operation != "+" and operation != "-" and operation != "/" and operation != "*":
        print("Please use one of the operations given.")
        operation = input("Pick and Operation- +, -, ÷, *: ")

    num = float(input("What is your number: "))

    if operation == "+":
        solution = solution + num
        print(solution)
    elif operation == "-":
        solution = solution - num
        print(solution)
    elif operation == "/":
        solution = solution / num2
        print(solution)
    elif operation == "*":
        solution = solution * num
        print(solution)

    should_continue = input("Do you want to do another operation from that number y/n: ")
    if should_continue == "Yes" or should_continue == "yes" or should_continue == "y" or should_continue == "Y":
        should_continue = True
    else:
        should_continue = False

print(f"Your end result is {solution}")



