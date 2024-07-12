#Exception handling in python
try:
    print(x)
except:
    print("An exception occurred")

#Many exceptions
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

#You can use the else keyword to define a block of code to be executed if no errors were raised:
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

#use of final block of code to be executed
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

#The exercise 
def convert_to_int(input_str):
    try:
        # Attempt to convert the input to an integer
        return int(input_str)
    except ValueError:
        # Handle the case where the value cannot be converted to an integer
        print("ValueError: The string cannot be converted to an integer.")
    except TypeError:
        # Handle the case where the input is not a string
        print("TypeError: The input is not a string.")

# Example usage:
result = convert_to_int("123")  
print(result)

result = convert_to_int("abc")  
print(result)

result = convert_to_int(123)    
print(result)

#Exercise 2
# Define the custom exception
class InvalidAgeError(Exception):
    pass

# Function that raises InvalidAgeError if age is negative
def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")
    else:
        print(f"Age {age} is valid.")

# Handling the custom exception
try:
    # Replace -1 with an input value to test
    check_age(-1)
except InvalidAgeError as e:
    print(f"Caught an invalid age error: {e}")

