try:
    num1 = float(input("Enter a first number:"))
    num2 = float(input("Enter a second number:"))
    operation = input("choose operation(+,-,*,/):")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2    
    elif operation == "/":
        if num2 == 0:
            print("division by zero is not allowed")
        else:
            result = num1 / num2
    else:    
        print("invalid operation")  
        result=None
         
    if 'result' in locals()and result is not None:  
        print("result:",result)

except ValueError:
    print("invalid input")     

