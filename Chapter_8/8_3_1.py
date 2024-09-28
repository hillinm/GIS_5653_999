new_word = input("Please type a word: Y")

if len(new_word) < 5:
    print("Your input is less than 5 characters long")
elif len(new_word) > 5:
    print("Your input is greater than 5 characters long")
else:
    print("Your input is 5 characters long")