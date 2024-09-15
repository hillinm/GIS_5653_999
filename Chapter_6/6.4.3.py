number = input("What number would you like to double? ")

def doubles(number):
    for i in range(3):
        number = int(number) * 2
        print(number)

doubles(number)