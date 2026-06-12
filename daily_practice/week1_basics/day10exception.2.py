try:
    num = int(input("Enter number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Enter a valid number!")
finally:
    print("Program finished!")