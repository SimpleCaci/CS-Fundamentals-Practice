while True:
    try:
        num1 = float(input("What's the first number?"))
        num2 = float(input("What's the second number?"))
        operation = input("Which order of operation would you like to complete? (+,-,*,/)").strip()
        
        break
    except:
        print("One of the values entered is invalid")

    
output = None
match operation: #switches essentially
    case "+":
        output = num1 + num2
    case "-":
        output = num1 - num2
    case "*":
        output = num1 * num2
    case "/":
        try:
            output = num1 / num2
        except ZeroDivisionError:
            print("Cannot divide by zero.")


print(f'Your result is {output}')