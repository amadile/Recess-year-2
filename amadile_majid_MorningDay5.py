#python functions
#functions without arguments
def first_function():
    print("introduction to functions in python")
first_function()    

def greet(name='Guest'):
    print(f"I am a software programmer, {name}!")
#calling the function
greet()

#functions with more than one parameter
def namePrint(real_name, nick_name):
    print(real_name + " " + nick_name)

namePrint("Amadile", "Majid")


def print_user_info(**user_info):
    for key, value in user_info.items():
        print(f"{key}: {value}")

# Example usage:
print_user_info(name="John", age=30, location="Seattle")
