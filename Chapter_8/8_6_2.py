new_word = input("Please type in a string: ")

try:
    index = int(input("Please enter an integer: "))
    print(new_word[index])
except ValueError:
    print("Invalid Number")
except IndexError:
    print("Index is out of bounds")