# Python Keywords Cheatsheet

# A list of all Python keywords can be obtained from the keyword module:
import keyword
print(keyword.kwlist)
# Output:
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


# 1. False: Boolean value, result of comparison operations.
print(1 > 2)
# Output: False

# 2. None: Represents the absence of a value.
x = None
print(x)
# Output: None

# 3. True: Boolean value, result of comparison operations.
print(2 > 1)
# Output: True

# 4. and: A logical operator.
print(True and False)
# Output: False

# 5. as: To create an alias.
import math as m
print(m.pi)
# Output: 3.141592653589793

# 6. assert: For debugging.
x = 1
# assert x > 1, "x should be greater than 1"
# Output: AssertionError: x should be greater than 1

# 7. async: To declare an asynchronous function.
async def my_async_func():
    return "Hello from async"

# 8. await: To call an asynchronous function.
# import asyncio
# async def main():
#     result = await my_async_func()
#     print(result)
# asyncio.run(main())
# Output: Hello from async

# 9. break: To exit a loop.
for i in range(5):
    if i == 3:
        break
    print(i)
# Output:
# 0
# 1
# 2

# 10. class: To define a class.
class MyClass:
    x = 5
my_object = MyClass()
print(my_object.x)
# Output: 5

# 11. continue: To continue to the next iteration of a loop.
for i in range(5):
    if i == 3:
        continue
    print(i)
# Output:
# 0
# 1
# 2
# 4

# 12. def: To define a function.
def my_func():
    print("Hello from a function")
my_func()
# Output: Hello from a function

# 13. del: To delete an object.
x = 5
del x
# print(x)
# Output: NameError: name 'x' is not defined

# 14. elif: Conditional statement, same as else if.
x = 10
if x < 5:
    print("x is less than 5")
elif x == 10:
    print("x is 10")
else:
    print("x is greater than 10")
# Output: x is 10

# 15. else: Conditional statement.
x = 5
if x > 10:
    print("x is greater than 10")
else:
    print("x is not greater than 10")
# Output: x is not greater than 10

# 16. except: To handle exceptions.
try:
    print(1 / 0)
except ZeroDivisionError:
    print("You cannot divide by zero!")
# Output: You cannot divide by zero!

# 17. finally: To execute code regardless of the result of the try- and except blocks.
try:
    print(1 / 1)
except ZeroDivisionError:
    print("You cannot divide by zero!")
finally:
    print("The 'try except' is finished")
# Output:
# 1.0
# The 'try except' is finished

# 18. for: To create a for loop.
for i in range(3):
    print(i)
# Output:
# 0
# 1
# 2

# 19. from: To import specific parts of a module.
from math import pi
print(pi)
# Output: 3.141592653589793

# 20. global: To declare a global variable.
def my_func():
    global x
    x = "hello"
my_func()
print(x)
# Output: hello

# 21. if: Conditional statement.
if 5 > 2:
    print("5 is greater than 2")
# Output: 5 is greater than 2

# 22. import: To import a module.
import math
print(math.pi)
# Output: 3.141592653589793

# 23. in: To check if a value is present in a list, tuple, etc.
my_list = [1, 2, 3]
print(1 in my_list)
# Output: True

# 24. is: To test if two variables refer to the same object.
x = ["apple", "banana", "cherry"]
y = x
print(x is y)
# Output: True

# 25. lambda: To create an anonymous function.
x = lambda a: a + 10
print(x(5))
# Output: 15

# 26. nonlocal: To declare a non-local variable.
def my_func1():
    x = "John"
    def my_func2():
        nonlocal x
        x = "hello"
    my_func2()
    return x
print(my_func1())
# Output: hello

# 27. not: A logical operator.
print(not True)
# Output: False

# 28. or: A logical operator.
print(True or False)
# Output: True

# 29. pass: A null statement, a placeholder.
def my_empty_func():
    pass # placeholder for future code

# 30. raise: To raise an exception.
# x = -1
# if x < 0:
#     raise Exception("Sorry, no numbers below zero")
# Output: Exception: Sorry, no numbers below zero

# 31. return: To exit a function and return a value.
def my_func():
    return "Hello from a function"
print(my_func())
# Output: Hello from a function

# 32. try: To make a try...except statement.
try:
    print(1 / 0)
except ZeroDivisionError:
    print("You cannot divide by zero!")
# Output: You cannot divide by zero!

# 33. while: To create a while loop.
i = 0
while i < 3:
    print(i)
    i += 1
# Output:
# 0
# 1
# 2

# 34. with: Used to wrap the execution of a block with methods defined by a context manager.
with open("python_keywords_cheatsheet.py", "r") as f:
    # The file is automatically closed when the block is exited.
    pass

# 35. yield: To create a generator function.
def my_generator():
    yield 1
    yield 2
    yield 3
for value in my_generator():
    print(value)
# Output:
# 1
# 2
# 3
