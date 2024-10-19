from functools import wraps
'''
Написати декоратор, який буде виводити аргументи функції

my_function(1, 2, 3, 4, 5)

Calling function 'my_function'
With arguments 1, 2, 3, 4, 5
'''

def print_arguments(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # print(args, kwargs)
        print(f"Calling {function.__name__}")
        result = function(*args, **kwargs)
        # print(result)
        return result
    return wrapper

# @print_arguments
def my_function(one, two, three, four=4, five="five"):
    """Documentation for my function"""
    return "Hello"

def my_other_function(*args, **kwargs):
    print(args)
    print(kwargs)


# print(my_function.__name__)
# print(my_function.__doc__)
my_other_function.__name__ = "hello"
print(my_other_function.__name__)

# result = my_function(1, 2, 3, 4, 5)
# print(result)
# print(result + " world!")

# my_other_function(1, 2, 3, 3, 4, arg1=1, arg2="World")
# my_other_function()
# print(1, 2, 3, 4, 5, 6, 7)


# print(1, 2, 3, 4, 5)

arguments = ["one", 2, "Three", [1, 2, 3]]
# print(*arguments)

# arguments_dict = {"arg1": 1, "arg2": "Two"}
# print(**arguments_dict)

list_1 = [1, 2, 3]
list_2 = [*list_1, 6, 7]
# print(list_2)

list_2[0] = 0
# print(list_2)
# print(list_1)

