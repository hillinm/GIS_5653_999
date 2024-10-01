### User inputs a number, converts to a float, and assigns it to the variable number.
number = float(input("Please input a number: "))

### Nested conditional statement
if number < 0:
    print("This is a negative number.")
elif number == 0:
    print("The provided value is 0.")
elif number > 0 and number < 10:
    print("This is a positive, single-digit number.")
elif number >= 10 and number < 100:
    print("This is a positive, double-digit number.")
elif number >= 100:
    print("This is a positive number.")