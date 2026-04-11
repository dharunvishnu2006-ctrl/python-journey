try:
    num = int(input("Enter number:"))
    result = 10/num
    print("Result:",result)
except ZeroDivisionError:
    print("cannot divide by zero!") 
except ValueError:
    print("enter a valid number!")       
