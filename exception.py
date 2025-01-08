try:
    # code we are going to try
    pass
except Exception:   # better to use actual exception rather than this catch all
    # code to handle the exception
    pass


try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("You can't divide by zero... nor can I!")
except ValueError:
    print("Invalid input! Please enter a number!")

# catch all - use sparingly!
try:
    # code
    pass
except Exception as e:
    print(f"A exception occurred, it was: {e}")

# Using else with try-except
# The else block executes if no excetions occur
try:
    # code
    pass
except Exception as e:
    print(f"A exception occurred, it was: {e}")
else:
    # Execure if no exception
    pass

# An example...
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero - no can do")
else:
    print(f"Result is {result}")

# the finally block
# Executes code regardless of whther an exception occurred
# Useful in clean up
try:
    result = 10 / 0
except Exception as e:
    print(f"Division by zero - no can do. {e}")
else:
    print(f"Result is {result}")
finally:
    print("This always prints..")

# Raise Exception
# Use raise to generate an exception manually
"""
if conditon:
    raise ExceptionType("Error message")
"""


def check_positive(number):
    if number < 0:
        raise ValueError("Number must be positive")
    return number


try:
    print(check_positive(-5))
except ValueError as e:
    print(e)


class EdgbastionException(Exception):
    pass


try:
    raise EdgbastionException("This is some crazy message from a special exception")
except EdgbastionException as e:
    print(e)


class AgeError(Exception):
    pass


def check_age(age):
    if age < 18:
        raise AgeError("You order these drinks you need to be 18 or over")


try:
    check_age(16)
except AgeError as e:
    print(e)
