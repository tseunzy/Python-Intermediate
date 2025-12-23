
print("==========Error Handling ===========")

# try/except block
try:
    # Code that might cause an error but not always certain
    result = 10 / 0
    print("this won't execute")
except ZeroDivisionError:
    # Handle the specific error
    print("error: cannot divide by zero")

print("Program continues.")

print("==========Example 2===========")

# # handling multiple operations
# try:
#     number = int(input("Enter a number: "))
#     reciprocal = 1 / number
#     print(f"Reciprocal: {reciprocal}")
# except ValueError: # Handle error where an alphabet is sed instead of number 
#     print("that not a valid number!")
# except ZeroDivisionError:
#     print("cannot divide by zero!")

# print("Program completed.")


print("==========Example 3===========")

try:
    x = [1, 2, 3]
    print(x[10])  # indexError
except LookupError: 
    print("caught by LookupError")


print("==========Example 4===========")
try:
    x = [1, 2, 3]
    print(x[10])  # indexError
except Exception: 
    print("caught by Exception, but the type of error not define")


print("==========Example 5===========")
# Always close files, even if errors occur
file = None
try:
    file = open("example76.txt", "w")
    file.write("Hello, Sam!")
    # Simulate an error
    result = 10 / 0  # this cause ZeroDivisionError
except ZeroDivisionError:
    print("math error occur")
finally:                # this always runs no matter 
    # this ALWAYS runs
    if file:
        file.close()
        print("file was closed in finally block")

print("program continues")


print("==========Example 6===========")

# Example, using the cleanup of a calculator 
def calculate():
    result = None
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        operation = input("Enter operation (+, -, *, /): ")
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!") # raise catches the error firstly 
            result = num1 / num2
        else:
            raise ValueError("Invalid operation!") # So as this
        
        print(f"Result: {result}")
    except Exception:
        print(f"Enter an integer number")

    except ValueError as e:
        print(f"Input error: {e}")
    
    except ZeroDivisionError as e:
        print(f"Math error: {e}")
    
    finally:        # Always show final message
        print("-" * 30)
        print("Calculation complete!")
        print(f"Final result was: {result}")
      
calculate() # Run the calculator





# Always executes finally - No matter what happens in try/except





# Found this
"""
BaseException
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    └── FloatingPointError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── OSError
      │    ├── FileNotFoundError
      │    └── PermissionError
      ├── TypeError
      ├── ValueError
      └── RuntimeError
"""